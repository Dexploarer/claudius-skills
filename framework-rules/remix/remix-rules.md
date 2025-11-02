# Remix Framework Rules

> Best practices for Remix - full stack web framework

---

## 🎯 Overview

Remix is a full-stack React framework focused on web fundamentals, progressive enhancement, and excellent user experience.

---

## 📁 Project Structure

```
remix-app/
├── app/
│   ├── routes/              # File-based routing
│   │   ├── _index.tsx      # Index route
│   │   ├── about.tsx       # /about
│   │   ├── blog.$slug.tsx  # Dynamic route
│   │   └── api.posts.ts    # API route
│   ├── components/         # React components
│   ├── utils/             # Utilities
│   ├── models/            # Data models
│   ├── styles/            # CSS files
│   ├── entry.client.tsx   # Client entry
│   ├── entry.server.tsx   # Server entry
│   └── root.tsx           # Root component
├── public/                # Static files
└── remix.config.js        # Configuration
```

---

## 🔧 Core Patterns

### 1. Loader (Data Fetching)

```typescript
// app/routes/posts._index.tsx
import { json } from '@remix-run/node';
import { useLoaderData } from '@remix-run/react';
import type { LoaderFunctionArgs } from '@remix-run/node';

export async function loader({ request }: LoaderFunctionArgs) {
  const posts = await db.post.findMany();

  return json({ posts });
}

export default function PostsIndex() {
  const { posts } = useLoaderData<typeof loader>();

  return (
    <div>
      <h1>Posts</h1>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.excerpt}</p>
        </article>
      ))}
    </div>
  );
}
```

### 2. Actions (Mutations)

```typescript
// app/routes/posts.new.tsx
import { json, redirect } from '@remix-run/node';
import { Form, useActionData } from '@remix-run/react';
import type { ActionFunctionArgs } from '@remix-run/node';

export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const title = formData.get('title');
  const content = formData.get('content');

  const errors: Record<string, string> = {};

  if (!title) errors.title = 'Title is required';
  if (!content) errors.content = 'Content is required';

  if (Object.keys(errors).length) {
    return json({ errors }, { status: 400 });
  }

  const post = await db.post.create({
    data: { title, content }
  });

  return redirect(`/posts/${post.id}`);
}

export default function NewPost() {
  const actionData = useActionData<typeof action>();

  return (
    <Form method="post">
      <div>
        <label htmlFor="title">Title</label>
        <input type="text" name="title" id="title" />
        {actionData?.errors?.title && (
          <p className="error">{actionData.errors.title}</p>
        )}
      </div>

      <div>
        <label htmlFor="content">Content</label>
        <textarea name="content" id="content" />
        {actionData?.errors?.content && (
          <p className="error">{actionData.errors.content}</p>
        )}
      </div>

      <button type="submit">Create Post</button>
    </Form>
  );
}
```

### 3. Nested Routes & Layouts

```typescript
// app/routes/dashboard.tsx (Layout)
import { Outlet } from '@remix-run/react';

export default function DashboardLayout() {
  return (
    <div className="dashboard">
      <nav>
        <a href="/dashboard">Overview</a>
        <a href="/dashboard/settings">Settings</a>
      </nav>
      <main>
        <Outlet /> {/* Child routes render here */}
      </main>
    </div>
  );
}

// app/routes/dashboard._index.tsx
export default function DashboardIndex() {
  return <h1>Dashboard Overview</h1>;
}

// app/routes/dashboard.settings.tsx
export default function DashboardSettings() {
  return <h1>Settings</h1>;
}
```

---

## 🔒 Best Practices

### 1. Progressive Enhancement
- Forms work without JavaScript
- Use `<Form>` component, not `<form>`
- Handle both POST and GET

### 2. Error Handling

```typescript
// app/routes/posts.$id.tsx
import { json } from '@remix-run/node';
import { useRouteError, isRouteErrorResponse } from '@remix-run/react';

export async function loader({ params }: LoaderFunctionArgs) {
  const post = await db.post.findUnique({ where: { id: params.id } });

  if (!post) {
    throw new Response('Not Found', { status: 404 });
  }

  return json({ post });
}

export function ErrorBoundary() {
  const error = useRouteError();

  if (isRouteErrorResponse(error)) {
    return (
      <div>
        <h1>{error.status}</h1>
        <p>{error.statusText}</p>
      </div>
    );
  }

  return <div>Something went wrong</div>;
}
```

### 3. Meta Tags

```typescript
import type { MetaFunction } from '@remix-run/node';

export const meta: MetaFunction<typeof loader> = ({ data }) => {
  return [
    { title: data.post.title },
    { name: 'description', content: data.post.excerpt },
    { property: 'og:title', content: data.post.title },
  ];
};
```

---

**Last Updated:** 2025-11-02
**Framework Version:** Remix 2.0+
