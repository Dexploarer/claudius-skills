---
name: react-component-generator
description: Generates React components with TypeScript, hooks, and best practices. Use when user asks to "create React component", "generate component", or "scaffold component".
allowed-tools: [Write, Read, Glob]
---

# React Component Generator

Generates modern React components following best practices with TypeScript support.

## When to Use

- "Create a Button component"
- "Generate a UserProfile component"
- "Scaffold a DataTable component"

## Instructions

### 1. Gather Requirements
- Component name (PascalCase)
- Component type (functional, with state, with effects)
- Props needed
- TypeScript types
- Styling approach

### 2. Generate Component Structure

**Functional Component:**
```typescript
import React from 'react';
import styles from './ComponentName.module.css';

interface ComponentNameProps {
  // Props here
}

export const ComponentName: React.FC<ComponentNameProps> = ({
  // Destructure props
}) => {
  return (
    <div className={styles.container}>
      {/* Component JSX */}
    </div>
  );
};
```

**With State:**
```typescript
import React, { useState } from 'react';

export const ComponentName: React.FC<Props> = () => {
  const [state, setState] = useState<Type>(initialValue);

  return <div>{/* ... */}</div>;
};
```

**With Effects:**
```typescript
import React, { useEffect } from 'react';

export const ComponentName: React.FC<Props> = () => {
  useEffect(() => {
    // Effect logic
    return () => {
      // Cleanup
    };
  }, [dependencies]);

  return <div>{/* ... */}</div>;
};
```

### 3. Add PropTypes/TypeScript Interfaces

```typescript
interface ComponentNameProps {
  title: string;
  onAction?: () => void;
  children?: React.ReactNode;
  className?: string;
}
```

### 4. Create Associated Files

- `ComponentName.tsx` - Component file
- `ComponentName.module.css` - Styles
- `ComponentName.test.tsx` - Tests
- `index.ts` - Barrel export

### 5. Add Documentation

```typescript
/**
 * ComponentName - Brief description
 *
 * @example
 * <ComponentName title="Hello" onAction={handleClick} />
 */
```

## Best Practices

- Use functional components
- TypeScript for type safety
- CSS Modules for styling
- Proper prop destructuring
- Meaningful names
- Add tests
- Export from index.ts
