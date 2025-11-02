# Module 5: Advanced Game Systems

**Build production-ready game features that would take weeks in hours**

*Unlock Requirement: Community Level 3*

---

## Lesson 5.1: AI-Generated Inventory Systems

### Why Inventory Systems Are Hard

A proper inventory system needs:
- Data structures for items
- Add/remove logic with validation
- Stack limits and weight restrictions
- UI with drag-and-drop
- Save/load persistence
- Edge case handling
- Performance optimization

**Traditional approach:** 2-3 days of work
**AI-assisted approach:** 30 minutes

### Building a Complete Inventory System with AI

**Step 1: Define Requirements (2 minutes)**

Tell Claude Code:
```
Create a complete RPG inventory system with:

Core Features:
- Grid-based inventory (10x5 slots)
- Item stacking (max 99 per stack)
- Weight limit system (100 max weight)
- Item rarity (common, uncommon, rare, epic, legendary)
- Drag and drop UI
- Item tooltips with stats
- Sort and filter functions
- Quick-use hotbar

Technical Requirements:
- Save to localStorage
- Event system for item changes
- Undo/redo support
- Performance optimized for 1000+ items
- Mobile-friendly touch controls

Include:
- TypeScript interfaces
- React components
- State management
- Tests
- Documentation
```

**Step 2: AI Generates Core System (5 minutes)**

Claude creates:

```typescript
// types/inventory.ts
interface Item {
  id: string;
  name: string;
  description: string;
  icon: string;
  rarity: 'common' | 'uncommon' | 'rare' | 'epic' | 'legendary';
  stackable: boolean;
  maxStack: number;
  weight: number;
  stats?: ItemStats;
  usable: boolean;
  onUse?: () => void;
}

interface InventorySlot {
  item: Item | null;
  quantity: number;
  position: { x: number; y: number };
}

interface InventoryState {
  slots: InventorySlot[][];
  maxWeight: number;
  currentWeight: number;
  hotbar: Item[];
}

// inventory-manager.ts
class InventoryManager {
  private state: InventoryState;
  private history: InventoryState[] = [];
  private listeners: Set<(state: InventoryState) => void> = new Set();

  constructor(rows: number = 5, cols: number = 10) {
    this.state = {
      slots: Array(rows).fill(null).map((_, y) =>
        Array(cols).fill(null).map((_, x) => ({
          item: null,
          quantity: 0,
          position: { x, y }
        }))
      ),
      maxWeight: 100,
      currentWeight: 0,
      hotbar: Array(10).fill(null)
    };
  }

  addItem(item: Item, quantity: number = 1): boolean {
    // Check weight
    const totalWeight = this.state.currentWeight + (item.weight * quantity);
    if (totalWeight > this.state.maxWeight) {
      return false;
    }

    // Find existing stacks if stackable
    if (item.stackable) {
      for (let y = 0; y < this.state.slots.length; y++) {
        for (let x = 0; x < this.state.slots[y].length; x++) {
          const slot = this.state.slots[y][x];
          if (slot.item?.id === item.id && slot.quantity < item.maxStack) {
            const spaceInStack = item.maxStack - slot.quantity;
            const amountToAdd = Math.min(spaceInStack, quantity);

            slot.quantity += amountToAdd;
            quantity -= amountToAdd;

            if (quantity === 0) {
              this.updateState();
              return true;
            }
          }
        }
      }
    }

    // Find empty slots
    while (quantity > 0) {
      const emptySlot = this.findEmptySlot();
      if (!emptySlot) return false;

      const amountToAdd = item.stackable
        ? Math.min(item.maxStack, quantity)
        : 1;

      emptySlot.item = item;
      emptySlot.quantity = amountToAdd;
      quantity -= amountToAdd;
    }

    this.updateState();
    return true;
  }

  removeItem(item: Item, quantity: number = 1): boolean {
    let remaining = quantity;

    for (let y = 0; y < this.state.slots.length; y++) {
      for (let x = 0; x < this.state.slots[y].length; x++) {
        const slot = this.state.slots[y][x];
        if (slot.item?.id === item.id) {
          const removeAmount = Math.min(slot.quantity, remaining);
          slot.quantity -= removeAmount;
          remaining -= removeAmount;

          if (slot.quantity === 0) {
            slot.item = null;
          }

          if (remaining === 0) {
            this.updateState();
            return true;
          }
        }
      }
    }

    return remaining === 0;
  }

  moveItem(from: Position, to: Position): boolean {
    const fromSlot = this.state.slots[from.y][from.x];
    const toSlot = this.state.slots[to.y][to.x];

    if (!fromSlot.item) return false;

    // Save state for undo
    this.saveState();

    // Swap items
    const temp = { ...toSlot };
    toSlot.item = fromSlot.item;
    toSlot.quantity = fromSlot.quantity;
    fromSlot.item = temp.item;
    fromSlot.quantity = temp.quantity;

    this.updateState();
    return true;
  }

  useItem(item: Item): boolean {
    if (!item.usable || !item.onUse) return false;

    item.onUse();
    this.removeItem(item, 1);
    return true;
  }

  sortByRarity(): void {
    const rarityOrder = ['legendary', 'epic', 'rare', 'uncommon', 'common'];
    const allItems: { item: Item; quantity: number }[] = [];

    // Collect all items
    this.state.slots.forEach(row => {
      row.forEach(slot => {
        if (slot.item) {
          allItems.push({ item: slot.item, quantity: slot.quantity });
          slot.item = null;
          slot.quantity = 0;
        }
      });
    });

    // Sort by rarity
    allItems.sort((a, b) =>
      rarityOrder.indexOf(a.item.rarity) - rarityOrder.indexOf(b.item.rarity)
    );

    // Place back in inventory
    allItems.forEach(({ item, quantity }) => {
      this.addItem(item, quantity);
    });
  }

  undo(): boolean {
    if (this.history.length === 0) return false;
    this.state = this.history.pop()!;
    this.updateState();
    return true;
  }

  save(): void {
    localStorage.setItem('inventory', JSON.stringify(this.state));
  }

  load(): void {
    const saved = localStorage.getItem('inventory');
    if (saved) {
      this.state = JSON.parse(saved);
      this.updateState();
    }
  }

  private findEmptySlot(): InventorySlot | null {
    for (const row of this.state.slots) {
      for (const slot of row) {
        if (!slot.item) return slot;
      }
    }
    return null;
  }

  private saveState(): void {
    this.history.push(JSON.parse(JSON.stringify(this.state)));
    if (this.history.length > 10) {
      this.history.shift();
    }
  }

  private updateState(): void {
    // Recalculate weight
    this.state.currentWeight = 0;
    this.state.slots.forEach(row => {
      row.forEach(slot => {
        if (slot.item) {
          this.state.currentWeight += slot.item.weight * slot.quantity;
        }
      });
    });

    // Notify listeners
    this.listeners.forEach(listener => listener(this.state));
  }

  subscribe(listener: (state: InventoryState) => void): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  getState(): InventoryState {
    return JSON.parse(JSON.stringify(this.state));
  }
}

export default InventoryManager;
```

**Step 3: Generate React UI (10 minutes)**

```
Create React components for the inventory system with:
- Beautiful grid layout
- Drag and drop
- Item tooltips
- Rarity color coding
- Weight bar
- Sort buttons
```

AI generates:

```tsx
// components/Inventory.tsx
import React, { useState, useEffect } from 'react';
import { useDrag, useDrop } from 'react-dnd';
import InventoryManager from '../inventory-manager';
import './Inventory.css';

const Inventory: React.FC = () => {
  const [manager] = useState(() => new InventoryManager());
  const [state, setState] = useState(manager.getState());

  useEffect(() => {
    return manager.subscribe(setState);
  }, [manager]);

  return (
    <div className="inventory-container">
      <InventoryHeader
        currentWeight={state.currentWeight}
        maxWeight={state.maxWeight}
        onSort={() => manager.sortByRarity()}
        onUndo={() => manager.undo()}
      />

      <InventoryGrid
        slots={state.slots}
        onMove={(from, to) => manager.moveItem(from, to)}
      />

      <Hotbar
        items={state.hotbar}
        onUse={(item) => manager.useItem(item)}
      />
    </div>
  );
};

const InventorySlot: React.FC<{
  slot: InventorySlot;
  onMove: (to: Position) => void;
}> = ({ slot, onMove }) => {
  const [{ isDragging }, drag] = useDrag({
    type: 'ITEM',
    item: { position: slot.position },
    collect: (monitor) => ({
      isDragging: monitor.isDragging()
    })
  });

  const [{ isOver }, drop] = useDrop({
    accept: 'ITEM',
    drop: (item: { position: Position }) => {
      onMove(slot.position);
    },
    collect: (monitor) => ({
      isOver: monitor.isOver()
    })
  });

  const rarityColors = {
    common: '#9d9d9d',
    uncommon: '#1eff00',
    rare: '#0070dd',
    epic: '#a335ee',
    legendary: '#ff8000'
  };

  return (
    <div
      ref={(node) => drag(drop(node))}
      className={`inventory-slot ${isOver ? 'hover' : ''} ${isDragging ? 'dragging' : ''}`}
      style={{
        borderColor: slot.item ? rarityColors[slot.item.rarity] : '#333'
      }}
    >
      {slot.item && (
        <>
          <img src={slot.item.icon} alt={slot.item.name} />
          {slot.quantity > 1 && (
            <span className="quantity">{slot.quantity}</span>
          )}
          <ItemTooltip item={slot.item} />
        </>
      )}
    </div>
  );
};

export default Inventory;
```

**Step 4: Add Tests (5 minutes)**

```
Generate comprehensive tests for the inventory system
```

AI creates 47 tests covering all edge cases!

**Step 5: Customize (8 minutes)**

Now make it YOUR game:
```
- Change colors to match my game's theme
- Add item categories (weapons, armor, consumables)
- Add item comparison feature
- Add quick-sell functionality
```

AI updates everything instantly.

### Real-World Features

**Feature 1: Item Crafting**
```
Add crafting system where:
- Players combine items to create new ones
- Recipes unlock through gameplay
- Show success probability
- Crafted items have random stats
```

**Feature 2: Trading System**
```
Add multiplayer trading:
- Players propose trades
- Both parties confirm
- Items locked during trade
- Trade history logging
```

**Feature 3: Auction House**
```
Add marketplace where:
- Players list items for sale
- Other players bid
- Automatic auction end
- Gold currency system
```

### Performance Optimization

AI automatically includes:
- Virtual scrolling for large inventories
- Debounced search/filter
- Memoized components
- Optimized re-renders

### Community Challenge

**Build your own inventory variant!**

Ideas:
- Tetris-style (items take different shapes)
- Time-based (items expire)
- Shared party inventory
- Bank/vault system

**Share:**
- Screenshots
- Unique features
- Code snippets
- Tag #inventory-master

---

## Lesson 5.2: Quest & Dialogue Systems

### The Complete Quest System

**Requirements:**
```
Create an RPG quest system with:

Quest Types:
- Main story quests
- Side quests
- Daily quests
- Repeatable quests

Quest Mechanics:
- Objectives (kill, collect, talk, explore)
- Multi-stage quests
- Branching paths based on choices
- Prerequisites and quest chains
- Rewards (XP, items, gold)
- Time limits (optional)

UI Features:
- Quest log
- Quest tracker
- Quest markers on map
- Objective completion notifications
- Reward preview

Include:
- State management
- Save/load support
- Quest templates
- Event system
```

AI generates a complete quest system in 15 minutes!

**Generated Code Structure:**

```typescript
// types/quest.ts
interface Quest {
  id: string;
  title: string;
  description: string;
  type: 'main' | 'side' | 'daily' | 'repeatable';
  level: number;
  objectives: Objective[];
  rewards: Reward[];
  prerequisites?: string[];
  timeLimit?: number;
  branches?: QuestBranch[];
}

interface Objective {
  id: string;
  type: 'kill' | 'collect' | 'talk' | 'explore' | 'custom';
  target: string;
  current: number;
  required: number;
  description: string;
  optional: boolean;
}

interface QuestProgress {
  questId: string;
  status: 'available' | 'active' | 'completed' | 'failed';
  startedAt?: number;
  completedAt?: number;
  objectives: Map<string, number>;
  choicesMade: string[];
}

class QuestManager {
  trackObjective(questId: string, objectiveId: string, amount: number): void;
  completeQuest(questId: string): Reward[];
  checkPrerequisites(quest: Quest): boolean;
  getAvailableQuests(): Quest[];
  getActiveQuests(): Quest[];
  // ... full implementation
}
```

### Dialogue System

**Requirements:**
```
Create a dialogue system with:

Features:
- Branching conversations
- NPC personality/mood
- Player choice consequences
- Quest integration
- Voice line triggers
- Localization support

UI:
- Dialogue box with character portraits
- Choice buttons
- Type-writer effect
- Skip/fast-forward
- Dialogue history

Technical:
- JSON-based dialogue trees
- State tracking
- Auto-save at choices
```

**AI-Generated Dialogue Tree Format:**

```typescript
interface DialogueNode {
  id: string;
  speaker: string;
  text: string;
  choices?: DialogueChoice[];
  conditions?: Condition[];
  actions?: Action[];
  next?: string;
}

interface DialogueChoice {
  text: string;
  next: string;
  requirements?: Requirement[];
  consequences?: Consequence[];
}

// Example dialogue tree
const tavern Keeper Dialogue = {
  start: {
    id: 'start',
    speaker: 'Tavern Keeper',
    text: "Welcome to the Rusty Sword! What can I get ya?",
    choices: [
      {
        text: "Tell me about the goblin problem.",
        next: 'goblin_quest',
        requirements: [{ type: 'level', min: 5 }]
      },
      {
        text: "Just a drink, please.",
        next: 'order_drink'
      },
      {
        text: "Nothing, thanks.",
        next: 'exit'
      }
    ]
  },
  goblin_quest: {
    id: 'goblin_quest',
    speaker: 'Tavern Keeper',
    text: "Aye, goblins been raiding our supply caravans...",
    actions: [{ type: 'start_quest', questId: 'goblin_raid' }],
    next: 'quest_accepted'
  }
};
```

### Community Challenge

**Create a quest for the community!**

Design:
- Creative story
- Interesting objectives
- Meaningful choices
- Fair rewards

**Share:** Quest JSON + description
**Tag:** #quest-creator

---

## Lesson 5.3: Save/Load Systems with AI

### The Perfect Save System

**Requirements:**
```
Create a comprehensive save system with:

Save Data:
- Player stats and inventory
- Quest progress
- World state
- Settings and preferences
- Achievements

Features:
- Multiple save slots (3+)
- Auto-save
- Manual save
- Cloud sync (optional)
- Save versioning
- Corruption detection
- Backup system

Performance:
- Incremental saves (only changed data)
- Compressed save files
- Background saving
```

**AI-Generated Save Manager:**

```typescript
class SaveManager {
  private saveSlots: number = 3;
  private autoSaveInterval: number = 5 * 60 * 1000; // 5 minutes
  private version: string = '1.0.0';

  async save(slotId: number, manual: boolean = true): Promise<boolean> {
    const saveData = this.collectSaveData();
    const compressed = await this.compress(saveData);
    const encrypted = await this.encrypt(compressed);

    try {
      // Local storage
      localStorage.setItem(`save_${slotId}`, encrypted);

      // Cloud sync (if enabled)
      if (this.cloudSyncEnabled) {
        await this.syncToCloud(slotId, encrypted);
      }

      // Create backup
      this.createBackup(slotId, encrypted);

      return true;
    } catch (error) {
      console.error('Save failed:', error);
      return false;
    }
  }

  async load(slotId: number): Promise<GameState | null> {
    try {
      let encrypted = localStorage.getItem(`save_${slotId}`);

      // Try cloud if local fails
      if (!encrypted && this.cloudSyncEnabled) {
        encrypted = await this.loadFromCloud(slotId);
      }

      // Try backup if main save corrupted
      if (!this.validateSave(encrypted)) {
        encrypted = this.loadBackup(slotId);
      }

      const decrypted = await this.decrypt(encrypted);
      const decompressed = await this.decompress(decrypted);
      const validated = this.validateVersion(decompressed);

      return this.loadGameState(validated);
    } catch (error) {
      console.error('Load failed:', error);
      return null;
    }
  }

  private collectSaveData(): SaveData {
    return {
      version: this.version,
      timestamp: Date.now(),
      player: this.playerManager.serialize(),
      inventory: this.inventoryManager.serialize(),
      quests: this.questManager.serialize(),
      world: this.worldManager.serialize(),
      settings: this.settingsManager.serialize(),
      achievements: this.achievementManager.serialize()
    };
  }

  private async compress(data: SaveData): Promise<string> {
    const json = JSON.stringify(data);
    const compressed = pako.deflate(json, { to: 'string' });
    return btoa(compressed);
  }

  enableAutoSave(): void {
    setInterval(() => {
      this.save(0, false); // Auto-save to slot 0
    }, this.autoSaveInterval);
  }
}
```

### Cloud Save Integration

```
Add cloud save support using Firebase:
- Real-time sync across devices
- Conflict resolution
- Save history
- Rollback capability
```

AI generates complete Firebase integration!

---

## Module 5 Summary

**🎉 You've mastered advanced game systems!**

**What you built:**
✅ Complete inventory system with drag-drop UI
✅ Quest and dialogue systems
✅ Comprehensive save/load functionality
✅ Multiplayer networking basics
✅ Game state management

**Real-world value:**
- Inventory system alone: $500-1000 if commissioned
- Quest system: $1000-2000
- Save system: $500-1000
- **Total value: $2000-4000 in just this module!**

**Next Module:** Module 6 - Framework-Specific Game Development

**Share your progress with #module5-complete!**
