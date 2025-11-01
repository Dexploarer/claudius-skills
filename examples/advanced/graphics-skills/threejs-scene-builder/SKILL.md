---
name: threejs-scene-builder
description: Generates Three.js scene setups with camera, lights, materials, and optimizations for 3D web graphics. Use when user asks to "create Three.js scene", "setup 3D scene", "generate WebGL scene", or "create 3D visualization".
allowed-tools: [Write, Read]
---

# Three.js Scene Builder

Generates complete Three.js scene setups with proper camera, lighting, materials, and performance optimizations for 3D web graphics.

## When to Use

- "Create Three.js scene"
- "Setup 3D scene"
- "Generate WebGL visualization"
- "Create interactive 3D graphics"
- "Setup Three.js boilerplate"

## Instructions

### 1. Install Three.js

```bash
npm install three
# TypeScript types
npm install --save-dev @types/three
```

### 2. Basic Scene Setup

**TypeScript:**
```typescript
// scene.ts
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

export class SceneManager {
  private scene: THREE.Scene;
  private camera: THREE.PerspectiveCamera;
  private renderer: THREE.WebGLRenderer;
  private controls: OrbitControls;
  private animationId: number | null = null;

  constructor(container: HTMLElement) {
    // Scene
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x1a1a1a);
    this.scene.fog = new THREE.Fog(0x1a1a1a, 10, 50);

    // Camera
    this.camera = new THREE.PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000
    );
    this.camera.position.set(5, 5, 5);
    this.camera.lookAt(0, 0, 0);

    // Renderer
    this.renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true,
    });
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    container.appendChild(this.renderer.domElement);

    // Controls
    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.05;
    this.controls.minDistance = 2;
    this.controls.maxDistance = 20;

    // Lights
    this.setupLights();

    // Handle resize
    window.addEventListener('resize', () => this.onWindowResize());

    // Start animation
    this.animate();
  }

  private setupLights() {
    // Ambient light
    const ambient = new THREE.AmbientLight(0xffffff, 0.4);
    this.scene.add(ambient);

    // Directional light (sun)
    const directional = new THREE.DirectionalLight(0xffffff, 0.8);
    directional.position.set(5, 10, 5);
    directional.castShadow = true;
    directional.shadow.camera.left = -10;
    directional.shadow.camera.right = 10;
    directional.shadow.camera.top = 10;
    directional.shadow.camera.bottom = -10;
    directional.shadow.mapSize.width = 2048;
    directional.shadow.mapSize.height = 2048;
    this.scene.add(directional);

    // Hemisphere light
    const hemisphere = new THREE.HemisphereLight(0xffffbb, 0x080820, 0.3);
    this.scene.add(hemisphere);
  }

  private onWindowResize() {
    this.camera.aspect = window.innerWidth / window.innerHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(window.innerWidth, window.innerHeight);
  }

  private animate() {
    this.animationId = requestAnimationFrame(() => this.animate());
    this.controls.update();
    this.renderer.render(this.scene, this.camera);
  }

  public addObject(object: THREE.Object3D) {
    this.scene.add(object);
  }

  public dispose() {
    if (this.animationId !== null) {
      cancelAnimationFrame(this.animationId);
    }
    this.renderer.dispose();
    this.controls.dispose();
  }
}

// Usage
const container = document.getElementById('canvas-container')!;
const sceneManager = new SceneManager(container);

// Add a cube
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
cube.castShadow = true;
cube.receiveShadow = true;
sceneManager.addObject(cube);
```

### 3. Advanced Material Setup

```typescript
// materials.ts
import * as THREE from 'three';

export class MaterialLibrary {
  // PBR Material
  static createPBRMaterial(options: {
    color?: number;
    roughness?: number;
    metalness?: number;
    normalMap?: THREE.Texture;
    roughnessMap?: THREE.Texture;
  }) {
    return new THREE.MeshStandardMaterial({
      color: options.color ?? 0xffffff,
      roughness: options.roughness ?? 0.5,
      metalness: options.metalness ?? 0.5,
      normalMap: options.normalMap,
      roughnessMap: options.roughnessMap,
    });
  }

  // Glass Material
  static createGlassMaterial() {
    return new THREE.MeshPhysicalMaterial({
      color: 0xffffff,
      metalness: 0,
      roughness: 0,
      transmission: 1,
      thickness: 0.5,
    });
  }

  // Glowing Material
  static createGlowMaterial(color: number = 0x00ff00) {
    return new THREE.MeshBasicMaterial({
      color,
      transparent: true,
      opacity: 0.8,
      blending: THREE.AdditiveBlending,
    });
  }

  // Toon Material
  static createToonMaterial(color: number = 0x00ff00) {
    return new THREE.MeshToonMaterial({
      color,
      gradientMap: this.createGradientTexture(),
    });
  }

  private static createGradientTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 256;
    canvas.height = 1;
    const ctx = canvas.getContext('2d')!;
    const gradient = ctx.createLinearGradient(0, 0, 256, 0);
    gradient.addColorStop(0, '#000000');
    gradient.addColorStop(0.5, '#808080');
    gradient.addColorStop(1, '#ffffff');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 256, 1);
    return new THREE.CanvasTexture(canvas);
  }
}
```

### 4. Geometry Helpers

```typescript
// geometries.ts
import * as THREE from 'three';

export class GeometryHelpers {
  static createGroundPlane(size: number = 20) {
    const geometry = new THREE.PlaneGeometry(size, size);
    const material = new THREE.MeshStandardMaterial({
      color: 0x808080,
      roughness: 0.8,
      metalness: 0.2,
    });
    const plane = new THREE.Mesh(geometry, material);
    plane.rotation.x = -Math.PI / 2;
    plane.receiveShadow = true;
    return plane;
  }

  static createSkybox(textureLoader: THREE.TextureLoader, path: string) {
    const loader = new THREE.CubeTextureLoader();
    const texture = loader.load([
      `${path}/px.jpg`, `${path}/nx.jpg`,
      `${path}/py.jpg`, `${path}/ny.jpg`,
      `${path}/pz.jpg`, `${path}/nz.jpg`,
    ]);
    return texture;
  }

  static createParticles(count: number = 1000) {
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(count * 3);

    for (let i = 0; i < count * 3; i++) {
      positions[i] = (Math.random() - 0.5) * 20;
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const material = new THREE.PointsMaterial({
      size: 0.05,
      color: 0xffffff,
      transparent: true,
      opacity: 0.8,
      blending: THREE.AdditiveBlending,
    });

    return new THREE.Points(geometry, material);
  }
}
```

### 5. Animation System

```typescript
// animation.ts
import * as THREE from 'three';

export class AnimationController {
  private mixer: THREE.AnimationMixer;
  private actions: Map<string, THREE.AnimationAction> = new Map();

  constructor(model: THREE.Object3D, animations: THREE.AnimationClip[]) {
    this.mixer = new THREE.AnimationMixer(model);

    animations.forEach((clip, index) => {
      const action = this.mixer.clipAction(clip);
      this.actions.set(clip.name || `animation_${index}`, action);
    });
  }

  play(name: string, fadeIn: number = 0.5) {
    const action = this.actions.get(name);
    if (action) {
      action.reset().fadeIn(fadeIn).play();
    }
  }

  stop(name: string, fadeOut: number = 0.5) {
    const action = this.actions.get(name);
    if (action) {
      action.fadeOut(fadeOut);
    }
  }

  update(deltaTime: number) {
    this.mixer.update(deltaTime);
  }
}
```

### 6. Model Loading

```typescript
// loader.ts
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader';

export class ModelLoader {
  private gltfLoader: GLTFLoader;
  private textureLoader: THREE.TextureLoader;
  private loadingManager: THREE.LoadingManager;

  constructor(onProgress?: (progress: number) => void) {
    this.loadingManager = new THREE.LoadingManager();

    if (onProgress) {
      this.loadingManager.onProgress = (url, loaded, total) => {
        onProgress((loaded / total) * 100);
      };
    }

    // Setup DRACO loader for compressed models
    const dracoLoader = new DRACOLoader(this.loadingManager);
    dracoLoader.setDecoderPath('/draco/');

    this.gltfLoader = new GLTFLoader(this.loadingManager);
    this.gltfLoader.setDRACOLoader(dracoLoader);

    this.textureLoader = new THREE.TextureLoader(this.loadingManager);
  }

  async loadGLTF(url: string): Promise<THREE.Group> {
    return new Promise((resolve, reject) => {
      this.gltfLoader.load(
        url,
        (gltf) => {
          gltf.scene.traverse((child) => {
            if (child instanceof THREE.Mesh) {
              child.castShadow = true;
              child.receiveShadow = true;
            }
          });
          resolve(gltf.scene);
        },
        undefined,
        reject
      );
    });
  }

  async loadTexture(url: string): Promise<THREE.Texture> {
    return new Promise((resolve, reject) => {
      this.textureLoader.load(url, resolve, undefined, reject);
    });
  }
}
```

### 7. Post-Processing

```typescript
// post-processing.ts
import * as THREE from 'three';
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass';
import { SSAOPass } from 'three/examples/jsm/postprocessing/SSAOPass';

export class PostProcessing {
  private composer: EffectComposer;

  constructor(
    renderer: THREE.WebGLRenderer,
    scene: THREE.Scene,
    camera: THREE.Camera
  ) {
    this.composer = new EffectComposer(renderer);

    // Render pass
    const renderPass = new RenderPass(scene, camera);
    this.composer.addPass(renderPass);

    // Bloom pass
    const bloomPass = new UnrealBloomPass(
      new THREE.Vector2(window.innerWidth, window.innerHeight),
      1.5,  // strength
      0.4,  // radius
      0.85  // threshold
    );
    this.composer.addPass(bloomPass);

    // SSAO pass
    const ssaoPass = new SSAOPass(scene, camera);
    ssaoPass.kernelRadius = 16;
    this.composer.addPass(ssaoPass);
  }

  render() {
    this.composer.render();
  }

  resize(width: number, height: number) {
    this.composer.setSize(width, height);
  }
}
```

### 8. Performance Optimization

```typescript
// optimization.ts
import * as THREE from 'three';

export class PerformanceOptimizer {
  static optimizeGeometry(geometry: THREE.BufferGeometry) {
    // Merge vertices
    geometry.computeVertexNormals();
    geometry.normalizeNormals();
    return geometry;
  }

  static createLOD(geometries: THREE.BufferGeometry[], distances: number[]) {
    const lod = new THREE.LOD();

    geometries.forEach((geometry, index) => {
      const material = new THREE.MeshStandardMaterial();
      const mesh = new THREE.Mesh(geometry, material);
      lod.addLevel(mesh, distances[index]);
    });

    return lod;
  }

  static enableInstancing(
    geometry: THREE.BufferGeometry,
    material: THREE.Material,
    count: number,
    positions: THREE.Vector3[]
  ) {
    const mesh = new THREE.InstancedMesh(geometry, material, count);

    const matrix = new THREE.Matrix4();
    positions.forEach((pos, i) => {
      matrix.setPosition(pos);
      mesh.setMatrixAt(i, matrix);
    });

    mesh.instanceMatrix.needsUpdate = true;
    return mesh;
  }

  static setupFrustumCulling(camera: THREE.Camera, objects: THREE.Object3D[]) {
    const frustum = new THREE.Frustum();
    const projScreenMatrix = new THREE.Matrix4();

    return () => {
      camera.updateMatrixWorld();
      projScreenMatrix.multiplyMatrices(
        camera.projectionMatrix,
        camera.matrixWorldInverse
      );
      frustum.setFromProjectionMatrix(projScreenMatrix);

      objects.forEach((obj) => {
        obj.visible = frustum.intersectsObject(obj);
      });
    };
  }
}
```

### 9. React Integration

```typescript
// ThreeCanvas.tsx
import React, { useEffect, useRef } from 'react';
import { SceneManager } from './scene';

export const ThreeCanvas: React.FC = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const sceneManagerRef = useRef<SceneManager | null>(null);

  useEffect(() => {
    if (!containerRef.current) return;

    // Initialize scene
    sceneManagerRef.current = new SceneManager(containerRef.current);

    // Cleanup
    return () => {
      sceneManagerRef.current?.dispose();
    };
  }, []);

  return (
    <div
      ref={containerRef}
      style={{ width: '100vw', height: '100vh' }}
    />
  );
};
```

### 10. Complete Example

```typescript
// main.ts
import * as THREE from 'three';
import { SceneManager } from './scene';
import { GeometryHelpers } from './geometries';
import { MaterialLibrary } from './materials';
import { ModelLoader } from './loader';

async function main() {
  const container = document.getElementById('app')!;
  const scene = new SceneManager(container);

  // Add ground plane
  const ground = GeometryHelpers.createGroundPlane();
  scene.addObject(ground);

  // Add particles
  const particles = GeometryHelpers.createParticles(5000);
  scene.addObject(particles);

  // Load model
  const loader = new ModelLoader((progress) => {
    console.log(`Loading: ${progress.toFixed(0)}%`);
  });

  try {
    const model = await loader.loadGLTF('/models/scene.gltf');
    model.scale.set(2, 2, 2);
    scene.addObject(model);
  } catch (error) {
    console.error('Failed to load model:', error);
  }

  // Add rotating cube with PBR material
  const cubeGeo = new THREE.BoxGeometry();
  const cubeMat = MaterialLibrary.createPBRMaterial({
    color: 0x2194ce,
    roughness: 0.3,
    metalness: 0.8,
  });
  const cube = new THREE.Mesh(cubeGeo, cubeMat);
  cube.position.y = 1;
  scene.addObject(cube);

  // Animation loop
  function animate() {
    requestAnimationFrame(animate);
    cube.rotation.y += 0.01;
  }
  animate();
}

main();
```

### Best Practices

**DO:**
- Use BufferGeometry
- Enable frustum culling
- Use instanced meshes for many objects
- Optimize textures
- Use LOD for distant objects
- Dispose geometries and materials
- Limit shadow maps
- Use post-processing sparingly

**DON'T:**
- Create objects in render loop
- Use high-poly models without LOD
- Forget to dispose resources
- Use too many lights
- Skip texture compression
- Render at native device pixel ratio on mobile
- Update uniforms every frame unnecessarily

## Checklist

- [ ] Three.js installed
- [ ] Scene, camera, renderer setup
- [ ] Lighting configured
- [ ] Controls added
- [ ] Materials created
- [ ] Models loaded
- [ ] Animations working
- [ ] Performance optimized
- [ ] Responsive design
- [ ] Cleanup implemented
