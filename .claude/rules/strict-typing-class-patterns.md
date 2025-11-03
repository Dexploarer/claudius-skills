# Strict Type Checking & Class-Based Patterns

> **Enforce strict TypeScript with class-based architecture over interfaces**

## 🎯 Core Philosophy

**This project follows strict typing and class-based patterns:**

1. **Strict Type Checking** - Zero tolerance for `any`, implicit types, or loose typing
2. **Classes Over Interfaces** - Use classes as single source of truth for structure and behavior
3. **Type Safety First** - Compile-time guarantees over runtime flexibility
4. **Explicit Over Implicit** - All types must be explicitly declared
5. **OOP Principles** - Leverage encapsulation, inheritance, and polymorphism

---

## ✅ TypeScript Strict Mode Configuration

### Required tsconfig.json Settings

**ALWAYS use these strict compiler options:**

```json
{
  "compilerOptions": {
    /* Strict Type Checking */
    "strict": true,                           // Enable all strict type checks
    "noImplicitAny": true,                    // Error on expressions with implied 'any'
    "strictNullChecks": true,                 // Enable strict null checking
    "strictFunctionTypes": true,              // Enable strict function type checking
    "strictBindCallApply": true,              // Enable strict bind/call/apply
    "strictPropertyInitialization": true,     // Ensure properties are initialized
    "noImplicitThis": true,                   // Error on 'this' with implied 'any'
    "alwaysStrict": true,                     // Parse in strict mode

    /* Additional Checks */
    "noUnusedLocals": true,                   // Report unused local variables
    "noUnusedParameters": true,               // Report unused parameters
    "noImplicitReturns": true,                // Report missing returns
    "noFallthroughCasesInSwitch": true,      // Report fallthrough cases
    "noUncheckedIndexedAccess": true,        // Include 'undefined' in index signatures
    "noImplicitOverride": true,               // Ensure override keyword is used
    "noPropertyAccessFromIndexSignature": true, // Enforce dot notation

    /* Advanced Strict Checks */
    "exactOptionalPropertyTypes": true,       // Distinguish undefined from missing
    "allowUnusedLabels": false,               // Disallow unused labels
    "allowUnreachableCode": false,            // Disallow unreachable code

    /* Module & Resolution */
    "esModuleInterop": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,

    /* Emit */
    "declaration": true,                      // Generate .d.ts files
    "declarationMap": true,                   // Generate sourcemaps for .d.ts
    "sourceMap": true,
    "removeComments": false,                  // Keep comments for documentation
    "emitDecoratorMetadata": true,           // Emit metadata for decorators
    "experimentalDecorators": true            // Enable decorators
  }
}
```

### ESLint Strict Rules

**Required .eslintrc.json configuration:**

```json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "project": "./tsconfig.json"
  },
  "rules": {
    /* Strict Type Rules */
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/no-implicit-any-catch": "error",
    "@typescript-eslint/no-unsafe-argument": "error",
    "@typescript-eslint/no-unsafe-assignment": "error",
    "@typescript-eslint/no-unsafe-call": "error",
    "@typescript-eslint/no-unsafe-member-access": "error",
    "@typescript-eslint/no-unsafe-return": "error",

    /* Explicit Type Rules */
    "@typescript-eslint/explicit-function-return-type": "error",
    "@typescript-eslint/explicit-module-boundary-types": "error",
    "@typescript-eslint/typedef": ["error", {
      "arrowParameter": true,
      "variableDeclaration": true,
      "memberVariableDeclaration": true,
      "parameter": true,
      "propertyDeclaration": true
    }],

    /* No Implicit Returns */
    "@typescript-eslint/explicit-member-accessibility": ["error", {
      "accessibility": "explicit"
    }],

    /* Prefer Classes */
    "@typescript-eslint/prefer-class": "error",
    "@typescript-eslint/no-empty-interface": "error",

    /* Null Safety */
    "@typescript-eslint/no-non-null-assertion": "error",
    "@typescript-eslint/no-unnecessary-condition": "error"
  }
}
```

---

## 🏛️ Classes Over Interfaces - The Rules

### ✅ DO: Use Classes

**Classes are the primary building block:**

```typescript
// ✅ GOOD: Class with explicit types and behavior
export class User {
  private _id: string;
  private _email: string;
  private _createdAt: Date;

  public constructor(id: string, email: string) {
    this._id = id;
    this._email = email;
    this._createdAt = new Date();
  }

  public getId(): string {
    return this._id;
  }

  public getEmail(): string {
    return this._email;
  }

  public updateEmail(newEmail: string): void {
    this.validateEmail(newEmail);
    this._email = newEmail;
  }

  public getCreatedAt(): Date {
    return this._createdAt;
  }

  private validateEmail(email: string): void {
    if (!email.includes('@')) {
      throw new Error('Invalid email format');
    }
  }

  public toJSON(): UserJSON {
    return {
      id: this._id,
      email: this._email,
      createdAt: this._createdAt.toISOString(),
    };
  }
}

// Type for serialization only
export type UserJSON = {
  id: string;
  email: string;
  createdAt: string;
};
```

**Why classes?**
- ✅ Single source of truth for data structure AND behavior
- ✅ Encapsulation with private fields
- ✅ Validation logic lives with the data
- ✅ Inheritance and polymorphism
- ✅ Constructor guarantees valid state
- ✅ Runtime type checking via `instanceof`

### ❌ DON'T: Use Interfaces for Data Structures

```typescript
// ❌ BAD: Interface with no behavior
interface User {
  id: string;
  email: string;
  createdAt: Date;
}

// ❌ BAD: Validation separated from data
function createUser(id: string, email: string): User {
  if (!email.includes('@')) {
    throw new Error('Invalid email');
  }
  return { id, email, createdAt: new Date() };
}
```

**Problems with interfaces:**
- ❌ No encapsulation
- ❌ No validation
- ❌ No behavior/methods
- ❌ Compile-time only (erased at runtime)
- ❌ No `instanceof` checks
- ❌ Easy to create invalid states

### When Interfaces ARE Allowed

**Interfaces are ONLY for:**

1. **Contract definitions (polymorphism)**
```typescript
// ✅ GOOD: Interface for polymorphic behavior
export interface IEmailService {
  sendEmail(to: string, subject: string, body: string): Promise<void>;
}

export class SendGridEmailService implements IEmailService {
  public async sendEmail(to: string, subject: string, body: string): Promise<void> {
    // SendGrid implementation
  }
}

export class MailgunEmailService implements IEmailService {
  public async sendEmail(to: string, subject: string, body: string): Promise<void> {
    // Mailgun implementation
  }
}
```

2. **Third-party library contracts**
```typescript
// ✅ GOOD: Interface for external API contract
export interface IExternalAPIResponse {
  status: number;
  data: unknown;
}
```

3. **Type-only serialization formats**
```typescript
// ✅ GOOD: Type for JSON serialization (use 'type', not 'interface')
export type UserDTO = {
  id: string;
  email: string;
  createdAt: string;
};
```

---

## 📋 Strict Typing Rules

### Rule 1: No `any` - Ever

```typescript
// ❌ NEVER use 'any'
function processData(data: any): any {
  return data;
}

// ✅ ALWAYS use specific types
function processData<T extends Record<string, unknown>>(data: T): T {
  return data;
}

// ✅ OR use unknown and type guards
function processData(data: unknown): ProcessedData {
  if (!isValidData(data)) {
    throw new Error('Invalid data');
  }
  return processDataInternal(data);
}

function isValidData(data: unknown): data is ValidData {
  return typeof data === 'object' && data !== null && 'id' in data;
}
```

### Rule 2: All Variables Must Have Explicit Types

```typescript
// ❌ BAD: Implicit types
const user = { id: '1', name: 'John' };
let count = 0;
const items = [];

// ✅ GOOD: Explicit types
const user: User = new User('1', 'John');
let count: number = 0;
const items: Item[] = [];
```

### Rule 3: All Functions Must Have Explicit Return Types

```typescript
// ❌ BAD: No return type
function getUser(id: string) {
  return users.find(u => u.id === id);
}

// ✅ GOOD: Explicit return type
function getUser(id: string): User | undefined {
  return users.find((u: User): boolean => u.getId() === id);
}

// ✅ GOOD: Explicit promise type
async function fetchUser(id: string): Promise<User> {
  const response: Response = await fetch(`/api/users/${id}`);
  const data: unknown = await response.json();
  return User.fromJSON(data);
}
```

### Rule 4: No Non-Null Assertions

```typescript
// ❌ BAD: Non-null assertion
const user = users.find(u => u.id === id)!;
user.getName(); // Might crash!

// ✅ GOOD: Explicit null check
const user: User | undefined = users.find((u: User) => u.getId() === id);
if (!user) {
  throw new Error(`User ${id} not found`);
}
user.getName(); // Safe
```

### Rule 5: Strict Null Checks - Handle undefined

```typescript
// ❌ BAD: Assuming value exists
function processUser(user: User | undefined): void {
  console.log(user.getName()); // Error!
}

// ✅ GOOD: Handle undefined
function processUser(user: User | undefined): void {
  if (!user) {
    throw new Error('User is required');
  }
  console.log(user.getName()); // Safe
}

// ✅ GOOD: Use optional chaining
function getUserName(user: User | undefined): string | undefined {
  return user?.getName();
}
```

### Rule 6: Array Access Must Handle undefined

```typescript
// ❌ BAD: Assuming index exists
const firstItem = items[0];
firstItem.process(); // Might crash!

// ✅ GOOD: Check for undefined
const firstItem: Item | undefined = items[0];
if (!firstItem) {
  throw new Error('No items available');
}
firstItem.process(); // Safe
```

### Rule 7: All Class Properties Must Be Initialized

```typescript
// ❌ BAD: Uninitialized properties
class User {
  private id: string;      // Error!
  private email: string;   // Error!
}

// ✅ GOOD: Initialize in constructor
class User {
  private readonly _id: string;
  private _email: string;

  public constructor(id: string, email: string) {
    this._id = id;
    this._email = email;
  }
}

// ✅ GOOD: Initialize with default value
class Counter {
  private _count: number = 0;

  public increment(): void {
    this._count++;
  }
}
```

### Rule 8: Use Readonly for Immutable Data

```typescript
// ✅ GOOD: Readonly properties
class User {
  private readonly _id: string;
  private readonly _createdAt: Date;
  private _email: string; // Mutable

  public constructor(id: string, email: string) {
    this._id = id;
    this._email = email;
    this._createdAt = new Date();
  }

  public getId(): string {
    return this._id; // Cannot be changed
  }

  public updateEmail(email: string): void {
    this._email = email; // Can be changed
  }
}
```

### Rule 9: Explicit Accessibility Modifiers

```typescript
// ❌ BAD: No accessibility modifiers
class User {
  id: string;

  constructor(id: string) {
    this.id = id;
  }

  getName(): string {
    return this.name;
  }
}

// ✅ GOOD: Explicit accessibility
class User {
  private readonly _id: string;

  public constructor(id: string) {
    this._id = id;
  }

  public getId(): string {
    return this._id;
  }

  private validateId(id: string): boolean {
    return id.length > 0;
  }
}
```

### Rule 10: Type Guards for Unknown Data

```typescript
// ✅ GOOD: Type guard for external data
class User {
  private readonly _id: string;
  private readonly _email: string;

  public constructor(id: string, email: string) {
    this._id = id;
    this._email = email;
  }

  public static fromJSON(data: unknown): User {
    if (!User.isValidUserData(data)) {
      throw new Error('Invalid user data');
    }
    return new User(data.id, data.email);
  }

  private static isValidUserData(data: unknown): data is { id: string; email: string } {
    return (
      typeof data === 'object' &&
      data !== null &&
      'id' in data &&
      typeof data.id === 'string' &&
      'email' in data &&
      typeof data.email === 'string'
    );
  }
}
```

---

## 🏗️ Class Architecture Patterns

### Pattern 1: Domain Models (Entities)

```typescript
export class User {
  private readonly _id: string;
  private _email: string;
  private _profile: UserProfile;
  private readonly _createdAt: Date;
  private _updatedAt: Date;

  public constructor(
    id: string,
    email: string,
    profile: UserProfile,
    createdAt: Date = new Date(),
    updatedAt: Date = new Date()
  ) {
    this._id = id;
    this._email = email;
    this._profile = profile;
    this._createdAt = createdAt;
    this._updatedAt = updatedAt;
  }

  public getId(): string {
    return this._id;
  }

  public getEmail(): string {
    return this._email;
  }

  public updateEmail(email: string): void {
    this.validateEmail(email);
    this._email = email;
    this._updatedAt = new Date();
  }

  public getProfile(): UserProfile {
    return this._profile;
  }

  public updateProfile(profile: UserProfile): void {
    this._profile = profile;
    this._updatedAt = new Date();
  }

  private validateEmail(email: string): void {
    if (!email.includes('@')) {
      throw new Error('Invalid email format');
    }
  }

  public static fromJSON(data: unknown): User {
    // Type guard and construction
  }

  public toJSON(): UserDTO {
    return {
      id: this._id,
      email: this._email,
      profile: this._profile.toJSON(),
      createdAt: this._createdAt.toISOString(),
      updatedAt: this._updatedAt.toISOString(),
    };
  }
}
```

### Pattern 2: Value Objects

```typescript
export class Email {
  private readonly _value: string;

  public constructor(value: string) {
    this.validate(value);
    this._value = value.toLowerCase().trim();
  }

  public getValue(): string {
    return this._value;
  }

  public getDomain(): string {
    return this._value.split('@')[1] ?? '';
  }

  public equals(other: Email): boolean {
    return this._value === other._value;
  }

  private validate(value: string): void {
    if (!value.includes('@')) {
      throw new Error('Invalid email format');
    }
    if (value.length > 255) {
      throw new Error('Email too long');
    }
  }

  public toString(): string {
    return this._value;
  }
}
```

### Pattern 3: Services (with Dependency Injection)

```typescript
export class UserService {
  private readonly _repository: UserRepository;
  private readonly _emailService: IEmailService;
  private readonly _logger: ILogger;

  public constructor(
    repository: UserRepository,
    emailService: IEmailService,
    logger: ILogger
  ) {
    this._repository = repository;
    this._emailService = emailService;
    this._logger = logger;
  }

  public async createUser(email: string, profile: UserProfile): Promise<User> {
    this._logger.info(`Creating user with email: ${email}`);

    const user: User = new User(
      this.generateId(),
      email,
      profile
    );

    await this._repository.save(user);
    await this._emailService.sendWelcomeEmail(email);

    this._logger.info(`User created: ${user.getId()}`);
    return user;
  }

  private generateId(): string {
    return crypto.randomUUID();
  }
}
```

### Pattern 4: Repositories

```typescript
export class UserRepository {
  private readonly _db: IDatabase;

  public constructor(db: IDatabase) {
    this._db = db;
  }

  public async findById(id: string): Promise<User | undefined> {
    const row: unknown = await this._db.query(
      'SELECT * FROM users WHERE id = ?',
      [id]
    );

    if (!row) {
      return undefined;
    }

    return User.fromJSON(row);
  }

  public async save(user: User): Promise<void> {
    const data: UserDTO = user.toJSON();
    await this._db.execute(
      'INSERT INTO users (id, email, created_at) VALUES (?, ?, ?)',
      [data.id, data.email, data.createdAt]
    );
  }

  public async update(user: User): Promise<void> {
    const data: UserDTO = user.toJSON();
    await this._db.execute(
      'UPDATE users SET email = ?, updated_at = ? WHERE id = ?',
      [data.email, data.updatedAt, data.id]
    );
  }
}
```

---

## 🎯 Summary - Quick Reference

### Always Do ✅
- ✅ Use classes for all domain models
- ✅ Enable strict mode in tsconfig.json
- ✅ Explicit types for all variables
- ✅ Explicit return types for all functions
- ✅ Private fields with public methods
- ✅ Readonly for immutable data
- ✅ Handle undefined/null explicitly
- ✅ Use type guards for unknown data
- ✅ Initialize all class properties
- ✅ Explicit accessibility modifiers

### Never Do ❌
- ❌ Never use `any`
- ❌ Never use interfaces for data structures
- ❌ Never use non-null assertions (!)
- ❌ Never leave variables untyped
- ❌ Never omit function return types
- ❌ Never access arrays without undefined checks
- ❌ Never use implicit 'this'
- ❌ Never skip property initialization
- ❌ Never use implicit accessibility

---

## 📚 Related Resources

**See also:**
- `.claude/skills/class-builder.md` - Automated class generation
- `templates/class-template.ts` - Boilerplate class template
- `hooks-collection/strict-typing/` - Enforcement hooks
- `.eslintrc.strict.json` - Strict ESLint configuration
- `tsconfig.strict.json` - Strict TypeScript configuration

---

**Last Updated:** 2025-11-03
**Priority:** CRITICAL - Enforce on all TypeScript code
**Applies To:** All TypeScript files in the project
