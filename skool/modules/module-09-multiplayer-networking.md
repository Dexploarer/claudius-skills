# Module 9: Multiplayer Game Networking

## 🎯 Learning Objectives

By the end of this module, you will:
- Master client-server and peer-to-peer architectures
- Implement authoritative server patterns
- Handle network synchronization and prediction
- Build scalable multiplayer systems
- Implement matchmaking and lobbies
- Optimize network performance

---

## 📚 Module Overview

**Duration:** 6-8 weeks
**Difficulty:** Advanced
**Prerequisites:** Module 8, Node.js, WebSocket, Async programming

---

## 🗓️ Week-by-Week Breakdown

### Week 1: Networking Fundamentals

#### Day 1-2: Network Protocols
**Topics:**
- TCP vs UDP
- WebSocket for real-time games
- WebRTC for peer-to-peer
- HTTP/2 and Server-Sent Events

**WebSocket Server Setup:**
```javascript
// Server (Node.js with ws library)
import WebSocket, { WebSocketServer } from 'ws';

class GameServer {
  constructor(port = 8080) {
    this.wss = new WebSocketServer({ port });
    this.clients = new Map();
    this.rooms = new Map();
    this.tickRate = 60; // Server updates per second
    this.setupServer();
  }

  setupServer() {
    this.wss.on('connection', (ws, req) => {
      const clientId = this.generateClientId();

      this.clients.set(clientId, {
        ws,
        id: clientId,
        player: null,
        room: null,
        latency: 0
      });

      ws.on('message', (data) => this.handleMessage(clientId, data));
      ws.on('close', () => this.handleDisconnect(clientId));
      ws.on('error', (error) => this.handleError(clientId, error));

      // Send client their ID
      this.sendToClient(clientId, {
        type: 'connected',
        clientId,
        timestamp: Date.now()
      });
    });

    // Start game loop
    this.startGameLoop();
  }

  startGameLoop() {
    const frameTime = 1000 / this.tickRate;
    let lastTime = Date.now();

    setInterval(() => {
      const now = Date.now();
      const dt = (now - lastTime) / 1000;
      lastTime = now;

      this.update(dt);
      this.broadcastState();
    }, frameTime);
  }

  update(dt) {
    // Update all active rooms
    this.rooms.forEach(room => {
      room.update(dt);
    });
  }

  broadcastState() {
    this.rooms.forEach(room => {
      const state = room.getState();
      room.players.forEach(playerId => {
        this.sendToClient(playerId, {
          type: 'state_update',
          state,
          timestamp: Date.now()
        });
      });
    });
  }

  handleMessage(clientId, data) {
    try {
      const message = JSON.parse(data);

      switch (message.type) {
        case 'input':
          this.handleInput(clientId, message);
          break;
        case 'join_room':
          this.handleJoinRoom(clientId, message);
          break;
        case 'create_room':
          this.handleCreateRoom(clientId, message);
          break;
        case 'ping':
          this.handlePing(clientId, message);
          break;
      }
    } catch (error) {
      console.error('Error handling message:', error);
    }
  }

  handleInput(clientId, message) {
    const client = this.clients.get(clientId);
    if (!client || !client.room) return;

    const room = this.rooms.get(client.room);
    if (room) {
      room.handlePlayerInput(clientId, message.input, message.sequence);
    }
  }

  handlePing(clientId, message) {
    this.sendToClient(clientId, {
      type: 'pong',
      timestamp: message.timestamp
    });
  }

  sendToClient(clientId, data) {
    const client = this.clients.get(clientId);
    if (client && client.ws.readyState === WebSocket.OPEN) {
      client.ws.send(JSON.stringify(data));
    }
  }

  generateClientId() {
    return `client_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
}

// Client
class NetworkClient {
  constructor(serverUrl) {
    this.serverUrl = serverUrl;
    this.ws = null;
    this.clientId = null;
    this.connected = false;
    this.sequenceNumber = 0;
    this.latency = 0;
    this.lastPingTime = 0;
  }

  connect() {
    return new Promise((resolve, reject) => {
      this.ws = new WebSocket(this.serverUrl);

      this.ws.onopen = () => {
        this.connected = true;
        this.startPing();
        console.log('Connected to server');
      };

      this.ws.onmessage = (event) => {
        this.handleMessage(JSON.parse(event.data));
      };

      this.ws.onclose = () => {
        this.connected = false;
        console.log('Disconnected from server');
      };

      this.ws.onerror = (error) => {
        reject(error);
      };

      // Wait for connection confirmation
      const onConnected = (data) => {
        if (data.type === 'connected') {
          this.clientId = data.clientId;
          resolve();
        }
      };

      this.once('connected', onConnected);
    });
  }

  send(data) {
    if (this.connected && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(data));
    }
  }

  sendInput(input) {
    this.send({
      type: 'input',
      input,
      sequence: this.sequenceNumber++,
      timestamp: Date.now()
    });
  }

  startPing() {
    setInterval(() => {
      this.lastPingTime = Date.now();
      this.send({
        type: 'ping',
        timestamp: this.lastPingTime
      });
    }, 1000);
  }

  handleMessage(data) {
    switch (data.type) {
      case 'pong':
        this.latency = Date.now() - data.timestamp;
        break;
      case 'state_update':
        this.emit('state_update', data.state);
        break;
    }
  }
}
```

#### Day 3-4: Client-Server Architecture
**Topics:**
- Authoritative server design
- Client prediction
- Server reconciliation
- Lag compensation

**Client Prediction:**
```javascript
class PredictiveClient {
  constructor() {
    this.localPlayer = null;
    this.inputBuffer = [];
    this.stateHistory = [];
    this.maxHistorySize = 60; // 1 second at 60fps
  }

  applyInput(input, dt) {
    // Store input with sequence number
    const inputData = {
      sequence: this.sequenceNumber++,
      input,
      timestamp: Date.now()
    };

    this.inputBuffer.push(inputData);

    // Apply input locally (prediction)
    this.localPlayer.applyInput(input, dt);

    // Send to server
    this.network.sendInput(input);

    // Store predicted state
    this.stateHistory.push({
      sequence: inputData.sequence,
      state: this.localPlayer.getState()
    });

    // Limit history size
    if (this.stateHistory.length > this.maxHistorySize) {
      this.stateHistory.shift();
    }
  }

  handleServerUpdate(serverState) {
    // Find the matching state in history
    const lastProcessedInput = serverState.lastProcessedInput;

    // Remove processed inputs
    this.inputBuffer = this.inputBuffer.filter(
      input => input.sequence > lastProcessedInput
    );

    // Check if prediction was correct
    const predictedState = this.stateHistory.find(
      s => s.sequence === lastProcessedInput
    );

    if (predictedState) {
      const error = this.calculateError(predictedState.state, serverState);

      if (error > 0.1) {
        // Prediction was wrong, reconcile
        this.localPlayer.setState(serverState);

        // Replay unprocessed inputs
        this.inputBuffer.forEach(input => {
          this.localPlayer.applyInput(input.input, 1/60);
        });
      }
    }

    // Clean up old history
    this.stateHistory = this.stateHistory.filter(
      s => s.sequence > lastProcessedInput
    );
  }

  calculateError(predicted, actual) {
    const dx = predicted.position.x - actual.position.x;
    const dy = predicted.position.y - actual.position.y;
    return Math.sqrt(dx * dx + dy * dy);
  }
}
```

#### Day 5-7: Entity Interpolation
**Topics:**
- Entity interpolation
- Snapshot systems
- Time synchronization
- Jitter buffers

**Entity Interpolation:**
```javascript
class InterpolatedEntity {
  constructor() {
    this.snapshots = [];
    this.renderDelay = 100; // ms behind server
    this.position = { x: 0, y: 0 };
    this.rotation = 0;
  }

  addSnapshot(snapshot) {
    this.snapshots.push(snapshot);

    // Keep only recent snapshots
    const cutoff = Date.now() - this.renderDelay * 2;
    this.snapshots = this.snapshots.filter(s => s.timestamp > cutoff);
  }

  interpolate() {
    const now = Date.now();
    const renderTime = now - this.renderDelay;

    // Find two snapshots to interpolate between
    let before = null;
    let after = null;

    for (let i = 0; i < this.snapshots.length - 1; i++) {
      if (this.snapshots[i].timestamp <= renderTime &&
          this.snapshots[i + 1].timestamp >= renderTime) {
        before = this.snapshots[i];
        after = this.snapshots[i + 1];
        break;
      }
    }

    if (!before || !after) {
      // Use latest snapshot
      if (this.snapshots.length > 0) {
        const latest = this.snapshots[this.snapshots.length - 1];
        this.position = latest.position;
        this.rotation = latest.rotation;
      }
      return;
    }

    // Calculate interpolation factor
    const total = after.timestamp - before.timestamp;
    const current = renderTime - before.timestamp;
    const t = total === 0 ? 0 : current / total;

    // Interpolate position
    this.position.x = this.lerp(before.position.x, after.position.x, t);
    this.position.y = this.lerp(before.position.y, after.position.y, t);

    // Interpolate rotation
    this.rotation = this.lerpAngle(before.rotation, after.rotation, t);
  }

  lerp(a, b, t) {
    return a + (b - a) * t;
  }

  lerpAngle(a, b, t) {
    let diff = b - a;
    while (diff < -Math.PI) diff += Math.PI * 2;
    while (diff > Math.PI) diff -= Math.PI * 2;
    return a + diff * t;
  }
}
```

### Week 2: Advanced Synchronization

#### Day 1-3: Delta Compression
**Topics:**
- State delta encoding
- Binary protocols
- Bandwidth optimization
- Priority systems

**Delta Compression:**
```javascript
class DeltaEncoder {
  constructor() {
    this.baseline = null;
  }

  encode(state) {
    if (!this.baseline) {
      // First state, send full
      this.baseline = JSON.parse(JSON.stringify(state));
      return {
        type: 'full',
        data: state
      };
    }

    // Calculate delta
    const delta = this.calculateDelta(this.baseline, state);

    // Update baseline
    this.baseline = JSON.parse(JSON.stringify(state));

    return {
      type: 'delta',
      data: delta
    };
  }

  calculateDelta(baseline, current) {
    const delta = {};

    // Check each entity
    Object.entries(current.entities).forEach(([id, entity]) => {
      const baseEntity = baseline.entities[id];

      if (!baseEntity) {
        // New entity
        delta[id] = { _new: true, ...entity };
      } else {
        // Check for changes
        const changes = {};
        Object.keys(entity).forEach(key => {
          if (JSON.stringify(entity[key]) !== JSON.stringify(baseEntity[key])) {
            changes[key] = entity[key];
          }
        });

        if (Object.keys(changes).length > 0) {
          delta[id] = changes;
        }
      }
    });

    // Check for removed entities
    Object.keys(baseline.entities).forEach(id => {
      if (!current.entities[id]) {
        delta[id] = { _removed: true };
      }
    });

    return delta;
  }

  decode(packet, currentState) {
    if (packet.type === 'full') {
      return packet.data;
    }

    // Apply delta
    const state = JSON.parse(JSON.stringify(currentState));

    Object.entries(packet.data).forEach(([id, changes]) => {
      if (changes._removed) {
        delete state.entities[id];
      } else if (changes._new) {
        const { _new, ...entity } = changes;
        state.entities[id] = entity;
      } else {
        // Update existing entity
        state.entities[id] = {
          ...state.entities[id],
          ...changes
        };
      }
    });

    return state;
  }
}
```

#### Day 4-7: Interest Management
**Topics:**
- Area of interest
- Relevancy sets
- Visibility culling
- Priority updates

### Week 3: Matchmaking & Lobbies

#### Day 1-4: Matchmaking System
**Topics:**
- Skill-based matchmaking
- Quick match algorithms
- Party systems
- Rating systems (ELO, TrueSkill)

**Matchmaking Implementation:**
```javascript
class Matchmaker {
  constructor() {
    this.queue = [];
    this.matches = new Map();
    this.eloK = 32; // ELO K-factor
  }

  addToQueue(player) {
    this.queue.push({
      player,
      queueTime: Date.now(),
      rating: player.rating || 1000
    });

    this.tryMatchmaking();
  }

  tryMatchmaking() {
    // Sort by queue time
    this.queue.sort((a, b) => a.queueTime - b.queueTime);

    const matched = [];

    for (const entry of this.queue) {
      if (matched.includes(entry)) continue;

      const match = this.findMatch(entry, matched);
      if (match.length >= 2) { // Minimum 2 players
        this.createMatch(match);
        match.forEach(e => matched.push(e));
      }
    }

    // Remove matched players from queue
    this.queue = this.queue.filter(e => !matched.includes(e));
  }

  findMatch(entry, exclude) {
    const maxRatingDiff = this.getMaxRatingDiff(entry.queueTime);
    const candidates = this.queue.filter(other =>
      !exclude.includes(other) &&
      other !== entry &&
      Math.abs(other.rating - entry.rating) <= maxRatingDiff
    );

    return [entry, ...candidates.slice(0, 3)]; // Max 4 players
  }

  getMaxRatingDiff(queueTime) {
    const timeWaited = Date.now() - queueTime;
    const baseRange = 100;
    const expandRate = 10; // +10 rating per second
    return baseRange + (timeWaited / 1000) * expandRate;
  }

  createMatch(players) {
    const matchId = this.generateMatchId();

    this.matches.set(matchId, {
      id: matchId,
      players: players.map(e => e.player),
      createdAt: Date.now(),
      state: 'starting'
    });

    // Notify players
    players.forEach(entry => {
      entry.player.emit('match_found', { matchId });
    });

    return matchId;
  }

  updateRatings(matchId, results) {
    const match = this.matches.get(matchId);
    if (!match) return;

    // Simple ELO calculation for 1v1
    if (match.players.length === 2) {
      const [p1, p2] = match.players;
      const r1 = p1.rating;
      const r2 = p2.rating;

      const e1 = 1 / (1 + Math.pow(10, (r2 - r1) / 400));
      const e2 = 1 / (1 + Math.pow(10, (r1 - r2) / 400));

      const s1 = results.winner === p1.id ? 1 : 0;
      const s2 = 1 - s1;

      p1.rating = r1 + this.eloK * (s1 - e1);
      p2.rating = r2 + this.eloK * (s2 - e2);
    }
  }
}
```

#### Day 5-7: Lobby System
**Topics:**
- Room creation and management
- Player ready states
- Host migration
- Game configuration

### Week 4: Scalability

#### Day 1-3: Server Architecture
**Topics:**
- Dedicated servers
- Server pooling
- Load balancing
- Auto-scaling

#### Day 4-7: Database Integration
**Topics:**
- Player data persistence
- Leaderboards
- Match history
- Analytics

### Weeks 5-6: Advanced Topics

#### Anti-Cheat Systems
**Topics:**
- Server-side validation
- Movement verification
- Rate limiting
- Replay analysis

#### Voice Chat Integration
**Topics:**
- WebRTC for voice
- Spatial audio
- Push-to-talk
- Voice activity detection

### Final Weeks: Capstone Project

**Build a Complete Multiplayer Game**

Requirements:
- Real-time multiplayer (2-4 players)
- Authoritative server
- Client prediction and interpolation
- Matchmaking system
- Lobby functionality
- Player progression
- Anti-cheat measures

---

## 🎓 Assignments & Projects

### Assignment 1: Network Protocol
Implement a custom binary protocol with:
- Delta compression
- Reliable ordered delivery
- Packet prioritization
- Bandwidth monitoring

### Assignment 2: Prediction System
Build client prediction with:
- Input buffering
- Server reconciliation
- Rollback and replay
- Error visualization

### Assignment 3: Matchmaking Algorithm
Create matchmaking with:
- Skill-based matching
- Party support
- Queue time optimization
- Fair team balancing

### Final Project: Multiplayer Game
Build a complete multiplayer game with all systems integrated.

---

## 📖 Resources

### Books
- "Multiplayer Game Programming" by Josh Glazer
- "Networked Graphics" by Anthony Steed

### Articles
- [Source Multiplayer Networking](https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking)
- [Overwatch Gameplay Architecture](https://www.youtube.com/watch?v=W3aieHjyNvw)
- [Fast-Paced Multiplayer](http://www.gabrielgambetta.com/client-server-game-architecture.html)

### Tools
- Wireshark (packet analysis)
- Clumsy (network simulation)
- Lighthouse (load testing)

---

## ✅ Assessment Criteria

### Technical (50%)
- Network architecture
- Performance optimization
- Cheat prevention

### Multiplayer Features (30%)
- Synchronization quality
- Matchmaking effectiveness
- Scalability

### Final Project (20%)
- Gameplay experience
- Network performance
- Documentation

**Passing Grade:** 75%

---

## 💼 Career Applications

- Multiplayer Programmer
- Network Engineer
- Backend Developer
- DevOps Engineer

**Average Salary:** $85,000 - $160,000

---

**Module Created:** 2025-11-02
