# Fresh Framework Rules

> Best practices for Fresh - Deno web framework

---

## 🎯 Overview

Fresh is a next-generation web framework built for Deno with server-side rendering and islands architecture.

---

## 📁 Project Structure

```
fresh-app/
├── routes/             # File-based routing
│   ├── index.tsx      # Homepage
│   ├── _app.tsx       # App wrapper
│   └── api/           # API routes
├── islands/           # Interactive islands
├── components/        # Server components
├── static/            # Static files
├── fresh.gen.ts       # Generated manifest
└── main.ts            # Entry point
```

---

## 🔧 Core Patterns

### 1. Route with Data

```tsx
// routes/posts/index.tsx
import { Handlers, PageProps } from "$fresh/server.ts";

export const handler: Handlers = {
  async GET(req, ctx) {
    const posts = await db.posts.findMany();
    return ctx.render({ posts });
  }
};

export default function PostsPage({ data }: PageProps) {
  return (
    <div>
      <h1>Posts</h1>
      {data.posts.map((post) => (
        <article key={post.id}>
          <h2>{post.title}</h2>
        </article>
      ))}
    </div>
  );
}
```

### 2. Island (Interactive Component)

```tsx
// islands/Counter.tsx
import { useState } from "preact/hooks";

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>
        Count: {count}
      </button>
    </div>
  );
}
```

### 3. API Route

```ts
// routes/api/users.ts
import { Handlers } from "$fresh/server.ts";

export const handler: Handlers = {
  async GET(req, ctx) {
    const users = await db.users.findMany();
    return new Response(JSON.stringify(users), {
      headers: { "Content-Type": "application/json" }
    });
  }
};
```

---

## 🔒 Best Practices

### 1. Islands Architecture
- Server components by default
- Islands for interactivity
- Minimal JavaScript

### 2. Deno-First
- Use Deno standard library
- Import from URLs
- TypeScript by default

### 3. Performance
- No build step
- Fast hot reload
- Edge-ready

---

**Last Updated:** 2025-11-02
**Framework Version:** Fresh 1.6+
