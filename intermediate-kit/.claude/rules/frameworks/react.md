# React Framework Rules - Intermediate Kit

> **Modern React development with TypeScript, hooks, and best practices**

---

## 🎯 React in Intermediate Kit

**Skill:** `react-component-generator`
**Location:** `intermediate-kit/.claude/skills/react-component-generator.md`

**Stack:**
- React 18+
- TypeScript
- Functional Components
- React Hooks
- Styled-components / CSS Modules

---

## 📋 Component Patterns

### 1. Functional Component with TypeScript

```tsx
import React, { useState, useEffect } from 'react';

interface UserCardProps {
  userId: string;
  onUserClick?: (userId: string) => void;
}

export const UserCard: React.FC<UserCardProps> = ({ userId, onUserClick }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUser(userId).then(setUser).finally(() => setLoading(false));
  }, [userId]);

  if (loading) return <div>Loading...</div>;
  if (!user) return <div>User not found</div>;

  return (
    <div className="user-card" onClick={() => onUserClick?.(userId)}>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  );
};
```

### 2. Custom Hooks

```tsx
function useUser(userId: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    setLoading(true);
    fetchUser(userId)
      .then(setUser)
      .catch(setError)
      .finally(() => setLoading(false));
  }, [userId]);

  return { user, loading, error };
}
```

### 3. Context for State Management

```tsx
interface UserContextType {
  user: User | null;
  login: (credentials: Credentials) => Promise<void>;
  logout: () => void;
}

const UserContext = createContext<UserContextType | undefined>(undefined);

export const UserProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  const login = async (credentials: Credentials) => {
    const user = await authAPI.login(credentials);
    setUser(user);
  };

  const logout = () => setUser(null);

  return (
    <UserContext.Provider value={{ user, login, logout }}>
      {children}
    </UserContext.Provider>
  );
};

export const useUser = () => {
  const context = useContext(UserContext);
  if (!context) throw new Error('useUser must be used within UserProvider');
  return context;
};
```

---

## 🎨 Styling Approaches

### 1. Styled-components

```tsx
import styled from 'styled-components';

const Card = styled.div<{ $primary?: boolean }>`
  padding: 1rem;
  background: ${props => props.$primary ? '#007bff' : '#fff'};
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
`;

const Title = styled.h2`
  font-size: 1.5rem;
  color: #333;
`;

export const UserCard: React.FC<Props> = ({ user, primary }) => (
  <Card $primary={primary}>
    <Title>{user.name}</Title>
  </Card>
);
```

### 2. CSS Modules

```tsx
import styles from './UserCard.module.css';

export const UserCard: React.FC<Props> = ({ user }) => (
  <div className={styles.card}>
    <h2 className={styles.title}>{user.name}</h2>
  </div>
);
```

---

## 🧪 Testing

### Component Tests with React Testing Library

```tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { UserCard } from './UserCard';

describe('UserCard', () => {
  it('renders user information', () => {
    const user = { id: '1', name: 'John Doe', email: 'john@example.com' };
    render(<UserCard user={user} />);

    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });

  it('calls onUserClick when clicked', () => {
    const onUserClick = jest.fn();
    const user = { id: '1', name: 'John Doe', email: 'john@example.com' };

    render(<UserCard user={user} onUserClick={onUserClick} />);
    fireEvent.click(screen.getByText('John Doe'));

    expect(onUserClick).toHaveBeenCalledWith('1');
  });
});
```

### Hook Tests

```tsx
import { renderHook, waitFor } from '@testing-library/react';
import { useUser } from './useUser';

describe('useUser', () => {
  it('fetches user data', async () => {
    const { result } = renderHook(() => useUser('123'));

    expect(result.current.loading).toBe(true);

    await waitFor(() => expect(result.current.loading).toBe(false));
    expect(result.current.user).toEqual({ id: '123', name: 'John' });
  });
});
```

---

## 🚀 Performance Optimization

### 1. React.memo for Expensive Components

```tsx
export const ExpensiveComponent = React.memo<Props>(({ data }) => {
  // Expensive rendering logic
  return <div>{/* ... */}</div>;
});
```

### 2. useMemo for Expensive Calculations

```tsx
const filteredUsers = useMemo(() => {
  return users.filter(u => u.name.includes(search));
}, [users, search]);
```

### 3. useCallback for Stable Function References

```tsx
const handleClick = useCallback((id: string) => {
  // Handle click
}, [/* dependencies */]);
```

### 4. Code Splitting

```tsx
const LazyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}
```

---

## 📦 Project Structure

```
src/
├── components/
│   ├── common/           # Reusable components
│   │   ├── Button.tsx
│   │   └── Input.tsx
│   ├── features/         # Feature-specific components
│   │   ├── auth/
│   │   │   ├── LoginForm.tsx
│   │   │   └── RegisterForm.tsx
│   │   └── users/
│   │       ├── UserList.tsx
│   │       └── UserCard.tsx
│   └── layout/           # Layout components
│       ├── Header.tsx
│       └── Footer.tsx
├── hooks/                # Custom hooks
│   ├── useUser.ts
│   └── useAuth.ts
├── context/              # React Context
│   ├── UserContext.tsx
│   └── ThemeContext.tsx
├── services/             # API services
│   ├── api.ts
│   └── auth.ts
├── types/                # TypeScript types
│   └── index.ts
└── App.tsx
```

---

## 🔗 Related Commands

- `/bundle-analyze` - Analyze React bundle size
- `/performance-profile` - Profile React component renders
- `/coverage-report` - Test coverage for React components

## 🔗 Related Agents

- `performance-optimizer` - Optimize React performance
- `system-architect` - Design React architecture

---

**Last Updated:** 2025-11-01
**React Version:** 18+
**TypeScript:** Required
