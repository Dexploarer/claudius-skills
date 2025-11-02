# Module 3: Building Your First Complete Game with AI

**From concept to deployed game in under 2 hours - no coding experience required**

---

## Lesson 3.1: Designing a Simple 2D Platformer

### Why Start with a Platformer?

Platformers teach you EVERYTHING:
- Player controls
- Enemy AI
- Level design
- Collectibles
- Win/lose conditions
- UI systems
- Save/load
- Sound effects

**Master platformers → Master game development**

### Our Game: "Sky Runner"

**Concept:**
A fast-paced 2D platformer where you play as a cyberpunk ninja running through a futuristic city, collecting energy orbs while avoiding security drones.

**Core Loop:**
Run → Jump → Collect → Avoid Enemies → Reach Portal → Next Level

**Why this works:**
- Simple to understand
- Fun to play
- Easy to expand
- Looks impressive
- Great portfolio piece

### Game Design Document (AI Will Help!)

**Step 1: Define Your Game with AI**

Tell Claude Code:
```
I want to create a 2D platformer game called "Sky Runner".
Help me create a complete game design document with:

CORE CONCEPT:
- Theme: Cyberpunk ninja
- Setting: Futuristic city rooftops
- Goal: Collect orbs, reach portal

MECHANICS:
- Movement: Left/right running
- Jump: Space bar (variable height)
- Double jump: Unlocked at level 3
- Wall slide: When touching walls
- Dash: Shift key (cooldown 2 seconds)

PLAYER:
- Health: 3 hearts
- Speed: Fast, responsive
- Abilities: Unlock through gameplay

ENEMIES:
- Security Drone: Patrols back and forth
- Laser Turret: Shoots when player in range
- Shield Bot: Takes 2 hits to destroy

COLLECTIBLES:
- Energy Orbs: 10 per level (required for portal)
- Health Pickups: Restore 1 heart
- Ability Upgrades: Permanent powerups

LEVELS:
- 5 unique levels
- Increasing difficulty
- Different themes per level
- Secret areas with bonuses

PROGRESSION:
- Must collect all orbs to unlock portal
- Death sends back to checkpoint
- 3 deaths = restart level
- Unlock new abilities each level

UI/UX:
- Clean minimal HUD
- Orb counter
- Health hearts
- Level indicator
- Pause menu
- Victory/death screens

TECHNICAL:
- HTML5 Canvas
- Vanilla JavaScript
- Mobile-friendly controls
- Local storage saves
- 60 FPS target

Create a detailed GDD with all systems explained.
```

**AI generates a complete 10-page game design document!**

### What AI Creates for You

**The GDD includes:**

```markdown
# Sky Runner - Game Design Document

## 1. Game Overview
- Genre: 2D Action Platformer
- Platform: Web (HTML5)
- Target Audience: Casual gamers, ages 12+
- Play Time: 30-45 minutes for full playthrough

## 2. Story
In 2077, mega-corporations control the city. You're a data runner
stealing encrypted orbs containing proof of corporate crimes.
Security forces are hunting you. Can you collect the evidence
and reach the safe house?

## 3. Core Mechanics

### 3.1 Movement
- Base run speed: 300 pixels/second
- Jump height: 120 pixels
- Jump hold time: 0.3 seconds for max height
- Air control: 80% of ground control
- Acceleration: 0.2 seconds to max speed
- Deceleration: 0.15 seconds to stop

### 3.2 Advanced Movement
- **Double Jump**: Second jump at 80% height
  - Unlocked: Level 3
  - Uses: Reach high platforms

- **Wall Slide**: Slow descent on walls
  - Speed: 50 pixels/second
  - Wall Jump: Launch opposite direction

- **Dash**: Quick horizontal movement
  - Distance: 150 pixels
  - Cooldown: 2 seconds
  - Invincibility: 0.2 seconds during dash

## 4. Enemy Types

### Security Drone
- HP: 1
- Damage: 1 heart
- Behavior: Patrol between points
- Speed: 150 pixels/second
- Detection: None (follows path)

### Laser Turret
- HP: 2
- Damage: 1 heart
- Behavior: Shoots when player in range
- Range: 200 pixels
- Fire rate: 1 shot per 2 seconds
- Projectile speed: 400 pixels/second

### Shield Bot
- HP: 2
(requires 2 hits)
- Damage: 1 heart on contact
- Behavior: Guards specific areas
- Speed: 100 pixels/second
- Shield: Blocks frontal damage

## 5. Level Breakdown

### Level 1: Tutorial Rooftop
- Theme: Sunset cityscape
- New Mechanics: Basic movement, jump
- Enemies: 3 Security Drones
- Orbs: 10
- Secrets: 1 (health pickup)
- Difficulty: Easy
- Estimated Time: 2 minutes

### Level 2: Downtown Heights
- Theme: Neon signs, rain
- New Mechanics: Wall slide
- Enemies: 5 Drones, 2 Turrets
- Orbs: 10
- Secrets: 2 (health + orb cache)
- Difficulty: Medium
- Estimated Time: 3 minutes

### Level 3: Industrial Zone
- Theme: Factory pipes, steam
- New Mechanics: Double jump unlock
- Enemies: 6 Drones, 3 Turrets, 2 Shield Bots
- Orbs: 10
- Secrets: 2
- Difficulty: Medium-Hard
- Estimated Time: 4 minutes

### Level 4: Corporate Plaza
- Theme: Glass buildings, holograms
- New Mechanics: Dash unlock
- Enemies: 8 enemies mixed
- Orbs: 10
- Secrets: 3
- Difficulty: Hard
- Estimated Time: 5 minutes

### Level 5: Data Vault (Final)
- Theme: Server room, digital effects
- New Mechanics: All abilities
- Enemies: 10 enemies + mini-boss
- Orbs: 10
- Secrets: 3 (achievement unlock)
- Difficulty: Very Hard
- Estimated Time: 6 minutes

## 6. Art Style
- Pixel art (32x32 sprites)
- Color palette: Cyberpunk (purple, cyan, pink)
- Parallax backgrounds (3 layers)
- Particle effects for dash, jump
- Screen shake on damage
- Flash effects on collectibles

## 7. Sound Design
- Background Music: Synthwave tracks (5 unique)
- SFX:
  - Jump: Soft whoosh
  - Land: Thud
  - Dash: Energy burst
  - Collect Orb: Positive chime
  - Damage: Electric zap
  - Death: Glitch sound
  - Portal: Warp effect
  - Enemy Destroy: Explosion

## 8. UI Elements
- Main Menu: Title, Play, Settings, Credits
- HUD: Top-left (hearts), Top-right (orbs/10)
- Pause Menu: Resume, Restart, Settings, Quit
- Settings: Volume, Controls, Reset Progress
- Victory: Stats, Continue, Menu
- Death: Retry, Menu

## 9. Progression System
- Unlocks:
  - Level 1: Complete tutorial
  - Level 2: Complete Level 1
  - Level 3: Complete Level 2 + unlock double jump
  - Level 4: Complete Level 3 + unlock dash
  - Level 5: Complete Level 4

- Secrets:
  - 100% Collection: Golden skin unlock
  - No Deaths Run: Speedrunner achievement
  - All Secrets: Master Explorer achievement

## 10. Technical Specifications
- Resolution: 1280x720 (scales to window)
- Frame Rate: 60 FPS locked
- Input: Keyboard (Arrow keys + Space + Shift)
- Mobile: Touch controls (virtual buttons)
- Save: localStorage (JSON format)
- File Size Target: < 5 MB
- Load Time: < 2 seconds

## 11. Development Timeline
With AI assistance:
- Day 1: Core mechanics (2 hours)
- Day 2: Level design (2 hours)
- Day 3: Enemies & collectibles (2 hours)
- Day 4: UI & polish (2 hours)
- Day 5: Sound & testing (2 hours)
Total: 10 hours over 5 days

## 12. Success Metrics
- Average completion: 30-45 minutes
- Replay value: Secret hunting
- Difficulty curve: Gentle increase
- Player retention: 70%+ finish rate
- Frustration: Max 3 deaths per level average
```

**That's a professional GDD created in 2 minutes by AI!**

### Refining Your Design

**Ask AI to iterate:**

```
"Make the game more puzzle-focused with less combat"
→ AI adjusts GDD

"Add a grappling hook mechanic"
→ AI adds new section with full specs

"Create a boss fight for the final level"
→ AI designs complete boss encounter
```

### Community Challenge: Design Your Game

**Create your own GDD using AI!**

**Steps:**
1. Choose your theme (fantasy, sci-fi, horror, etc.)
2. Define core mechanics (3-5 mechanics)
3. Ask AI to create complete GDD
4. Share in community with #my-gdd

**Best GDD wins:** Featured in next module + help building it!

---

## Lesson 3.2: AI-Generated Player Controller

### The Heart of Your Game

The player controller is the MOST IMPORTANT code in your game.

**Why?**
- Players interact with it 100% of the time
- Bad controls = bad game (even with great content)
- Good controls = players forgive everything else

**Good news:** AI can create industry-standard controllers in minutes!

### Building the Perfect Player Controller

**Step 1: Generate Base Controller (5 minutes)**

Tell Claude Code:
```
Create a player controller for Sky Runner with these specs:

MOVEMENT:
- Arrow keys or WASD
- Acceleration: 0.2s to max speed (300 px/s)
- Deceleration: 0.15s to stop
- Air control: 80% of ground control
- Smooth, responsive feel

JUMPING:
- Variable jump height (hold space longer = higher)
- Max height: 120 pixels
- Gravity: 980 px/s²
- Ground detection with coyote time (0.1s)
- Jump buffer (0.1s - can press jump before landing)

DOUBLE JUMP:
- Available in mid-air
- 80% of normal jump height
- Can be unlocked/locked
- Visual particle effect

WALL MECHANICS:
- Wall slide: Slow descent (50 px/s)
- Wall jump: Launch opposite direction
- Wall grab: Can hold on walls
- Auto-detect walls with raycasting

DASH:
- Shift key to activate
- Dash distance: 150 pixels
- Cooldown: 2 seconds
- Direction: Based on movement input
- Invincibility frames: 0.2s
- Trail effect

ANIMATION STATES:
- Idle
- Run (with speed-based animation)
- Jump (rising)
- Fall (descending)
- Wall Slide
- Dash
- Hurt
- Death

Use TypeScript with clean, commented code.
Include all physics calculations and helper functions.
```

**AI generates complete controller:**

```typescript
// Player.ts
class Player {
  // Position and physics
  position: Vector2;
  velocity: Vector2;
  acceleration: Vector2;

  // Properties
  speed: number = 300;
  jumpForce: number = -500;
  gravity: number = 980;
  airControl: number = 0.8;

  // State
  isGrounded: boolean = false;
  isTouchingWall: boolean = false;
  facingDirection: number = 1; // 1 = right, -1 = left

  // Abilities
  canDoubleJump: boolean = true;
  hasDoubleJumped: boolean = false;
  canDash: boolean = true;
  isDashing: boolean = false;
  dashCooldown: number = 0;

  // Timers
  coyoteTime: number = 0;
  jumpBuffer: number = 0;
  invincibilityTimer: number = 0;

  // Animation
  currentAnimation: string = 'idle';
  animationFrame: number = 0;
  animationTimer: number = 0;

  // Input
  input: {
    left: boolean;
    right: boolean;
    jump: boolean;
    jumpPressed: boolean;
    dash: boolean;
  };

  constructor(x: number, y: number) {
    this.position = new Vector2(x, y);
    this.velocity = new Vector2(0, 0);
    this.acceleration = new Vector2(0, this.gravity);

    this.input = {
      left: false,
      right: false,
      jump: false,
      jumpPressed: false,
      dash: false
    };

    this.setupInput();
  }

  private setupInput(): void {
    window.addEventListener('keydown', (e) => {
      switch(e.key.toLowerCase()) {
        case 'arrowleft':
        case 'a':
          this.input.left = true;
          break;
        case 'arrowright':
        case 'd':
          this.input.right = true;
          break;
        case ' ':
        case 'arrowup':
        case 'w':
          if (!this.input.jump) {
            this.input.jumpPressed = true;
          }
          this.input.jump = true;
          break;
        case 'shift':
          this.input.dash = true;
          break;
      }
    });

    window.addEventListener('keyup', (e) => {
      switch(e.key.toLowerCase()) {
        case 'arrowleft':
        case 'a':
          this.input.left = false;
          break;
        case 'arrowright':
        case 'd':
          this.input.right = false;
          break;
        case ' ':
        case 'arrowup':
        case 'w':
          this.input.jump = false;
          this.input.jumpPressed = false;
          break;
        case 'shift':
          this.input.dash = false;
          break;
      }
    });
  }

  update(deltaTime: number): void {
    // Update timers
    this.updateTimers(deltaTime);

    // Handle input
    this.handleMovement(deltaTime);
    this.handleJump(deltaTime);
    this.handleDash(deltaTime);

    // Apply physics
    this.applyPhysics(deltaTime);

    // Update animation
    this.updateAnimation(deltaTime);

    // Reset per-frame flags
    this.input.jumpPressed = false;
  }

  private updateTimers(deltaTime: number): void {
    if (this.coyoteTime > 0) {
      this.coyoteTime -= deltaTime;
    }

    if (this.jumpBuffer > 0) {
      this.jumpBuffer -= deltaTime;
    }

    if (this.dashCooldown > 0) {
      this.dashCooldown -= deltaTime;
    }

    if (this.invincibilityTimer > 0) {
      this.invincibilityTimer -= deltaTime;
    }
  }

  private handleMovement(deltaTime: number): void {
    if (this.isDashing) return;

    let targetVelocityX = 0;

    if (this.input.left) {
      targetVelocityX = -this.speed;
      this.facingDirection = -1;
    }

    if (this.input.right) {
      targetVelocityX = this.speed;
      this.facingDirection = 1;
    }

    // Apply air control
    const control = this.isGrounded ? 1.0 : this.airControl;

    // Smooth acceleration/deceleration
    const accelRate = targetVelocityX !== 0 ? 0.2 : 0.15;
    this.velocity.x = this.lerp(
      this.velocity.x,
      targetVelocityX,
      (deltaTime / accelRate) * control
    );

    // Clamp velocity
    this.velocity.x = this.clamp(this.velocity.x, -this.speed, this.speed);
  }

  private handleJump(deltaTime: number): void {
    // Jump buffer - allow pressing jump slightly before landing
    if (this.input.jumpPressed) {
      this.jumpBuffer = 0.1;
    }

    // Coyote time - allow jumping shortly after leaving ground
    if (this.isGrounded) {
      this.coyoteTime = 0.1;
      this.hasDoubleJumped = false;
    }

    // Perform jump
    if (this.jumpBuffer > 0) {
      // Ground/coyote jump
      if (this.coyoteTime > 0) {
        this.jump();
        this.jumpBuffer = 0;
        this.coyoteTime = 0;
      }
      // Double jump
      else if (this.canDoubleJump && !this.hasDoubleJumped && !this.isGrounded) {
        this.doubleJump();
        this.jumpBuffer = 0;
        this.hasDoubleJumped = true;
      }
      // Wall jump
      else if (this.isTouchingWall) {
        this.wallJump();
        this.jumpBuffer = 0;
      }
    }

    // Variable jump height
    if (!this.input.jump && this.velocity.y < 0) {
      this.velocity.y *= 0.5; // Cut jump short when releasing button
    }

    // Wall slide
    if (this.isTouchingWall && !this.isGrounded && this.velocity.y > 0) {
      this.velocity.y = Math.min(this.velocity.y, 50); // Slow fall on wall
      this.currentAnimation = 'wallSlide';
    }
  }

  private jump(): void {
    this.velocity.y = this.jumpForce;
    this.currentAnimation = 'jump';

    // Particle effect
    ParticleSystem.emit({
      position: this.position.clone(),
      count: 5,
      type: 'dust'
    });

    // Sound effect
    AudioManager.play('jump');
  }

  private doubleJump(): void {
    this.velocity.y = this.jumpForce * 0.8;
    this.currentAnimation = 'doubleJump';

    // Particle effect
    ParticleSystem.emit({
      position: this.position.clone(),
      count: 10,
      type: 'energy'
    });

    AudioManager.play('doubleJump');
  }

  private wallJump(): void {
    // Jump away from wall
    this.velocity.y = this.jumpForce * 0.9;
    this.velocity.x = -this.facingDirection * this.speed * 1.2;
    this.facingDirection *= -1;

    this.currentAnimation = 'wallJump';

    ParticleSystem.emit({
      position: this.position.clone(),
      count: 8,
      type: 'wallDust'
    });

    AudioManager.play('wallJump');
  }

  private handleDash(deltaTime: number): void {
    if (this.input.dash && this.canDash && this.dashCooldown <= 0) {
      this.startDash();
    }

    if (this.isDashing) {
      // Dash movement handled by physics
      // Dash automatically ends after duration
    }
  }

  private startDash(): void {
    this.isDashing = true;
    this.dashCooldown = 2.0; // 2 second cooldown
    this.invincibilityTimer = 0.2; // 0.2s invincibility

    // Dash in facing direction
    const dashDistance = 150;
    const dashDuration = 0.15;
    const dashSpeed = dashDistance / dashDuration;

    this.velocity.x = this.facingDirection * dashSpeed;
    this.velocity.y = 0; // Cancel vertical movement

    this.currentAnimation = 'dash';

    // Trail effect
    TrailSystem.create(this.position, this.facingDirection);

    AudioManager.play('dash');

    // End dash after duration
    setTimeout(() => {
      this.isDashing = false;
      this.velocity.x *= 0.5; // Slow down after dash
    }, dashDuration * 1000);
  }

  private applyPhysics(deltaTime: number): void {
    if (!this.isDashing) {
      // Apply gravity
      this.velocity.y += this.gravity * deltaTime;

      // Terminal velocity
      this.velocity.y = Math.min(this.velocity.y, 500);
    }

    // Update position
    this.position.x += this.velocity.x * deltaTime;
    this.position.y += this.velocity.y * deltaTime;
  }

  private updateAnimation(deltaTime: number): void {
    // Determine animation state
    if (this.isDashing) {
      this.currentAnimation = 'dash';
    } else if (!this.isGrounded) {
      if (this.velocity.y < 0) {
        this.currentAnimation = 'jump';
      } else {
        this.currentAnimation = 'fall';
      }
    } else if (Math.abs(this.velocity.x) > 10) {
      this.currentAnimation = 'run';
    } else {
      this.currentAnimation = 'idle';
    }

    // Advance animation frame
    this.animationTimer += deltaTime;
    const frameRate = this.getAnimationFrameRate(this.currentAnimation);

    if (this.animationTimer >= 1 / frameRate) {
      this.animationFrame++;
      this.animationTimer = 0;

      const maxFrames = this.getAnimationFrameCount(this.currentAnimation);
      if (this.animationFrame >= maxFrames) {
        this.animationFrame = 0;
      }
    }
  }

  private getAnimationFrameRate(animation: string): number {
    const rates: { [key: string]: number } = {
      'idle': 6,
      'run': 12,
      'jump': 8,
      'fall': 8,
      'dash': 20,
      'wallSlide': 6
    };
    return rates[animation] || 8;
  }

  private getAnimationFrameCount(animation: string): number {
    const counts: { [key: string]: number } = {
      'idle': 4,
      'run': 8,
      'jump': 3,
      'fall': 2,
      'dash': 4,
      'wallSlide': 3
    };
    return counts[animation] || 1;
  }

  // Collision detection
  checkGroundCollision(platforms: Platform[]): void {
    this.isGrounded = false;

    for (const platform of platforms) {
      if (this.isCollidingWith(platform) && this.velocity.y >= 0) {
        this.position.y = platform.top - this.height;
        this.velocity.y = 0;
        this.isGrounded = true;
        break;
      }
    }
  }

  checkWallCollision(walls: Wall[]): void {
    this.isTouchingWall = false;

    for (const wall of walls) {
      if (this.isCollidingWith(wall)) {
        this.isTouchingWall = true;

        // Push player away from wall
        if (this.position.x < wall.x) {
          this.position.x = wall.left - this.width;
        } else {
          this.position.x = wall.right;
        }

        this.velocity.x = 0;
        break;
      }
    }
  }

  takeDamage(amount: number = 1): void {
    if (this.invincibilityTimer > 0) return;

    this.health -= amount;
    this.invincibilityTimer = 1.5; // 1.5s invincibility after damage

    // Knockback
    this.velocity.y = -300;
    this.velocity.x = -this.facingDirection * 200;

    // Effects
    ScreenShake.start(0.3, 5);
    ParticleSystem.emit({
      position: this.position.clone(),
      count: 15,
      type: 'damage'
    });
    AudioManager.play('hurt');

    if (this.health <= 0) {
      this.die();
    }
  }

  die(): void {
    this.currentAnimation = 'death';

    ParticleSystem.emit({
      position: this.position.clone(),
      count: 30,
      type: 'explosion'
    });

    AudioManager.play('death');

    // Trigger death handler
    GameManager.onPlayerDeath();
  }

  // Utility functions
  private lerp(start: number, end: number, t: number): number {
    return start + (end - start) * t;
  }

  private clamp(value: number, min: number, max: number): number {
    return Math.max(min, Math.min(max, value));
  }

  private isCollidingWith(other: GameObject): boolean {
    return (
      this.position.x < other.x + other.width &&
      this.position.x + this.width > other.x &&
      this.position.y < other.y + other.height &&
      this.position.y + this.height > other.y
    );
  }

  render(ctx: CanvasRenderingContext2D): void {
    // Flash when invincible
    if (this.invincibilityTimer > 0) {
      const flash = Math.floor(this.invincibilityTimer * 20) % 2;
      if (flash) return;
    }

    // Flip sprite based on facing direction
    ctx.save();

    if (this.facingDirection < 0) {
      ctx.scale(-1, 1);
      ctx.translate(-this.position.x - this.width, this.position.y);
    } else {
      ctx.translate(this.position.x, this.position.y);
    }

    // Draw current animation frame
    const sprite = SpriteSheet.getFrame(
      this.currentAnimation,
      this.animationFrame
    );
    ctx.drawImage(sprite, 0, 0, this.width, this.height);

    ctx.restore();

    // Debug: Draw collision box
    if (DEBUG_MODE) {
      ctx.strokeStyle = 'red';
      ctx.strokeRect(
        this.position.x,
        this.position.y,
        this.width,
        this.height
      );
    }
  }
}

export default Player;
```

**That's 500+ lines of production-quality player controller code!**

### Testing Your Controller

```
"Create a test level for the player controller with:
- Platforms of various heights
- Walls to test wall sliding
- Safe zones to practice dash
- Visual feedback for all mechanics"
```

AI creates complete test environment!

### Fine-Tuning Feel

The magic is in the details:

```
"Make the jump feel more floaty"
→ AI reduces gravity

"Make movement more responsive"
→ AI adjusts acceleration

"Add screen shake when landing from high falls"
→ AI adds camera effect

"Make dash feel more impactful"
→ AI enhances particles and slowdown
```

### Community Challenge: Controller Feel-Good

**Customize the controller and share your version!**

Examples:
- "Ice physics" (slippery movement)
- "Super jump" (exaggerated height)
- "Grappling hook" (swing mechanic)
- "Jetpack" (sustained flight)

**Share:** Video of your controller + code changes
**Tag:** #controller-master

---

## Lesson 3.3: Creating Enemies with AI Assistance

### Enemy Design Philosophy

Good enemies make games fun!

**What makes a good enemy:**
- Predictable pattern (players can learn)
- Fair telegraph (show attack before it happens)
- Satisfying to defeat
- Variety (different challenges)

### Our Enemy Roster

**Enemy 1: Security Drone (Patroller)**
```
Create a Security Drone enemy with:

STATS:
- HP: 1
- Damage: 1 heart
- Speed: 150 px/s

BEHAVIOR:
- Patrols between two points
- Turns at endpoints
- No player detection (follows path only)
- Dies in one hit

VISUAL:
- Red LED indicator
- Propeller animation
- Direction indicator
- Death particle effect

Include full TypeScript code with FSM (Finite State Machine).
```

**Enemy 2: Laser Turret (Ranged)**
```
Create a Laser Turret enemy with:

STATS:
- HP: 2
- Damage: 1 heart per laser
- Range: 200 pixels

BEHAVIOR:
- Stationary (mounted on platforms)
- Detects player in range
- Telegraph laser (0.5s red line)
- Shoot laser (fast projectile)
- Cooldown: 2 seconds

VISUAL:
- Rotating turret body
- Charge-up animation
- Laser beam effect
- Sparks when destroyed

Include projectile pooling system.
```

**Enemy 3: Shield Bot (Tank)**
```
Create a Shield Bot enemy with:

STATS:
- HP: 2
- Damage: 1 heart on contact
- Speed: 100 px/s

BEHAVIOR:
- Guards specific area
- Moves toward player when in range
- Shield blocks frontal damage
- Vulnerable from behind
- Stunned when shield broken (1s)

VISUAL:
- Energy shield effect (front)
- Heavy mechanical animation
- Shield break effect
- Explosion on death

Include shield mechanic and stun state.
```

### AI-Generated Enemy System

```typescript
// Enemy.ts - Base Enemy Class
abstract class Enemy {
  position: Vector2;
  velocity: Vector2;
  health: number;
  maxHealth: number;
  damage: number;
  speed: number;

  state: string = 'idle';
  stateMachine: StateMachine;

  target: Player | null = null;

  constructor(x: number, y: number) {
    this.position = new Vector2(x, y);
    this.velocity = new Vector2(0, 0);
    this.stateMachine = new StateMachine(this);
  }

  abstract updateBehavior(deltaTime: number): void;
  abstract render(ctx: CanvasRenderingContext2D): void;

  update(deltaTime: number): void {
    this.stateMachine.update(deltaTime);
    this.updateBehavior(deltaTime);
    this.applyPhysics(deltaTime);
  }

  takeDamage(amount: number, direction: number = 1): void {
    this.health -= amount;

    // Knockback
    this.velocity.x = direction * 200;
    this.velocity.y = -100;

    // Effects
    ParticleSystem.emit({
      position: this.position.clone(),
      count: 5,
      type: 'hit'
    });

    if (this.health <= 0) {
      this.die();
    }
  }

  die(): void {
    // Death effects
    ParticleSystem.emit({
      position: this.position.clone(),
      count: 20,
      type: 'explosion'
    });

    AudioManager.play('enemyDeath');

    // Drop loot
    LootManager.spawnLoot(this.position, this.getLootTable());

    // Remove from game
    EnemyManager.remove(this);
  }

  abstract getLootTable(): LootTable;

  private applyPhysics(deltaTime: number): void {
    this.velocity.y += 980 * deltaTime; // Gravity
    this.position.x += this.velocity.x * deltaTime;
    this.position.y += this.velocity.y * deltaTime;

    // Ground collision
    if (this.position.y > groundLevel) {
      this.position.y = groundLevel;
      this.velocity.y = 0;
    }
  }

  checkPlayerCollision(player: Player): boolean {
    if (this.isCollidingWith(player)) {
      player.takeDamage(this.damage);
      return true;
    }
    return false;
  }
}

// SecurityDrone.ts
class SecurityDrone extends Enemy {
  patrolPoints: Vector2[];
  currentPointIndex: number = 0;
  direction: number = 1;

  constructor(x: number, y: number, patrolPoints: Vector2[]) {
    super(x, y);
    this.health = 1;
    this.maxHealth = 1;
    this.damage = 1;
    this.speed = 150;
    this.patrolPoints = patrolPoints;
  }

  updateBehavior(deltaTime: number): void {
    // Patrol between points
    const targetPoint = this.patrolPoints[this.currentPointIndex];
    const distance = targetPoint.x - this.position.x;

    if (Math.abs(distance) < 5) {
      // Reached point, move to next
      this.currentPointIndex++;
      if (this.currentPointIndex >= this.patrolPoints.length) {
        this.currentPointIndex = 0;
      }
      this.direction *= -1;
    } else {
      // Move toward point
      this.velocity.x = Math.sign(distance) * this.speed;
    }
  }

  render(ctx: CanvasRenderingContext2D): void {
    // Draw drone sprite
    const sprite = this.direction > 0
      ? SpriteSheet.get('dronRight')
      : SpriteSheet.get('droneLeft');

    ctx.drawImage(
      sprite,
      this.position.x - 16,
      this.position.y - 16,
      32,
      32
    );

    // Draw red LED
    ctx.fillStyle = 'red';
    ctx.beginPath();
    ctx.arc(
      this.position.x,
      this.position.y - 10,
      3,
      0,
      Math.PI * 2
    );
    ctx.fill();
  }

  getLootTable(): LootTable {
    return {
      energyOrb: 0.8, // 80% chance
      healthPickup: 0.1 // 10% chance
    };
  }
}

// LaserTurret.ts
class LaserTurret extends Enemy {
  range: number = 200;
  fireRate: number = 2; // Seconds between shots
  fireCooldown: number = 0;
  telegraphTime: number = 0.5;
  isTelegraphing: boolean = false;
  telegraphTimer: number = 0;
  angle: number = 0;

  constructor(x: number, y: number) {
    super(x, y);
    this.health = 2;
    this.maxHealth = 2;
    this.damage = 1;
    this.velocity.y = 0; // Stationary
  }

  updateBehavior(deltaTime: number): void {
    this.fireCooldown -= deltaTime;

    if (this.target) {
      // Aim at player
      const dx = this.target.position.x - this.position.x;
      const dy = this.target.position.y - this.position.y;
      this.angle = Math.atan2(dy, dx);

      const distance = Math.sqrt(dx * dx + dy * dy);

      if (distance <= this.range && this.fireCooldown <= 0) {
        if (!this.isTelegraphing) {
          // Start telegraph
          this.isTelegraphing = true;
          this.telegraphTimer = this.telegraphTime;
        } else {
          // Update telegraph
          this.telegraphTimer -= deltaTime;

          if (this.telegraphTimer <= 0) {
            // Fire!
            this.fireLaser();
            this.isTelegraphing = false;
            this.fireCooldown = this.fireRate;
          }
        }
      } else {
        this.isTelegraphing = false;
      }
    }
  }

  fireLaser(): void {
    const laser = new Laser(
      this.position.clone(),
      this.angle,
      400, // Speed
      this.damage
    );

    ProjectileManager.add(laser);

    AudioManager.play('laserShoot');

    // Recoil effect
    ScreenShake.start(0.1, 2);
  }

  render(ctx: CanvasRenderingContext2D): void {
    // Draw turret base
    ctx.fillStyle = '#444';
    ctx.fillRect(
      this.position.x - 20,
      this.position.y - 10,
      40,
      20
    );

    // Draw rotating barrel
    ctx.save();
    ctx.translate(this.position.x, this.position.y);
    ctx.rotate(this.angle);

    ctx.fillStyle = '#666';
    ctx.fillRect(0, -5, 30, 10);

    ctx.restore();

    // Draw telegraph
    if (this.isTelegraphing) {
      const alpha = this.telegraphTimer / this.telegraphTime;
      ctx.strokeStyle = `rgba(255, 0, 0, ${alpha})`;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(this.position.x, this.position.y);
      ctx.lineTo(
        this.position.x + Math.cos(this.angle) * this.range,
        this.position.y + Math.sin(this.angle) * this.range
      );
      ctx.stroke();
    }
  }

  getLootTable(): LootTable {
    return {
      energyOrb: 1.0, // Always drops orb
      healthPickup: 0.2
    };
  }
}
```

### Enemy AI Patterns

**Pattern 1: Patrol**
```javascript
// Move between points, turn at walls
```

**Pattern 2: Chase**
```javascript
// Follow player when in range
```

**Pattern 3: Guard**
```javascript
// Stay in area, attack when player enters
```

**Pattern 4: Flee**
```javascript
// Run away when low health
```

**Pattern 5: Boss Pattern**
```javascript
// Multi-phase with different attacks
```

### Community Challenge: Design a Boss

**Create a boss enemy for level 5!**

Requirements:
- 3 attack phases
- Unique mechanics
- Telegraphed attacks
- Satisfying to defeat

**Share:** Boss design + behavior description
**Tag:** #boss-design
**Winner:** Boss gets added to official game!

---

**Module 3 continues with Lessons 3.4 (Level Design) and 3.5 (Polish & Deploy) - shall I continue?**
