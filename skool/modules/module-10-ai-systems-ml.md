# Module 10: AI Systems & Machine Learning for Games

## 🎯 Learning Objectives

- Implement intelligent NPC behavior (FSM, Behavior Trees, GOAP)
- Apply machine learning to game AI
- Create adaptive difficulty systems
- Build procedural content generation with AI
- Implement pathfinding algorithms (A*, NavMesh)
- Design emergent gameplay systems

---

## 📚 Module Overview

**Duration:** 6-8 weeks | **Difficulty:** Advanced
**Prerequisites:** Module 8, Python/JavaScript, Basic ML knowledge

---

## 🗓️ Core Topics

### Week 1-2: Classical Game AI

**Finite State Machines:**
```javascript
class EnemyFSM {
  constructor(entity) {
    this.entity = entity;
    this.states = {
      idle: new IdleState(this),
      patrol: new PatrolState(this),
      chase: new ChaseState(this),
      attack: new AttackState(this)
    };
    this.currentState = this.states.idle;
  }

  update(dt) {
    const nextState = this.currentState.update(dt);
    if (nextState) this.transition(nextState);
  }

  transition(stateName) {
    this.currentState.exit();
    this.currentState = this.states[stateName];
    this.currentState.enter();
  }
}
```

**Behavior Trees:**
```javascript
class BehaviorTree {
  constructor(root) {
    this.root = root;
  }

  tick(entity, dt) {
    return this.root.execute(entity, dt);
  }
}

class SelectorNode {
  constructor(children) {
    this.children = children;
  }

  execute(entity, dt) {
    for (const child of this.children) {
      const result = child.execute(entity, dt);
      if (result === 'SUCCESS' || result === 'RUNNING') {
        return result;
      }
    }
    return 'FAILURE';
  }
}

// Usage
const enemyBehavior = new BehaviorTree(
  new SelectorNode([
    new SequenceNode([
      new ConditionNode((e) => e.canSeePlayer()),
      new ActionNode((e) => e.attackPlayer())
    ]),
    new ActionNode((e) => e.patrol())
  ])
);
```

**A* Pathfinding:**
```javascript
class Pathfinder {
  findPath(start, goal, grid) {
    const openSet = [start];
    const cameFrom = new Map();
    const gScore = new Map();
    const fScore = new Map();

    gScore.set(start, 0);
    fScore.set(start, this.heuristic(start, goal));

    while (openSet.length > 0) {
      const current = this.getLowestFScore(openSet, fScore);

      if (current === goal) {
        return this.reconstructPath(cameFrom, current);
      }

      openSet.splice(openSet.indexOf(current), 1);

      for (const neighbor of this.getNeighbors(current, grid)) {
        const tentativeGScore = gScore.get(current) + 1;

        if (tentativeGScore < (gScore.get(neighbor) || Infinity)) {
          cameFrom.set(neighbor, current);
          gScore.set(neighbor, tentativeGScore);
          fScore.set(neighbor, tentativeGScore + this.heuristic(neighbor, goal));

          if (!openSet.includes(neighbor)) {
            openSet.push(neighbor);
          }
        }
      }
    }

    return null; // No path found
  }

  heuristic(a, b) {
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
  }
}
```

### Week 3-4: Machine Learning Integration

**Neural Network for Game AI:**
```python
import tensorflow as tf
import numpy as np

class GameAI:
    def __init__(self, state_size, action_size):
        self.model = self.build_model(state_size, action_size)
        self.memory = []
        self.gamma = 0.95  # Discount factor
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01

    def build_model(self, state_size, action_size):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(24, activation='relu', input_shape=(state_size,)),
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(action_size, activation='linear')
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return np.random.randint(0, self.action_size)

        q_values = self.model.predict(state[np.newaxis])
        return np.argmax(q_values[0])

    def train(self, batch_size=32):
        if len(self.memory) < batch_size:
            return

        minibatch = random.sample(self.memory, batch_size)

        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target += self.gamma * np.amax(self.model.predict(next_state[np.newaxis])[0])

            target_f = self.model.predict(state[np.newaxis])
            target_f[0][action] = target

            self.model.fit(state[np.newaxis], target_f, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
```

### Week 5-6: Procedural Generation

**PCG with WaveFunctionCollapse:**
```javascript
class WaveFunctionCollapse {
  constructor(tiles, width, height) {
    this.tiles = tiles;
    this.width = width;
    this.height = height;
    this.grid = this.initializeGrid();
  }

  initializeGrid() {
    const grid = [];
    for (let y = 0; y < this.height; y++) {
      grid[y] = [];
      for (let x = 0; x < this.width; x++) {
        grid[y][x] = {
          possibilities: [...this.tiles],
          collapsed: false
        };
      }
    }
    return grid;
  }

  generate() {
    while (!this.isFullyCollapsed()) {
      const cell = this.getLowestEntropyCell();
      if (!cell) break;

      this.collapse(cell);
      this.propagate(cell);
    }

    return this.grid;
  }

  getLowestEntropyCell() {
    let minEntropy = Infinity;
    let candidates = [];

    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        const cell = this.grid[y][x];
        if (!cell.collapsed) {
          const entropy = cell.possibilities.length;
          if (entropy < minEntropy) {
            minEntropy = entropy;
            candidates = [{ x, y }];
          } else if (entropy === minEntropy) {
            candidates.push({ x, y });
          }
        }
      }
    }

    return candidates[Math.floor(Math.random() * candidates.length)];
  }

  collapse(cell) {
    const { x, y } = cell;
    const possibilities = this.grid[y][x].possibilities;
    const chosen = possibilities[Math.floor(Math.random() * possibilities.length)];

    this.grid[y][x].possibilities = [chosen];
    this.grid[y][x].collapsed = true;
  }
}
```

### Week 7-8: Advanced Systems

**Utility AI:**
```javascript
class UtilityAI {
  constructor() {
    this.actions = [];
  }

  addAction(action) {
    this.actions.push(action);
  }

  selectBestAction(context) {
    let bestAction = null;
    let bestScore = -Infinity;

    for (const action of this.actions) {
      const score = action.calculateUtility(context);
      if (score > bestScore) {
        bestScore = score;
        bestAction = action;
      }
    }

    return bestAction;
  }
}

class Action {
  constructor(name, considerations) {
    this.name = name;
    this.considerations = considerations;
  }

  calculateUtility(context) {
    let score = 1.0;

    for (const consideration of this.considerations) {
      score *= consideration.evaluate(context);
    }

    return score;
  }
}

// Usage
const ai = new UtilityAI();

ai.addAction(new Action('attack', [
  { evaluate: (ctx) => ctx.playerNearby ? 1.0 : 0.0 },
  { evaluate: (ctx) => ctx.health / 100 }
]));

ai.addAction(new Action('heal', [
  { evaluate: (ctx) => 1.0 - (ctx.health / 100) },
  { evaluate: (ctx) => ctx.hasHealthPack ? 1.0 : 0.0 }
]));
```

---

## 🎓 Projects

1. **Smart NPC System** - Behavior trees + pathfinding
2. **ML Racing AI** - Train AI to race using reinforcement learning
3. **Procedural Dungeon** - WFC algorithm for level generation
4. **Adaptive Difficulty** - ML-powered dynamic difficulty adjustment

---

## 📖 Resources

- "AI for Games" by Ian Millington
- "Programming Game AI by Example" by Mat Buckland
- Unity ML-Agents Toolkit
- TensorFlow.js documentation

---

## ✅ Assessment

**Passing Grade:** 75%
- Behavior implementation (40%)
- ML integration (30%)
- Final project (30%)

**Career Paths:** AI Programmer, Gameplay Engineer, Technical Designer

**Salary Range:** $90,000 - $170,000

---

**Module Created:** 2025-11-02
