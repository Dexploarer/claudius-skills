# Game Genre Deep-Dive: Battle Royale Games

## 🎮 Genre Overview

Battle Royale games combine survival, exploration, and scavenging elements with last-player-standing gameplay. Players compete in large-scale matches (50-100+ players) on shrinking maps until only one survives.

**Key Examples:** Fortnite, PUBG, Apex Legends, Warzone

---

## 🏗️ Core Systems

### 1. Map Shrinking System (The Circle/Storm)

```javascript
class SafeZone {
  constructor(mapSize) {
    this.mapSize = mapSize;
    this.currentPhase = 0;
    this.phases = [
      { duration: 300, endRadius: 2000, damage: 1 },  // 5 min
      { duration: 240, endRadius: 1000, damage: 2 },  // 4 min
      { duration: 180, endRadius: 500, damage: 5 },   // 3 min
      { duration: 120, endRadius: 250, damage: 10 },  // 2 min
      { duration: 90, endRadius: 100, damage: 20 },   // 1.5 min
      { duration: 60, endRadius: 25, damage: 50 }     // 1 min
    ];

    this.currentZone = {
      center: { x: mapSize / 2, y: mapSize / 2 },
      radius: mapSize / 2
    };

    this.nextZone = this.calculateNextZone();
    this.shrinkProgress = 0;
  }

  calculateNextZone() {
    const phase = this.phases[this.currentPhase];
    const currentRadius = this.currentZone.radius;

    // Random center within current zone
    const angle = Math.random() * Math.PI * 2;
    const distance = Math.random() * (currentRadius - phase.endRadius);

    return {
      center: {
        x: this.currentZone.center.x + Math.cos(angle) * distance,
        y: this.currentZone.center.y + Math.sin(angle) * distance
      },
      radius: phase.endRadius
    };
  }

  update(deltaTime) {
    const phase = this.phases[this.currentPhase];

    this.shrinkProgress += deltaTime / phase.duration;

    if (this.shrinkProgress >= 1) {
      // Move to next phase
      this.currentPhase++;
      this.shrinkProgress = 0;
      this.currentZone = this.nextZone;

      if (this.currentPhase < this.phases.length) {
        this.nextZone = this.calculateNextZone();
      }
    } else {
      // Interpolate current zone
      this.currentZone = {
        center: this.lerp(
          this.currentZone.center,
          this.nextZone.center,
          this.shrinkProgress
        ),
        radius: this.lerp(
          this.currentZone.radius,
          this.nextZone.radius,
          this.shrinkProgress
        )
      };
    }
  }

  isInSafeZone(position) {
    const dx = position.x - this.currentZone.center.x;
    const dy = position.y - this.currentZone.center.y;
    const distance = Math.sqrt(dx * dx + dy * dy);

    return distance <= this.currentZone.radius;
  }

  getDamage() {
    return this.phases[this.currentPhase].damage;
  }

  lerp(a, b, t) {
    if (typeof a === 'object') {
      return {
        x: a.x + (b.x - a.x) * t,
        y: a.y + (b.y - a.y) * t
      };
    }
    return a + (b - a) * t;
  }
}
```

### 2. Loot System

```javascript
class LootSystem {
  constructor() {
    this.lootTables = {
      common: [
        { item: 'bandage', weight: 30, quantity: [2, 5] },
        { item: 'pistol', weight: 20, quantity: 1 },
        { item: 'ammo_light', weight: 25, quantity: [20, 40] },
        { item: 'wood', weight: 25, quantity: [30, 50] }
      ],
      rare: [
        { item: 'medkit', weight: 20, quantity: [1, 2] },
        { item: 'assault_rifle', weight: 15, quantity: 1 },
        { item: 'shield_potion', weight: 20, quantity: [1, 2] },
        { item: 'ammo_medium', weight: 25, quantity: [40, 60] },
        { item: 'metal', weight: 20, quantity: [30, 50] }
      ],
      epic: [
        { item: 'shield_cells', weight: 15, quantity: [3, 5] },
        { item: 'sniper_rifle', weight: 10, quantity: 1 },
        { item: 'rocket_launcher', weight: 8, quantity: 1 },
        { item: 'scope_4x', weight: 12, quantity: 1 },
        { item: 'body_armor_2', weight: 15, quantity: 1 }
      ],
      legendary: [
        { item: 'phoenix_kit', weight: 10, quantity: 1 },
        { item: 'legendary_weapon', weight: 5, quantity: 1 },
        { item: 'body_armor_3', weight: 8, quantity: 1 },
        { item: 'scope_8x', weight: 7, quantity: 1 }
      ]
    };

    this.spawnPoints = [];
  }

  generateLoot(location, tier = 'common') {
    const table = this.lootTables[tier];
    const item = this.selectWeighted(table);

    if (!item) return null;

    const quantity = Array.isArray(item.quantity)
      ? Math.floor(Math.random() * (item.quantity[1] - item.quantity[0] + 1)) + item.quantity[0]
      : item.quantity;

    return {
      itemId: item.item,
      quantity,
      position: location,
      tier
    };
  }

  selectWeighted(items) {
    const totalWeight = items.reduce((sum, item) => sum + item.weight, 0);
    let random = Math.random() * totalWeight;

    for (const item of items) {
      random -= item.weight;
      if (random <= 0) {
        return item;
      }
    }

    return items[0];
  }

  populateMap(buildings) {
    buildings.forEach(building => {
      const tier = this.getBuildingTier(building.type);
      const lootCount = this.getLootCount(building.size);

      for (let i = 0; i < lootCount; i++) {
        const position = this.getRandomPositionInBuilding(building);
        const loot = this.generateLoot(position, tier);
        this.spawnPoints.push(loot);
      }
    });
  }

  getBuildingTier(buildingType) {
    const tierMap = {
      'small_house': 'common',
      'large_house': 'rare',
      'warehouse': 'rare',
      'military_base': 'epic',
      'supply_drop': 'legendary'
    };

    return tierMap[buildingType] || 'common';
  }
}
```

### 3. Drop Mechanics (Parachute/Gliding)

```javascript
class ParachuteSystem {
  constructor() {
    this.deployHeight = 500;
    this.minDeployHeight = 50;
    this.freefall速度 = -50; // m/s
    this.parachuteSpeed = -5;
    this.horizontalSpeed = 20;
  }

  updatePlayer(player, input, deltaTime) {
    if (player.height > this.deployHeight) {
      // Free fall phase
      player.velocity.y = this.freefallSpeed;

      // Limited horizontal control
      player.velocity.x = input.x * this.horizontalSpeed * 0.3;
      player.velocity.z = input.z * this.horizontalSpeed * 0.3;

    } else if (player.height > this.minDeployHeight) {
      // Parachute deployed
      if (!player.parachuteDeployed) {
        player.parachuteDeployed = true;
        player.velocity.y = this.parachuteSpeed;
      }

      // Full horizontal control
      player.velocity.x = input.x * this.horizontalSpeed;
      player.velocity.z = input.z * this.horizontalSpeed;

      // Cut parachute for faster descent
      if (input.cutParachute) {
        player.velocity.y = this.freefallSpeed * 0.5;
      }

    } else {
      // Landing
      player.height = 0;
      player.landed = true;
      player.parachuteDeployed = false;
    }

    // Update position
    player.position.x += player.velocity.x * deltaTime;
    player.position.y += player.velocity.y * deltaTime;
    player.position.z += player.velocity.z * deltaTime;
    player.height = player.position.y;
  }
}
```

### 4. Inventory System

```javascript
class BRInventory {
  constructor() {
    this.slots = {
      weapons: [null, null, null], // Primary, secondary, melee
      healing: [],
      grenades: [],
      resources: { wood: 0, stone: 0, metal: 0 },
      armor: null,
      backpack: null
    };

    this.maxSlots = {
      healing: 5,
      grenades: 10
    };
  }

  addItem(item) {
    switch (item.category) {
      case 'weapon':
        return this.addWeapon(item);

      case 'healing':
        return this.addHealing(item);

      case 'grenade':
        return this.addGrenade(item);

      case 'resource':
        return this.addResource(item);

      case 'armor':
        this.slots.armor = item;
        return true;

      case 'backpack':
        this.slots.backpack = item;
        this.maxSlots.healing += item.bonusSlots;
        return true;
    }

    return false;
  }

  addWeapon(weapon) {
    // Find empty weapon slot
    const emptyIndex = this.slots.weapons.findIndex(w => w === null);

    if (emptyIndex !== -1) {
      this.slots.weapons[emptyIndex] = weapon;
      return true;
    }

    // Swap with current weapon
    const currentWeapon = this.slots.weapons[0];
    this.slots.weapons[0] = weapon;

    // Drop current weapon
    return { dropped: currentWeapon };
  }

  addHealing(item) {
    if (this.slots.healing.length < this.maxSlots.healing) {
      const existing = this.slots.healing.find(h => h.id === item.id);

      if (existing) {
        existing.quantity += item.quantity;
      } else {
        this.slots.healing.push(item);
      }

      return true;
    }

    return false;
  }

  useHealing(itemId) {
    const item = this.slots.healing.find(h => h.id === itemId);

    if (!item) return false;

    // Start healing animation/timer
    const healAmount = item.healAmount;
    const duration = item.duration;

    item.quantity--;

    if (item.quantity <= 0) {
      this.slots.healing = this.slots.healing.filter(h => h.id !== itemId);
    }

    return { healAmount, duration };
  }
}
```

---

## 🎲 Unique Mechanics

### Supply Drops

```javascript
class SupplyDropSystem {
  constructor(map) {
    this.map = map;
    this.drops = [];
    this.dropInterval = 120000; // 2 minutes
    this.nextDrop = this.dropInterval;
  }

  update(deltaTime, gameTime) {
    this.nextDrop -= deltaTime;

    if (this.nextDrop <= 0) {
      this.spawnSupplyDrop();
      this.nextDrop = this.dropInterval;
    }

    // Update falling drops
    this.drops.forEach(drop => {
      if (drop.falling) {
        drop.position.y -= 10 * deltaTime;

        if (drop.position.y <= 0) {
          drop.falling = false;
          drop.landed = true;
          this.announceDropLocation(drop);
        }
      }
    });
  }

  spawnSupplyDrop() {
    const safeZone = this.map.safeZone.currentZone;

    // Random position within safe zone
    const angle = Math.random() * Math.PI * 2;
    const distance = Math.random() * safeZone.radius;

    const drop = {
      id: `drop_${Date.now()}`,
      position: {
        x: safeZone.center.x + Math.cos(angle) * distance,
        y: 500, // Spawn height
        z: safeZone.center.y + Math.sin(angle) * distance
      },
      falling: true,
      landed: false,
      loot: this.generateSupplyDropLoot()
    };

    this.drops.push(drop);
    this.broadcastDropIncoming(drop);
  }

  generateSupplyDropLoot() {
    return [
      { item: 'legendary_weapon', quantity: 1 },
      { item: 'body_armor_3', quantity: 1 },
      { item: 'medkit', quantity: 3 },
      { item: 'shield_cells', quantity: 5 },
      { item: 'ammo_rare', quantity: 100 }
    ];
  }
}
```

---

## 📊 Matchmaking & Skill-Based

```javascript
class BRMatchmaking {
  constructor() {
    this.queue = [];
    this.matchSize = 100;
    this.skillBrackets = ['bronze', 'silver', 'gold', 'platinum', 'diamond'];
  }

  addPlayer(player) {
    this.queue.push({
      player,
      bracket: this.getSkillBracket(player.mmr),
      queueTime: Date.now()
    });

    this.tryFormMatch();
  }

  getSkillBracket(mmr) {
    if (mmr < 1000) return 'bronze';
    if (mmr < 1500) return 'silver';
    if (mmr < 2000) return 'gold';
    if (mmr < 2500) return 'platinum';
    return 'diamond';
  }

  tryFormMatch() {
    if (this.queue.length < this.matchSize) return;

    // Group by skill bracket
    const brackets = {};

    this.queue.forEach(entry => {
      if (!brackets[entry.bracket]) {
        brackets[entry.bracket] = [];
      }
      brackets[entry.bracket].push(entry);
    });

    // Fill match with similar skill levels
    const match = [];
    const targetBracket = this.getMostPopulatedBracket(brackets);

    // Add players from target bracket
    match.push(...brackets[targetBracket].slice(0, this.matchSize * 0.7));

    // Fill remaining spots with adjacent brackets
    const remaining = this.matchSize - match.length;
    const adjacentPlayers = this.getAdjacentBracketPlayers(
      targetBracket,
      brackets
    );

    match.push(...adjacentPlayers.slice(0, remaining));

    if (match.length >= this.matchSize * 0.9) { // 90% fill rate minimum
      this.startMatch(match.map(e => e.player));

      // Remove players from queue
      match.forEach(entry => {
        const index = this.queue.indexOf(entry);
        if (index !== -1) {
          this.queue.splice(index, 1);
        }
      });
    }
  }

  startMatch(players) {
    const match = new BattleRoyaleMatch(players);
    match.start();
  }
}
```

---

## 🏆 Ranking & Progression

```javascript
class BRRankingSystem {
  constructor() {
    this.ranks = [
      { name: 'Bronze', minPoints: 0, maxPoints: 1000 },
      { name: 'Silver', minPoints: 1000, maxPoints: 2000 },
      { name: 'Gold', minPoints: 2000, maxPoints: 3000 },
      { name: 'Platinum', minPoints: 3000, maxPoints: 4500 },
      { name: 'Diamond', minPoints: 4500, maxPoints: 6000 },
      { name: 'Master', minPoints: 6000, maxPoints: 8000 },
      { name: 'Predator', minPoints: 8000, maxPoints: Infinity }
    ];
  }

  calculatePoints(placement, kills, damageDealt, matchCount) {
    let points = 0;

    // Placement points
    const placementPoints = {
      1: 250, 2: 200, 3: 175, 4: 150, 5: 125,
      6-10: 100, 11-15: 75, 16-20: 50
    };

    if (placement <= 5) {
      points += placementPoints[placement];
    } else if (placement <= 10) {
      points += 100;
    } else if (placement <= 15) {
      points += 75;
    } else if (placement <= 20) {
      points += 50;
    }

    // Kill points
    points += kills * 20;

    // Performance bonus
    if (damageDealt > 2000) {
      points += 50;
    }

    // Entry cost (prevents rank camping)
    const entryCost = this.getEntryCost(matchCount);
    points -= entryCost;

    return points;
  }

  getEntryCost(playerRankPoints) {
    if (playerRankPoints < 1000) return 0;     // Bronze - free
    if (playerRankPoints < 2000) return 12;    // Silver
    if (playerRankPoints < 3000) return 24;    // Gold
    if (playerRankPoints < 4500) return 36;    // Platinum
    if (playerRankPoints < 6000) return 48;    // Diamond
    return 60;                                  // Master+
  }
}
```

---

## 🎨 Design Patterns

### Best Practices
1. **Map Variety** - Multiple POIs (Points of Interest)
2. **Loot Balance** - Fair distribution, hot zones
3. **Pacing** - Zone timing creates urgency
4. **Skill Gap** - Both luck and skill matter
5. **Spectator Mode** - Watch after death

### Common Pitfalls
- ❌ Too much RNG (all luck, no skill)
- ❌ Boring mid-game (empty map)
- ❌ Unfair final zones (open field)
- ❌ Poor weapon balance
- ❌ Network lag issues

---

## 📊 Analytics & KPIs

```javascript
class BRAnalytics {
  trackMatch(matchData) {
    return {
      averagePlacement: this.calculateAvgPlacement(matchData),
      hotDropPercentage: this.calculateHotDrops(matchData),
      averageKills: matchData.kills / matchData.players,
      averageDamage: matchData.damage / matchData.players,
      averageSurvivalTime: matchData.survivalTime / matchData.players,
      popularLandingZones: this.getPopularZones(matchData),
      weaponUsageStats: this.getWeaponStats(matchData)
    };
  }
}
```

### Key Metrics
- **Average Placement** - Player skill distribution
- **Hot Drop %** - Aggressive vs passive players
- **Avg Survival Time** - Match pacing
- **Kill Distribution** - Combat frequency
- **Weapon Usage** - Balance insights

---

## 🚀 Monetization

### Battle Pass
- Seasonal cosmetics
- XP progression
- Free + Premium tiers

### In-Game Store
- Character skins
- Weapon skins
- Emotes/Dances
- Cosmetic-only (no P2W)

---

## 📚 References

- Fortnite GDC Talk on Building Mechanics
- PUBG Technical Architecture
- Apex Legends Character Design
- Warzone Season Design

---

**Genre Guide Complete!** Ready to build your own Battle Royale?
