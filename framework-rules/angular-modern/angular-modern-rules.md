# Angular Modern (17+) Rules

> Best practices for Angular 17+ with standalone components and signals

---

## 🎯 Overview

Angular 17+ introduces standalone components, signals for reactivity, and improved developer experience.

---

## 📁 Project Structure

```
angular-app/
├── src/
│   ├── app/
│   │   ├── components/      # Standalone components
│   │   ├── services/        # Injectable services
│   │   ├── guards/          # Route guards
│   │   ├── app.component.ts # Root component
│   │   ├── app.config.ts    # App configuration
│   │   └── app.routes.ts    # Routes
│   ├── assets/              # Static assets
│   └── main.ts              # Bootstrap
└── angular.json             # Angular configuration
```

---

## 🔧 Core Patterns

### 1. Standalone Component with Signals

```typescript
import { Component, signal, computed } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-counter',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div>
      <button (click)="increment()">Count: {{ count() }}</button>
      <p>Doubled: {{ doubled() }}</p>
    </div>
  `
})
export class CounterComponent {
  count = signal(0);
  doubled = computed(() => this.count() * 2);

  increment() {
    this.count.update(value => value + 1);
  }
}
```

### 2. Service with Dependency Injection

```typescript
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class UserService {
  private http = inject(HttpClient);

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>('/api/users');
  }

  getUser(id: string): Observable<User> {
    return this.http.get<User>(`/api/users/${id}`);
  }
}
```

### 3. Routes Configuration

```typescript
// app.routes.ts
import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  {
    path: 'users/:id',
    component: UserDetailComponent,
    canActivate: [authGuard]
  },
  {
    path: 'admin',
    loadComponent: () => import('./admin/admin.component')
      .then(m => m.AdminComponent)
  }
];
```

### 4. Reactive Forms

```typescript
import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <form [formGroup]="loginForm" (ngSubmit)="onSubmit()">
      <input formControlName="email" type="email" />
      <input formControlName="password" type="password" />
      <button type="submit">Login</button>
    </form>
  `
})
export class LoginComponent {
  private fb = inject(FormBuilder);

  loginForm = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(8)]]
  });

  onSubmit() {
    if (this.loginForm.valid) {
      console.log(this.loginForm.value);
    }
  }
}
```

---

## 🔒 Best Practices

### 1. Use Standalone Components
- Simpler module structure
- Better tree-shaking
- Lazy loading support

### 2. Signals for State
- Use `signal()` for reactive state
- Use `computed()` for derived values
- Better performance than RxJS for simple state

### 3. Inject Function
- Use `inject()` in constructors
- Cleaner dependency injection
- Better type inference

---

**Last Updated:** 2025-11-02
**Framework Version:** Angular 17+
