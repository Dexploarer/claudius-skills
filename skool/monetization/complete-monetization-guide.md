# Complete Game Monetization Strategy Guide

## 💰 Monetization Overview

Comprehensive guide to monetizing indie games across all platforms and business models.

---

## 🎮 Business Models

### 1. Free-to-Play (F2P)

**Revenue Streams:**
- In-App Purchases (IAP)
- Advertisements
- Battle Passes
- Subscriptions

**Best For:** Mobile games, live-service games, multiplayer

**Average Revenue:** $0.50-$5 per DAU (Daily Active User)

#### Implementation

```javascript
class F2PEconomy {
  constructor() {
    this.currencies = {
      softCurrency: 0,  // Earned through gameplay
      hardCurrency: 0    // Purchased with real money
    };

    this.prices = {
      // IAP Packages
      starter: { price: 0.99, hardCurrency: 100, bonus: 0 },
      value: { price: 4.99, hardCurrency: 550, bonus: 50 },
      popular: { price: 9.99, hardCurrency: 1200, bonus: 200 },
      best: { price: 19.99, hardCurrency: 2600, bonus: 600 }
    };
  }

  // Soft currency sinks
  getSoftCurrencySinks() {
    return {
      upgrades: 1000,
      powerups: 50,
      continues: 100,
      speedups: 200
    };
  }

  // Hard currency exclusives
  getHardCurrencyItems() {
    return {
      exclusiveSkins: 500,
      premiumCharacters: 1500,
      instantUnlock: 300,
      removeAds: 1999  // Permanent
    };
  }

  // Daily rewards to drive retention
  getDailyReward(dayNumber) {
    const rewards = [
      { soft: 100, hard: 0 },
      { soft: 150, hard: 0 },
      { soft: 200, hard: 0 },
      { soft: 300, hard: 5 },
      { soft: 400, hard: 0 },
      { soft: 500, hard: 0 },
      { soft: 1000, hard: 20 }  // Day 7 special
    ];

    return rewards[(dayNumber - 1) % 7];
  }

  // Gacha/Lootbox system
  openLootbox(tier = 'common') {
    const tables = {
      common: [
        { item: 'common_card', chance: 0.70 },
        { item: 'rare_card', chance: 0.25 },
        { item: 'epic_card', chance: 0.05 }
      ],
      premium: [
        { item: 'rare_card', chance: 0.50 },
        { item: 'epic_card', chance: 0.40 },
        { item: 'legendary_card', chance: 0.10 }
      ]
    };

    return this.rollGacha(tables[tier]);
  }

  rollGacha(table) {
    const roll = Math.random();
    let cumulative = 0;

    for (const entry of table) {
      cumulative += entry.chance;
      if (roll <= cumulative) {
        return entry.item;
      }
    }
  }
}
```

### 2. Premium (Paid)

**Price Points:**
- Mobile: $0.99 - $9.99
- PC/Console: $9.99 - $59.99
- Indie: $4.99 - $19.99

**Best For:** Story-driven games, premium experiences

**Average Revenue:** 5,000-50,000 copies first year

#### Pricing Strategy

```javascript
class PricingStrategy {
  calculateOptimalPrice(gameType, qualityTier, platformreachability market) {
    const basePrices = {
      mobile: { low: 0.99, mid: 2.99, high: 4.99 },
      pc: { low: 4.99, mid: 14.99, high: 24.99 },
      console: { low: 19.99, mid: 39.99, high: 59.99 }
    };

    let price = basePrices[market][qualityTier];

    // Adjust for game length
    const lengthMultiplier = {
      'short': 0.7,      // < 3 hours
      'medium': 1.0,     // 3-10 hours
      'long': 1.3,       // 10-30 hours
      'very_long': 1.5   // 30+ hours
    };

    price *= lengthMultiplier[gameType];

    return Math.round(price * 100) / 100;
  }

  getLaunchDiscountStrategy() {
    return {
      weekOne: 0.10,      // 10% off launch week
      firstMonth: 0.15,   // 15% off first month
      seasonal: 0.25,     // 25% off seasonal sales
      deepDiscount: 0.50  // 50% off (rare, 1-2 times/year)
    };
  }

  calculateRegionalPricing(basePrice, region) {
    const ppp = {  // Purchasing Power Parity multipliers
      us: 1.0,
      eu: 1.0,
      uk: 0.9,
      canada: 0.85,
      australia: 0.9,
      brazil: 0.4,
      russia: 0.35,
      india: 0.25,
      china: 0.6,
      argentina: 0.3
    };

    return basePrice * (ppp[region] || 1.0);
  }
}
```

### 3. Subscription Model

**Tiers:**
- Basic: $2.99/month
- Premium: $7.99/month
- Ultimate: $14.99/month

**Best For:** Live-service games, content libraries

#### Subscription Implementation

```javascript
class SubscriptionManager {
  constructor() {
    this.tiers = {
      basic: {
        price: 2.99,
        benefits: [
          'ad_free',
          'double_soft_currency',
          'daily_premium_item'
        ]
      },
      premium: {
        price: 7.99,
        benefits: [
          'ad_free',
          'triple_soft_currency',
          'daily_premium_item',
          'exclusive_skins',
          'priority_support'
        ]
      },
      ultimate: {
        price: 14.99,
        benefits: [
          'ad_free',
          'quadruple_soft_currency',
          'daily_legendary_item',
          'exclusive_skins',
          'priority_support',
          'beta_access',
          'monthly_hard_currency'
        ]
      }
    };
  }

  getMonthlyValue(tier) {
    // Calculate perceived value vs. price
    const benefits = {
      ad_free: 4.99,
      soft_currency_boost: 9.99,
      exclusive_items: 14.99,
      hard_currency: 19.99
    };

    // Show players they're getting "3x value"
    return Object.values(benefits).reduce((a, b) => a + b, 0);
  }
}
```

### 4. Battle Pass

**Structure:**
- Free tier (limited rewards)
- Premium tier ($9.99)
- Duration: 60-90 days

**Best For:** Live-service, competitive games

```javascript
class BattlePassSystem {
  constructor(season) {
    this.season = season;
    this.maxLevel = 100;
    this.premiumPrice = 9.99;

    this.rewards = this.generateRewards();
  }

  generateRewards() {
    const rewards = [];

    for (let level = 1; level <= this.maxLevel; level++) {
      rewards.push({
        level,
        free: this.getFreeReward(level),
        premium: this.getPremiumReward(level)
      });
    }

    return rewards;
  }

  getFreeReward(level) {
    // Every 5 levels
    if (level % 5 === 0) {
      return {
        type: 'currency',
        amount: 100,
        rarity: 'common'
      };
    }

    return null;
  }

  getPremiumReward(level) {
    // Milestone rewards
    if (level === 1) return { type: 'skin', rarity: 'rare' };
    if (level === 25) return { type: 'skin', rarity: 'epic' };
    if (level === 50) return { type: 'emote', rarity: 'epic' };
    if (level === 100) return { type: 'skin', rarity: 'legendary' };

    // Regular rewards
    if (level % 10 === 0) {
      return { type: 'currency', amount: 500 };
    }

    return { type: 'xp_boost', amount: 1.1 };
  }

  calculateXPNeeded(level) {
    // Exponential curve
    return Math.floor(1000 * Math.pow(1.05, level - 1));
  }

  estimateTimeToComplete() {
    const totalXP = this.rewards.reduce((sum, reward) =>
      sum + this.calculateXPNeeded(reward.level), 0
    );

    const dailyXP = 5000; // Average player
    const days = totalXP / dailyXP;

    return {
      casual: Math.ceil(days * 1.5),
      average: Math.ceil(days),
      hardcore: Math.ceil(days * 0.7)
    };
  }
}
```

---

## 📊 Ad Integration

### Ad Types & Revenue

```javascript
class AdMonetization {
  constructor() {
    this.adTypes = {
      banner: {
        cpm: 0.50,  // $ per 1000 impressions
        frequency: 'always_visible'
      },
      interstitial: {
        cpm: 5.00,
        frequency: 'every_3_levels'
      },
      rewarded: {
        cpm: 15.00,
        frequency: 'player_choice'
      },
      native: {
        cpm: 2.00,
        frequency: 'menu_screens'
      }
    };
  }

  calculateAdRevenue(dau, adImpressions) {
    let revenue = 0;

    // Rewarded ads (highest value, opt-in)
    const rewardedWatchRate = 0.40; // 40% of players
    const rewardedPerDay = 3;
    revenue += (dau * rewardedWatchRate * rewardedPerDay *
                this.adTypes.rewarded.cpm / 1000);

    // Interstitials (forced)
    const interstitialPerDay = 10;
    revenue += (dau * interstitialPerDay *
                this.adTypes.interstitial.cpm / 1000);

    // Banners (always visible)
    const sessionLength = 20; // minutes
    const bannerRefreshRate = 2; // minutes
    revenue += (dau * (sessionLength / bannerRefreshRate) *
                this.adTypes.banner.cpm / 1000);

    return revenue;
  }

  getOptimalAdPlacement() {
    return {
      rewarded: [
        'extra_lives',
        'double_rewards',
        'skip_timer',
        'daily_bonus',
        'open_chest'
      ],
      interstitial: [
        'level_complete',
        'game_over',
        'main_menu_return'
      ],
      banner: [
        'gameplay_bottom',
        'menu_screens'
      ]
    };
  }

  // Balance ads with user experience
  calculateAdLoadFatigue(adsWatched) {
    // Reduce ad frequency as user watches more
    if (adsWatched > 50) return 0.5;  // 50% reduction
    if (adsWatched > 20) return 0.75; // 25% reduction
    return 1.0;
  }
}
```

---

## 💎 IAP Strategy

### Product Catalog

```javascript
class IAPCatalog {
  getProducts() {
    return {
      // Currency packs
      currency_small: {
        id: 'com.game.currency.100',
        price: 0.99,
        value: 100,
        bonus: 0
      },
      currency_medium: {
        id: 'com.game.currency.550',
        price: 4.99,
        value: 500,
        bonus: 50,
        label: 'MOST POPULAR'
      },
      currency_large: {
        id: 'com.game.currency.1200',
        price: 9.99,
        value: 1000,
        bonus: 200,
        label: 'BEST VALUE'
      },

      // Starter packs
      starter_pack: {
        id: 'com.game.starter',
        price: 1.99,
        oneTime: true,
        contents: [
          { type: 'currency', amount: 200 },
          { type: 'character', id: 'rare_hero' },
          { type: 'boost', duration: 24 * 3600 }
        ]
      },

      // Permanent upgrades
      remove_ads: {
        id: 'com.game.noads',
        price: 4.99,
        permanent: true
      },

      double_rewards: {
        id: 'com.game.double',
        price: 2.99,
        permanent: true
      },

      // Time-limited offers
      weekend_special: {
        id: 'com.game.weekend',
        price: 9.99,
        timeLimit: 48 * 3600,
        value: 2000,
        bonus: 1000,
        label: '3X VALUE - 48H ONLY'
      }
    };
  }

  // Dynamic pricing based on player behavior
  getPersonalizedOffer(player) {
    const daysSinceInstall = player.getDaysSinceInstall();
    const totalSpent = player.getTotalSpent();

    // First-time buyer incentive
    if (totalSpent === 0 && daysSinceInstall > 3) {
      return {
        id: 'com.game.firstbuy',
        price: 0.99,
        value: 500,  // 5x value
        label: 'FIRST PURCHASE SPECIAL'
      };
    }

    // Re-engagement offer
    if (player.daysSinceLastSession > 7) {
      return {
        id: 'com.game.comeback',
        price: 1.99,
        contents: ['exclusive_skin', 'currency_500'],
        label: 'WELCOME BACK'
      };
    }

    // Whale offer
    if (totalSpent > 100) {
      return {
        id: 'com.game.vip',
        price: 49.99,
        contents: ['legendary_bundle', 'currency_10000'],
        label: 'VIP EXCLUSIVE'
      };
    }

    return null;
  }
}
```

---

## 📈 Retention & LTV

### Lifetime Value Calculation

```javascript
class LTVCalculator {
  calculateLTV(playerData) {
    const {
      daysActive,
      totalSpent,
      adRevenue,
      engagementScore
    } = playerData;

    // Historical LTV
    const historicalLTV = totalSpent + adRevenue;

    // Predicted future LTV
    const avgDailyRevenue = historicalLTV / daysActive;
    const churnProbability = this.predictChurn(engagementScore);
    const expectedDaysRemaining = (1 / churnProbability) * 30;

    const predictedLTV = avgDailyRevenue * expectedDaysRemaining;

    return {
      historical: historicalLTV,
      predicted: predictedLTV,
      total: historicalLTV + predictedLTV
    };
  }

  predictChurn(engagementScore) {
    // Simple logistic regression
    if (engagementScore > 0.8) return 0.01;  // 1% daily churn
    if (engagementScore > 0.6) return 0.03;  // 3%
    if (engagementScore > 0.4) return 0.05;  // 5%
    return 0.10;  // 10%
  }

  calculatePaybackPeriod(cpi, ltv) {
    // How long to recoup acquisition cost
    const dailyRevenue = ltv / 365;
    return Math.ceil(cpi / dailyRevenue);
  }
}
```

---

## 🎯 Conversion Optimization

### A/B Testing

```javascript
class PriceTestingFramework {
  runPriceTest(product) {
    const variants = [
      { price: 4.99, testGroup: 'A' },
      { price: 5.99, testGroup: 'B' },
      { price: 6.99, testGroup: 'C' }
    ];

    return {
      variants,
      duration: 14, // days
      sampleSize: 1000, // users per variant
      metrics: [
        'conversion_rate',
        'revenue_per_user',
        'total_revenue'
      ]
    };
  }

  analyzeResults(results) {
    return results.map(variant => ({
      ...variant,
      totalRevenue: variant.conversions * variant.price,
      revenuePerUser: (variant.conversions * variant.price) / variant.users
    })).sort((a, b) => b.revenuePerUser - a.revenuePerUser);
  }
}
```

---

## 🌍 Regional Pricing

```javascript
const regionalPricing = {
  tier1: { // High income
    multiplier: 1.0,
    countries: ['US', 'CA', 'UK', 'AU', 'DE', 'FR']
  },
  tier2: { // Upper-middle income
    multiplier: 0.7,
    countries: ['BR', 'MX', 'AR', 'CL', 'ZA']
  },
  tier3: { // Lower-middle income
    multiplier: 0.4,
    countries: ['IN', 'PH', 'ID', 'VN', 'UA']
  },
  tier4: { // Low income
    multiplier: 0.25,
    countries: ['PK', 'BD', 'NG', 'EG']
  }
};
```

---

## 📊 KPIs to Track

### Essential Metrics

```javascript
const gameMetrics = {
  userAcquisition: {
    cpi: 0,            // Cost Per Install
    organicRate: 0,    // % organic vs paid
    viralK: 0          // Viral coefficient
  },

  engagement: {
    dau: 0,            // Daily Active Users
    mau: 0,            // Monthly Active Users
    sessionLength: 0,   // Average minutes
    sessionsPerDay: 0
  },

  retention: {
    day1: 0,           // % return day 1
    day7: 0,
    day30: 0
  },

  monetization: {
    arpu: 0,           // Average Revenue Per User
    arppu: 0,          // Average Revenue Per Paying User
    conversionRate: 0,  // % of users who pay
    ltv: 0             // Lifetime Value
  }
};
```

### Targets for Success

| Metric | Mobile F2P | Premium PC |
|--------|------------|------------|
| Day 1 Retention | 40%+ | 70%+ |
| Day 7 Retention | 20%+ | 50%+ |
| Conversion Rate | 2-5% | N/A |
| ARPU | $0.10-$1.00 | $10-$30 |
| LTV | $5-$20 | $15-$60 |

---

## 💡 Best Practices

### Do's ✅
- Clear value propositions
- Fair pricing
- Respect player time
- No pay-to-win in competitive games
- Transparent probabilities (lootboxes)
- Regional pricing
- Reward loyalty

### Don'ts ❌
- Aggressive paywall
- Deceptive advertising
- Unfair advantages
- Hidden costs
- Predatory mechanics
- Spam notifications
- Bait-and-switch

---

**Monetization Guide Complete!** Build sustainable revenue streams.
