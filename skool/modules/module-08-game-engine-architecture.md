# Module 8: Game Engine Architecture

## 🎯 Learning Objectives

By the end of this module, you will:
- Understand core game engine systems
- Build a custom game engine from scratch
- Implement ECS (Entity Component System) architecture
- Create modular, scalable game systems
- Master game loop optimization
- Design plugin architectures

---

## 📚 Module Overview

**Duration:** 5-7 weeks
**Difficulty:** Advanced
**Prerequisites:** Module 7, OOP, Design Patterns, Data Structures

---

## 🗓️ Week-by-Week Breakdown

### Week 1: Engine Fundamentals

#### Day 1-2: Game Loop Architecture
**Topics:**
- Fixed vs variable timestep
- Frame-independent movement
- Delta time management
- Update/Render decoupling

**Core Game Loop:**
```javascript
class GameEngine {
  constructor() {
    this.isRunning = false;
    this.fps = 60;
    this.targetFrameTime = 1000 / this.fps;
    this.accumulator = 0;
    this.currentTime = performance.now();
    this.systems = [];
    this.fixedTimeStep = 1 / 60; // 60 FPS fixed timestep
  }

  start() {
    this.isRunning = true;
    this.gameLoop();
  }

  stop() {
    this.isRunning = false;
  }

  gameLoop = () => {
    if (!this.isRunning) return;

    const newTime = performance.now();
    const frameTime = (newTime - this.currentTime) / 1000;
    this.currentTime = newTime;

    // Prevent spiral of death
    const maxFrameTime = 0.25;
    const deltaTime = Math.min(frameTime, maxFrameTime);

    this.accumulator += deltaTime;

    // Fixed timestep updates for physics/game logic
    while (this.accumulator >= this.fixedTimeStep) {
      this.fixedUpdate(this.fixedTimeStep);
      this.accumulator -= this.fixedTimeStep;
    }

    // Variable timestep for rendering
    const alpha = this.accumulator / this.fixedTimeStep;
    this.update(deltaTime);
    this.render(alpha);

    requestAnimationFrame(this.gameLoop);
  }

  fixedUpdate(dt) {
    // Physics, game logic
    this.systems.forEach(system => {
      if (system.fixedUpdate) {
        system.fixedUpdate(dt);
      }
    });
  }

  update(dt) {
    // Input, AI, animations
    this.systems.forEach(system => {
      if (system.update) {
        system.update(dt);
      }
    });
  }

  render(alpha) {
    // Interpolated rendering
    this.systems.forEach(system => {
      if (system.render) {
        system.render(alpha);
      }
    });
  }

  addSystem(system) {
    this.systems.push(system);
    if (system.init) system.init(this);
  }
}
```

#### Day 3-4: Scene Management
**Topics:**
- Scene graph architecture
- Scene loading/unloading
- Asset management
- State machines

**Scene Manager:**
```javascript
class SceneManager {
  constructor(engine) {
    this.engine = engine;
    this.scenes = new Map();
    this.currentScene = null;
    this.loadingScene = null;
  }

  registerScene(name, sceneClass) {
    this.scenes.set(name, sceneClass);
  }

  async loadScene(name, transition = null) {
    const SceneClass = this.scenes.get(name);
    if (!SceneClass) {
      throw new Error(`Scene '${name}' not found`);
    }

    this.loadingScene = name;

    // Unload current scene
    if (this.currentScene) {
      if (transition) await transition.out(this.currentScene);
      await this.currentScene.unload();
      this.currentScene = null;
    }

    // Load new scene
    const scene = new SceneClass(this.engine);
    await scene.preload();
    await scene.load();

    this.currentScene = scene;
    this.loadingScene = null;

    if (transition) await transition.in(scene);

    scene.onEnter();
  }

  getCurrentScene() {
    return this.currentScene;
  }
}

// Example scene implementation
class GameScene {
  constructor(engine) {
    this.engine = engine;
    this.entities = [];
    this.assets = new Map();
  }

  async preload() {
    // Show loading screen, start asset loading
    const assetList = this.getAssetList();
    const promises = assetList.map(asset => this.loadAsset(asset));
    await Promise.all(promises);
  }

  async load() {
    // Initialize game objects, systems
    this.setupSystems();
    this.createEntities();
  }

  onEnter() {
    // Scene entered, start gameplay
  }

  update(dt) {
    this.entities.forEach(entity => entity.update(dt));
  }

  render(alpha) {
    this.entities.forEach(entity => entity.render(alpha));
  }

  async unload() {
    // Cleanup
    this.entities.forEach(entity => entity.destroy());
    this.entities = [];
    this.assets.forEach(asset => asset.dispose());
    this.assets.clear();
  }

  getAssetList() {
    return [];
  }

  loadAsset(assetConfig) {
    // Asset loading implementation
  }

  setupSystems() {
    // System setup
  }

  createEntities() {
    // Entity creation
  }
}
```

#### Day 5-7: Entity Component System (ECS)
**Topics:**
- ECS vs OOP architectures
- Component design
- System implementation
- Entity management

**ECS Implementation:**
```javascript
// Component base class
class Component {
  constructor(entity) {
    this.entity = entity;
    this.enabled = true;
  }

  init() {}
  update(dt) {}
  destroy() {}
}

// Entity class
class Entity {
  constructor(id, name = 'Entity') {
    this.id = id;
    this.name = name;
    this.components = new Map();
    this.tags = new Set();
    this.active = true;
  }

  addComponent(componentClass, ...args) {
    const component = new componentClass(this, ...args);
    this.components.set(componentClass.name, component);
    component.init();
    return component;
  }

  getComponent(componentClass) {
    return this.components.get(componentClass.name);
  }

  hasComponent(componentClass) {
    return this.components.has(componentClass.name);
  }

  removeComponent(componentClass) {
    const component = this.components.get(componentClass.name);
    if (component) {
      component.destroy();
      this.components.delete(componentClass.name);
    }
  }

  addTag(tag) {
    this.tags.add(tag);
  }

  hasTag(tag) {
    return this.tags.has(tag);
  }

  update(dt) {
    if (!this.active) return;
    this.components.forEach(component => {
      if (component.enabled && component.update) {
        component.update(dt);
      }
    });
  }

  destroy() {
    this.components.forEach(component => component.destroy());
    this.components.clear();
  }
}

// System base class
class System {
  constructor() {
    this.entities = [];
    this.requiredComponents = [];
  }

  init(engine) {
    this.engine = engine;
  }

  addEntity(entity) {
    if (this.matchesRequirements(entity)) {
      this.entities.push(entity);
      this.onEntityAdded(entity);
    }
  }

  removeEntity(entity) {
    const index = this.entities.indexOf(entity);
    if (index !== -1) {
      this.entities.splice(index, 1);
      this.onEntityRemoved(entity);
    }
  }

  matchesRequirements(entity) {
    return this.requiredComponents.every(comp =>
      entity.hasComponent(comp)
    );
  }

  update(dt) {}
  fixedUpdate(dt) {}
  render(alpha) {}
  onEntityAdded(entity) {}
  onEntityRemoved(entity) {}
}

// Entity Manager
class EntityManager {
  constructor() {
    this.entities = new Map();
    this.systems = [];
    this.nextEntityId = 0;
  }

  createEntity(name) {
    const entity = new Entity(this.nextEntityId++, name);
    this.entities.set(entity.id, entity);

    // Notify systems
    this.systems.forEach(system => system.addEntity(entity));

    return entity;
  }

  destroyEntity(entityId) {
    const entity = this.entities.get(entityId);
    if (entity) {
      this.systems.forEach(system => system.removeEntity(entity));
      entity.destroy();
      this.entities.delete(entityId);
    }
  }

  getEntity(id) {
    return this.entities.get(id);
  }

  getEntitiesByTag(tag) {
    return Array.from(this.entities.values()).filter(e => e.hasTag(tag));
  }

  addSystem(system) {
    this.systems.push(system);
    // Add existing entities to new system
    this.entities.forEach(entity => system.addEntity(entity));
  }

  update(dt) {
    this.entities.forEach(entity => entity.update(dt));
  }
}
```

### Week 2: Core Engine Systems

#### Day 1-2: Input System
**Topics:**
- Input abstraction layer
- Keyboard, mouse, gamepad support
- Input mapping and rebinding
- Action-based input

**Input System:**
```javascript
class InputManager {
  constructor() {
    this.keys = new Map();
    this.mouseButtons = new Map();
    this.mousePosition = { x: 0, y: 0 };
    this.mouseDelta = { x: 0, y: 0 };
    this.gamepadIndex = null;
    this.actions = new Map();

    this.setupListeners();
  }

  setupListeners() {
    window.addEventListener('keydown', e => this.onKeyDown(e));
    window.addEventListener('keyup', e => this.onKeyUp(e));
    window.addEventListener('mousedown', e => this.onMouseDown(e));
    window.addEventListener('mouseup', e => this.onMouseUp(e));
    window.addEventListener('mousemove', e => this.onMouseMove(e));
    window.addEventListener('gamepadconnected', e => this.onGamepadConnected(e));
  }

  onKeyDown(event) {
    if (!this.keys.get(event.code)) {
      this.keys.set(event.code, {
        pressed: true,
        justPressed: true,
        justReleased: false
      });
    }
  }

  onKeyUp(event) {
    this.keys.set(event.code, {
      pressed: false,
      justPressed: false,
      justReleased: true
    });
  }

  isKeyPressed(keyCode) {
    return this.keys.get(keyCode)?.pressed || false;
  }

  isKeyJustPressed(keyCode) {
    return this.keys.get(keyCode)?.justPressed || false;
  }

  // Action mapping
  mapAction(actionName, inputs) {
    this.actions.set(actionName, inputs);
  }

  isActionPressed(actionName) {
    const inputs = this.actions.get(actionName);
    if (!inputs) return false;

    return inputs.some(input => {
      if (input.type === 'key') {
        return this.isKeyPressed(input.code);
      } else if (input.type === 'mouse') {
        return this.mouseButtons.get(input.button)?.pressed;
      } else if (input.type === 'gamepad') {
        return this.getGamepadButton(input.button);
      }
      return false;
    });
  }

  update() {
    // Clear just pressed/released flags
    this.keys.forEach((state, key) => {
      if (state.justPressed) state.justPressed = false;
      if (state.justReleased) state.justReleased = false;
    });

    this.mouseButtons.forEach((state, button) => {
      if (state.justPressed) state.justPressed = false;
      if (state.justReleased) state.justReleased = false;
    });
  }

  getGamepadState() {
    if (this.gamepadIndex === null) return null;
    const gamepad = navigator.getGamepads()[this.gamepadIndex];
    return gamepad;
  }
}
```

#### Day 3-4: Audio System
**Topics:**
- Web Audio API
- Sound effects and music management
- 3D spatial audio
- Audio pooling

#### Day 5-7: Physics System
**Topics:**
- Collision detection (AABB, SAT, GJK)
- Response and resolution
- Spatial partitioning (Quadtree, BVH)
- Integration with rendering

**Physics System:**
```javascript
class PhysicsSystem extends System {
  constructor() {
    super();
    this.requiredComponents = [TransformComponent, RigidBodyComponent];
    this.gravity = { x: 0, y: 9.8 };
    this.spatialHash = new SpatialHash(100); // 100 unit cells
  }

  fixedUpdate(dt) {
    // Apply forces
    this.entities.forEach(entity => {
      const rb = entity.getComponent(RigidBodyComponent);
      const transform = entity.getComponent(TransformComponent);

      if (!rb.isStatic) {
        // Apply gravity
        rb.velocity.y += this.gravity.y * dt;

        // Apply velocity
        transform.position.x += rb.velocity.x * dt;
        transform.position.y += rb.velocity.y * dt;

        // Apply drag
        rb.velocity.x *= (1 - rb.drag);
        rb.velocity.y *= (1 - rb.drag);
      }
    });

    // Collision detection
    this.detectCollisions();
  }

  detectCollisions() {
    this.spatialHash.clear();

    // Insert all entities into spatial hash
    this.entities.forEach(entity => {
      const transform = entity.getComponent(TransformComponent);
      const rb = entity.getComponent(RigidBodyComponent);
      this.spatialHash.insert(entity, transform.position, rb.bounds);
    });

    // Check potential collisions
    this.entities.forEach(entity1 => {
      const transform1 = entity1.getComponent(TransformComponent);
      const rb1 = entity1.getComponent(RigidBodyComponent);

      const nearby = this.spatialHash.getNearby(transform1.position, rb1.bounds);

      nearby.forEach(entity2 => {
        if (entity1.id >= entity2.id) return; // Avoid duplicate checks

        const transform2 = entity2.getComponent(TransformComponent);
        const rb2 = entity2.getComponent(RigidBodyComponent);

        if (this.checkAABB(transform1.position, rb1.bounds,
                          transform2.position, rb2.bounds)) {
          this.resolveCollision(entity1, entity2);
        }
      });
    });
  }

  checkAABB(pos1, bounds1, pos2, bounds2) {
    return pos1.x < pos2.x + bounds2.width &&
           pos1.x + bounds1.width > pos2.x &&
           pos1.y < pos2.y + bounds2.height &&
           pos1.y + bounds1.height > pos2.y;
  }

  resolveCollision(entity1, entity2) {
    // Collision resolution logic
    const rb1 = entity1.getComponent(RigidBodyComponent);
    const rb2 = entity2.getComponent(RigidBodyComponent);

    // Emit collision events
    entity1.emit('collision', { other: entity2 });
    entity2.emit('collision', { other: entity1 });
  }
}

class SpatialHash {
  constructor(cellSize) {
    this.cellSize = cellSize;
    this.cells = new Map();
  }

  getKey(x, y) {
    return `${Math.floor(x / this.cellSize)},${Math.floor(y / this.cellSize)}`;
  }

  insert(entity, position, bounds) {
    const minX = position.x;
    const minY = position.y;
    const maxX = position.x + bounds.width;
    const maxY = position.y + bounds.height;

    const startCell = this.getKey(minX, minY);
    const endCell = this.getKey(maxX, maxY);

    // Insert into all overlapping cells
    for (let x = minX; x <= maxX; x += this.cellSize) {
      for (let y = minY; y <= maxY; y += this.cellSize) {
        const key = this.getKey(x, y);
        if (!this.cells.has(key)) {
          this.cells.set(key, []);
        }
        this.cells.get(key).push(entity);
      }
    }
  }

  getNearby(position, bounds) {
    const key = this.getKey(position.x, position.y);
    return this.cells.get(key) || [];
  }

  clear() {
    this.cells.clear();
  }
}
```

### Week 3: Advanced Engine Features

#### Day 1-3: Event System
**Topics:**
- Observer pattern
- Event dispatching
- Event queuing
- Priority systems

#### Day 4-7: Resource Management
**Topics:**
- Asset loading pipeline
- Memory management
- Resource pooling
- Streaming

### Week 4: Plugin Architecture

#### Day 1-4: Plugin System Design
**Topics:**
- Plugin interfaces
- Dependency injection
- Hot reloading
- Version management

**Plugin Architecture:**
```javascript
class PluginManager {
  constructor(engine) {
    this.engine = engine;
    this.plugins = new Map();
    this.hooks = new Map();
  }

  async loadPlugin(pluginPath) {
    const module = await import(pluginPath);
    const Plugin = module.default;

    if (!Plugin.metadata) {
      throw new Error('Plugin missing metadata');
    }

    // Check dependencies
    const deps = Plugin.metadata.dependencies || [];
    for (const dep of deps) {
      if (!this.plugins.has(dep)) {
        throw new Error(`Missing dependency: ${dep}`);
      }
    }

    const plugin = new Plugin(this.engine);
    await plugin.onLoad();

    this.plugins.set(Plugin.metadata.name, plugin);

    // Register hooks
    if (plugin.hooks) {
      Object.entries(plugin.hooks).forEach(([hookName, handler]) => {
        this.registerHook(hookName, handler);
      });
    }

    return plugin;
  }

  registerHook(hookName, handler) {
    if (!this.hooks.has(hookName)) {
      this.hooks.set(hookName, []);
    }
    this.hooks.get(hookName).push(handler);
  }

  async callHook(hookName, ...args) {
    const handlers = this.hooks.get(hookName) || [];
    for (const handler of handlers) {
      await handler(...args);
    }
  }

  getPlugin(name) {
    return this.plugins.get(name);
  }
}

// Example plugin
class DebugPlugin {
  static metadata = {
    name: 'debug',
    version: '1.0.0',
    dependencies: []
  }

  constructor(engine) {
    this.engine = engine;
    this.enabled = true;
  }

  async onLoad() {
    console.log('Debug plugin loaded');
    this.setupDebugUI();
  }

  setupDebugUI() {
    // Debug UI setup
  }

  get hooks() {
    return {
      'engine.update': (dt) => {
        if (this.enabled) {
          this.debugUpdate(dt);
        }
      },
      'engine.render': (alpha) => {
        if (this.enabled) {
          this.debugRender(alpha);
        }
      }
    };
  }
}
```

### Week 5: Optimization & Tools

#### Day 1-3: Profiling & Debugging
**Topics:**
- Performance profiling
- Memory profiling
- Debug visualization
- Logging systems

#### Day 4-7: Editor Integration
**Topics:**
- Level editor architecture
- Serialization
- Real-time preview
- Asset pipeline

### Final Week: Capstone Project

**Build a Complete Game Engine**

Requirements:
- ECS architecture
- Scene management
- Input system
- Physics system (2D or 3D)
- Audio system
- Resource management
- Plugin system
- Debug tools

---

## 🎓 Assignments & Projects

### Assignment 1: Custom ECS Implementation
Build an ECS from scratch with:
- At least 5 component types
- At least 3 system types
- Entity pooling
- Component serialization

### Assignment 2: Physics Engine
Implement a 2D physics engine:
- AABB collision detection
- SAT for polygon collisions
- Spatial hashing optimization
- Collision response

### Assignment 3: Plugin System
Create a plugin architecture:
- Hot reload support
- Dependency management
- Event hooks
- 3 example plugins

### Final Project: Complete Game Engine
Build a full game engine and create a small game with it.

**Deliverables:**
- Engine source code
- API documentation
- Example game
- Performance benchmarks
- Plugin examples

---

## 📖 Resources

### Books
- "Game Engine Architecture" by Jason Gregory
- "Game Programming Patterns" by Robert Nystrom
- "Real-Time Collision Detection" by Christer Ericson

### Articles
- [Overwatch Gameplay Architecture](https://www.youtube.com/watch?v=W3aieHjyNvw)
- [Unity ECS Deep Dive](https://docs.unity3d.com/Packages/com.unity.entities@0.1/manual/)
- [Bevy Engine Architecture](https://bevyengine.org/learn/book/introduction/)

### Open Source Engines
- Phaser (JavaScript)
- Godot (C++/GDScript)
- Bevy (Rust)

---

## ✅ Assessment Criteria

### Technical Implementation (50%)
- Code architecture and design
- Performance optimization
- System decoupling

### Documentation (20%)
- API documentation
- Architecture diagrams
- Usage examples

### Final Project (30%)
- Engine completeness
- Game demonstration
- Innovation

**Passing Grade:** 75%

---

## 💼 Career Applications

- Game Engine Programmer
- Technical Director
- Tools Programmer
- Engine Architect

**Average Salary:** $90,000 - $180,000

---

**Module Created:** 2025-11-02
**Last Updated:** 2025-11-02
