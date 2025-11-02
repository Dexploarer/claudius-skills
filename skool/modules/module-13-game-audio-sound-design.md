# Module 13: Game Audio & Sound Design

## 🎯 Learning Objectives

- Implement dynamic audio systems with Web Audio API
- Create adaptive music systems
- Design sound effects for game events
- Implement 3D spatial audio
- Optimize audio performance
- Master audio middleware (FMOD, Wwise concepts)

**Duration:** 4-5 weeks | **Difficulty:** Intermediate

---

## 🗓️ Core Topics

### Week 1: Web Audio API Fundamentals

```javascript
class GameAudioEngine {
  constructor() {
    this.context = new (window.AudioContext || window.webkitAudioContext)();
    this.masterGain = this.context.createGain();
    this.masterGain.connect(this.context.destination);

    this.sounds = new Map();
    this.music = null;
    this.soundPool = new Map();
  }

  async loadSound(name, url) {
    const response = await fetch(url);
    const arrayBuffer = await response.arrayBuffer();
    const audioBuffer = await this.context.decodeAudioData(arrayBuffer);

    this.sounds.set(name, audioBuffer);
    return audioBuffer;
  }

  playSound(name, options = {}) {
    const buffer = this.sounds.get(name);
    if (!buffer) return null;

    const source = this.context.createBufferSource();
    source.buffer = buffer;

    const gainNode = this.context.createGain();
    gainNode.gain.value = options.volume || 1.0;

    source.connect(gainNode);
    gainNode.connect(this.masterGain);

    if (options.loop) {
      source.loop = true;
      source.loopStart = options.loopStart || 0;
      source.loopEnd = options.loopEnd || buffer.duration;
    }

    if (options.playbackRate) {
      source.playbackRate.value = options.playbackRate;
    }

    source.start(0, options.offset || 0);

    return { source, gainNode };
  }

  // 3D Spatial Audio
  create3DSound(name, position, options = {}) {
    const buffer = this.sounds.get(name);
    if (!buffer) return null;

    const source = this.context.createBufferSource();
    source.buffer = buffer;

    const panner = this.context.createPanner();
    panner.panningModel = 'HRTF';
    panner.distanceModel = 'inverse';
    panner.refDistance = options.refDistance || 1;
    panner.maxDistance = options.maxDistance || 10000;
    panner.rolloffFactor = options.rolloffFactor || 1;
    panner.coneInnerAngle = options.coneInnerAngle || 360;
    panner.coneOuterAngle = options.coneOuterAngle || 0;
    panner.coneOuterGain = options.coneOuterGain || 0;

    panner.setPosition(position.x, position.y, position.z);

    source.connect(panner);
    panner.connect(this.masterGain);

    source.start(0);

    return { source, panner };
  }

  setListenerPosition(position, orientation) {
    const listener = this.context.listener;

    if (listener.positionX) {
      listener.positionX.value = position.x;
      listener.positionY.value = position.y;
      listener.positionZ.value = position.z;

      listener.forwardX.value = orientation.forward.x;
      listener.forwardY.value = orientation.forward.y;
      listener.forwardZ.value = orientation.forward.z;

      listener.upX.value = orientation.up.x;
      listener.upY.value = orientation.up.y;
      listener.upZ.value = orientation.up.z;
    } else {
      listener.setPosition(position.x, position.y, position.z);
      listener.setOrientation(
        orientation.forward.x, orientation.forward.y, orientation.forward.z,
        orientation.up.x, orientation.up.y, orientation.up.z
      );
    }
  }
}
```

### Week 2: Adaptive Music System

```javascript
class AdaptiveMusicSystem {
  constructor(audioEngine) {
    this.audioEngine = audioEngine;
    this.layers = new Map();
    this.currentIntensity = 0;
    this.targetIntensity = 0;
    this.transitionSpeed = 2.0; // Intensity units per second
  }

  async loadMusicLayers(baseName, layerUrls) {
    const layers = [];

    for (let i = 0; i < layerUrls.length; i++) {
      const layer = await this.audioEngine.loadSound(
        `${baseName}_layer${i}`,
        layerUrls[i]
      );
      layers.push(layer);
    }

    this.layers.set(baseName, layers);
  }

  playAdaptiveMusic(name) {
    const layers = this.layers.get(name);
    if (!layers) return;

    const activeLayers = [];

    layers.forEach((layer, index) => {
      const audio = this.audioEngine.playSound(`${name}_layer${index}`, {
        loop: true,
        volume: 0
      });

      activeLayers.push({
        audio,
        intensity: index / (layers.length - 1)
      });
    });

    this.currentMusic = { name, layers: activeLayers };
  }

  setIntensity(intensity) {
    this.targetIntensity = Math.max(0, Math.min(1, intensity));
  }

  update(deltaTime) {
    if (!this.currentMusic) return;

    // Smoothly transition intensity
    if (this.currentIntensity < this.targetIntensity) {
      this.currentIntensity = Math.min(
        this.targetIntensity,
        this.currentIntensity + this.transitionSpeed * deltaTime
      );
    } else if (this.currentIntensity > this.targetIntensity) {
      this.currentIntensity = Math.max(
        this.targetIntensity,
        this.currentIntensity - this.transitionSpeed * deltaTime
      );
    }

    // Update layer volumes
    this.currentMusic.layers.forEach(layer => {
      const distance = Math.abs(layer.intensity - this.currentIntensity);
      const volume = Math.max(0, 1 - distance * 2);

      layer.audio.gainNode.gain.setTargetAtTime(
        volume,
        this.audioEngine.context.currentTime,
        0.1
      );
    });
  }

  // Vertical remixing
  enableLayer(layerIndex, fadeTime = 1.0) {
    const layer = this.currentMusic.layers[layerIndex];
    if (layer) {
      layer.audio.gainNode.gain.linearRampToValueAtTime(
        1.0,
        this.audioEngine.context.currentTime + fadeTime
      );
    }
  }

  disableLayer(layerIndex, fadeTime = 1.0) {
    const layer = this.currentMusic.layers[layerIndex];
    if (layer) {
      layer.audio.gainNode.gain.linearRampToValueAtTime(
        0.0,
        this.audioEngine.context.currentTime + fadeTime
      );
    }
  }

  // Horizontal re-sequencing
  scheduleTransition(nextSection, bars = 4) {
    const beatsPerBar = 4;
    const bpm = 120;
    const beatsPerSecond = bpm / 60;
    const transitionTime = (bars * beatsPerBar) / beatsPerSecond;

    setTimeout(() => {
      this.crossfadeMusic(nextSection, 2.0);
    }, transitionTime * 1000);
  }

  crossfadeMusic(nextName, duration = 2.0) {
    const current = this.currentMusic;

    if (current) {
      current.layers.forEach(layer => {
        layer.audio.gainNode.gain.linearRampToValueAtTime(
          0.0,
          this.audioEngine.context.currentTime + duration
        );
      });

      setTimeout(() => {
        current.layers.forEach(layer => {
          layer.audio.source.stop();
        });
      }, duration * 1000);
    }

    this.playAdaptiveMusic(nextName);
  }
}
```

### Week 3: Audio Effects & Processing

```javascript
class AudioEffectsProcessor {
  constructor(audioContext) {
    this.context = audioContext;
    this.effects = new Map();
  }

  createReverb(impulseResponse) {
    const convolver = this.context.createConvolver();
    convolver.buffer = impulseResponse;

    const wetGain = this.context.createGain();
    const dryGain = this.context.createGain();

    wetGain.gain.value = 0.5;
    dryGain.gain.value = 0.5;

    return {
      input: convolver,
      output: wetGain,
      wetGain,
      dryGain,
      process: (source) => {
        source.connect(convolver);
        source.connect(dryGain);
        convolver.connect(wetGain);
      }
    };
  }

  createDelay(delayTime = 0.5, feedback = 0.5) {
    const delay = this.context.createDelay();
    delay.delayTime.value = delayTime;

    const feedbackGain = this.context.createGain();
    feedbackGain.gain.value = feedback;

    delay.connect(feedbackGain);
    feedbackGain.connect(delay);

    return {
      input: delay,
      output: delay,
      delay,
      feedbackGain
    };
  }

  createFilter(type = 'lowpass', frequency = 1000) {
    const filter = this.context.createBiquadFilter();
    filter.type = type;
    filter.frequency.value = frequency;

    return filter;
  }

  createCompressor() {
    const compressor = this.context.createDynamicsCompressor();
    compressor.threshold.value = -24;
    compressor.knee.value = 30;
    compressor.ratio.value = 12;
    compressor.attack.value = 0.003;
    compressor.release.value = 0.25;

    return compressor;
  }

  // Chain effects
  createEffectChain(effects) {
    for (let i = 0; i < effects.length - 1; i++) {
      effects[i].connect(effects[i + 1]);
    }

    return {
      input: effects[0],
      output: effects[effects.length - 1]
    };
  }
}
```

### Week 4: Sound Design Techniques

```javascript
class ProceduralSoundGenerator {
  constructor(audioContext) {
    this.context = audioContext;
  }

  // Laser/Shoot sound
  createLaserSound() {
    const osc = this.context.createOscillator();
    const gainNode = this.context.createGain();

    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(800, this.context.currentTime);
    osc.frequency.exponentialRampToValueAtTime(
      100,
      this.context.currentTime + 0.3
    );

    gainNode.gain.setValueAtTime(0.3, this.context.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(
      0.01,
      this.context.currentTime + 0.3
    );

    osc.connect(gainNode);
    gainNode.connect(this.context.destination);

    osc.start();
    osc.stop(this.context.currentTime + 0.3);
  }

  // Explosion sound
  createExplosionSound() {
    const bufferSize = this.context.sampleRate * 2;
    const buffer = this.context.createBuffer(1, bufferSize, this.context.sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (this.context.sampleRate * 0.5));
    }

    const source = this.context.createBufferSource();
    source.buffer = buffer;

    const filter = this.context.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(2000, this.context.currentTime);
    filter.frequency.exponentialRampToValueAtTime(
      50,
      this.context.currentTime + 1.0
    );

    const gainNode = this.context.createGain();
    gainNode.gain.setValueAtTime(0.5, this.context.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(
      0.01,
      this.context.currentTime + 1.0
    );

    source.connect(filter);
    filter.connect(gainNode);
    gainNode.connect(this.context.destination);

    source.start();
  }

  // Footstep sound
  createFootstepSound(surface = 'wood') {
    const frequencies = {
      wood: [200, 400, 800],
      metal: [400, 800, 1600],
      grass: [150, 300, 600]
    };

    const freqs = frequencies[surface];

    const noise = this.createNoiseBuffer(0.1);
    const source = this.context.createBufferSource();
    source.buffer = noise;

    const filter = this.context.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.value = freqs[1];
    filter.Q.value = 2;

    const gainNode = this.context.createGain();
    gainNode.gain.setValueAtTime(0.3, this.context.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(
      0.01,
      this.context.currentTime + 0.15
    );

    source.connect(filter);
    filter.connect(gainNode);
    gainNode.connect(this.context.destination);

    source.start();
  }

  createNoiseBuffer(duration) {
    const bufferSize = this.context.sampleRate * duration;
    const buffer = this.context.createBuffer(1, bufferSize, this.context.sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < bufferSize; i++) {
      data[i] = Math.random() * 2 - 1;
    }

    return buffer;
  }
}
```

---

## 🎓 Projects

1. **Audio Engine** - Complete game audio system
2. **Adaptive Music Demo** - Dynamic music that responds to gameplay
3. **Sound Library** - Collection of procedural sound effects
4. **3D Audio Scene** - Spatial audio environment

---

## 📖 Resources

- Web Audio API documentation
- "The Game Audio Tutorial" by Stevens & Raybould
- freesound.org - Free sound effects
- FMOD/Wwise tutorials

---

## ✅ Assessment

**Passing Grade:** 70%
- Audio system implementation (40%)
- Sound design quality (30%)
- Final project (30%)

**Career Paths:** Audio Programmer, Sound Designer, Technical Sound Designer

**Salary Range:** $65,000 - $130,000

---

**Module Created:** 2025-11-02
