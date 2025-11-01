# Getting Started with Productivity Skills

**Welcome!** This guide will help you install and start using productivity skills for Claude Code within 15 minutes.

---

## Prerequisites

- ✅ Claude Code installed (CLI or desktop app)
- ✅ Basic familiarity with Claude Code
- ✅ 15 minutes of time

**New to Claude Code?** See [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/)

---

## Step 1: Choose Your Kit (2 minutes)

**Two options:**

### Option A: Starter Kit (Recommended for most)
**Best for:**
- Individuals
- Personal productivity
- Everyday tasks
- Learning the basics

**Includes:** 5 skills, 12 commands, 4 subagents

### Option B: Intermediate Kit
**Best for:**
- Team leaders
- Project managers
- Business owners
- Advanced users

**Includes:** 10 skills, 15 commands, 6 subagents

**Not sure?** Start with Starter Kit. You can always upgrade later.

---

## Step 2: Install (3 minutes)

### For Starter Kit:

```bash
# Navigate to where you cloned the repo
cd /path/to/claudius-skills

# Copy to your home directory (applies to all projects)
cp -r productivity-skills/starter-kit/.claude ~/

# OR copy to specific project
cp -r productivity-skills/starter-kit/.claude /path/to/your/project/
```

### For Intermediate Kit:

```bash
cp -r productivity-skills/intermediate-kit/.claude ~/
```

### Verify Installation:

```bash
# Check that files are there
ls ~/.claude/skills/
# Should see: meeting-notes-formatter.md, email-composer.md, etc.

ls ~/.claude/commands/
# Should see: schedule.md, prioritize.md, etc.

ls ~/.claude/subagents/
# Should see: content-writer.md, project-coordinator.md, etc.
```

✅ **Installation complete!**

---

## Step 3: Test It Out (5 minutes)

Let's verify everything works.

### Open Claude Code:

```bash
cd ~  # Or any directory
claude code
```

### Test a skill (auto-triggers):

Type in Claude Code:
```
Format these meeting notes:

met with sarah today discussed Q4
need to hire 2 people by december
budget is approved
```

**Expected:** Meeting Notes Formatter skill activates and creates formatted output.

### Test a command (manual):

Type:
```
/weekly-review
```

**Expected:** Claude guides you through a weekly review process.

### Test a subagent:

Type:
```
I need help from the content-writer to draft a professional email
```

**Expected:** The content-writer subagent responds with expertise.

✅ **Everything working!**

---

## Step 4: First Real Use (5 minutes)

Let's solve a real problem.

### Scenario 1: Clean Up Your Messy Meeting Notes

1. Find some messy meeting notes (from email, Slack, handwritten)
2. Type in Claude Code:
   ```
   Format my meeting notes:

   [paste your messy notes]
   ```
3. Get professional, actionable notes back
4. Copy to your note system (Notion, Obsidian, etc.)

**Time saved:** 10-15 minutes

---

### Scenario 2: Write a Tricky Email

1. Think of an email you've been putting off
2. Type:
   ```
   Write an email to [person] about [topic]
   ```
3. Get a professional draft with subject line
4. Personalize and send

**Time saved:** 15-20 minutes

---

### Scenario 3: Plan Your Week

1. Type:
   ```
   /weekly-review
   ```
2. Answer the prompts
3. Get comprehensive review + plan for next week
4. Save the output

**Time saved:** Creates structure you didn't have before

---

## Step 5: Build Your Habit (Ongoing)

### This Week:

**Daily (5-10 min):**
- [ ] Use `/schedule` or `/prioritize` to start your day
- [ ] Use email-composer for important emails
- [ ] Use meeting-notes-formatter after meetings

**Weekly (30 min):**
- [ ] Do `/weekly-review` every Sunday evening
- [ ] Reflect on what worked, what didn't
- [ ] Plan priorities for next week

**As-needed:**
- [ ] Use task-breakdown for complex projects
- [ ] Use brainstorm-facilitator for idea generation
- [ ] Call on subagents for expert help

### Next Week:

- [ ] Review which tools you actually used
- [ ] Double down on what's working
- [ ] Explore 1-2 new commands/skills
- [ ] Adjust system to your workflow

### This Month:

- [ ] Complete 4 weekly reviews (prove the habit)
- [ ] Try all 5 core skills at least once
- [ ] Customize 1-2 tools to your needs
- [ ] Measure impact (are you more productive?)

---

## Quick Reference

### 🎯 When to Use What

| Need | Tool | How |
|------|------|-----|
| Clean up notes | meeting-notes-formatter | Paste messy notes |
| Write email | email-composer | "Write email to..." |
| Plan project | task-breakdown | "Break down [project]" |
| Generate ideas | brainstorm-facilitator | "Brainstorm ideas for..." |
| Create report | report-generator | "Create report about..." |
| Weekly planning | `/weekly-review` | Run Sunday night |
| Daily planning | `/schedule` or `/prioritize` | Run each morning |
| Tough decision | `/decision` | When stuck on choices |
| Set goals | `/goal-setting` | For important goals |
| Write anything | content-writer subagent | Complex writing projects |

---

## Tips for Success

### DO:

✅ **Start small** - Use 3-5 tools consistently before adding more
✅ **Be specific** - "Write email to my manager about Q4 goals" > "Write email"
✅ **Build habits** - Weekly review is the cornerstone habit
✅ **Customize** - Adjust tools to match your workflow
✅ **Measure** - Track if you're actually more productive
✅ **Iterate** - Refine your system weekly

### DON'T:

❌ **Collect tools** - Use what works, ignore the rest
❌ **Perfect the system** - Good enough and consistent > perfect and unused
❌ **Skip execution** - Tools help planning, but you must do the work
❌ **Give up too soon** - Takes 2-3 weeks to feel natural
❌ **Use AI for everything** - Some things are better done by humans

---

## Common Issues & Solutions

### "Skills aren't triggering automatically"

**Solution:**
- Try different trigger phrases (listed in skill files)
- Be more explicit: "Use the email-composer skill to..."
- Check that skills are in `~/.claude/skills/` directory

### "Commands aren't working"

**Solution:**
- Make sure commands are in `~/.claude/commands/` directory
- Restart Claude Code if you just installed
- Try typing full command: `/weekly-review`

### "I don't know which tool to use"

**Solution:**
- Start with `/weekly-review` - it's the foundation
- Use email-composer and meeting-notes-formatter daily (high ROI)
- Add more tools as you master the basics

### "This feels like too much overhead"

**Solution:**
- Just use 3 tools for 2 weeks: weekly-review, email-composer, task-breakdown
- The 30-60 min/week investment saves hours of wasted effort
- Give it time - feels like work at first, becomes automatic

### "I'm not seeing results"

**Solution:**
- Are you using weekly-review consistently?
- Are you executing on plans you create?
- Are you measuring results? (tasks completed, goals achieved)
- Track metrics for 4 weeks before judging

---

## Next Steps

### Immediate (Today):
- [ ] Test that installation worked (see Step 3)
- [ ] Use one skill to solve a real problem (see Step 4)
- [ ] Schedule your first weekly review (Sunday evening)

### This Week:
- [ ] Use 3-5 tools daily
- [ ] Complete first weekly review
- [ ] Explore the [starter kit README](../../starter-kit/README.md)

### This Month:
- [ ] Follow the [Weekly Productivity System Tutorial](../../examples/beginner/weekly-productivity-system.md)
- [ ] Establish consistent habits
- [ ] Measure productivity improvements

### This Quarter:
- [ ] Master the starter kit
- [ ] Customize tools to your workflow
- [ ] Consider upgrading to intermediate kit (if needed)
- [ ] Share your success with others

---

## Learning Resources

### In This Repository:

**Documentation:**
- [Starter Kit README](../../starter-kit/README.md) - Full starter kit guide
- [Main README](../../README.md) - Overview of all kits
- [Best Practices](./best-practices.md) - Tips for effective use

**Tutorials:**
- [Weekly Productivity System](../../examples/beginner/weekly-productivity-system.md) - Comprehensive tutorial
- More tutorials coming soon!

**Templates:**
- [Template Library](../../templates/) - Reusable templates

### External Resources:

**Books:**
- *Getting Things Done* - David Allen (GTD method)
- *Atomic Habits* - James Clear (Building habits)
- *Deep Work* - Cal Newport (Focus and productivity)
- *Essentialism* - Greg McKeown (Doing less, better)

**Methodologies:**
- GTD (Getting Things Done)
- Pomodoro Technique
- Time Blocking
- Eisenhower Matrix

**Claude Code Docs:**
- [Official Documentation](https://docs.claude.com/en/docs/claude-code/)
- [Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Commands Guide](https://docs.claude.com/en/docs/claude-code/commands)

---

## Getting Help

**Have questions?**
- Check the [FAQ](./faq.md)
- Review skill documentation in `~/.claude/skills/`
- Open an issue in the repository

**Want to contribute?**
- Share your custom skills
- Submit improvements
- Write tutorials
- Help other users

---

## Success Stories

> "I installed this on Sunday, did my first weekly review, and already feel more in control. Can't wait to see where I am in a month." - First-time user

> "The email composer alone is worth it. I used to spend 30 minutes agonizing over every important email." - Sarah, Consultant

> "This is the system I've been looking for. Simple enough to stick with, powerful enough to make a real difference." - Mike, Product Manager

---

**You're ready to go!** Start with `/weekly-review` and build from there.

Remember: The best productivity system is the one you actually use. Start simple, be consistent, and iterate.

Good luck! 🚀

---

**Questions?** Open an issue or contribute to the docs!
