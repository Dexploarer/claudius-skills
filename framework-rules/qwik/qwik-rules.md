# Qwik Framework Rules

> Best practices for Qwik - resumable web framework

---

## 🎯 Overview

Qwik is a new kind of web framework that achieves instant-on interactivity through resumability instead of hydration.

---

## 📁 Project Structure

```
qwik-app/
├── src/
│   ├── components/     # Components
│   ├── routes/        # File-based routing
│   │   ├── index.tsx  # Homepage
│   │   └── layout.tsx # Root layout
│   ├── global.css     # Global styles
│   └── root.tsx       # Root component
├── public/            # Static files
└── vite.config.ts     # Configuration
```

---

## 🔧 Core Patterns

### 1. Component with State

```tsx
import { component$, useSignal } from '@builder.io/qwik';

export default component$(() => {
  const count = useSignal(0);

  return (
    <div>
      <button onClick$={() => count.value++}>
        Count: {count.value}
      </button>
    </div>
  );
});
```

### 2. Data Loader

```tsx
import { component$, useSignal, $, Resource, useResource$ } from '@builder.io/qwik';
import { routeLoader$ } from '@builder.io/qwik-city';

export const useUserData = routeLoader$(async (requestEvent) => {
  const res = await fetch('/api/user');
  return res.json();
});

export default component$(() => {
  const user = useUserData();

  return (
    <Resource
      value={user}
      onPending={() => <div>Loading...</div>}
      onResolved={(data) => <div>Hello {data.name}</div>}
    />
  );
});
```

### 3. Event Handlers ($)

```tsx
import { component$, $ } from '@builder.io/qwik';

export default component$(() => {
  // $ creates lazy-loaded event handler
  const handleClick = $((event: Event) => {
    console.log('Clicked!', event);
  });

  return <button onClick$={handleClick}>Click me</button>;
});
```

---

## 🔒 Best Practices

### 1. Use $ for Lazy Loading
- `component$()` - lazy component
- `$()` - lazy event handler
- `useSignal()` - reactive state

### 2. Resumability
- No hydration needed
- JavaScript loads on interaction
- Instant page interactivity

### 3. Fine-Grained Loading
- Components load individually
- Only interactive parts need JS
- Optimal performance

---

**Last Updated:** 2025-11-02
**Framework Version:** Qwik 1.5+
