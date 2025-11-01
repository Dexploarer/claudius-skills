# Vue Component Generator

Automatically generates Vue 3 components with Composition API, TypeScript, and best practices.

## What It Does

This skill creates production-ready Vue 3 components with:
- Composition API with `<script setup>`
- TypeScript support
- Props and emits typing
- Reactive state management
- Scoped CSS/SCSS
- Component documentation

## Installation

```bash
cp examples/intermediate/framework-skills/vue-component-generator/SKILL.md \
   .claude/skills/vue-component-generator.md
```

## Usage

Simply ask Claude to create Vue components naturally:

```
"create a Vue component for a user profile card"
"generate a data table component with sorting in Vue"
"build a modal component with Vue 3"
```

## Example Output

When you ask: *"create a Button component in Vue with loading state"*

Claude will generate:

**Button.vue:**
```vue
<template>
  <button
    :class="buttonClass"
    :disabled="disabled || loading"
    @click="handleClick"
  >
    <span v-if="loading" class="spinner"></span>
    <slot v-else></slot>
  </button>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  variant?: 'primary' | 'secondary' | 'danger'
  loading?: boolean
  disabled?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  loading: false,
  disabled: false
})

const emit = defineEmits<{
  click: []
}>()

const buttonClass = computed(() => ({
  'btn': true,
  [`btn-${props.variant}`]: true,
  'btn-loading': props.loading
}))

const handleClick = () => {
  if (!props.loading && !props.disabled) {
    emit('click')
  }
}
</script>

<style scoped>
.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary { background-color: #007bff; color: white; }
.btn-secondary { background-color: #6c757d; color: white; }
.btn-danger { background-color: #dc3545; color: white; }

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.spinner {
  display: inline-block;
  width: 1rem;
  height: 1rem;
  border: 2px solid rgba(255,255,255,0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
```

## Features

- ✅ Vue 3 Composition API
- ✅ TypeScript with proper typing
- ✅ Props and emits definitions
- ✅ Reactive state with `ref` and `computed`
- ✅ Scoped styles
- ✅ Accessibility attributes
- ✅ Event handling
- ✅ Slot support

## Use Cases

- Creating new UI components
- Building form elements
- Designing layout components
- Implementing data visualization
- Creating interactive widgets

## Best Practices Included

- Component naming conventions (PascalCase)
- Props validation and defaults
- Type-safe emits
- Scoped CSS to prevent style leaks
- Semantic HTML
- Accessibility considerations

## See Also

- [React Component Generator](../react-component-generator/) - React equivalent
- [Intermediate Kit](../../../../intermediate-kit/) - Full setup with all framework skills
- [Framework Skills Overview](../README.md) - All framework skills
