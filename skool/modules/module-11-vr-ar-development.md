# Module 11: VR/AR Development

## 🎯 Learning Objectives

- Build immersive VR experiences with WebXR
- Implement hand tracking and controller input
- Create AR applications with marker and markerless tracking
- Optimize for VR performance (90+ FPS)
- Design comfortable VR interactions
- Integrate spatial audio

---

## 📚 Module Overview

**Duration:** 5-6 weeks | **Difficulty:** Advanced
**Prerequisites:** Module 7 (3D Graphics), Three.js

---

## 🗓️ Core Topics

### Week 1-2: WebXR Fundamentals

**VR Setup:**
```javascript
import * as THREE from 'three';
import { VRButton } from 'three/examples/jsm/webxr/VRButton.js';

class VRApp {
  constructor() {
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.xr.enabled = true;
    document.body.appendChild(this.renderer.domElement);
    document.body.appendChild(VRButton.createButton(this.renderer));

    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 100);
    this.camera.position.set(0, 1.6, 3);

    this.controllers = this.setupControllers();
    this.renderer.setAnimationLoop(() => this.render());
  }

  setupControllers() {
    const controllers = [];

    for (let i = 0; i < 2; i++) {
      const controller = this.renderer.xr.getController(i);

      controller.addEventListener('selectstart', () => this.onSelectStart(i));
      controller.addEventListener('selectend', () => this.onSelectEnd(i));
      controller.addEventListener('squeeze', () => this.onSqueeze(i));

      const line = new THREE.Line(
        new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(0, 0, 0),
          new THREE.Vector3(0, 0, -1)
        ]),
        new THREE.LineBasicMaterial({ color: 0xffffff })
      );

      controller.add(line);
      this.scene.add(controller);

      // Controller model
      const grip = this.renderer.xr.getControllerGrip(i);
      controllers.push({ controller, grip, line });
      this.scene.add(grip);
    }

    return controllers;
  }

  onSelectStart(index) {
    const controller = this.controllers[index].controller;
    this.controllers[index].line.material.color.set(0x00ff00);

    // Raycasting
    const raycaster = new THREE.Raycaster();
    const tempMatrix = new THREE.Matrix4();

    tempMatrix.identity().extractRotation(controller.matrixWorld);
    raycaster.ray.origin.setFromMatrixPosition(controller.matrixWorld);
    raycaster.ray.direction.set(0, 0, -1).applyMatrix4(tempMatrix);

    const intersects = raycaster.intersectObjects(this.scene.children, true);

    if (intersects.length > 0) {
      this.handleInteraction(intersects[0].object);
    }
  }

  render() {
    this.renderer.render(this.scene, this.camera);
  }
}
```

**Hand Tracking:**
```javascript
class HandTracking {
  constructor(renderer, scene) {
    this.hand1 = renderer.xr.getHand(0);
    this.hand2 = renderer.xr.getHand(1);

    const handModel1 = new XRHandModelFactory().createHandModel(this.hand1, 'mesh');
    const handModel2 = new XRHandModelFactory().createHandModel(this.hand2, 'mesh');

    this.hand1.add(handModel1);
    this.hand2.add(handModel2);

    scene.add(this.hand1);
    scene.add(this.hand2);

    this.hand1.addEventListener('pinchstart', (e) => this.onPinchStart(e, 0));
    this.hand2.addEventListener('pinchstart', (e) => this.onPinchStart(e, 1));
  }

  onPinchStart(event, handIndex) {
    const hand = handIndex === 0 ? this.hand1 : this.hand2;
    const indexTip = hand.joints['index-finger-tip'];

    if (indexTip) {
      const position = new THREE.Vector3();
      indexTip.getWorldPosition(position);

      // Perform action at pinch position
      this.createParticle(position);
    }
  }

  createParticle(position) {
    const geometry = new THREE.SphereGeometry(0.01);
    const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
    const particle = new THREE.Mesh(geometry, material);
    particle.position.copy(position);
    this.scene.add(particle);
  }
}
```

### Week 3: AR with WebXR

**AR Application:**
```javascript
import { ARButton } from 'three/examples/jsm/webxr/ARButton.js';

class ARApp {
  constructor() {
    this.renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: true
    });
    this.renderer.xr.enabled = true;

    document.body.appendChild(ARButton.createButton(this.renderer, {
      requiredFeatures: ['hit-test'],
      optionalFeatures: ['dom-overlay'],
      domOverlay: { root: document.body }
    }));

    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera();

    this.reticle = this.createReticle();
    this.hitTestSource = null;

    this.renderer.setAnimationLoop((time, frame) => this.render(time, frame));
  }

  createReticle() {
    const geometry = new THREE.RingGeometry(0.15, 0.2, 32);
    const material = new THREE.MeshBasicMaterial();
    const reticle = new THREE.Mesh(geometry, material);

    reticle.matrixAutoUpdate = false;
    reticle.visible = false;
    this.scene.add(reticle);

    return reticle;
  }

  async render(time, frame) {
    if (frame) {
      const referenceSpace = this.renderer.xr.getReferenceSpace();

      if (!this.hitTestSource) {
        const session = this.renderer.xr.getSession();
        session.requestReferenceSpace('viewer').then((viewerSpace) => {
          session.requestHitTestSource({ space: viewerSpace })
            .then((source) => {
              this.hitTestSource = source;
            });
        });
      }

      if (this.hitTestSource) {
        const hitTestResults = frame.getHitTestResults(this.hitTestSource);

        if (hitTestResults.length > 0) {
          const hit = hitTestResults[0];
          const pose = hit.getPose(referenceSpace);

          this.reticle.visible = true;
          this.reticle.matrix.fromArray(pose.transform.matrix);
        } else {
          this.reticle.visible = false;
        }
      }
    }

    this.renderer.render(this.scene, this.camera);
  }

  placeObject() {
    if (this.reticle.visible) {
      const object = this.createARObject();
      object.position.setFromMatrixPosition(this.reticle.matrix);
      this.scene.add(object);
    }
  }
}
```

### Week 4: VR Performance Optimization

**Optimization Techniques:**
```javascript
class VROptimizer {
  constructor(scene, renderer) {
    this.scene = scene;
    this.renderer = renderer;
    this.targetFPS = 90;
    this.lodManager = new LODManager();
  }

  optimize() {
    // Reduce draw calls
    this.mergeMeshes();

    // Use instancing
    this.setupInstancing();

    // Implement foveated rendering
    this.enableFoveatedRendering();

    // Dynamic resolution scaling
    this.setupDynamicResolution();
  }

  mergeMeshes() {
    const geometries = [];
    const materials = [];

    this.scene.traverse((object) => {
      if (object.isMesh && object.userData.mergeable) {
        geometries.push(object.geometry);
        materials.push(object.material);
      }
    });

    if (geometries.length > 0) {
      const mergedGeometry = BufferGeometryUtils.mergeBufferGeometries(geometries);
      const mergedMesh = new THREE.Mesh(mergedGeometry, materials[0]);
      this.scene.add(mergedMesh);
    }
  }

  enableFoveatedRendering() {
    const gl = this.renderer.getContext();
    const ext = gl.getExtension('WEBGL_foveated_rendering');

    if (ext) {
      // Configure foveation
      ext.foveationLevel = 2; // 0-3, higher = more aggressive
    }
  }

  setupDynamicResolution() {
    let targetFrameTime = 1000 / this.targetFPS;
    let currentScale = 1.0;

    this.renderer.setAnimationLoop(() => {
      const frameTime = performance.now();

      // Adjust resolution based on performance
      if (frameTime > targetFrameTime * 1.2) {
        currentScale = Math.max(0.5, currentScale - 0.05);
      } else if (frameTime < targetFrameTime * 0.8) {
        currentScale = Math.min(1.0, currentScale + 0.05);
      }

      this.renderer.xr.setFramebufferScaleFactor(currentScale);
    });
  }
}
```

### Week 5-6: Advanced VR Interactions

**Locomotion System:**
```javascript
class VRLocomotion {
  constructor(camera, controllers) {
    this.camera = camera;
    this.controllers = controllers;
    this.teleportMarker = this.createTeleportMarker();
    this.movementSpeed = 2.0;
  }

  // Teleportation
  teleport(controller) {
    const raycaster = new THREE.Raycaster();
    const tempMatrix = new THREE.Matrix4();

    tempMatrix.identity().extractRotation(controller.matrixWorld);
    raycaster.ray.origin.setFromMatrixPosition(controller.matrixWorld);
    raycaster.ray.direction.set(0, 0, -1).applyMatrix4(tempMatrix);

    const intersects = raycaster.intersectObjects(this.scene.children, true);

    if (intersects.length > 0) {
      const point = intersects[0].point;
      this.teleportMarker.position.copy(point);
      this.teleportMarker.visible = true;

      // On trigger release
      this.camera.position.copy(point);
    }
  }

  // Smooth locomotion
  smoothMove(controller, deltaTime) {
    const gamepad = controller.gamepad;

    if (gamepad && gamepad.axes.length >= 4) {
      const x = gamepad.axes[2];
      const y = gamepad.axes[3];

      if (Math.abs(x) > 0.1 || Math.abs(y) > 0.1) {
        const forward = new THREE.Vector3(0, 0, -1);
        forward.applyQuaternion(this.camera.quaternion);
        forward.y = 0;
        forward.normalize();

        const right = new THREE.Vector3();
        right.crossVectors(forward, new THREE.Vector3(0, 1, 0));

        const movement = new THREE.Vector3();
        movement.addScaledVector(forward, -y);
        movement.addScaledVector(right, x);
        movement.multiplyScalar(this.movementSpeed * deltaTime);

        this.camera.position.add(movement);
      }
    }
  }

  // Snap turning
  snapTurn(direction) {
    const angle = direction * Math.PI / 4; // 45 degrees
    this.camera.rotateY(angle);
  }
}
```

---

## 🎓 Projects

1. **VR Gallery** - Interactive 3D art gallery
2. **AR Furniture Placement** - Place 3D models in real world
3. **VR Game** - Complete VR experience with locomotion
4. **Hand Tracking App** - Gesture-based interactions

---

## 📖 Resources

- [WebXR Device API](https://www.w3.org/TR/webxr/)
- "Learning Virtual Reality" by Tony Parisi
- Oculus Best Practices
- Google ARCore guidelines

---

## ✅ Assessment

**Passing Grade:** 70%
- VR application (30%)
- AR application (30%)
- Performance optimization (20%)
- Final project (20%)

**Career Paths:** VR Developer, AR Engineer, XR Specialist

**Salary Range:** $85,000 - $155,000

---

**Module Created:** 2025-11-02
