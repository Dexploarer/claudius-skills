# SolidJS Framework Rules

> Best practices for SolidJS - reactive JavaScript framework

---

## 🎯 Overview

SolidJS is a declarative JavaScript framework for building user interfaces with fine-grained reactivity and no virtual DOM.

---

## 📁 Project Structure

```
solidjs-app/
├── src/
│   ├── components/     # Reusable components
│   ├── pages/         # Page components
│   ├── stores/        # State management
│   ├── utils/         # Utilities
│   ├── App.tsx        # Root component
│   └── index.tsx      # Entry point
├── public/            # Static assets
└── vite.config.ts     # Vite configuration
```

---

## 🔧 Core Patterns

### 1. Reactive Component

```tsx
import { createSignal, createEffect } from 'solid-js';

function Counter() {
  const [count, setCount] = createSignal(0);

  // Computed value (reactive)
  const doubled = () => count() * 2;

  // Side effect
  createEffect(() => {
    console.log('Count changed:', count());
  });

  return (
    <div>
      <button onClick={() => setCount(count() + 1)}>
        Count: {count()} (doubled: {doubled()})
      </button>
    </div>
  );
}
```

### 2. Store for Complex State

```tsx
import { createStore } from 'solid-js/store';

const [todos, setTodos] = createStore({
  items: [],
  filter: 'all'
});

// Update nested state
setTodos('items', items => [...items, newTodo]);
setTodos('filter', 'completed');

// Computed
const filteredTodos = () => {
  return todos.items.filter(todo => {
    if (todos.filter === 'all') return true;
    if (todos.filter === 'completed') return todo.completed;
    return !todo.completed;
  });
};
```

### 3. Resource for Data Fetching

```tsx
import { createResource } from 'solid-js';

function UserProfile(props) {
  const [user] = createResource(
    () => props.userId,
    async (id) => {
      const res = await fetch(`/api/users/${id}`);
      return res.json();
    }
  );

  return (
    <div>
      <Show when={!user.loading} fallback={<p>Loading...</p>}>
        <h1>{user()?.name}</h1>
      </Show>
    </div>
  );
}
```

### 4. Control Flow

```tsx
import { Show, For, Switch, Match } from 'solid-js';

function App() {
  const [user, setUser] = createSignal(null);
  const [items, setItems] = createSignal([]);

  return (
    <>
      {/* Conditional rendering */}
      <Show when={user()} fallback={<Login />}>
        <Dashboard user={user()} />
      </Show>

      {/* List rendering */}
      <For each={items()}>
        {(item, index) => <Item data={item} index={index()} />}
      </For>

      {/* Switch/Match */}
      <Switch>
        <Match when={status() === 'loading'}>
          <Spinner />
        </Match>
        <Match when={status() === 'error'}>
          <Error />
        </Match>
        <Match when={status() === 'success'}>
          <Success />
        </Match>
      </Switch>
    </>
  );
}
```

---

## 🔒 Best Practices

### 1. Fine-Grained Reactivity
- Signals are functions: `count()` not `count`
- Only wrap changing values in signals
- Use `createMemo` for expensive computations

### 2. Avoid Destructuring Props
```tsx
// ❌ Bad - loses reactivity
function Component({ value }) {
  return <div>{value}</div>;
}

// ✅ Good - maintains reactivity
function Component(props) {
  return <div>{props.value}</div>;
}
```

### 3. Use Stores for Objects
- Use `createSignal` for primitives
- Use `createStore` for objects/arrays
- Stores have mutation helpers

---

**Last Updated:** 2025-11-02
**Framework Version:** SolidJS 1.8+
