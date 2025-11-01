# React Component Generator - Intermediate Skill

A framework-specific skill that generates modern React components with TypeScript, hooks, styling, and tests.

## What This Teaches

- Framework-specific skill development
- TypeScript integration
- Best practices enforcement
- Multi-file generation
- Test co-location
- CSS Modules pattern

## Installation

```bash
# Copy to your React project
cp SKILL.md /path/to/your-project/.claude/skills/react-component-generator.md
```

## When It Activates

The skill automatically activates when you:
- "Create a Button component"
- "Generate a UserProfile component with data fetching"
- "Build a DataTable component with sorting"
- "Scaffold a Modal component"

## What It Generates

For a component named `UserCard`, the skill creates:

```
src/components/UserCard/
├── UserCard.tsx           # Component implementation
├── UserCard.module.css    # Scoped styles
├── UserCard.test.tsx      # Unit tests
└── index.ts              # Barrel export
```

## Example Usage

### Basic Component

**You:**
```
"Create a Button component with loading state"
```

**Generated:**

`UserCard.tsx`:
```typescript
import React from 'react';
import styles from './Button.module.css';

interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  loading?: boolean;
  disabled?: boolean;
  variant?: 'primary' | 'secondary' | 'danger';
  className?: string;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  onClick,
  loading = false,
  disabled = false,
  variant = 'primary',
  className = '',
}) => {
  return (
    <button
      className={`${styles.button} ${styles[variant]} ${className}`}
      onClick={onClick}
      disabled={disabled || loading}
    >
      {loading ? <span className={styles.spinner}>...</span> : children}
    </button>
  );
};
```

`Button.module.css`:
```css
.button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s;
}

.button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.primary {
  background-color: #007bff;
  color: white;
}

.primary:hover:not(:disabled) {
  background-color: #0056b3;
}

.secondary {
  background-color: #6c757d;
  color: white;
}

.danger {
  background-color: #dc3545;
  color: white;
}

.spinner {
  display: inline-block;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

`Button.test.tsx`:
```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders children', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('calls onClick when clicked', () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click</Button>);

    fireEvent.click(screen.getByText('Click'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('shows loading state', () => {
    render(<Button loading>Click</Button>);
    expect(screen.getByText('...')).toBeInTheDocument();
  });

  it('disables button when loading', () => {
    render(<Button loading>Click</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });

  it('applies variant classes', () => {
    const { container } = render(<Button variant="danger">Delete</Button>);
    expect(container.firstChild).toHaveClass('danger');
  });
});
```

`index.ts`:
```typescript
export { Button } from './Button';
export type { ButtonProps } from './Button';
```

### Component with Hooks

**You:**
```
"Create a SearchBox component with debounced search"
```

**Generated component includes:**
- `useState` for input value
- `useEffect` for debouncing
- `useCallback` for memoized handlers
- Proper cleanup in useEffect
- TypeScript types for all callbacks

### Component with API Calls

**You:**
```
"Create a UserProfile component that fetches user data from an API"
```

**Generated component includes:**
- Custom hook: `useUserData(userId)`
- Loading state management
- Error handling
- TypeScript interfaces for API response
- Retry logic
- Tests with mocked API calls

## Component Patterns Supported

### 1. Presentational Components
```
"Create a Card component for displaying content"
```
- Props-driven
- No state
- Focused on UI
- Easy to test

### 2. Container Components
```
"Create a UserListContainer that fetches and displays users"
```
- Data fetching
- State management
- Business logic
- Connects to APIs

### 3. Form Components
```
"Create a LoginForm with validation"
```
- Controlled inputs
- Form state management
- Validation logic
- Submit handling
- Error display

### 4. Higher-Order Components
```
"Create a withAuth HOC for protected routes"
```
- Component wrapping
- Props injection
- Authentication logic

### 5. Custom Hooks
```
"Create a useLocalStorage hook"
```
- Reusable logic
- State management
- Side effects
- TypeScript generics

## Features

### TypeScript Support
- Full type safety
- Props interfaces
- Generic types
- Proper event typing

### Hooks Best Practices
- Proper dependency arrays
- Cleanup functions
- Memoization where appropriate
- Custom hooks for reusable logic

### Styling
- CSS Modules for scoping
- BEM naming convention option
- Responsive design
- CSS variables support

### Testing
- React Testing Library
- User-centric tests
- Accessibility checks
- Mocked dependencies

### Accessibility
- ARIA attributes
- Keyboard navigation
- Screen reader support
- Focus management

## Customization

### Change Styling Approach

Edit the skill to use styled-components:

```markdown
### Styling
Use styled-components:

\`\`\`typescript
import styled from 'styled-components';

const StyledButton = styled.button<{ variant: string }>`
  padding: 0.5rem 1rem;
  background: ${props => props.variant === 'primary' ? '#007bff' : '#6c757d'};
`;
\`\`\`
```

### Add Custom Hooks Pattern

```markdown
### Custom Hooks

Always extract reusable logic to custom hooks:

\`\`\`typescript
// hooks/useApi.ts
export function useApi<T>(url: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    // Fetch logic
  }, [url]);

  return { data, loading, error };
}
\`\`\`
```

### Team-Specific Patterns

```markdown
### Our Component Structure

Components must include:
1. TypeScript interface exported
2. Data-testid attributes for testing
3. Storybook story file
4. PropTypes as runtime validation

\`\`\`typescript
export interface ButtonProps {
  // ...
}

Button.propTypes = {
  // Runtime validation
};
\`\`\`
```

## Advanced Usage

### Composite Components

**You:**
```
"Create a DataTable component with sorting, filtering, and pagination"
```

**Result:**
```
DataTable/
├── DataTable.tsx
├── components/
│   ├── TableHeader.tsx
│   ├── TableBody.tsx
│   ├── TablePagination.tsx
│   └── TableFilters.tsx
├── hooks/
│   ├── useTableSort.ts
│   ├── useTableFilter.ts
│   └── useTablePagination.ts
├── DataTable.module.css
├── DataTable.test.tsx
└── index.ts
```

### Component with Context

**You:**
```
"Create a ThemeProvider component with theme switching"
```

**Generates:**
- Context creation
- Provider component
- Custom hook: `useTheme()`
- TypeScript types
- Tests for context

### Optimized Components

**You:**
```
"Create a VirtualList component for rendering large lists"
```

**Includes:**
- React.memo for optimization
- useMemo for expensive calculations
- useCallback for stable references
- Virtualization logic
- Performance tests

## Real-World Examples

### Example 1: Dashboard Widget

```
"Create a MetricsCard component that shows a metric with trend"
```

Generates:
- Card with title, value, and trend indicator
- Color coding (green for up, red for down)
- Percentage change display
- Loading skeleton
- Error state
- Tests for all states

### Example 2: Authentication Form

```
"Create a SignUpForm with email, password, and validation"
```

Generates:
- Controlled form inputs
- Real-time validation
- Password strength indicator
- Submit handling
- Error messages
- Accessibility labels
- Complete test suite

### Example 3: Modal Dialog

```
"Create a Modal component with overlay and animations"
```

Generates:
- Portal rendering
- Focus trap
- ESC key handling
- Click outside to close
- Animation with CSS transitions
- Accessibility (role, aria-labels)
- Tests for interactions

## Troubleshooting

### Skill Doesn't Activate

**Problem:** Skill doesn't trigger for React components

**Solution:**
- Check description includes your trigger phrases
- Try more explicit: "create React component"
- Verify skill is in `.claude/skills/`

### Wrong File Structure

**Problem:** Files created in wrong location

**Solution:** Be specific:
```
"Create a Button component in src/components/Button/"
```

### Missing Features

**Problem:** Generated component lacks needed features

**Solution:** Be detailed in request:
```
"Create a Button component with:
- loading state
- disabled state
- icon support
- size variants (small, medium, large)
- full TypeScript types
- comprehensive tests"
```

## Best Practices

### ✅ Do:
- Be specific about component requirements
- Request TypeScript types explicitly
- Ask for tests with components
- Specify styling approach
- Mention accessibility needs

### ❌ Don't:
- Create overly complex components
- Skip tests
- Ignore TypeScript types
- Forget about accessibility
- Generate without reviewing

## Integration with Your Workflow

### With Storybook

Add to skill:
```markdown
### Storybook Story

Create {ComponentName}.stories.tsx:

\`\`\`typescript
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  component: Button,
};

export default meta;
type Story = StoryObj<typeof Button>;

export const Primary: Story = {
  args: {
    children: 'Click me',
    variant: 'primary',
  },
};
\`\`\`
```

### With Testing Library

Already included! All components come with React Testing Library tests.

### With TypeScript Strict Mode

Skill generates strict TypeScript:
- No `any` types
- Proper null checks
- Exhaustive switch statements
- Required props marked clearly

## Learning Path

### Level 1: Use As-Is
- Generate simple components
- Review generated code
- Understand patterns

### Level 2: Customize
- Add your team's patterns
- Modify styling approach
- Add additional files (stories, etc.)

### Level 3: Extend
- Add more component types
- Create specialized variants
- Build component library

## Related Resources

- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [React Testing Library](https://testing-library.com/react)
- [CSS Modules](https://github.com/css-modules/css-modules)

## Next Steps

1. Install the skill in your React project
2. Generate a few components
3. Customize for your needs
4. Share with your team
5. Build your component library!

---

**Pro Tip:** Combine with a code-reviewer subagent to automatically review generated components for quality and best practices!
