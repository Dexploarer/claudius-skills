# SvelteKit Framework Rules

> Best practices and patterns for SvelteKit development with Claude Code

---

## 🎯 Overview

These rules guide Claude Code when working with SvelteKit projects, ensuring best practices for routing, data loading, forms, and performance optimization.

---

## 📁 Project Structure

```
sveltekit-app/
├── src/
│   ├── routes/                 # File-based routing
│   │   ├── +page.svelte       # Page component
│   │   ├── +page.ts           # Page load function
│   │   ├── +page.server.ts    # Server-side load
│   │   ├── +layout.svelte     # Layout component
│   │   ├── +layout.ts         # Layout load
│   │   ├── +server.ts         # API endpoint
│   │   └── +error.svelte      # Error page
│   ├── lib/                   # Shared code
│   │   ├── components/        # Reusable components
│   │   ├── stores/           # Svelte stores
│   │   ├── utils/            # Utilities
│   │   └── server/           # Server-only code
│   ├── app.html              # HTML template
│   └── hooks.server.ts       # Server hooks
├── static/                    # Static assets
├── tests/                     # Tests
└── svelte.config.js          # SvelteKit config
```

---

## 🔧 Core Patterns

### 1. Page with Data Loading

```typescript
// src/routes/posts/+page.ts
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch, params }) => {
  const response = await fetch('/api/posts');
  const posts = await response.json();

  return {
    posts
  };
};
```

```svelte
<!-- src/routes/posts/+page.svelte -->
<script lang="ts">
  import type { PageData } from './$types';

  export let data: PageData;
</script>

<h1>Posts</h1>

{#each data.posts as post}
  <article>
    <h2>{post.title}</h2>
    <p>{post.excerpt}</p>
  </article>
{/each}
```

### 2. Server-Side Data Loading

```typescript
// src/routes/posts/[id]/+page.server.ts
import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ params, locals }) => {
  const post = await locals.db.getPost(params.id);

  if (!post) {
    throw error(404, 'Post not found');
  }

  return {
    post
  };
};
```

### 3. Form Actions

```typescript
// src/routes/login/+page.server.ts
import type { Actions } from './$types';
import { fail, redirect } from '@sveltejs/kit';

export const actions: Actions = {
  default: async ({ request, cookies }) => {
    const data = await request.formData();
    const email = data.get('email');
    const password = data.get('password');

    if (!email || !password) {
      return fail(400, { email, missing: true });
    }

    const user = await authenticateUser(email, password);

    if (!user) {
      return fail(400, { email, incorrect: true });
    }

    cookies.set('session', user.sessionId, {
      path: '/',
      httpOnly: true,
      sameSite: 'strict',
      secure: true,
      maxAge: 60 * 60 * 24 * 7 // 1 week
    });

    throw redirect(303, '/dashboard');
  }
};
```

### 4. API Endpoints

```typescript
// src/routes/api/posts/+server.ts
import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

export const GET: RequestHandler = async ({ url, locals }) => {
  const limit = Number(url.searchParams.get('limit') ?? '10');
  const posts = await locals.db.getPosts({ limit });

  return json(posts);
};

export const POST: RequestHandler = async ({ request, locals }) => {
  const post = await request.json();
  const created = await locals.db.createPost(post);

  return json(created, { status: 201 });
};
```

### 5. Layouts with Loading

```typescript
// src/routes/+layout.server.ts
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {
  return {
    user: locals.user
  };
};
```

```svelte
<!-- src/routes/+layout.svelte -->
<script lang="ts">
  import type { LayoutData } from './$types';

  export let data: LayoutData;
</script>

<nav>
  {#if data.user}
    <span>Welcome, {data.user.name}</span>
  {:else}
    <a href="/login">Login</a>
  {/if}
</nav>

<slot />
```

---

## 🎨 Component Patterns

### Reactive Component

```svelte
<script lang="ts">
  let count = 0;

  // Reactive declaration
  $: doubled = count * 2;

  // Reactive statement
  $: if (count > 10) {
    console.log('Count is high!');
  }

  function increment() {
    count += 1;
  }
</script>

<button on:click={increment}>
  Count: {count} (doubled: {doubled})
</button>
```

### Component with Props and Events

```svelte
<script lang="ts">
  import { createEventDispatcher } from 'svelte';

  export let title: string;
  export let items: string[] = [];

  const dispatch = createEventDispatcher<{
    select: string;
  }>();

  function handleSelect(item: string) {
    dispatch('select', item);
  }
</script>

<h2>{title}</h2>

<ul>
  {#each items as item}
    <li>
      <button on:click={() => handleSelect(item)}>
        {item}
      </button>
    </li>
  {/each}
</ul>
```

### Store Usage

```typescript
// src/lib/stores/counter.ts
import { writable } from 'svelte/store';

export const count = writable(0);

export function increment() {
  count.update(n => n + 1);
}

export function decrement() {
  count.update(n => n - 1);
}
```

```svelte
<!-- Component using store -->
<script lang="ts">
  import { count, increment, decrement } from '$lib/stores/counter';
</script>

<button on:click={decrement}>-</button>
<span>{$count}</span>
<button on:click={increment}>+</button>
```

---

## 🔒 Best Practices

### 1. Use TypeScript
- Enable strict mode
- Use generated types from `$types`
- Define component prop types

### 2. Server vs Client Code
- Use `+page.server.ts` for server-only data
- Use `+page.ts` for universal code
- Keep secrets in server files only

### 3. Forms
- Use progressive enhancement
- Handle both JS and non-JS scenarios
- Validate on both client and server

### 4. Performance
- Use `{#key}` for proper reactivity
- Lazy load heavy components
- Optimize images with `@sveltejs/enhanced-img`

### 5. Security
- Validate all form inputs on server
- Use CSRF protection for mutations
- Set secure cookie options

---

## ⚡ Performance Optimization

### Image Optimization

```svelte
<script>
  import { Image } from '@sveltejs/enhanced-img';
  import heroImage from '$lib/images/hero.jpg';
</script>

<Image src={heroImage} alt="Hero" />
```

### Code Splitting

```svelte
<script>
  import { browser } from '$app/environment';

  let HeavyComponent;

  if (browser) {
    import('$lib/components/HeavyComponent.svelte')
      .then(module => HeavyComponent = module.default);
  }
</script>

{#if HeavyComponent}
  <svelte:component this={HeavyComponent} />
{/if}
```

---

## 🧪 Testing

```typescript
// tests/routes/home.test.ts
import { expect, test } from '@playwright/test';

test('home page loads', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('h1')).toHaveText('Welcome');
});
```

---

**Last Updated:** 2025-11-02
**Framework Version:** SvelteKit 2.0+
