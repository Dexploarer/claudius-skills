# Nuxt 3 Framework Rules

> Best practices for Nuxt 3 - the Vue.js framework

---

## 🎯 Overview

Nuxt 3 is a full-stack Vue.js framework with server-side rendering, file-based routing, and auto imports.

---

## 📁 Project Structure

```
nuxt3-app/
├── pages/              # File-based routing
│   ├── index.vue      # Homepage
│   └── about.vue      # /about
├── components/        # Auto-imported components
├── composables/       # Auto-imported composables
├── layouts/           # Page layouts
├── server/            # Server routes
│   └── api/          # API endpoints
├── public/            # Static files
└── nuxt.config.ts    # Configuration
```

---

## 🔧 Core Patterns

### 1. Page with Data Fetching

```vue
<script setup lang="ts">
const { data: posts } = await useFetch('/api/posts');
</script>

<template>
  <div>
    <h1>Posts</h1>
    <article v-for="post in posts" :key="post.id">
      <h2>{{ post.title }}</h2>
      <p>{{ post.excerpt }}</p>
    </article>
  </div>
</template>
```

### 2. API Route

```typescript
// server/api/posts.ts
export default defineEventHandler(async (event) => {
  const posts = await db.posts.findMany();
  return posts;
});

// server/api/posts/[id].ts
export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id');
  const post = await db.posts.findUnique({ where: { id } });
  return post;
});
```

### 3. Composable

```typescript
// composables/useAuth.ts
export const useAuth = () => {
  const user = useState('user', () => null);

  const login = async (credentials) => {
    const data = await $fetch('/api/auth/login', {
      method: 'POST',
      body: credentials
    });
    user.value = data.user;
  };

  const logout = async () => {
    await $fetch('/api/auth/logout', { method: 'POST' });
    user.value = null;
  };

  return { user, login, logout };
};
```

### 4. Layout

```vue
<!-- layouts/default.vue -->
<template>
  <div>
    <nav>
      <NuxtLink to="/">Home</NuxtLink>
      <NuxtLink to="/about">About</NuxtLink>
    </nav>
    <main>
      <slot />
    </main>
  </div>
</template>
```

---

## 🔒 Best Practices

### 1. Use Auto Imports
- Components are auto-imported
- Composables are auto-imported
- No need for manual imports

### 2. Server Routes
- Use `server/api/` for APIs
- Use `server/routes/` for SSR routes
- Type-safe with TypeScript

### 3. Data Fetching
- `useFetch` for external APIs
- `useAsyncData` for complex logic
- `$fetch` for programmatic calls

---

**Last Updated:** 2025-11-02
**Framework Version:** Nuxt 3.10+
