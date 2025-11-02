# Module 12: Mobile Game Development

## 🎯 Learning Objectives

- Build cross-platform mobile games (iOS/Android)
- Implement touch controls and gestures
- Optimize for mobile performance and battery life
- Handle different screen sizes and aspect ratios
- Integrate mobile SDKs (ads, analytics, IAP)
- Deploy to app stores

---

## 📚 Module Overview

**Duration:** 5-6 weeks | **Difficulty:** Intermediate-Advanced
**Prerequisites:** Module 7-8, JavaScript/React Native/Unity

---

## 🗓️ Core Topics

### Week 1: Mobile Game Fundamentals

**React Native Game Setup:**
```javascript
import React, { useRef, useEffect } from 'react';
import { View, PanResponder, Dimensions } from 'react-native';
import { GameEngine } from 'react-native-game-engine';

const MobileGame = () => {
  const gameEngine = useRef(null);
  const { width, height } = Dimensions.get('window');

  const panResponder = PanResponder.create({
    onStartShouldSetPanResponder: () => true,
    onPanResponderGrant: (evt, gestureState) => {
      const { locationX, locationY } = evt.nativeEvent;
      handleTouch({ x: locationX, y: locationY });
    },
    onPanResponderMove: (evt, gestureState) => {
      const { moveX, moveY } = gestureState;
      handleDrag({ x: moveX, y: moveY });
    }
  });

  const systems = [
    PhysicsSystem,
    RenderSystem,
    InputSystem
  ];

  return (
    <View style={{ flex: 1 }} {...panResponder.panHandlers}>
      <GameEngine
        ref={gameEngine}
        systems={systems}
        entities={entities}
        running={true}
        style={{ flex: 1 }}
      />
    </View>
  );
};
```

**Touch Input System:**
```javascript
class TouchInputManager {
  constructor() {
    this.touches = new Map();
    this.gestures = {
      tap: [],
      swipe: [],
      pinch: []
    };
  }

  handleTouchStart(touch) {
    this.touches.set(touch.identifier, {
      id: touch.identifier,
      startX: touch.clientX,
      startY: touch.clientY,
      currentX: touch.clientX,
      currentY: touch.clientY,
      startTime: Date.now()
    });
  }

  handleTouchMove(touch) {
    const data = this.touches.get(touch.identifier);
    if (data) {
      data.currentX = touch.clientX;
      data.currentY = touch.clientY;
    }
  }

  handleTouchEnd(touch) {
    const data = this.touches.get(touch.identifier);
    if (!data) return;

    const duration = Date.now() - data.startTime;
    const dx = data.currentX - data.startX;
    const dy = data.currentY - data.startY;
    const distance = Math.sqrt(dx * dx + dy * dy);

    // Detect tap
    if (duration < 300 && distance < 10) {
      this.emit('tap', { x: touch.clientX, y: touch.clientY });
    }

    // Detect swipe
    if (distance > 50) {
      const angle = Math.atan2(dy, dx);
      const direction = this.getSwipeDirection(angle);
      this.emit('swipe', { direction, distance, duration });
    }

    this.touches.delete(touch.identifier);
  }

  getSwipeDirection(angle) {
    const deg = angle * 180 / Math.PI;
    if (deg > -45 && deg < 45) return 'right';
    if (deg >= 45 && deg < 135) return 'down';
    if (deg <= -45 && deg > -135) return 'up';
    return 'left';
  }

  detectPinch() {
    if (this.touches.size === 2) {
      const [touch1, touch2] = Array.from(this.touches.values());

      const currentDist = this.distance(
        touch1.currentX, touch1.currentY,
        touch2.currentX, touch2.currentY
      );

      const startDist = this.distance(
        touch1.startX, touch1.startY,
        touch2.startX, touch2.startY
      );

      const scale = currentDist / startDist;
      this.emit('pinch', { scale });
    }
  }

  distance(x1, y1, x2, y2) {
    return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
  }
}
```

### Week 2: Responsive Design

**Adaptive UI System:**
```javascript
class ResponsiveUI {
  constructor() {
    this.baseWidth = 1920;
    this.baseHeight = 1080;
    this.safeArea = this.getSafeArea();
  }

  getSafeArea() {
    // iOS notch/Android punch-hole handling
    return {
      top: window.safeArea?.top || 0,
      bottom: window.safeArea?.bottom || 0,
      left: window.safeArea?.left || 0,
      right: window.safeArea?.right || 0
    };
  }

  scaleElement(element, originalSize) {
    const scaleX = window.innerWidth / this.baseWidth;
    const scaleY = window.innerHeight / this.baseHeight;
    const scale = Math.min(scaleX, scaleY);

    return {
      width: originalSize.width * scale,
      height: originalSize.height * scale,
      fontSize: originalSize.fontSize * scale
    };
  }

  getAspectRatio() {
    return window.innerWidth / window.innerHeight;
  }

  layoutForAspectRatio() {
    const ratio = this.getAspectRatio();

    if (ratio > 2) {
      // Ultra-wide (foldable phones)
      return 'ultra-wide';
    } else if (ratio > 1.7) {
      // Modern phones (18:9, 19:9, 20:9)
      return 'tall';
    } else if (ratio > 1.5) {
      // Standard (16:9)
      return 'standard';
    } else {
      // Tablets (4:3)
      return 'tablet';
    }
  }
}
```

### Week 3: Performance Optimization

**Mobile Performance:**
```javascript
class MobileOptimizer {
  constructor() {
    this.targetFPS = 60;
    this.renderScale = this.detectRenderScale();
    this.particlePool = new ParticlePool(100);
    this.objectPool = new ObjectPool();
  }

  detectRenderScale() {
    // Detect device performance tier
    const cpuCores = navigator.hardwareConcurrency || 4;
    const memory = navigator.deviceMemory || 4;

    if (cpuCores >= 8 && memory >= 6) {
      return 1.0; // High-end
    } else if (cpuCores >= 4 && memory >= 4) {
      return 0.8; // Mid-range
    } else {
      return 0.6; // Low-end
    }
  }

  optimizeTextures() {
    // Use compressed textures
    const formats = ['astc', 'etc2', 'pvrtc'];

    formats.forEach(format => {
      if (this.supportsFormat(format)) {
        this.loadCompressedTexture(format);
      }
    });
  }

  reduceBatteryDrain() {
    // Lower frame rate when inactive
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        this.targetFPS = 30;
      } else {
        this.targetFPS = 60;
      }
    });

    // Throttle updates
    let lastUpdate = 0;
    const minFrameTime = 1000 / this.targetFPS;

    this.gameLoop = (timestamp) => {
      if (timestamp - lastUpdate >= minFrameTime) {
        this.update((timestamp - lastUpdate) / 1000);
        lastUpdate = timestamp;
      }
      requestAnimationFrame(this.gameLoop);
    };
  }

  enableLowPowerMode() {
    // Reduce visual effects
    this.particleCount = Math.floor(this.particleCount * 0.5);
    this.shadowQuality = 'low';
    this.postProcessing = false;
  }
}

class ObjectPool {
  constructor() {
    this.pools = new Map();
  }

  register(type, factory, initialSize = 10) {
    const pool = {
      factory,
      available: [],
      inUse: []
    };

    for (let i = 0; i < initialSize; i++) {
      pool.available.push(factory());
    }

    this.pools.set(type, pool);
  }

  acquire(type) {
    const pool = this.pools.get(type);
    if (!pool) return null;

    let obj;
    if (pool.available.length > 0) {
      obj = pool.available.pop();
    } else {
      obj = pool.factory();
    }

    pool.inUse.push(obj);
    return obj;
  }

  release(type, obj) {
    const pool = this.pools.get(type);
    if (!pool) return;

    const index = pool.inUse.indexOf(obj);
    if (index !== -1) {
      pool.inUse.splice(index, 1);
      pool.available.push(obj);

      // Reset object
      if (obj.reset) obj.reset();
    }
  }
}
```

### Week 4: SDK Integration

**Ads Integration:**
```javascript
import { AdMobRewarded, AdMobInterstitial } from '@react-native-firebase/admob';

class AdManager {
  constructor() {
    this.interstitialLoaded = false;
    this.rewardedLoaded = false;
    this.setupAds();
  }

  setupAds() {
    // Interstitial
    AdMobInterstitial.setAdUnitID('ca-app-pub-xxxxx');
    AdMobInterstitial.addEventListener('adLoaded', () => {
      this.interstitialLoaded = true;
    });

    // Rewarded
    AdMobRewarded.setAdUnitID('ca-app-pub-xxxxx');
    AdMobRewarded.addEventListener('adLoaded', () => {
      this.rewardedLoaded = true;
    });
  }

  async showInterstitial() {
    if (this.interstitialLoaded) {
      await AdMobInterstitial.showAd();
      AdMobInterstitial.requestAd();
      this.interstitialLoaded = false;
    }
  }

  async showRewarded(callback) {
    if (this.rewardedLoaded) {
      AdMobRewarded.addEventListener('rewarded', (reward) => {
        callback(reward);
      });

      await AdMobRewarded.showAd();
      AdMobRewarded.requestAd();
      this.rewardedLoaded = false;
    }
  }
}
```

**In-App Purchases:**
```javascript
import * as RNIap from 'react-native-iap';

class IAPManager {
  constructor() {
    this.products = [];
    this.init();
  }

  async init() {
    try {
      await RNIap.initConnection();
      const products = await RNIap.getProducts([
        'com.game.coins100',
        'com.game.coins500',
        'com.game.noads'
      ]);
      this.products = products;
    } catch (error) {
      console.error('IAP init failed:', error);
    }
  }

  async purchase(productId) {
    try {
      const purchase = await RNIap.requestPurchase(productId);
      await this.processPurchase(purchase);
      await RNIap.finishTransaction(purchase);
    } catch (error) {
      console.error('Purchase failed:', error);
    }
  }

  async processPurchase(purchase) {
    // Grant items
    switch (purchase.productId) {
      case 'com.game.coins100':
        this.grantCoins(100);
        break;
      case 'com.game.coins500':
        this.grantCoins(500);
        break;
      case 'com.game.noads':
        this.removeAds();
        break;
    }
  }

  async restorePurchases() {
    try {
      const purchases = await RNIap.getAvailablePurchases();
      purchases.forEach(purchase => {
        this.processPurchase(purchase);
      });
    } catch (error) {
      console.error('Restore failed:', error);
    }
  }
}
```

### Week 5-6: App Store Deployment

**Build Configuration:**
```javascript
// app.json (Expo)
{
  "expo": {
    "name": "My Game",
    "slug": "my-game",
    "version": "1.0.0",
    "orientation": "landscape",
    "icon": "./assets/icon.png",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#000000"
    },
    "updates": {
      "fallbackToCacheTimeout": 0
    },
    "assetBundlePatterns": ["**/*"],
    "ios": {
      "bundleIdentifier": "com.yourcompany.game",
      "buildNumber": "1.0.0",
      "supportsTablet": true,
      "infoPlist": {
        "UIRequiresFullScreen": true
      }
    },
    "android": {
      "package": "com.yourcompany.game",
      "versionCode": 1,
      "permissions": [
        "INTERNET",
        "ACCESS_NETWORK_STATE"
      ],
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#FFFFFF"
      }
    }
  }
}
```

---

## 🎓 Projects

1. **Casual Puzzle Game** - Match-3 or similar
2. **Endless Runner** - Mobile-optimized with IAP
3. **Multiplayer Arena** - Real-time mobile game
4. **Hyper-Casual Game** - Simple, addictive gameplay

---

## 📖 Resources

- React Native documentation
- Unity Mobile Optimization Guide
- App Store Review Guidelines
- Google Play Best Practices

---

## ✅ Assessment

**Passing Grade:** 70%
- Touch controls (20%)
- Performance (30%)
- SDK integration (20%)
- Published app (30%)

**Career Paths:** Mobile Game Developer, Unity Developer, React Native Engineer

**Salary Range:** $75,000 - $140,000

---

**Module Created:** 2025-11-02
