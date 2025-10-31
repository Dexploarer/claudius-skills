# Calculator Helper Skill - Beginner Example

A simple skill that performs mathematical calculations, unit conversions, and numeric computations.

## What This Example Teaches

- Creating a computational skill
- Formatting mathematical output clearly
- Showing step-by-step working
- Using read-only tools (no file modifications needed)

## How to Use

### 1. Install the Skill

```bash
# Copy to your Claude config
cp SKILL.md ~/.claude/skills/calculator-helper.md

# Or for project-specific
cp SKILL.md your-project/.claude/skills/calculator-helper.md
```

### 2. Try It Out

```bash
cd your-project
claude

# Then ask:
"Calculate 25% of 1500"
"Convert 75 Fahrenheit to Celsius"
"What's 145 * 23?"
"If I invest $1000 at 5% for 3 years compound, what do I get?"
```

### 3. Watch It Activate

The skill automatically activates when you mention:
- "calculate"
- "compute"
- "convert"
- "what is the result"
- Any math-related question

## Example Usage

**You:**
```
I need to calculate a 15% tip on a $67.50 bill
```

**Claude (using calculator-helper skill):**
```
Calculating 15% tip on $67.50:

Tip amount: 67.50 × 0.15 = $10.13
Total bill: 67.50 + 10.13 = $77.63

Answer:
- Tip: $10.13
- Total to pay: $77.63
```

**You:**
```
Convert 100 kilometers to miles
```

**Claude (using calculator-helper skill):**
```
Converting 100 kilometers to miles:

Conversion factor: 1 km = 0.621371 miles

100 km × 0.621371 = 62.1371 miles

Answer: 100 km = 62.14 miles (approximately 62 miles)
```

## What Makes This a Good Beginner Example?

### 1. Clear, Specific Purpose
- Focused on mathematical computations
- Doesn't try to do file operations or code modifications
- Easy to understand and test

### 2. Read-Only Operation
```yaml
allowed-tools: [Read]
```
- Only needs Read tool (for context if needed)
- Can't modify files or run commands
- Very safe to use

### 3. Multiple Use Cases
- Arithmetic calculations
- Unit conversions
- Financial calculations
- Percentage calculations
- Scientific computations

### 4. Shows Working
- Displays step-by-step calculations
- Explains formulas used
- Makes results verifiable

## Customization Ideas

### Add Business-Specific Calculations
```markdown
## Company-Specific Formulas

**Gross Margin:**
(Revenue - COGS) / Revenue × 100

**Customer Lifetime Value:**
Average Order Value × Purchase Frequency × Customer Lifespan
```

### Add Domain-Specific Conversions
```markdown
## Printing Industry Conversions

- 1 point = 1/72 inch
- 1 pica = 12 points = 1/6 inch
- Letter size = 8.5 × 11 inches = 612 × 792 points
```

### Support Your Local Units
```markdown
## Australian Measurements

- 1 cup = 250ml (vs 236.588ml in US)
- 1 tablespoon = 20ml (vs 15ml in US)
- Metric system preferred
```

## Common Issues

### Skill doesn't activate?

**Check:** Description needs calculation trigger words
```yaml
# ❌ Too vague
description: Does math

# ✅ Specific with triggers
description: Performs calculations. Use when user asks to "calculate", "compute", or needs math help
```

### Results seem imprecise?

**Fix:** Specify rounding rules in the skill:
```markdown
## Rounding Rules

- Money: 2 decimal places
- Percentages: 2 decimal places
- Scientific: 4 significant figures
- Measurements: 2 decimal places
```

### Need more conversion types?

**Add:** Expand the conversion reference section:
```markdown
## Data/Digital Conversions

- 1 KB = 1,024 bytes
- 1 MB = 1,024 KB
- 1 GB = 1,024 MB
```

## Tips for Use

### For Simple Calculations
Just ask naturally:
- "What's 15% of 200?"
- "Convert 50 miles to km"
- "Calculate 25 * 18"

### For Complex Problems
Provide all details:
- "Calculate compound interest on $5000 at 6% annually for 3 years"
- "Scale a recipe from 4 to 9 servings if it needs 2.5 cups flour"

### For Conversions
Be specific about units:
- "Convert 100 km to miles" (not just "convert 100")
- "What's 75°F in Celsius?" (specify temperature)

## Learning Opportunities

### Understand Activation
This skill teaches how descriptions trigger activation:
- Specific keywords ("calculate", "compute")
- Natural language patterns ("what is the result of")
- Context clues (numbers with math operators)

### See Tool Restrictions
With only `[Read]` tool:
- Can read files for context
- Can't modify anything
- Very safe and focused

### Practice Clear Output
Learn to format results:
- Show formulas
- Display working
- Provide clear final answers
- Include units

## Next Steps

### Extend This Skill
- Add statistical calculations (mean, median, mode)
- Support matrix operations
- Add probability calculations
- Include geometry formulas

### Create Related Skills
- `unit-converter` - Focused only on conversions
- `financial-calculator` - Business-specific calculations
- `recipe-scaler` - Cooking-specific math

### Combine With Other Skills
- Use with `comment-generator` to document calculation code
- Pair with code review for validating numeric logic
- Integrate with data analysis workflows

## Files

- `SKILL.md` - The skill file (copy this to `.claude/skills/`)
- `README.md` - This documentation

## Related Examples

- **comment-generator** - Another read-only, focused skill
- **todo-finder** - Another analysis-focused skill
- See intermediate examples for domain-specific calculators
