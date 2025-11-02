# Game Templates - Copy & Paste to Build Games Instantly

**Pre-built game templates you can customize with AI in minutes**

---

## How to Use These Templates

1. **Copy the prompt** for the game type you want
2. **Paste into Claude Code**
3. **AI generates complete game**
4. **Customize** with additional requests
5. **Deploy** and share!

Each template includes:
- Complete game mechanics
- UI/UX
- Asset requirements
- Extensibility points
- Time to customize

---

## Template 1: 2D Platformer "Pixel Runner"

### Base Prompt

```
Create a 2D platformer game called "Pixel Runner" with:

CORE MECHANICS:
- Smooth player movement (WASD/Arrow keys)
- Variable jump height (longer press = higher jump)
- Double jump ability
- Wall sliding
- Dash move (Shift key)

ENEMIES:
- Slime: Patrols back and forth
- Bat: Flies in sine wave pattern
- Spikes: Static hazards

COLLECTIBLES:
- Coins: Basic points
- Gems: Bonus points
- Hearts: Health restore
- Stars: Unlock abilities

LEVELS:
- 5 levels with increasing difficulty
- Moving platforms
- Disappearing platforms
- Checkpoints
- Level timer

UI:
- Score display
- Lives counter
- Level indicator
- Pause menu with settings
- Death screen with retry

TECHNICAL:
- HTML5 Canvas
- Vanilla JavaScript
- Sprite animation system
- Collision detection (AABB)
- Local storage for progress
- Mobile touch controls

Include complete code, asset requirements list, and level design data structure.
```

### Customize It (Examples)

**Make it unique:**
```
"Change theme to cyberpunk ninja"
"Add wall running mechanic"
"Create boss fight for level 5"
"Add weapons system (shuriken throwing)"
```

**Add features:**
```
"Add local 2-player mode"
"Create level editor"
"Add achievements system"
"Implement leaderboards"
```

### Time Estimate
- Base game: 15 minutes
- Customization: 10-30 minutes
- **Total: 25-45 minutes**

---

## Template 2: Top-Down Shooter "Neon Assault"

### Base Prompt

```
Create a top-down shooter called "Neon Assault" with:

CONTROLS:
- WASD: Movement
- Mouse: Aim
- Left Click: Shoot
- Space: Dash
- R: Reload

WEAPONS:
- Pistol: Starter weapon, unlimited ammo
- Shotgun: Close range, limited ammo
- Rifle: Auto-fire, medium range
- Sniper: High damage, slow fire rate
- Rocket Launcher: Explosive damage

ENEMIES:
- Grunts: Move toward player, low HP
- Snipers: Keep distance, high accuracy
- Tanks: Slow, high HP, heavy damage
- Drones: Flying, erratic movement

GAME MODES:
- Wave Survival: Endless waves
- Timed: Kill quota in time limit
- Boss Rush: Fight 5 unique bosses

SYSTEMS:
- Health and armor
- Ammo management
- Weapon switching (number keys)
- Upgrades between waves
- Damage numbers
- Particle effects

UI:
- Health/armor bars
- Ammo counter
- Wave indicator
- Weapon selector
- Upgrade shop
- Death statistics

TECHNICAL:
- Canvas 2D rendering
- Quadtree spatial partitioning
- Bullet pooling for performance
- Particle system
- Sound manager
- Save/load system

Include complete code, weapon balancing, and enemy spawning algorithm.
```

### Customize It

```
"Add vehicles (tank, mech)"
"Create co-op multiplayer"
"Add skill tree system"
"Implement roguelike elements (random weapons)"
```

### Time Estimate
- Base game: 20 minutes
- Customization: 15-40 minutes
- **Total: 35-60 minutes**

---

## Template 3: Match-3 Puzzle "Gem Crush"

### Base Prompt

```
Create a match-3 puzzle game called "Gem Crush" with:

MECHANICS:
- 8x8 grid
- Swap adjacent gems
- Match 3+ to clear
- Gravity and gem falling
- Cascade combos

GEM TYPES:
- 6 basic colors
- Striped gems (match 4): Clear row/column
- Bomb gems (match 5): 3x3 explosion
- Rainbow gems (match 5+): Clear all of one color

SPECIAL FEATURES:
- Combo multiplier
- Timed mode: 60 seconds
- Moves mode: 30 moves limit
- Target mode: Collect specific gems
- Obstacle blocks

POWER-UPS:
- Hammer: Destroy single gem
- Shuffle: Reorganize board
- Color Bomb: Remove one color
- Extra moves/time

PROGRESSION:
- 50 levels
- Star rating (1-3 stars)
- Difficulty curve
- New mechanics every 10 levels

UI:
- Score display
- Move/time counter
- Target progress
- Lives system
- Level map

TECHNICAL:
- Canvas or DOM-based
- Match detection algorithm
- Animation tweening
- Sound effects
- Particle effects
- Save progress

Include complete code, level design format, and balancing system.
```

### Customize It

```
"Add daily challenges"
"Create tournament mode"
"Add character progression"
"Implement in-app purchases"
```

### Time Estimate
- Base game: 20 minutes
- Customization: 15-30 minutes
- **Total: 35-50 minutes**

---

## Template 4: RPG Battle System "Fantasy Battle"

### Base Prompt

```
Create a turn-based RPG battle system called "Fantasy Battle" with:

PARTY SYSTEM:
- 3 heroes (Warrior, Mage, Healer)
- HP, MP, Stats (ATK, DEF, SPD, MAG)
- Equipment slots (Weapon, Armor, Accessory)
- Level and XP system

BATTLE MECHANICS:
- Turn order based on SPD stat
- Action menu: Attack, Magic, Items, Defend
- Elemental system (Fire, Water, Earth, Wind)
- Status effects (Poison, Burn, Stun, Sleep)
- Combo attacks (specific skill sequences)

SKILLS:
- Warrior: Slash, Power Strike, Taunt, Rage
- Mage: Fireball, Ice Shard, Lightning, Heal
- Healer: Cure, Revive, Barrier, Cleanse

ENEMIES:
- 10 enemy types
- Boss enemies with unique patterns
- Enemy AI (prioritize targets, use skills)
- Loot drops

UI:
- Character portraits and HP/MP bars
- Battle log
- Skill selection menu
- Damage numbers with animations
- Victory screen with rewards

SYSTEMS:
- Equipment system
- Inventory management
- Save/load battles
- Tutorial battle
- Difficulty settings

TECHNICAL:
- State machine for battle flow
- Damage calculation formulas
- AI decision tree
- Animation system
- Sound effects
- Battle transitions

Include complete code, skill balancing, and enemy AI patterns.
```

### Customize It

```
"Add real-time combat option"
"Create job/class system"
"Add summons/pets"
"Implement crafting system"
```

### Time Estimate
- Base game: 30 minutes
- Customization: 20-45 minutes
- **Total: 50-75 minutes**

---

## Template 5: Idle Clicker "Cookie Empire"

### Base Prompt

```
Create an idle clicker game called "Cookie Empire" with:

CORE LOOP:
- Click to generate cookies
- Buy upgrades with cookies
- Upgrades generate cookies passively
- Prestige system for multipliers

UPGRADES:
Tier 1:
- Grandma: 1 cookie/sec (Cost: 10)
- Farm: 5 cookies/sec (Cost: 100)
- Factory: 20 cookies/sec (Cost: 1,000)

Tier 2:
- Mine: 100 cookies/sec (Cost: 10,000)
- Wizard: 500 cookies/sec (Cost: 100,000)
- Portal: 2,000 cookies/sec (Cost: 1,000,000)

Tier 3:
- Time Machine: 10,000 cookies/sec
- Galaxy: 50,000 cookies/sec
- Universe: 200,000 cookies/sec

FEATURES:
- Offline progress
- Golden cookies (random bonus)
- Achievements (100+ achievements)
- Prestige currency (sugar)
- Sugar upgrades (permanent multipliers)
- Auto-clickers
- Mini-games for bonuses

UI:
- Big cookie to click
- Upgrade shop
- Stats display
- Achievement panel
- Prestige panel
- Settings

TECHNICAL:
- Big number formatting (1.5M, 2.3B, etc.)
- Save/load with compression
- Offline time calculation
- Notification system
- Cloud save (optional)
- Anti-cheat

Include complete code, balancing formulas, and progression curve.
```

### Customize It

```
"Add seasonal events"
"Create clan/guild system"
"Add trading between players"
"Implement battle system for resources"
```

### Time Estimate
- Base game: 25 minutes
- Customization: 15-35 minutes
- **Total: 40-60 minutes**

---

## Template 6: Racing Game "Neon Racer"

### Base Prompt

```
Create a top-down racing game called "Neon Racer" with:

CONTROLS:
- Arrow Keys/WASD: Steering and acceleration
- Space: Brake/Reverse
- Shift: Boost

RACING:
- 6 unique tracks
- 4 AI opponents
- Lap system
- Checkpoints
- Position tracking (1st, 2nd, etc.)

FEATURES:
- Boost pickups
- Oil slick hazards
- Speed pads
- Shortcuts
- Weather effects (rain, snow)

GAME MODES:
- Single Race
- Time Trial
- Tournament (5 races)
- Elimination (last place eliminated each lap)

VEHICLES:
- 3 car types (Speed, Balanced, Handling)
- Unlockable vehicles
- Customization (color, decals)
- Upgrade system (engine, tires, boost)

UI:
- Speedometer
- Lap counter
- Position indicator
- Minimap
- Race results
- Garage/customization

TECHNICAL:
- Sprite rotation and scaling
- AI pathfinding
- Collision with track bounds
- Particle effects (smoke, sparks)
- Sound effects
- Ghost replay for time trials

Include complete code, track design format, and AI racing algorithm.
```

### Customize It

```
"Add combat (weapons on track)"
"Create track editor"
"Add online multiplayer"
"Implement drift mechanics"
```

### Time Estimate
- Base game: 30 minutes
- Customization: 20-40 minutes
- **Total: 50-70 minutes**

---

## Template 7: Tower Defense "Castle Guard"

### Base Prompt

```
Create a tower defense game called "Castle Guard" with:

TOWERS:
- Arrow Tower: Fast, low damage
- Cannon Tower: Slow, high damage, AoE
- Magic Tower: Medium speed, slows enemies
- Lightning Tower: Chain lightning
- Ice Tower: Freezes enemies

ENEMIES:
- Goblin: Fast, low HP
- Orc: Medium stats
- Troll: Slow, high HP
- Flying Demon: Flies over obstacles
- Boss: Unique abilities each wave

MECHANICS:
- Grid-based tower placement
- Tower upgrades (3 levels each)
- Wave system (20 waves)
- Path that enemies follow
- Lives system
- Gold economy

FEATURES:
- Different maps (3 unique maps)
- Tower selling (50% refund)
- Speed controls (1x, 2x, 4x)
- Wave preview
- Special abilities (meteor, freeze all)

UI:
- Tower selection menu
- Upgrade panel
- Wave indicator
- Gold counter
- Lives display
- Victory/defeat screens

TECHNICAL:
- Pathfinding (A* algorithm)
- Tower targeting priority
- Damage calculations
- Particle effects
- Sound effects
- Save/load game state

Include complete code, balancing spreadsheet, and wave progression.
```

### Customize It

```
"Add hero units that level up"
"Create mazing strategy (build your path)"
"Add tower synergies"
"Implement endless mode"
```

### Time Estimate
- Base game: 35 minutes
- Customization: 20-45 minutes
- **Total: 55-80 minutes**

---

## Template 8: Card Battler "Deck Master"

### Base Prompt

```
Create a deck-building card game called "Deck Master" with:

CARD SYSTEM:
- 50 unique cards
- Card types: Attack, Defense, Spell, Summon
- Mana cost (0-10 mana)
- Rarity (Common, Rare, Epic, Legendary)

GAMEPLAY:
- Turn-based
- 30 card deck
- Draw 5 cards per turn
- 10 max mana, +1 per turn
- Attack enemy hero (30 HP)

CARD EFFECTS:
- Direct damage
- Healing
- Card draw
- Mana manipulation
- Creature summoning
- Board clear

CREATURES:
- Attack and HP stats
- Can attack each turn
- Defender: Must be attacked first
- Charge: Can attack immediately
- Taunt, Poison, Lifesteal

PROGRESSION:
- 10 AI opponents
- Unlock cards by winning
- Deck building screen
- Card crafting system
- Daily quests

UI:
- Hand display
- Mana crystals
- Hero portraits and HP
- Board state
- Deck and discard counters
- Card collection

TECHNICAL:
- Card data structure
- Game state management
- AI opponent logic
- Animation system
- Sound effects
- Save/load decks

Include complete code, card database, and AI decision making.
```

### Customize It

```
"Add PvP multiplayer"
"Create draft mode"
"Add tournament mode"
"Implement card trading"
```

### Time Estimate
- Base game: 40 minutes
- Customization: 25-50 minutes
- **Total: 65-90 minutes**

---

## Template 9: Metroidvania "Shadow Explorer"

### Base Prompt

```
Create a metroidvania platformer called "Shadow Explorer" with:

CORE MECHANICS:
- Smooth platforming
- Wall jumping
- Dash ability
- Grappling hook
- Unlockable abilities

ABILITIES:
- Double Jump (unlocked: Area 2)
- Dash (unlocked: Area 3)
- Wall Run (unlocked: Area 4)
- Grapple (unlocked: Area 5)
- Shadow Form (unlocked: Boss)

MAP:
- Interconnected world
- 5 major areas
- Secret rooms
- Save points
- Ability gates (can't pass without ability)

COMBAT:
- Sword attack (3-hit combo)
- Ranged attack (limited ammo)
- Special attacks
- Enemy variety (10 types)
- Boss battles (5 unique bosses)

PROGRESSION:
- Health upgrades
- Energy upgrades
- Weapon upgrades
- Collectibles (100% completion)

UI:
- Mini-map
- Health/energy bars
- Ability indicators
- Inventory
- Map screen (unlockable)

TECHNICAL:
- Tile-based level design
- Camera system (smooth following)
- Save system with checkpoints
- Particle effects
- Animation state machine
- Sound and music

Include complete code, map editor format, and ability progression.
```

### Customize It

```
"Add RPG elements (leveling, stats)"
"Create randomizer mode"
"Add New Game+ with harder enemies"
"Implement speedrun timer"
```

### Time Estimate
- Base game: 45 minutes
- Customization: 30-60 minutes
- **Total: 75-105 minutes**

---

## Template 10: Roguelike "Dungeon Depths"

### Base Prompt

```
Create a roguelike dungeon crawler called "Dungeon Depths" with:

CORE LOOP:
- Procedurally generated floors
- Permadeath
- Run-based progression
- Random items and enemies

GAMEPLAY:
- Turn-based movement
- Combat (attack, defend, use items)
- Hunger system
- Vision/fog of war
- 20 floors to complete

CHARACTER:
- HP, Strength, Defense, Luck
- Equipment slots (Weapon, Armor, Ring)
- Inventory (20 slots)
- Status effects

ITEMS:
- Weapons: Swords, bows, magic staffs
- Armor: Cloth, leather, plate
- Consumables: Potions, scrolls, food
- Unique artifacts

ENEMIES:
- 15 enemy types
- Boss every 5 floors
- Enemy scaling with depth
- Special abilities

FEATURES:
- Procedural dungeon generation
- Item identification
- Shops every 3 floors
- Cursed items
- Secret rooms

META PROGRESSION:
- Permanent upgrades with gems
- Unlockable character classes
- Achievement system
- Daily challenges

UI:
- Top-down view
- Status bars
- Message log
- Inventory screen
- Character sheet

TECHNICAL:
- Dungeon generation algorithm
- Pathfinding for enemies
- Turn system
- Save/load (single save)
- Seed-based generation
- Leaderboard

Include complete code, item database, and generation algorithms.
```

### Customize It

```
"Add multiple character classes"
"Create challenge modes (speed run, no items)"
"Add pets/companions"
"Implement clan halls (persistent upgrades)"
```

### Time Estimate
- Base game: 50 minutes
- Customization: 30-60 minutes
- **Total: 80-110 minutes**

---

## Bonus: Multiplayer Templates

### Template 11: .io Game "Circle.io"

```
Create a multiplayer .io game with:
- Real-time WebSocket gameplay
- Grow by collecting orbs
- Eat smaller players
- Leaderboard
- Smooth interpolation
- Mobile controls
- Server-authoritative

Customize: Add abilities, teams, game modes
Time: 60-90 minutes
```

### Template 12: Turn-Based Multiplayer "Chess Clone"

```
Create turn-based multiplayer game:
- Socket.io for networking
- Room system
- Player matching
- Turn validation
- Move history
- Spectator mode
- ELO rating

Customize: Different game (checkers, cards, etc.)
Time: 50-80 minutes
```

---

## How to Combine Templates

**Example 1: Metroidvania + Roguelike**
```
"Take the Shadow Explorer template and add:
- Procedural level generation
- Permadeath with meta progression
- Random ability pickups
- Seed-based randomization"
```

**Example 2: Card Game + RPG Battle**
```
"Combine Deck Master and Fantasy Battle:
- Use card system for all attacks
- Build deck between battles
- Enemies have decks too
- Loot is cards"
```

**Example 3: Tower Defense + Roguelike**
```
"Merge Castle Guard with Dungeon Depths:
- Random tower types each run
- Roguelike meta progression
- Procedural wave composition
- Permadeath but unlock new towers"
```

---

## Custom Template Generator

**Don't see what you want? Use this:**

```
Create a [GENRE] game called "[NAME]" with:

CORE MECHANICS:
- [Mechanic 1]
- [Mechanic 2]
- [Mechanic 3]

FEATURES:
- [Feature 1]
- [Feature 2]
- [Feature 3]

GAME MODES:
- [Mode 1]
- [Mode 2]

PROGRESSION:
- [System 1]
- [System 2]

UI:
- [Element 1]
- [Element 2]

TECHNICAL:
- [Technology choice]
- [Performance requirement]
- [Platform target]

Include complete code, asset list, and [SPECIFIC NEED].
```

---

## Tips for Success

### DO:
✅ Start with a template
✅ Customize gradually
✅ Test after each change
✅ Keep it simple at first
✅ Add polish later

### DON'T:
❌ Try to build everything at once
❌ Ignore performance
❌ Skip testing
❌ Forget mobile users
❌ Over-complicate

---

## Next Steps

1. **Pick a template** that excites you
2. **Copy the prompt** to Claude Code
3. **Get the base game** in 15-50 minutes
4. **Customize** to make it unique
5. **Deploy** and share!

**Share your games with #template-game in the community!**

---

**Pro Tip:** Mix and match features from different templates to create unique hybrid games!

**Questions?** Tag #templates in the community
