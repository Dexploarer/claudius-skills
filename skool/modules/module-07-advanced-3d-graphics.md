# Module 7: Advanced 3D Graphics & Rendering

## 🎯 Learning Objectives

By the end of this module, you will:
- Master advanced Three.js rendering techniques
- Implement custom shaders and materials
- Optimize 3D performance for production
- Create realistic lighting and shadows
- Build interactive 3D environments
- Understand GPU programming fundamentals

---

## 📚 Module Overview

**Duration:** 4-6 weeks
**Difficulty:** Advanced
**Prerequisites:** Basic Three.js, JavaScript ES6+, Linear algebra basics

---

## 🗓️ Week-by-Week Breakdown

### Week 1: Advanced Rendering Techniques

#### Day 1-2: Custom Shaders
**Topics:**
- GLSL fundamentals
- Vertex and fragment shaders
- Shader uniforms and attributes
- ShaderMaterial in Three.js

**Practical Exercise:**
```javascript
// Custom animated shader material
const vertexShader = `
  varying vec2 vUv;
  varying vec3 vPosition;
  uniform float time;

  void main() {
    vUv = uv;
    vPosition = position;

    vec3 pos = position;
    pos.z += sin(pos.x * 10.0 + time) * 0.1;

    gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
  }
`;

const fragmentShader = `
  varying vec2 vUv;
  varying vec3 vPosition;
  uniform float time;
  uniform vec3 color1;
  uniform vec3 color2;

  void main() {
    float mixer = sin(vUv.y * 10.0 + time) * 0.5 + 0.5;
    vec3 color = mix(color1, color2, mixer);
    gl_FragColor = vec4(color, 1.0);
  }
`;

const material = new THREE.ShaderMaterial({
  vertexShader,
  fragmentShader,
  uniforms: {
    time: { value: 0 },
    color1: { value: new THREE.Color(0x00ff00) },
    color2: { value: new THREE.Color(0x0000ff) }
  }
});
```

**Assignment:** Create a custom shader that simulates water waves

#### Day 3-4: Post-Processing Effects
**Topics:**
- EffectComposer setup
- Built-in passes (Bloom, DOF, SSAO)
- Custom post-processing passes
- Performance optimization

**Code Example:**
```javascript
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass';
import { SSAOPass } from 'three/examples/jsm/postprocessing/SSAOPass';

class AdvancedRenderer {
  constructor(scene, camera, renderer) {
    this.composer = new EffectComposer(renderer);

    // Base render
    const renderPass = new RenderPass(scene, camera);
    this.composer.addPass(renderPass);

    // SSAO for realistic ambient occlusion
    const ssaoPass = new SSAOPass(scene, camera, window.innerWidth, window.innerHeight);
    ssaoPass.kernelRadius = 16;
    this.composer.addPass(ssaoPass);

    // Bloom for glowing effects
    const bloomPass = new UnrealBloomPass(
      new THREE.Vector2(window.innerWidth, window.innerHeight),
      1.5, 0.4, 0.85
    );
    this.composer.addPass(bloomPass);
  }

  render() {
    this.composer.render();
  }
}
```

#### Day 5-7: Advanced Lighting Systems
**Topics:**
- PBR (Physically Based Rendering)
- IBL (Image-Based Lighting)
- Light probes and reflection probes
- Shadow mapping techniques

**Project:** Build a realistic product showcase with IBL

### Week 2: Performance Optimization

#### Day 1-3: GPU Optimization
**Topics:**
- Draw call batching
- Instancing for repeated geometry
- Level of Detail (LOD) systems
- Frustum culling
- Occlusion culling

**Implementation Example:**
```javascript
class OptimizedScene {
  constructor() {
    this.instancedMeshes = new Map();
    this.lodLevels = 3;
  }

  // Instanced rendering for massive object counts
  createInstancedObjects(geometry, material, count) {
    const mesh = new THREE.InstancedMesh(geometry, material, count);
    const dummy = new THREE.Object3D();

    for (let i = 0; i < count; i++) {
      dummy.position.set(
        Math.random() * 100 - 50,
        Math.random() * 100 - 50,
        Math.random() * 100 - 50
      );
      dummy.rotation.set(
        Math.random() * Math.PI,
        Math.random() * Math.PI,
        Math.random() * Math.PI
      );
      dummy.updateMatrix();
      mesh.setMatrixAt(i, dummy.matrix);
    }

    mesh.instanceMatrix.needsUpdate = true;
    return mesh;
  }

  // LOD system for distant objects
  createLODObject(geometries, material) {
    const lod = new THREE.LOD();

    const distances = [0, 50, 100];
    geometries.forEach((geometry, index) => {
      const mesh = new THREE.Mesh(geometry, material);
      lod.addLevel(mesh, distances[index]);
    });

    return lod;
  }

  // Frustum culling optimization
  updateVisibility(camera) {
    const frustum = new THREE.Frustum();
    const matrix = new THREE.Matrix4().multiplyMatrices(
      camera.projectionMatrix,
      camera.matrixWorldInverse
    );
    frustum.setFromProjectionMatrix(matrix);

    this.scene.traverse((object) => {
      if (object.isMesh) {
        object.visible = frustum.intersectsObject(object);
      }
    });
  }
}
```

#### Day 4-7: Memory Management
**Topics:**
- Texture atlas creation
- Geometry merging
- Dispose patterns
- Memory leak prevention

**Performance Checklist:**
- [ ] Reduce draw calls to < 100
- [ ] Keep triangle count under budget
- [ ] Use texture atlases
- [ ] Implement object pooling
- [ ] Profile with Chrome DevTools

### Week 3: Advanced Materials & Textures

#### Day 1-3: PBR Materials
**Topics:**
- Albedo, metalness, roughness maps
- Normal and displacement mapping
- Ambient occlusion
- Environment mapping

**Material Setup:**
```javascript
class PBRMaterialBuilder {
  static async createMaterial(texturePaths) {
    const textureLoader = new THREE.TextureLoader();

    const [albedo, normal, metalness, roughness, ao] = await Promise.all([
      textureLoader.loadAsync(texturePaths.albedo),
      textureLoader.loadAsync(texturePaths.normal),
      textureLoader.loadAsync(texturePaths.metalness),
      textureLoader.loadAsync(texturePaths.roughness),
      textureLoader.loadAsync(texturePaths.ao)
    ]);

    return new THREE.MeshStandardMaterial({
      map: albedo,
      normalMap: normal,
      metalnessMap: metalness,
      roughnessMap: roughness,
      aoMap: ao,
      envMapIntensity: 1.0
    });
  }
}
```

#### Day 4-7: Procedural Textures
**Topics:**
- Noise functions in shaders
- Procedural patterns
- Dynamic texture generation
- Texture streaming

### Week 4: Interactive 3D Environments

#### Day 1-3: Physics Integration
**Topics:**
- Cannon.js / Ammo.js setup
- Rigid body dynamics
- Collision detection
- Raycasting for interaction

**Physics System:**
```javascript
import CANNON from 'cannon';

class PhysicsWorld {
  constructor() {
    this.world = new CANNON.World();
    this.world.gravity.set(0, -9.82, 0);
    this.bodies = [];
  }

  createRigidBody(mesh, mass = 1, shape = 'box') {
    let cannonShape;

    if (shape === 'box') {
      const box = new THREE.Box3().setFromObject(mesh);
      const size = box.getSize(new THREE.Vector3());
      cannonShape = new CANNON.Box(new CANNON.Vec3(
        size.x / 2,
        size.y / 2,
        size.z / 2
      ));
    } else if (shape === 'sphere') {
      cannonShape = new CANNON.Sphere(mesh.geometry.parameters.radius);
    }

    const body = new CANNON.Body({
      mass,
      shape: cannonShape,
      position: new CANNON.Vec3(
        mesh.position.x,
        mesh.position.y,
        mesh.position.z
      )
    });

    this.world.addBody(body);
    this.bodies.push({ mesh, body });

    return body;
  }

  update(deltaTime) {
    this.world.step(1 / 60, deltaTime);

    this.bodies.forEach(({ mesh, body }) => {
      mesh.position.copy(body.position);
      mesh.quaternion.copy(body.quaternion);
    });
  }
}
```

#### Day 4-7: Advanced Interactions
**Topics:**
- Object picking and selection
- Drag and drop in 3D
- Gizmos and handles
- VR/AR interactions

**Final Project:** Create an interactive 3D configurator with physics

---

## 🎓 Assignments & Projects

### Assignment 1: Custom Shader Library
Create a library of 5 reusable shaders:
1. Animated gradient
2. Holographic effect
3. Dissolve effect
4. Fresnel glow
5. Stylized toon shader

### Assignment 2: Performance Optimization Challenge
Take a poorly optimized scene (provided) and:
- Reduce draw calls by 80%
- Improve framerate from 30fps to 60fps
- Implement LOD system
- Add object pooling

### Assignment 3: PBR Material Showcase
Create a material showcase featuring:
- 10 different PBR materials
- Proper lighting setup
- Environment reflections
- Interactive material editor

### Final Project: Interactive 3D Experience
Build a complete interactive 3D application:
- Custom shaders and materials
- Physics simulation
- Post-processing effects
- Optimized for 60fps
- Mobile-responsive

**Requirements:**
- Minimum 100 interactive objects
- Custom shader effects
- Performance budget: < 16ms frame time
- Full documentation

---

## 📖 Resources

### Required Reading
- [The Book of Shaders](https://thebookofshaders.com/)
- [Learn OpenGL - PBR Theory](https://learnopengl.com/PBR/Theory)
- [Three.js Documentation](https://threejs.org/docs/)

### Video Tutorials
- "Advanced Three.js" by Bruno Simon
- "Shader Programming Fundamentals" series
- "GPU Performance Optimization" talks from GDC

### Tools
- [Shader Toy](https://www.shadertoy.com/) - Shader experimentation
- [glslEditor](http://editor.thebookofshaders.com/) - GLSL practice
- [Three.js Editor](https://threejs.org/editor/) - Scene building

---

## ✅ Assessment Criteria

### Knowledge Check (30%)
- Shader programming quiz
- Performance optimization scenarios
- Material theory questions

### Assignments (40%)
- Code quality and organization
- Creative implementation
- Performance metrics

### Final Project (30%)
- Technical complexity
- User experience
- Performance optimization
- Code documentation

**Passing Grade:** 70%

---

## 🎯 Learning Outcomes

Upon completion, you will be able to:
- ✅ Write custom GLSL shaders
- ✅ Implement advanced rendering techniques
- ✅ Optimize 3D applications for production
- ✅ Create realistic materials using PBR
- ✅ Build interactive 3D environments
- ✅ Debug and profile GPU performance

---

## 💼 Career Applications

This module prepares you for:
- 3D Web Developer
- WebGL Specialist
- Graphics Programmer
- Technical Artist
- VR/AR Developer

**Average Salary Range:** $80,000 - $150,000

---

## 🔄 Next Steps

After completing this module:
- **Module 8:** Game Engine Architecture
- **Module 9:** Multiplayer Systems
- **Advanced Tutorial:** Building a 3D Product Configurator
- **Genre Deep-Dive:** First-Person 3D Games

---

**Module Created:** 2025-11-02
**Last Updated:** 2025-11-02
**Instructor:** Claudius Skills Team
**Support:** [Discord Community](#) | [Office Hours](#)
