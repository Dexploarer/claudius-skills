# Module 14: Live Operations & Analytics

## 🎯 Learning Objectives

- Implement game analytics and telemetry
- Build live operations systems
- Create A/B testing frameworks
- Design player retention strategies
- Monitor KPIs and metrics
- Implement remote configuration

**Duration:** 4-5 weeks | **Difficulty:** Advanced

---

## 🗓️ Core Topics

### Week 1: Analytics Implementation

```javascript
class GameAnalytics {
  constructor(apiKey, environment = 'production') {
    this.apiKey = apiKey;
    this.environment = environment;
    this.sessionId = this.generateSessionId();
    this.playerId = this.getPlayerId();
    this.eventQueue = [];
    this.batchSize = 10;
    this.flushInterval = 30000; // 30 seconds

    this.startSession();
    this.setupAutoFlush();
  }

  // Core events
  trackEvent(category, action, label, value) {
    const event = {
      category,
      action,
      label,
      value,
      timestamp: Date.now(),
      sessionId: this.sessionId,
      playerId: this.playerId,
      environment: this.environment
    };

    this.eventQueue.push(event);

    if (this.eventQueue.length >= this.batchSize) {
      this.flush();
    }
  }

  // Game-specific events
  trackGameStart(level, difficulty) {
    this.trackEvent('game', 'start', level, { difficulty });
  }

  trackGameEnd(level, score, duration, outcome) {
    this.trackEvent('game', 'end', level, {
      score,
      duration,
      outcome, // 'win', 'lose', 'quit'
      performance: this.calculatePerformance(score, duration)
    });
  }

  trackPurchase(productId, price, currency) {
    this.trackEvent('monetization', 'purchase', productId, {
      price,
      currency,
      timestamp: Date.now()
    });
  }

  trackAdView(adType, placement) {
    this.trackEvent('monetization', 'ad_view', placement, {
      adType, // 'interstitial', 'rewarded', 'banner'
      timestamp: Date.now()
    });
  }

  trackTutorialProgress(step, completed) {
    this.trackEvent('tutorial', 'progress', step, {
      completed,
      timestamp: Date.now()
    });
  }

  // Funnel tracking
  trackFunnelStep(funnelName, stepIndex, stepName) {
    this.trackEvent('funnel', funnelName, stepName, {
      stepIndex,
      timestamp: Date.now()
    });
  }

  // User progression
  trackLevelUp(newLevel, experience) {
    this.trackEvent('progression', 'level_up', 'player_level', {
      newLevel,
      experience,
      timestamp: Date.now()
    });
  }

  // Economy tracking
  trackCurrencyEarned(currencyType, amount, source) {
    this.trackEvent('economy', 'currency_earned', currencyType, {
      amount,
      source,
      balance: this.getCurrencyBalance(currencyType)
    });
  }

  trackCurrencySpent(currencyType, amount, sink) {
    this.trackEvent('economy', 'currency_spent', currencyType, {
      amount,
      sink,
      balance: this.getCurrencyBalance(currencyType)
    });
  }

  // Session management
  startSession() {
    this.sessionStart = Date.now();
    this.trackEvent('session', 'start', 'game_session', {
      platform: this.getPlatform(),
      deviceInfo: this.getDeviceInfo()
    });
  }

  endSession() {
    const duration = Date.now() - this.sessionStart;
    this.trackEvent('session', 'end', 'game_session', {
      duration,
      events: this.eventQueue.length
    });
    this.flush();
  }

  // Data persistence
  async flush() {
    if (this.eventQueue.length === 0) return;

    const events = [...this.eventQueue];
    this.eventQueue = [];

    try {
      await fetch(`https://analytics-api.example.com/events`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-API-Key': this.apiKey
        },
        body: JSON.stringify({
          events,
          playerId: this.playerId,
          sessionId: this.sessionId
        })
      });
    } catch (error) {
      // Re-queue events if failed
      this.eventQueue.unshift(...events);
      console.error('Analytics flush failed:', error);
    }
  }

  setupAutoFlush() {
    setInterval(() => this.flush(), this.flushInterval);

    // Flush on page unload
    window.addEventListener('beforeunload', () => this.flush());
  }

  // Utility methods
  generateSessionId() {
    return `${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  getPlayerId() {
    let playerId = localStorage.getItem('playerId');
    if (!playerId) {
      playerId = `player_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
      localStorage.setItem('playerId', playerId);
    }
    return playerId;
  }

  getPlatform() {
    const ua = navigator.userAgent;
    if (/Android/i.test(ua)) return 'android';
    if (/iPhone|iPad|iPod/i.test(ua)) return 'ios';
    return 'web';
  }

  getDeviceInfo() {
    return {
      screen: `${screen.width}x${screen.height}`,
      language: navigator.language,
      memory: navigator.deviceMemory,
      cores: navigator.hardwareConcurrency
    };
  }
}
```

### Week 2: A/B Testing Framework

```javascript
class ABTestingManager {
  constructor(analytics) {
    this.analytics = analytics;
    this.experiments = new Map();
    this.assignments = new Map();
  }

  async loadExperiments() {
    const response = await fetch('https://api.example.com/experiments');
    const experiments = await response.json();

    experiments.forEach(exp => {
      this.experiments.set(exp.id, exp);
    });

    this.assignExperiments();
  }

  assignExperiments() {
    this.experiments.forEach((experiment, id) => {
      if (!this.isEligible(experiment)) return;

      // Check if already assigned
      let assignment = localStorage.getItem(`exp_${id}`);

      if (!assignment) {
        // Assign to variant
        assignment = this.selectVariant(experiment.variants);
        localStorage.setItem(`exp_${id}`, assignment);

        // Track assignment
        this.analytics.trackEvent('experiment', 'assigned', id, {
          variant: assignment
        });
      }

      this.assignments.set(id, assignment);
    });
  }

  selectVariant(variants) {
    const rand = Math.random();
    let cumulative = 0;

    for (const variant of variants) {
      cumulative += variant.weight;
      if (rand <= cumulative) {
        return variant.id;
      }
    }

    return variants[0].id;
  }

  getVariant(experimentId) {
    return this.assignments.get(experimentId) || 'control';
  }

  isEligible(experiment) {
    // Check eligibility criteria
    const playerLevel = this.getPlayerLevel();
    const daysSinceInstall = this.getDaysSinceInstall();

    if (experiment.minLevel && playerLevel < experiment.minLevel) {
      return false;
    }

    if (experiment.minDays && daysSinceInstall < experiment.minDays) {
      return false;
    }

    return true;
  }

  // Track experiment events
  trackConversion(experimentId, metric, value) {
    const variant = this.getVariant(experimentId);

    this.analytics.trackEvent('experiment', 'conversion', experimentId, {
      variant,
      metric,
      value
    });
  }
}

// Usage
const abTest = new ABTestingManager(analytics);
await abTest.loadExperiments();

// Use different variants
const variant = abTest.getVariant('tutorial_v2');

if (variant === 'variant_a') {
  // Show new tutorial
  showNewTutorial();
} else {
  // Show control tutorial
  showOldTutorial();
}

// Track conversion
abTest.trackConversion('tutorial_v2', 'completed', 1);
```

### Week 3: Remote Configuration

```javascript
class RemoteConfig {
  constructor() {
    this.config = new Map();
    this.defaultConfig = new Map();
    this.lastFetch = 0;
    this.cacheExpiry = 3600000; // 1 hour
  }

  setDefaults(defaults) {
    Object.entries(defaults).forEach(([key, value]) => {
      this.defaultConfig.set(key, value);
      this.config.set(key, value);
    });
  }

  async fetch() {
    const now = Date.now();

    if (now - this.lastFetch < this.cacheExpiry) {
      return; // Use cached config
    }

    try {
      const response = await fetch('https://api.example.com/config', {
        headers: {
          'X-Player-Id': this.getPlayerId(),
          'X-Platform': this.getPlatform()
        }
      });

      const remoteConfig = await response.json();

      Object.entries(remoteConfig).forEach(([key, value]) => {
        this.config.set(key, value);
      });

      this.lastFetch = now;
      this.saveToCache();
    } catch (error) {
      console.error('Failed to fetch remote config:', error);
      this.loadFromCache();
    }
  }

  getString(key) {
    return this.config.get(key) || this.defaultConfig.get(key) || '';
  }

  getNumber(key) {
    const value = this.config.get(key) || this.defaultConfig.get(key);
    return typeof value === 'number' ? value : 0;
  }

  getBoolean(key) {
    const value = this.config.get(key) || this.defaultConfig.get(key);
    return Boolean(value);
  }

  getJSON(key) {
    const value = this.config.get(key) || this.defaultConfig.get(key);
    return typeof value === 'object' ? value : {};
  }

  saveToCache() {
    const configObj = Object.fromEntries(this.config);
    localStorage.setItem('remote_config', JSON.stringify(configObj));
    localStorage.setItem('remote_config_timestamp', this.lastFetch.toString());
  }

  loadFromCache() {
    const cached = localStorage.getItem('remote_config');
    const timestamp = localStorage.getItem('remote_config_timestamp');

    if (cached) {
      const configObj = JSON.parse(cached);
      Object.entries(configObj).forEach(([key, value]) => {
        this.config.set(key, value);
      });
      this.lastFetch = parseInt(timestamp) || 0;
    }
  }
}

// Usage
const config = new RemoteConfig();

config.setDefaults({
  daily_reward_amount: 100,
  shop_discount: 0,
  feature_new_ui: false,
  difficulty_multiplier: 1.0,
  event_config: {
    active: false,
    start_time: 0,
    end_time: 0
  }
});

await config.fetch();

const rewardAmount = config.getNumber('daily_reward_amount');
const useNewUI = config.getBoolean('feature_new_ui');
const eventConfig = config.getJSON('event_config');
```

### Week 4: KPI Dashboard & Retention

```javascript
class KPITracker {
  constructor(analytics) {
    this.analytics = analytics;
    this.kpis = {
      dau: 0,      // Daily Active Users
      mau: 0,      // Monthly Active Users
      retention: {
        day1: 0,
        day7: 0,
        day30: 0
      },
      arpu: 0,     // Average Revenue Per User
      arppu: 0,    // Average Revenue Per Paying User
      ltv: 0,      // Lifetime Value
      conversionRate: 0
    };
  }

  calculateRetention(cohort, day) {
    // Track player return
    const installDate = this.getInstallDate();
    const daysSinceInstall = this.getDaysSinceInstall(installDate);

    if (daysSinceInstall === day) {
      this.analytics.trackEvent('retention', `day${day}`, 'returned', {
        cohort,
        installDate
      });
    }
  }

  trackSessionDuration() {
    const sessionStart = performance.now();

    window.addEventListener('beforeunload', () => {
      const duration = (performance.now() - sessionStart) / 1000;

      this.analytics.trackEvent('engagement', 'session_duration', 'seconds', {
        duration,
        date: new Date().toISOString().split('T')[0]
      });
    });
  }

  // Cohort analysis
  async getCohortAnalysis(startDate, endDate) {
    const response = await fetch(
      `https://api.example.com/cohorts?start=${startDate}&end=${endDate}`
    );

    return await response.json();
  }
}
```

---

## 🎓 Projects

1. **Analytics Dashboard** - Real-time game metrics
2. **A/B Testing System** - Feature testing framework
3. **Live Events Manager** - Timed events and promotions
4. **Player Segmentation Tool** - Cohort analysis system

---

## 📖 Resources

- Google Analytics for Games
- Unity Analytics documentation
- "Game Analytics" by El-Nasr et al.
- Mixpanel, Amplitude tutorials

---

## ✅ Assessment

**Passing Grade:** 75%
- Analytics implementation (35%)
- A/B testing system (25%)
- KPI tracking (20%)
- Final project (20%)

**Career Paths:** Game Analyst, Product Manager, LiveOps Manager

**Salary Range:** $70,000 - $145,000

---

**Module Created:** 2025-11-02
