# Create Component Command

Quickly scaffold new components with proper boilerplate for your framework.

## What It Does

- Detects your framework automatically
- Creates component file with boilerplate
- Includes TypeScript types if applicable
- Offers to create test file
- Provides next steps

## Installation

```bash
cp examples/beginner/basic-commands/create-component/command.md \
   .claude/commands/create-component.md
```

## Usage

```bash
/create-component ComponentName
/create-component Button react
/create-component UserCard
```

## Supports

- React (JS/TS)
- Vue (2/3)
- Angular
- Svelte
- Web Components

## Example Output

For `/create-component Button` in a React+TypeScript project:

**Button.tsx:**
```typescript
import React from 'react'

interface ButtonProps {
  children: React.ReactNode
  onClick?: () => void
  disabled?: boolean
}

export const Button: React.FC<ButtonProps> = ({
  children,
  onClick,
  disabled = false
}) => {
  return (
    <button onClick={onClick} disabled={disabled}>
      {children}
    </button>
  )
}
```

**Button.module.css:**
```css
.button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
```

## See Also

- [Framework Skills](../../../intermediate/framework-skills/) - Advanced component generation
- [Extract Function](../extract-function/) - Refactor existing code
