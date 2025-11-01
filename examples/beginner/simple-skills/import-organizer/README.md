# Import Organizer Skill

Automatically organizes and sorts import/require statements in your code files.

## What It Does

- Sorts imports alphabetically
- Groups imports by source (external, internal, types)
- Removes duplicate imports
- Follows language-specific conventions
- Preserves import comments

## Installation

```bash
cp examples/beginner/simple-skills/import-organizer/SKILL.md \
   .claude/skills/import-organizer.md
```

## Usage

```
"organize imports in App.tsx"
"sort the imports in this file"
"clean up import statements"
```

## Supported Languages

- JavaScript/TypeScript
- Python
- Java
- Go
- Rust

## Example

**Before:**
```javascript
import { utils } from './utils'
import React from 'react'
import axios from 'axios'
import React from 'react'  // duplicate
import { Button } from './components/Button'
```

**After:**
```javascript
import axios from 'axios'
import React from 'react'

import { Button } from './components/Button'
import { utils } from './utils'
```
