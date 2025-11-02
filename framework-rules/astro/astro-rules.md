# Astro Framework Rules

> Best practices for Astro - the web framework for content-driven websites

---

## 🎯 Overview

These rules guide Claude Code when working with Astro projects, focusing on content-first development, islands architecture, and multi-framework support.

---

## 📁 Project Structure

```
astro-project/
├── src/
│   ├── pages/              # File-based routing
│   │   ├── index.astro    # Homepage
│   │   ├── about.astro    # About page
│   │   ├── blog/
│   │   │   ├── index.astro
│   │   │   └── [slug].astro  # Dynamic route
│   │   └── api/           # API endpoints
│   ├── layouts/           # Layout components
│   ├── components/        # Reusable components
│   ├── content/          # Content collections
│   │   ├── config.ts     # Content schema
│   │   └── blog/         # Blog posts (Markdown)
│   └── styles/           # Global styles
├── public/               # Static assets
└── astro.config.mjs     # Astro configuration
```

---

## 🔧 Core Patterns

### 1. Basic Page

```astro
---
// src/pages/index.astro
import Layout from '../layouts/Layout.astro';
import Card from '../components/Card.astro';

const title = 'Welcome to Astro';
---

<Layout title={title}>
  <main>
    <h1>{title}</h1>
    <Card
      title="Getting Started"
      body="Follow the quick start guide."
      href="/docs"
    />
  </main>
</Layout>

<style>
  main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }
</style>
```

### 2. Content Collections

```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    author: z.string(),
    tags: z.array(z.string()),
    image: z.string().optional(),
  }),
});

export const collections = {
  blog: blogCollection,
};
```

```astro
---
// src/pages/blog/[slug].astro
import { getCollection } from 'astro:content';
import Layout from '../../layouts/Layout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map(post => ({
    params: { slug: post.slug },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await post.render();
---

<Layout title={post.data.title}>
  <article>
    <h1>{post.data.title}</h1>
    <p class="meta">
      By {post.data.author} on {post.data.pubDate.toLocaleDateString()}
    </p>
    <Content />
  </article>
</Layout>
```

### 3. Islands Architecture (Interactive Components)

```astro
---
// src/pages/interactive.astro
import Layout from '../layouts/Layout.astro';
import Counter from '../components/Counter.tsx'; // React
import TodoList from '../components/TodoList.vue'; // Vue
---

<Layout title="Interactive Page">
  <!-- Static content (no JS) -->
  <h1>Interactive Components</h1>

  <!-- Hydrate on page load -->
  <Counter client:load />

  <!-- Hydrate when visible -->
  <TodoList client:visible />

  <!-- Hydrate on idle -->
  <HeavyComponent client:idle />

  <!-- No hydration (static HTML only) -->
  <StaticComponent />
</Layout>
```

### 4. API Endpoints

```typescript
// src/pages/api/posts.json.ts
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async ({ params, request }) => {
  const posts = await getCollection('blog');

  return new Response(
    JSON.stringify({
      posts: posts.map(post => ({
        slug: post.slug,
        title: post.data.title,
        description: post.data.description,
      }))
    }),
    {
      status: 200,
      headers: {
        'Content-Type': 'application/json'
      }
    }
  );
};

export const POST: APIRoute = async ({ request }) => {
  const data = await request.json();

  // Process data

  return new Response(JSON.stringify({ success: true }), {
    status: 201,
    headers: {
      'Content-Type': 'application/json'
    }
  });
};
```

---

## 🎨 Multi-Framework Support

### React Component

```tsx
// src/components/Counter.tsx
import { useState } from 'react';

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

### Vue Component

```vue
<!-- src/components/TodoList.vue -->
<script setup lang="ts">
import { ref } from 'vue';

const todos = ref<string[]>([]);
const newTodo = ref('');

function addTodo() {
  if (newTodo.value.trim()) {
    todos.value.push(newTodo.value);
    newTodo.value = '';
  }
}
</script>

<template>
  <div>
    <input v-model="newTodo" @keyup.enter="addTodo" />
    <button @click="addTodo">Add</button>
    <ul>
      <li v-for="todo in todos" :key="todo">{{ todo }}</li>
    </ul>
  </div>
</template>
```

---

## 🔒 Best Practices

### 1. Use Content Collections
- Define schemas for type safety
- Store content in `src/content/`
- Use Markdown/MDX for blog posts

### 2. Optimize Performance
- Use `client:*` directives wisely
- Minimize hydrated components
- Leverage static generation

### 3. Images
- Use `<Image />` component
- Optimize images automatically
- Use proper formats (WebP, AVIF)

### 4. SEO
- Use `<SEO />` component in layouts
- Add meta tags
- Generate sitemaps

---

## ⚡ Performance Patterns

### Image Optimization

```astro
---
import { Image } from 'astro:assets';
import hero from '../images/hero.jpg';
---

<Image
  src={hero}
  alt="Hero image"
  width={1200}
  height={600}
  format="webp"
  quality={80}
/>
```

### Partial Hydration

```astro
<!-- Load immediately -->
<CriticalComponent client:load />

<!-- Load when visible -->
<BelowFoldComponent client:visible />

<!-- Load on idle -->
<NonCriticalComponent client:idle />

<!-- Load on specific event -->
<ModalComponent client:only="react" />
```

---

**Last Updated:** 2025-11-02
**Framework Version:** Astro 4.0+
