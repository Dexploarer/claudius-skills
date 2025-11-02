# Module 6: Framework-Specific Game Development

**Master popular frameworks with AI assistance - build games for any platform**

*Unlock Requirement: Community Level 3*

---

## Lesson 6.1: React Game Development with AI

### Why React for Games?

**React is PERFECT for:**
- Browser-based games
- UI-heavy games (card games, strategy)
- Turn-based games
- Puzzle games
- Hybrid games (React UI + Canvas gameplay)

**Benefits:**
- Component-based architecture
- State management built-in
- Huge ecosystem
- Hot reload for fast iteration
- Easy deployment

### Building a React Game in 15 Minutes

**Step 1: Generate React Game Boilerplate (2 minutes)**

Tell Claude Code:
```
Create a React game project with TypeScript:

SETUP:
- Vite for fast dev server
- TypeScript for type safety
- React 18 with hooks
- CSS Modules for styling
- Game loop with requestAnimationFrame
- Component structure for game systems

PROJECT STRUCTURE:
src/
├── components/
│   ├── Game.tsx         # Main game component
│   ├── Player.tsx       # Player component
│   ├── Enemy.tsx        # Enemy component
│   ├── UI/              # UI components
│   └── Canvas.tsx       # Canvas wrapper
├── hooks/
│   ├── useGameLoop.ts   # Game loop hook
│   ├── useInput.ts      # Input handling hook
│   └── useCollision.ts  # Collision detection
├── systems/
│   ├── PhysicsSystem.ts
│   ├── RenderSystem.ts
│   └── AudioSystem.ts
└── types/
    └── game.ts          # Type definitions

Include package.json, tsconfig.json, and vite.config.ts
```

**AI generates complete React game foundation!**

**Generated Code:**

```typescript
// src/hooks/useGameLoop.ts
import { useEffect, useRef, useCallback } from 'react';

export function useGameLoop(
  update: (deltaTime: number) => void,
  fps: number = 60
) {
  const requestRef = useRef<number>();
  const previousTimeRef = useRef<number>();
  const fpsInterval = 1000 / fps;

  const animate = useCallback((time: number) => {
    if (previousTimeRef.current !== undefined) {
      const deltaTime = time - previousTimeRef.current;

      if (deltaTime >= fpsInterval) {
        update(deltaTime / 1000); // Convert to seconds
        previousTimeRef.current = time - (deltaTime % fpsInterval);
      }
    } else {
      previousTimeRef.current = time;
    }

    requestRef.current = requestAnimationFrame(animate);
  }, [update, fpsInterval]);

  useEffect(() => {
    requestRef.current = requestAnimationFrame(animate);
    return () => {
      if (requestRef.current) {
        cancelAnimationFrame(requestRef.current);
      }
    };
  }, [animate]);
}

// src/hooks/useInput.ts
import { useEffect, useState, useCallback } from 'react';

interface InputState {
  keys: Set<string>;
  mouse: {
    x: number;
    y: number;
    buttons: Set<number>;
  };
}

export function useInput() {
  const [input, setInput] = useState<InputState>({
    keys: new Set(),
    mouse: { x: 0, y: 0, buttons: new Set() }
  });

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      setInput(prev => ({
        ...prev,
        keys: new Set(prev.keys).add(e.key.toLowerCase())
      }));
    };

    const handleKeyUp = (e: KeyboardEvent) => {
      setInput(prev => {
        const newKeys = new Set(prev.keys);
        newKeys.delete(e.key.toLowerCase());
        return { ...prev, keys: newKeys };
      });
    };

    const handleMouseMove = (e: MouseEvent) => {
      setInput(prev => ({
        ...prev,
        mouse: { ...prev.mouse, x: e.clientX, y: e.clientY }
      }));
    };

    const handleMouseDown = (e: MouseEvent) => {
      setInput(prev => ({
        ...prev,
        mouse: {
          ...prev.mouse,
          buttons: new Set(prev.mouse.buttons).add(e.button)
        }
      }));
    };

    const handleMouseUp = (e: MouseEvent) => {
      setInput(prev => {
        const newButtons = new Set(prev.mouse.buttons);
        newButtons.delete(e.button);
        return {
          ...prev,
          mouse: { ...prev.mouse, buttons: newButtons }
        };
      });
    };

    window.addEventListener('keydown', handleKeyDown);
    window.addEventListener('keyup', handleKeyUp);
    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('mousedown', handleMouseDown);
    window.addEventListener('mouseup', handleMouseUp);

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      window.removeEventListener('keyup', handleKeyUp);
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('mousedown', handleMouseDown);
      window.removeEventListener('mouseup', handleMouseUp);
    };
  }, []);

  const isKeyPressed = useCallback(
    (key: string) => input.keys.has(key.toLowerCase()),
    [input.keys]
  );

  const isMouseButtonPressed = useCallback(
    (button: number) => input.mouse.buttons.has(button),
    [input.mouse.buttons]
  );

  return {
    input,
    isKeyPressed,
    isMouseButtonPressed
  };
}

// src/components/Game.tsx
import React, { useState, useCallback, useRef } from 'react';
import { useGameLoop } from '../hooks/useGameLoop';
import { useInput } from '../hooks/useInput';
import Canvas from './Canvas';
import UI from './UI/GameUI';
import styles from './Game.module.css';

interface GameState {
  player: {
    x: number;
    y: number;
    vx: number;
    vy: number;
    health: number;
  };
  enemies: Array<{
    id: number;
    x: number;
    y: number;
    health: number;
  }>;
  score: number;
  gameOver: boolean;
}

const Game: React.FC = () => {
  const [gameState, setGameState] = useState<GameState>({
    player: { x: 400, y: 300, vx: 0, vy: 0, health: 100 },
    enemies: [],
    score: 0,
    gameOver: false
  });

  const { isKeyPressed, input } = useInput();
  const canvasRef = useRef<HTMLCanvasElement>(null);

  // Game update logic
  const update = useCallback((deltaTime: number) => {
    if (gameState.gameOver) return;

    setGameState(prev => {
      const newState = { ...prev };

      // Player movement
      const speed = 300;
      if (isKeyPressed('a') || isKeyPressed('arrowleft')) {
        newState.player.vx = -speed;
      } else if (isKeyPressed('d') || isKeyPressed('arrowright')) {
        newState.player.vx = speed;
      } else {
        newState.player.vx = 0;
      }

      if (isKeyPressed('w') || isKeyPressed('arrowup')) {
        newState.player.vy = -speed;
      } else if (isKeyPressed('s') || isKeyPressed('arrowdown')) {
        newState.player.vy = speed;
      } else {
        newState.player.vy = 0;
      }

      // Update player position
      newState.player.x += newState.player.vx * deltaTime;
      newState.player.y += newState.player.vy * deltaTime;

      // Keep player in bounds
      newState.player.x = Math.max(0, Math.min(800 - 32, newState.player.x));
      newState.player.y = Math.max(0, Math.min(600 - 32, newState.player.y));

      // Update enemies (simple AI)
      newState.enemies = newState.enemies.map(enemy => {
        const dx = newState.player.x - enemy.x;
        const dy = newState.player.y - enemy.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance > 5) {
          const enemySpeed = 100;
          enemy.x += (dx / distance) * enemySpeed * deltaTime;
          enemy.y += (dy / distance) * enemySpeed * deltaTime;
        }

        return enemy;
      });

      // Collision detection
      newState.enemies.forEach(enemy => {
        const dx = newState.player.x - enemy.x;
        const dy = newState.player.y - enemy.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < 32) {
          newState.player.health -= 1;
          if (newState.player.health <= 0) {
            newState.gameOver = true;
          }
        }
      });

      return newState;
    });
  }, [gameState.gameOver, isKeyPressed]);

  // Use game loop
  useGameLoop(update, 60);

  // Render logic
  const render = useCallback((ctx: CanvasRenderingContext2D) => {
    // Clear canvas
    ctx.fillStyle = '#1a1a2e';
    ctx.fillRect(0, 0, 800, 600);

    // Draw player
    ctx.fillStyle = '#00ff00';
    ctx.fillRect(gameState.player.x, gameState.player.y, 32, 32);

    // Draw enemies
    ctx.fillStyle = '#ff0000';
    gameState.enemies.forEach(enemy => {
      ctx.fillRect(enemy.x, enemy.y, 32, 32);
    });
  }, [gameState]);

  return (
    <div className={styles.gameContainer}>
      <Canvas
        width={800}
        height={600}
        render={render}
        canvasRef={canvasRef}
      />
      <UI
        score={gameState.score}
        health={gameState.player.health}
        gameOver={gameState.gameOver}
      />
    </div>
  );
};

export default Game;

// src/components/Canvas.tsx
import React, { useEffect, useRef } from 'react';

interface CanvasProps {
  width: number;
  height: number;
  render: (ctx: CanvasRenderingContext2D) => void;
  canvasRef?: React.RefObject<HTMLCanvasElement>;
}

const Canvas: React.FC<CanvasProps> = ({
  width,
  height,
  render,
  canvasRef: externalRef
}) => {
  const internalRef = useRef<HTMLCanvasElement>(null);
  const ref = externalRef || internalRef;

  useEffect(() => {
    const canvas = ref.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationId: number;

    const animate = () => {
      render(ctx);
      animationId = requestAnimationFrame(animate);
    };

    animate();

    return () => {
      cancelAnimationFrame(animationId);
    };
  }, [render, ref]);

  return (
    <canvas
      ref={ref}
      width={width}
      height={height}
      style={{ border: '1px solid #333', display: 'block' }}
    />
  );
};

export default Canvas;

// package.json
{
  "name": "react-game",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "test": "vitest"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@vitejs/plugin-react": "^4.2.0",
    "typescript": "^5.3.0",
    "vite": "^5.0.0",
    "vitest": "^1.0.0"
  }
}
```

**Step 2: Add Specific Game Features (10 minutes)**

```
Add to the React game:

FEATURES:
- Top-down shooter gameplay
- Enemy spawning system (wave-based)
- Power-ups (health, speed boost, shield)
- Particle effects for shooting
- Score system with combo multiplier
- Pause menu with React components
- Settings panel (volume, difficulty)
- High score persistence
- Weapon upgrade system
```

**AI adds everything with clean React patterns!**

**Step 3: Polish UI (3 minutes)**

```
Create beautiful game UI with:
- Animated health bar
- Score counter with pop effect
- Wave indicator
- Weapon display
- Power-up timers
- Victory/defeat screens
- Responsive layout for mobile

Use Tailwind CSS or styled-components
```

### React Game Patterns

**Pattern 1: State Management**

```typescript
// Using Zustand for game state
import create from 'zustand';

interface GameStore {
  player: Player;
  enemies: Enemy[];
  score: number;
  updatePlayer: (updates: Partial<Player>) => void;
  addEnemy: (enemy: Enemy) => void;
  removeEnemy: (id: number) => void;
  incrementScore: (amount: number) => void;
}

export const useGameStore = create<GameStore>((set) => ({
  player: { x: 0, y: 0, health: 100 },
  enemies: [],
  score: 0,

  updatePlayer: (updates) =>
    set((state) => ({
      player: { ...state.player, ...updates }
    })),

  addEnemy: (enemy) =>
    set((state) => ({
      enemies: [...state.enemies, enemy]
    })),

  removeEnemy: (id) =>
    set((state) => ({
      enemies: state.enemies.filter((e) => e.id !== id)
    })),

  incrementScore: (amount) =>
    set((state) => ({
      score: state.score + amount
    }))
}));
```

**Pattern 2: Component Composition**

```tsx
// Composable game UI
<GameContainer>
  <GameCanvas>
    <Player />
    <EnemyList enemies={enemies} />
    <ProjectileList projectiles={projectiles} />
    <ParticleSystem />
  </GameCanvas>

  <GameUI>
    <HealthBar health={player.health} />
    <ScoreDisplay score={score} />
    <WeaponIndicator weapon={player.weapon} />
    <MiniMap entities={entities} />
  </GameUI>

  {isPaused && <PauseMenu onResume={resume} />}
  {gameOver && <GameOverScreen score={score} />}
</GameContainer>
```

**Pattern 3: Custom Hooks**

```typescript
// Reusable game hooks
function useCollision(entity1: Entity, entity2: Entity) {
  const [isColliding, setIsColliding] = useState(false);

  useEffect(() => {
    const checkCollision = () => {
      const collision = detectCollision(entity1, entity2);
      setIsColliding(collision);
    };

    const interval = setInterval(checkCollision, 16);
    return () => clearInterval(interval);
  }, [entity1, entity2]);

  return isColliding;
}

function useSpawner(spawnFunction: () => void, interval: number) {
  useEffect(() => {
    const timer = setInterval(spawnFunction, interval);
    return () => clearInterval(timer);
  }, [spawnFunction, interval]);
}
```

### Real Project: Card Game

```
Create a deck-building card game in React with:

GAMEPLAY:
- Draw cards from deck
- Play cards (cost mana)
- Attack opponent
- End turn
- AI opponent

FEATURES:
- Drag-and-drop cards
- Animated card effects
- Deck builder UI
- Collection manager
- Deck statistics

TECHNICAL:
- React DnD for dragging
- Framer Motion for animations
- React Spring for physics
- Immer for state updates

Include 50 unique cards with effects
```

**AI generates complete card game!**

---

## Lesson 6.2: Vue 3 Game Development

### Why Vue for Games?

**Perfect for:**
- Browser games
- Progressive web apps
- Mobile-first games
- Prototype-to-production

**Benefits:**
- Simple learning curve
- Composition API (flexible)
- Reactivity system (powerful)
- Small bundle size
- Great tooling (Vite)

### Building a Vue Game

**Generate Vue game with AI:**

```
Create a Vue 3 game with TypeScript and Composition API:

GAME: Tower Defense

FEATURES:
- Grid-based tower placement
- Enemy pathfinding
- Tower upgrades
- Wave system
- Resource management

TECH STACK:
- Vue 3 Composition API
- TypeScript
- Pinia for state management
- Vite for building
- Canvas for rendering
- Web Workers for pathfinding

Generate complete project structure with components, stores, and utilities
```

**AI creates production-ready Vue game!**

```vue
<!-- components/Game.vue -->
<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { useGameStore } from '@/stores/game';
import { useGameLoop } from '@/composables/useGameLoop';
import GameCanvas from './GameCanvas.vue';
import TowerSelector from './TowerSelector.vue';
import WaveIndicator from './WaveIndicator.vue';

const gameStore = useGameStore();
const { start, stop } = useGameLoop(update, 60);

function update(deltaTime: number) {
  gameStore.update(deltaTime);
}

function handleCellClick(x: number, y: number) {
  if (gameStore.selectedTower) {
    gameStore.placeTower(x, y, gameStore.selectedTower);
  }
}

onMounted(() => {
  start();
});

onUnmounted(() => {
  stop();
});
</script>

<template>
  <div class="game">
    <GameCanvas
      :grid="gameStore.grid"
      :towers="gameStore.towers"
      :enemies="gameStore.enemies"
      @cell-click="handleCellClick"
    />

    <div class="ui">
      <TowerSelector
        :towers="availableTowers"
        :selected="gameStore.selectedTower"
        @select="gameStore.selectTower"
      />

      <WaveIndicator
        :current-wave="gameStore.currentWave"
        :next-wave-in="gameStore.nextWaveIn"
      />

      <div class="resources">
        <span>Gold: {{ gameStore.gold }}</span>
        <span>Lives: {{ gameStore.lives }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.game {
  display: flex;
  gap: 20px;
}

.ui {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>

<!-- composables/useGameLoop.ts -->
import { ref } from 'vue';

export function useGameLoop(
  update: (deltaTime: number) => void,
  fps: number = 60
) {
  const isRunning = ref(false);
  let animationId: number;
  let lastTime = 0;

  function gameLoop(currentTime: number) {
    if (!isRunning.value) return;

    const deltaTime = (currentTime - lastTime) / 1000;
    lastTime = currentTime;

    if (deltaTime < 1) {
      update(deltaTime);
    }

    animationId = requestAnimationFrame(gameLoop);
  }

  function start() {
    if (isRunning.value) return;

    isRunning.value = true;
    lastTime = performance.now();
    animationId = requestAnimationFrame(gameLoop);
  }

  function stop() {
    isRunning.value = false;
    if (animationId) {
      cancelAnimationFrame(animationId);
    }
  }

  return { start, stop, isRunning };
}

// stores/game.ts
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useGameStore = defineStore('game', () => {
  // State
  const towers = ref<Tower[]>([]);
  const enemies = ref<Enemy[]>([]);
  const gold = ref(100);
  const lives = ref(20);
  const currentWave = ref(0);
  const nextWaveIn = ref(10);
  const selectedTower = ref<string | null>(null);

  // Computed
  const canAffordTower = computed(() => (towerType: string) => {
    const tower = towerTypes[towerType];
    return gold.value >= tower.cost;
  });

  // Actions
  function update(deltaTime: number) {
    // Update towers
    towers.value.forEach(tower => tower.update(deltaTime));

    // Update enemies
    enemies.value.forEach(enemy => enemy.update(deltaTime));

    // Check for dead enemies
    enemies.value = enemies.value.filter(enemy => {
      if (enemy.health <= 0) {
        gold.value += enemy.goldReward;
        return false;
      }
      return true;
    });

    // Update wave timer
    nextWaveIn.value -= deltaTime;
    if (nextWaveIn.value <= 0) {
      spawnWave();
    }
  }

  function placeTower(x: number, y: number, towerType: string) {
    if (!canAffordTower.value(towerType)) return;

    const tower = createTower(x, y, towerType);
    towers.value.push(tower);
    gold.value -= tower.cost;
  }

  function spawnWave() {
    currentWave.value++;
    const enemyCount = 10 + currentWave.value * 2;

    for (let i = 0; i < enemyCount; i++) {
      setTimeout(() => {
        enemies.value.push(createEnemy(currentWave.value));
      }, i * 1000);
    }

    nextWaveIn.value = 30;
  }

  function selectTower(towerType: string | null) {
    selectedTower.value = towerType;
  }

  return {
    towers,
    enemies,
    gold,
    lives,
    currentWave,
    nextWaveIn,
    selectedTower,
    canAffordTower,
    update,
    placeTower,
    spawnWave,
    selectTower
  };
});
```

### Vue Game Advantages

**Reactivity System:**
```vue
<script setup>
const player = reactive({
  x: 100,
  y: 100,
  health: 100
});

// UI automatically updates!
watch(() => player.health, (newHealth) => {
  if (newHealth <= 0) {
    gameOver();
  }
});
</script>
```

**Component Flexibility:**
```vue
<!-- Reusable game components -->
<Enemy
  v-for="enemy in enemies"
  :key="enemy.id"
  :enemy="enemy"
  @killed="handleEnemyKilled"
/>
```

---

## Lesson 6.3: Unity with AI (C#)

### AI-Assisted Unity Development

**The power:**
```
"Create a Unity FPS controller with:
- WASD movement
- Mouse look
- Jump and crouch
- Sprint
- Headbob effect
- Footstep sounds"
```

**AI generates complete C# script:**

```csharp
using UnityEngine;

[RequireComponent(typeof(CharacterController))]
public class FPSController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField] private float walkSpeed = 5f;
    [SerializeField] private float sprintSpeed = 8f;
    [SerializeField] private float crouchSpeed = 2.5f;
    [SerializeField] private float jumpForce = 5f;
    [SerializeField] private float gravity = -9.81f;

    [Header("Mouse Look")]
    [SerializeField] private float mouseSensitivity = 100f;
    [SerializeField] private Transform playerCamera;
    [SerializeField] private float minLookAngle = -80f;
    [SerializeField] private float maxLookAngle = 80f;

    [Header("Crouch")]
    [SerializeField] private float standHeight = 2f;
    [SerializeField] private float crouchHeight = 1f;
    [SerializeField] private float crouchTransitionSpeed = 10f;

    [Header("Headbob")]
    [SerializeField] private bool enableHeadbob = true;
    [SerializeField] private float bobSpeed = 10f;
    [SerializeField] private float bobAmount = 0.05f;

    [Header("Audio")]
    [SerializeField] private AudioClip[] footstepSounds;
    [SerializeField] private float footstepInterval = 0.5f;

    private CharacterController controller;
    private Vector3 velocity;
    private bool isGrounded;
    private bool isCrouching;
    private float xRotation = 0f;
    private float headbobTimer;
    private Vector3 originalCameraPos;
    private float footstepTimer;
    private AudioSource audioSource;

    private void Start()
    {
        controller = GetComponent<CharacterController>();
        audioSource = GetComponent<AudioSource>();

        if (playerCamera == null)
            playerCamera = Camera.main.transform;

        originalCameraPos = playerCamera.localPosition;

        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    private void Update()
    {
        HandleMovement();
        HandleMouseLook();
        HandleCrouch();
        HandleJump();
        HandleHeadbob();
        HandleFootsteps();
    }

    private void HandleMovement()
    {
        isGrounded = controller.isGrounded;

        float moveSpeed = walkSpeed;

        if (Input.GetKey(KeyCode.LeftShift) && !isCrouching)
        {
            moveSpeed = sprintSpeed;
        }

        if (isCrouching)
        {
            moveSpeed = crouchSpeed;
        }

        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");

        Vector3 move = transform.right * x + transform.forward * z;
        controller.Move(move * moveSpeed * Time.deltaTime);

        // Apply gravity
        if (isGrounded && velocity.y < 0)
        {
            velocity.y = -2f;
        }

        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }

    private void HandleMouseLook()
    {
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity * Time.deltaTime;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity * Time.deltaTime;

        xRotation -= mouseY;
        xRotation = Mathf.Clamp(xRotation, minLookAngle, maxLookAngle);

        playerCamera.localRotation = Quaternion.Euler(xRotation, 0f, 0f);
        transform.Rotate(Vector3.up * mouseX);
    }

    private void HandleCrouch()
    {
        if (Input.GetKeyDown(KeyCode.C))
        {
            isCrouching = !isCrouching;
        }

        float targetHeight = isCrouching ? crouchHeight : standHeight;
        controller.height = Mathf.Lerp(
            controller.height,
            targetHeight,
            Time.deltaTime * crouchTransitionSpeed
        );

        Vector3 center = controller.center;
        center.y = controller.height / 2f;
        controller.center = center;
    }

    private void HandleJump()
    {
        if (Input.GetButtonDown("Jump") && isGrounded && !isCrouching)
        {
            velocity.y = Mathf.Sqrt(jumpForce * -2f * gravity);
        }
    }

    private void HandleHeadbob()
    {
        if (!enableHeadbob) return;

        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");
        bool isMoving = Mathf.Abs(horizontalInput) > 0.1f || Mathf.Abs(verticalInput) > 0.1f;

        if (isMoving && isGrounded)
        {
            headbobTimer += Time.deltaTime * bobSpeed;

            float bobOffsetY = Mathf.Sin(headbobTimer) * bobAmount;
            float bobOffsetX = Mathf.Cos(headbobTimer * 0.5f) * bobAmount * 0.5f;

            playerCamera.localPosition = new Vector3(
                originalCameraPos.x + bobOffsetX,
                originalCameraPos.y + bobOffsetY,
                originalCameraPos.z
            );
        }
        else
        {
            headbobTimer = 0f;
            playerCamera.localPosition = Vector3.Lerp(
                playerCamera.localPosition,
                originalCameraPos,
                Time.deltaTime * 5f
            );
        }
    }

    private void HandleFootsteps()
    {
        if (footstepSounds.Length == 0) return;

        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");
        bool isMoving = Mathf.Abs(horizontalInput) > 0.1f || Mathf.Abs(verticalInput) > 0.1f;

        if (isMoving && isGrounded)
        {
            footstepTimer += Time.deltaTime;

            if (footstepTimer >= footstepInterval)
            {
                footstepTimer = 0f;
                AudioClip clip = footstepSounds[Random.Range(0, footstepSounds.Length)];
                audioSource.PlayOneShot(clip);
            }
        }
    }
}
```

**Boom! Production-ready Unity controller!**

### Unity AI Workflow

**1. Generate Scripts:**
```
"Create enemy AI with:
- State machine (Patrol, Chase, Attack, Flee)
- Nav mesh pathfinding
- Attack range detection
- Health system
- Ragdoll on death"
```

**2. Create Systems:**
```
"Generate inventory system for Unity:
- ScriptableObject for items
- UI with drag-drop
- Save/load with JSON
- Equipment slots
- Item tooltips"
```

**3. Build Tools:**
```
"Create Unity editor tool for:
- Level generation
- Spawn point placement
- LOD group setup
- Batch renaming"
```

---

**Module 6 continues with Godot, Phaser, and more frameworks - shall I continue with more modules and guides?**
