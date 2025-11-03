# class-builder

**Skill Name:** Class Builder & Strict TypeScript Generator

**Description:** Automatically generates strictly-typed TypeScript classes following class-over-interface patterns with full encapsulation, validation, and type safety.

**Category:** Development Tools / Code Generation

**Complexity:** Intermediate

**Use Cases:**
- Generate domain model classes
- Create value objects with validation
- Build service classes with dependency injection
- Generate repository classes
- Create strictly-typed DTOs and serialization

---

## 🎯 Activation Triggers

This skill activates when the user mentions:
- "create a class for [entity]"
- "generate [Model] class"
- "build a TypeScript class for [domain object]"
- "create domain model for [entity]"
- "generate strict class"
- "create value object"
- "build service class"
- "create repository class"

---

## 🏗️ Class Generation Templates

### Template 1: Domain Entity Class

**Use for:** Main domain objects (User, Product, Order, etc.)

```typescript
export class User {
  // Private fields with readonly for immutability
  private readonly _id: string;
  private _email: string;
  private _profile: UserProfile;
  private readonly _createdAt: Date;
  private _updatedAt: Date;

  // Constructor with validation
  public constructor(
    id: string,
    email: string,
    profile: UserProfile,
    createdAt: Date = new Date(),
    updatedAt: Date = new Date()
  ) {
    this.validateId(id);
    this.validateEmail(email);

    this._id = id;
    this._email = email;
    this._profile = profile;
    this._createdAt = createdAt;
    this._updatedAt = updatedAt;
  }

  // Public getters (no setters for readonly)
  public getId(): string {
    return this._id;
  }

  public getEmail(): string {
    return this._email;
  }

  public getProfile(): UserProfile {
    return this._profile;
  }

  public getCreatedAt(): Date {
    return this._createdAt;
  }

  public getUpdatedAt(): Date {
    return this._updatedAt;
  }

  // Public mutators with validation
  public updateEmail(email: string): void {
    this.validateEmail(email);
    this._email = email;
    this._updatedAt = new Date();
  }

  public updateProfile(profile: UserProfile): void {
    this._profile = profile;
    this._updatedAt = new Date();
  }

  // Private validation methods
  private validateId(id: string): void {
    if (!id || id.trim().length === 0) {
      throw new Error('User ID cannot be empty');
    }
  }

  private validateEmail(email: string): void {
    if (!email.includes('@')) {
      throw new Error('Invalid email format');
    }
    if (email.length > 255) {
      throw new Error('Email too long');
    }
  }

  // Static factory method from JSON
  public static fromJSON(data: unknown): User {
    if (!User.isValidUserData(data)) {
      throw new Error('Invalid user data structure');
    }

    return new User(
      data.id,
      data.email,
      UserProfile.fromJSON(data.profile),
      new Date(data.createdAt),
      new Date(data.updatedAt)
    );
  }

  // Type guard for JSON data
  private static isValidUserData(data: unknown): data is {
    id: string;
    email: string;
    profile: unknown;
    createdAt: string;
    updatedAt: string;
  } {
    return (
      typeof data === 'object' &&
      data !== null &&
      'id' in data &&
      typeof data.id === 'string' &&
      'email' in data &&
      typeof data.email === 'string' &&
      'profile' in data &&
      'createdAt' in data &&
      typeof data.createdAt === 'string' &&
      'updatedAt' in data &&
      typeof data.updatedAt === 'string'
    );
  }

  // Serialization method
  public toJSON(): UserDTO {
    return {
      id: this._id,
      email: this._email,
      profile: this._profile.toJSON(),
      createdAt: this._createdAt.toISOString(),
      updatedAt: this._updatedAt.toISOString(),
    };
  }

  // Equality check
  public equals(other: User): boolean {
    return this._id === other._id;
  }

  // Clone method
  public clone(): User {
    return new User(
      this._id,
      this._email,
      this._profile.clone(),
      new Date(this._createdAt),
      new Date(this._updatedAt)
    );
  }
}

// DTO type for serialization (use 'type', not 'interface')
export type UserDTO = {
  id: string;
  email: string;
  profile: UserProfileDTO;
  createdAt: string;
  updatedAt: string;
};
```

---

### Template 2: Value Object

**Use for:** Immutable value objects (Email, Money, Address, etc.)

```typescript
export class Email {
  private readonly _value: string;

  public constructor(value: string) {
    this.validate(value);
    // Normalize the value
    this._value = value.toLowerCase().trim();
  }

  public getValue(): string {
    return this._value;
  }

  public getLocalPart(): string {
    return this._value.split('@')[0] ?? '';
  }

  public getDomain(): string {
    return this._value.split('@')[1] ?? '';
  }

  // Value objects use value-based equality
  public equals(other: Email): boolean {
    return this._value === other._value;
  }

  private validate(value: string): void {
    if (!value || value.trim().length === 0) {
      throw new Error('Email cannot be empty');
    }

    if (!value.includes('@')) {
      throw new Error('Invalid email format: missing @');
    }

    const parts: string[] = value.split('@');
    if (parts.length !== 2) {
      throw new Error('Invalid email format: multiple @ symbols');
    }

    const [localPart, domain] = parts;
    if (!localPart || !domain) {
      throw new Error('Invalid email format: empty local part or domain');
    }

    if (value.length > 255) {
      throw new Error('Email too long (max 255 characters)');
    }

    // Add more validation as needed
    const emailRegex: RegExp = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(value)) {
      throw new Error('Invalid email format');
    }
  }

  // Static factory methods
  public static from(value: string): Email {
    return new Email(value);
  }

  public static fromJSON(data: unknown): Email {
    if (typeof data !== 'string') {
      throw new Error('Email data must be a string');
    }
    return new Email(data);
  }

  // Serialization
  public toJSON(): string {
    return this._value;
  }

  public toString(): string {
    return this._value;
  }
}
```

---

### Template 3: Service Class

**Use for:** Application services with business logic

```typescript
export class UserService {
  // Dependencies injected via constructor
  private readonly _userRepository: IUserRepository;
  private readonly _emailService: IEmailService;
  private readonly _logger: ILogger;
  private readonly _validator: IValidator;

  public constructor(
    userRepository: IUserRepository,
    emailService: IEmailService,
    logger: ILogger,
    validator: IValidator
  ) {
    this._userRepository = userRepository;
    this._emailService = emailService;
    this._logger = logger;
    this._validator = validator;
  }

  // Public service methods with explicit return types
  public async createUser(
    email: string,
    profile: UserProfileData
  ): Promise<User> {
    this._logger.info(`Creating user with email: ${email}`);

    // Validation
    await this.validateEmailUnique(email);
    this._validator.validateProfile(profile);

    // Create domain object
    const user: User = new User(
      this.generateId(),
      email,
      new UserProfile(profile.firstName, profile.lastName, profile.bio)
    );

    // Persist
    await this._userRepository.save(user);

    // Side effects
    await this._emailService.sendWelcomeEmail(user.getEmail());

    this._logger.info(`User created successfully: ${user.getId()}`);
    return user;
  }

  public async getUserById(id: string): Promise<User> {
    this._logger.debug(`Fetching user: ${id}`);

    const user: User | undefined = await this._userRepository.findById(id);
    if (!user) {
      throw new UserNotFoundError(id);
    }

    return user;
  }

  public async updateUserEmail(
    userId: string,
    newEmail: string
  ): Promise<User> {
    this._logger.info(`Updating email for user: ${userId}`);

    const user: User = await this.getUserById(userId);
    await this.validateEmailUnique(newEmail);

    user.updateEmail(newEmail);
    await this._userRepository.update(user);

    await this._emailService.sendEmailChangeConfirmation(
      user.getEmail()
    );

    this._logger.info(`Email updated successfully for user: ${userId}`);
    return user;
  }

  public async deleteUser(userId: string): Promise<void> {
    this._logger.info(`Deleting user: ${userId}`);

    const user: User = await this.getUserById(userId);
    await this._userRepository.delete(user.getId());

    this._logger.info(`User deleted: ${userId}`);
  }

  // Private helper methods
  private generateId(): string {
    return crypto.randomUUID();
  }

  private async validateEmailUnique(email: string): Promise<void> {
    const existing: User | undefined =
      await this._userRepository.findByEmail(email);

    if (existing) {
      throw new EmailAlreadyExistsError(email);
    }
  }
}

// Service interfaces (for dependency injection)
export interface IUserRepository {
  findById(id: string): Promise<User | undefined>;
  findByEmail(email: string): Promise<User | undefined>;
  save(user: User): Promise<void>;
  update(user: User): Promise<void>;
  delete(id: string): Promise<void>;
}

export interface IEmailService {
  sendWelcomeEmail(to: string): Promise<void>;
  sendEmailChangeConfirmation(to: string): Promise<void>;
}

export interface ILogger {
  info(message: string): void;
  debug(message: string): void;
  error(message: string, error?: Error): void;
}

export interface IValidator {
  validateProfile(profile: UserProfileData): void;
}

// Custom errors
export class UserNotFoundError extends Error {
  public constructor(userId: string) {
    super(`User not found: ${userId}`);
    this.name = 'UserNotFoundError';
  }
}

export class EmailAlreadyExistsError extends Error {
  public constructor(email: string) {
    super(`Email already exists: ${email}`);
    this.name = 'EmailAlreadyExistsError';
  }
}
```

---

### Template 4: Repository Class

**Use for:** Data access layer

```typescript
export class UserRepository implements IUserRepository {
  private readonly _db: IDatabase;
  private readonly _logger: ILogger;

  public constructor(db: IDatabase, logger: ILogger) {
    this._db = db;
    this._logger = logger;
  }

  public async findById(id: string): Promise<User | undefined> {
    this._logger.debug(`Finding user by ID: ${id}`);

    const row: unknown = await this._db.queryOne(
      'SELECT * FROM users WHERE id = ?',
      [id]
    );

    if (!row) {
      return undefined;
    }

    return User.fromJSON(row);
  }

  public async findByEmail(email: string): Promise<User | undefined> {
    this._logger.debug(`Finding user by email: ${email}`);

    const row: unknown = await this._db.queryOne(
      'SELECT * FROM users WHERE email = ?',
      [email]
    );

    if (!row) {
      return undefined;
    }

    return User.fromJSON(row);
  }

  public async findAll(): Promise<User[]> {
    this._logger.debug('Finding all users');

    const rows: unknown[] = await this._db.query('SELECT * FROM users');

    return rows.map((row: unknown): User => User.fromJSON(row));
  }

  public async save(user: User): Promise<void> {
    this._logger.debug(`Saving user: ${user.getId()}`);

    const data: UserDTO = user.toJSON();

    await this._db.execute(
      `INSERT INTO users (id, email, profile, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?)`,
      [
        data.id,
        data.email,
        JSON.stringify(data.profile),
        data.createdAt,
        data.updatedAt,
      ]
    );
  }

  public async update(user: User): Promise<void> {
    this._logger.debug(`Updating user: ${user.getId()}`);

    const data: UserDTO = user.toJSON();

    const result: { affectedRows: number } = await this._db.execute(
      `UPDATE users
       SET email = ?, profile = ?, updated_at = ?
       WHERE id = ?`,
      [data.email, JSON.stringify(data.profile), data.updatedAt, data.id]
    );

    if (result.affectedRows === 0) {
      throw new Error(`User not found: ${user.getId()}`);
    }
  }

  public async delete(id: string): Promise<void> {
    this._logger.debug(`Deleting user: ${id}`);

    const result: { affectedRows: number } = await this._db.execute(
      'DELETE FROM users WHERE id = ?',
      [id]
    );

    if (result.affectedRows === 0) {
      throw new Error(`User not found: ${id}`);
    }
  }

  public async count(): Promise<number> {
    const row: unknown = await this._db.queryOne(
      'SELECT COUNT(*) as count FROM users'
    );

    if (!this.isCountRow(row)) {
      throw new Error('Invalid count query result');
    }

    return row.count;
  }

  private isCountRow(row: unknown): row is { count: number } {
    return (
      typeof row === 'object' &&
      row !== null &&
      'count' in row &&
      typeof row.count === 'number'
    );
  }
}

export interface IDatabase {
  query(sql: string, params?: unknown[]): Promise<unknown[]>;
  queryOne(sql: string, params?: unknown[]): Promise<unknown | undefined>;
  execute(sql: string, params?: unknown[]): Promise<{ affectedRows: number }>;
}
```

---

## 🎯 Class Generation Workflow

### Step 1: Gather Requirements

**Ask the user:**
```
"I'll generate a [EntityName] class. To ensure it meets your needs:

1. What type of class? (Domain Entity, Value Object, Service, Repository)
2. What properties should it have?
3. Which properties are mutable vs immutable?
4. What validation rules apply?
5. What methods/behavior does it need?
6. Does it need serialization (toJSON/fromJSON)?
7. Does it interact with external services/repositories?"
```

### Step 2: Generate Class Structure

**Based on requirements, choose template:**
- Domain Entity → Use Template 1
- Value Object → Use Template 2
- Service → Use Template 3
- Repository → Use Template 4

### Step 3: Apply Strict Typing Rules

**Ensure:**
- ✅ All properties have explicit types
- ✅ All methods have explicit return types
- ✅ All parameters have explicit types
- ✅ No `any` types anywhere
- ✅ Proper use of readonly
- ✅ Private fields with public accessors
- ✅ Validation in constructors
- ✅ Type guards for external data
- ✅ Explicit null/undefined handling

### Step 4: Add Documentation

**Add TSDoc comments:**
```typescript
/**
 * Represents a user in the system.
 *
 * @remarks
 * This class enforces email validation and tracks creation/update timestamps.
 *
 * @example
 * ```typescript
 * const user = new User('123', 'john@example.com', profile);
 * user.updateEmail('newemail@example.com');
 * ```
 */
export class User {
  // ...
}
```

---

## 📋 Pre-Generation Checklist

Before generating any class, verify:

- [ ] Class name is PascalCase and descriptive
- [ ] All properties are private with _ prefix
- [ ] Readonly used for immutable properties
- [ ] Constructor validates all inputs
- [ ] Public getters for all properties
- [ ] Public setters (mutators) validate inputs
- [ ] All methods have explicit return types
- [ ] No `any` types used
- [ ] Type guards for external data (fromJSON)
- [ ] Serialization method (toJSON) if needed
- [ ] Proper error handling
- [ ] TSDoc comments added

---

## 🚨 Common Mistakes to Avoid

### Mistake 1: Using Interfaces for Data

```typescript
// ❌ BAD
interface User {
  id: string;
  email: string;
}

// ✅ GOOD
class User {
  private readonly _id: string;
  private _email: string;
  // ... with methods
}
```

### Mistake 2: Public Mutable Fields

```typescript
// ❌ BAD
class User {
  public email: string;
}

// ✅ GOOD
class User {
  private _email: string;

  public getEmail(): string {
    return this._email;
  }

  public updateEmail(email: string): void {
    this.validateEmail(email);
    this._email = email;
  }
}
```

### Mistake 3: No Validation

```typescript
// ❌ BAD
public constructor(email: string) {
  this._email = email;
}

// ✅ GOOD
public constructor(email: string) {
  this.validateEmail(email);
  this._email = email;
}
```

---

## 🎓 Best Practices

1. **Single Responsibility** - One class, one concern
2. **Encapsulation** - Hide internal state, expose behavior
3. **Immutability** - Use readonly where possible
4. **Validation** - Validate in constructor and mutators
5. **Type Safety** - Explicit types everywhere
6. **Factory Methods** - Static constructors for complex creation
7. **Error Handling** - Throw meaningful errors
8. **Documentation** - TSDoc for public APIs

---

## 🔗 Related Resources

**See also:**
- `.claude/rules/strict-typing-class-patterns.md` - Complete guidelines
- `hooks-collection/strict-typing/` - Enforcement hooks
- `templates/class-template.ts` - Boilerplate templates
- `tsconfig.strict.json` - Strict TypeScript config

---

**Last Updated:** 2025-11-03
**Priority:** HIGH - Use for all class generation
**Complexity:** Intermediate
