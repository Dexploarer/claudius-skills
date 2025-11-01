---
name: advanced-feature-skill
description: Generate React components with TypeScript, tests, and styling. Use when user asks to "create component", "scaffold React component", or "generate TypeScript component"
allowed-tools: [Write, Read, Glob, Grep, Edit]
---

# Advanced Feature Skill - Intermediate Template

A comprehensive skill that handles multiple related tasks with framework-specific knowledge.

## When to Use

Activate this skill when the user wants to:
- "Create a React component"
- "Generate a Button component with TypeScript"
- "Scaffold a data table component"
- "Build a form component with validation"

## What This Skill Does

This skill creates complete component packages including:
1. ✅ Component file with TypeScript
2. ✅ Styling (CSS Modules or styled-components)
3. ✅ Unit tests (React Testing Library)
4. ✅ Type definitions
5. ✅ Barrel export (index.ts)
6. ✅ Documentation comments

## Instructions

### Phase 1: Gather Requirements

**Ask the user for:**
- Component name (PascalCase)
- Component purpose/description
- Required props
- State management needs
- Styling preferences

**Infer from context:**
- Project structure (check existing components)
- Styling approach (CSS Modules vs styled-components vs Tailwind)
- Testing framework (check package.json)
- TypeScript configuration

**Example questions to ask:**
```
"What props should the {ComponentName} accept?"
"Does it need local state or will it be stateless?"
"Should it fetch data or receive data via props?"
```

### Phase 2: Analyze Existing Code

Before generating, check existing patterns:

1. **Find similar components:**
   ```bash
   # Use Glob to find existing components
   Find components in src/components/
   ```

2. **Check styling approach:**
   ```bash
   # Look for *.module.css or styled-components
   Check for styling patterns
   ```

3. **Review testing patterns:**
   ```bash
   # Find test files to match style
   Look for *.test.tsx or *.spec.tsx
   ```

### Phase 3: Generate Component Structure

Create this file structure:
```
src/components/{ComponentName}/
├── {ComponentName}.tsx           # Main component
├── {ComponentName}.module.css    # Styles
├── {ComponentName}.test.tsx      # Tests
├── {ComponentName}.types.ts      # Type definitions (if complex)
└── index.ts                      # Barrel export
```

### Phase 4: Create Component File

**Template structure:**
```typescript
import React, { useState, useEffect, useCallback } from 'react';
import styles from './{ComponentName}.module.css';
import { {ComponentName}Props } from './types';

/**
 * {ComponentName} - Brief description
 *
 * @example
 * <{ComponentName}
 *   title="Example"
 *   onAction={handleAction}
 * />
 */
export const {ComponentName}: React.FC<{ComponentName}Props> = ({
  // Destructure props with defaults
  title,
  onAction,
  children,
  className = '',
}) => {
  // State management
  const [state, setState] = useState<StateType>(initialValue);

  // Effects
  useEffect(() => {
    // Effect logic
    return () => {
      // Cleanup
    };
  }, [dependencies]);

  // Event handlers
  const handleEvent = useCallback(() => {
    // Handler logic
  }, [dependencies]);

  // Render
  return (
    <div className={`${styles.container} ${className}`}>
      {/* Component JSX */}
    </div>
  );
};
```

### Phase 5: Create Type Definitions

```typescript
// {ComponentName}.types.ts
export interface {ComponentName}Props {
  /**
   * The title to display
   */
  title: string;

  /**
   * Callback when action is triggered
   */
  onAction?: () => void;

  /**
   * Child elements to render
   */
  children?: React.ReactNode;

  /**
   * Additional CSS class names
   */
  className?: string;
}

export interface {ComponentName}State {
  // State interface if complex
}
```

### Phase 6: Create Styles

**CSS Modules approach:**
```css
/* {ComponentName}.module.css */
.container {
  /* Container styles */
  padding: 1rem;
  border-radius: 4px;
}

.title {
  /* Title styles */
  font-size: 1.5rem;
  font-weight: bold;
}

/* Responsive design */
@media (max-width: 768px) {
  .container {
    padding: 0.5rem;
  }
}
```

**Styled-components approach (if detected):**
```typescript
import styled from 'styled-components';

export const Container = styled.div`
  padding: 1rem;
  border-radius: 4px;

  @media (max-width: 768px) {
    padding: 0.5rem;
  }
`;
```

### Phase 7: Create Tests

```typescript
// {ComponentName}.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { {ComponentName} } from './{ComponentName}';

describe('{ComponentName}', () => {
  it('renders without crashing', () => {
    render(<{ComponentName} title="Test" />);
    expect(screen.getByText('Test')).toBeInTheDocument();
  });

  it('calls onAction when clicked', () => {
    const handleAction = jest.fn();
    render(<{ComponentName} title="Test" onAction={handleAction} />);

    fireEvent.click(screen.getByRole('button'));
    expect(handleAction).toHaveBeenCalledTimes(1);
  });

  it('renders children correctly', () => {
    render(
      <{ComponentName} title="Test">
        <span>Child content</span>
      </{ComponentName}>
    );

    expect(screen.getByText('Child content')).toBeInTheDocument();
  });

  it('applies custom className', () => {
    const { container } = render(
      <{ComponentName} title="Test" className="custom-class" />
    );

    expect(container.firstChild).toHaveClass('custom-class');
  });
});
```

### Phase 8: Create Barrel Export

```typescript
// index.ts
export { {ComponentName} } from './{ComponentName}';
export type { {ComponentName}Props } from './types';
```

### Phase 9: Show Summary

After creating all files, show a summary:
```
✅ Created {ComponentName} component

📁 Files created:
   - {ComponentName}.tsx (156 lines)
   - {ComponentName}.module.css (24 lines)
   - {ComponentName}.test.tsx (45 lines)
   - {ComponentName}.types.ts (18 lines)
   - index.ts (2 lines)

📋 Next steps:
   1. Review the component code
   2. Run tests: npm test {ComponentName}
   3. Import: import { {ComponentName} } from '@/components/{ComponentName}'
   4. Use: <{ComponentName} title="Hello" />

🎨 Customization options:
   - Modify styles in {ComponentName}.module.css
   - Add more props in {ComponentName}.types.ts
   - Extend tests in {ComponentName}.test.tsx
```

## Best Practices

### Component Design

✅ **Single Responsibility:** Each component should do one thing
✅ **Composable:** Should work well with other components
✅ **Testable:** Easy to test in isolation
✅ **Accessible:** Include ARIA attributes
✅ **Performant:** Use React.memo when appropriate

### TypeScript

✅ **Strict types:** No `any` types
✅ **Proper interfaces:** Export prop types
✅ **Generic types:** Use generics for flexible components
✅ **Discriminated unions:** For variant props

### Testing

✅ **User-centric:** Test behavior, not implementation
✅ **Comprehensive:** Test happy path and edge cases
✅ **Accessible:** Use Testing Library queries
✅ **Maintainable:** Clear test descriptions

### Styling

✅ **Scoped styles:** Use CSS Modules or styled-components
✅ **Responsive:** Mobile-first approach
✅ **Consistent:** Follow design system
✅ **Performance:** Avoid inline styles in render

## Advanced Features

### Custom Hooks

If the component needs complex logic, extract to a custom hook:

```typescript
// hooks/use{ComponentName}.ts
export function use{ComponentName}({
  initialValue,
  options,
}: {
  initialValue: Type;
  options?: Options;
}) {
  const [state, setState] = useState(initialValue);

  useEffect(() => {
    // Effect logic
  }, [options]);

  const methods = useMemo(() => ({
    update: (value: Type) => setState(value),
    reset: () => setState(initialValue),
  }), [initialValue]);

  return { state, ...methods };
}
```

### Compound Components

For complex components, use the compound pattern:

```typescript
export const {ComponentName} = {
  Root: {ComponentName}Root,
  Header: {ComponentName}Header,
  Body: {ComponentName}Body,
  Footer: {ComponentName}Footer,
};

// Usage:
<{ComponentName}.Root>
  <{ComponentName}.Header>Title</{ComponentName}.Header>
  <{ComponentName}.Body>Content</{ComponentName}.Body>
  <{ComponentName}.Footer>Actions</{ComponentName}.Footer>
</{ComponentName}.Root>
```

### Context Integration

If component needs to consume context:

```typescript
import { useTheme } from '@/context/ThemeContext';

export const {ComponentName}: React.FC<Props> = (props) => {
  const theme = useTheme();

  return (
    <div style={{ color: theme.colors.text }}>
      {/* Component content */}
    </div>
  );
};
```

## Patterns and Examples

### Pattern 1: Data Display Component

For components that display data:
- Receive data via props
- Handle loading and error states
- Include empty state
- Support data transformation

### Pattern 2: Form Component

For form inputs:
- Controlled components
- Validation
- Error display
- Accessibility labels

### Pattern 3: Container Component

For components with business logic:
- Data fetching
- State management
- Error handling
- Loading states

## Customization for Your Project

### Project-Specific Patterns

```markdown
## Our Component Standards

All components must:
1. Include Storybook story
2. Have at least 80% test coverage
3. Include PropTypes for runtime validation
4. Follow our naming convention: {Feature}{Type}
5. Use our custom hooks from @/hooks
```

### Team Conventions

```markdown
## Team Guidelines

### File Structure
src/
├── components/
│   └── {ComponentName}/
│       ├── {ComponentName}.tsx
│       ├── {ComponentName}.styles.ts
│       ├── {ComponentName}.test.tsx
│       ├── {ComponentName}.stories.tsx
│       └── index.ts

### Import Order
1. React imports
2. Third-party imports
3. Internal imports
4. Type imports
5. Style imports
```

## Common Pitfalls

❌ **Over-engineering:** Don't add complexity until needed
❌ **Prop drilling:** Use context or composition instead
❌ **Giant components:** Split into smaller pieces
❌ **Missing tests:** Always include tests
❌ **Poor naming:** Use descriptive names

## Integration Examples

### With State Management (Redux)

```typescript
import { useSelector, useDispatch } from 'react-redux';
import { selectData, updateData } from '@/store/slices';

export const {ComponentName}: React.FC<Props> = (props) => {
  const data = useSelector(selectData);
  const dispatch = useDispatch();

  const handleUpdate = () => {
    dispatch(updateData(newData));
  };

  // Component logic
};
```

### With React Query

```typescript
import { useQuery, useMutation } from '@tanstack/react-query';

export const {ComponentName}: React.FC<Props> = ({ id }) => {
  const { data, isLoading, error } = useQuery({
    queryKey: ['item', id],
    queryFn: () => fetchItem(id),
  });

  if (isLoading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} />;

  return <div>{/* Component content */}</div>;
};
```

## Success Criteria

A well-generated component should:
- ✅ Compile without TypeScript errors
- ✅ Pass all tests
- ✅ Be accessible (ARIA, keyboard navigation)
- ✅ Be responsive
- ✅ Follow project conventions
- ✅ Be well-documented

## Notes

- Always check existing patterns before generating
- Ask user if unsure about requirements
- Provide alternatives when multiple approaches are valid
- Include migration guide if changing existing component
- Document breaking changes clearly
