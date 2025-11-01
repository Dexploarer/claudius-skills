# Tutorial: Creating Your First Skill

Learn how to create a simple, useful skill from scratch.

## What You'll Build

A skill that automatically adds TODO comments to your code when you describe what needs to be done.

## Prerequisites

- Claude Code installed
- Basic understanding of markdown
- A test project to try it in

## Step 1: Create the Skill File

Create a new file in your project:

```bash
mkdir -p .claude/skills
touch .claude/skills/todo-adder.md
```

## Step 2: Add the YAML Frontmatter

Open `todo-adder.md` and add:

```yaml
---
name: todo-adder
description: Adds TODO comments to code when user describes what needs to be done later
allowed-tools: [Edit, Read, Write]
---
```

**What this does:**
- `name`: Unique identifier for your skill
- `description`: Tells Claude when to use this skill (be specific!)
- `allowed-tools`: Limits what the skill can do (optional)

## Step 3: Write the Instructions

After the frontmatter, add:

```markdown
# TODO Comment Adder

Helps users quickly add TODO comments to their code.

## When to Activate

- "add a TODO to remind me to..."
- "leave a TODO comment for..."
- "mark this for later..."
- "remind me to come back and..."

## Process

1. **Identify the location**:
   - If user mentions specific file, use that
   - If in context of code discussion, use current file
   - Ask if unclear

2. **Format the TODO**:
   - Use language-appropriate comment syntax
   - Include date (optional)
   - Include description from user
   - Add context if needed

3. **Insert the TODO**:
   - Place at the logical location
   - Use proper indentation
   - Don't break existing code

## TODO Format Examples

**JavaScript/TypeScript:**
```javascript
// TODO: Add error handling for API failures
```

**Python:**
```python
# TODO: Optimize this query - currently N+1
```

**HTML:**
```html
<!-- TODO: Add accessibility attributes -->
```

## Best Practices

- Keep TODO comments concise but clear
- Include WHY something is needed
- Add priority if mentioned (TODO(P1):)
- Suggest creating issue for complex TODOs
```

## Step 4: Test Your Skill

1. Save the file
2. Start Claude Code in your project
3. Try it out:

```
"add a TODO to remind me to add error handling in app.js"
```

Claude should:
1. Recognize your skill should activate
2. Read app.js
3. Add a properly formatted TODO comment
4. Show you the change

## Step 5: Refine and Improve

Based on testing, you might:

- Adjust the description for better matching
- Add more trigger phrases
- Improve the formatting rules
- Add support for more languages

## Tips for Success

1. **Be specific in the description** - "Adds TODO comments" is better than "helps with TODOs"
2. **Test with variations** - Try different phrasings
3. **Start simple** - Don't overcomplicate the first version
4. **Check the tool restrictions** - Only include tools you actually need

## Common Mistakes

❌ **Too broad description:** "Helps with code organization"
✅ **Specific description:** "Adds TODO comments to code when user describes tasks for later"

❌ **Missing trigger phrases:** Just instructions, no examples
✅ **Clear triggers:** List specific phrases that should activate it

❌ **Complex logic:** Trying to do too much
✅ **Focused purpose:** One skill, one job

## Next Steps

Now that you've created your first skill:

1. Create more skills for your workflow
2. Try adding [slash commands](./your-first-command.md)
3. Explore [subagents](./creating-a-subagent.md)
4. Share your skill with the community!

## Full Example

Here's the complete `todo-adder.md`:

```markdown
---
name: todo-adder
description: Adds TODO comments to code when user describes what needs to be done later
allowed-tools: [Edit, Read, Write]
---

# TODO Comment Adder

Helps users quickly add TODO comments to their code.

## When to Activate
- "add a TODO to remind me to..."
- "leave a TODO comment for..."
- "mark this for later..."

## Process
1. Identify the location (file and line)
2. Format TODO with proper comment syntax
3. Insert at appropriate location
4. Confirm with user

## Examples

JavaScript:
```javascript
// TODO: Add validation
```

Python:
```python
# TODO: Optimize performance
```
```

## Resources

- [Skill Template](../../../templates/skill-template.md) - Blank template
- [More Examples](../simple-skills/) - See other simple skills
- [Claude Code Docs](https://docs.claude.com/claude-code/skills) - Official docs

Happy skill creating! 🎉
