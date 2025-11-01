# Productivity Skills - Starter Kit

> **Transform everyday tasks, creative work, and personal management with AI-powered productivity skills**

This starter kit provides foundational productivity, creativity, and management capabilities for Claude Code - designed for anyone looking to be more organized, creative, and effective in their daily work and life.

---

## 📦 What's Included

### ✨ 5 Core Skills (Auto-triggered)

1. **📝 Meeting Notes Formatter**
   - Triggers: "format my meeting notes", "organize these notes"
   - Transforms raw meeting notes into professional, actionable documents
   - Extracts action items, decisions, and next steps

2. **✉️ Email Composer**
   - Triggers: "write an email", "compose email to", "draft email about"
   - Creates professional emails with appropriate tone and structure
   - Handles requests, follow-ups, thank yous, and more

3. **📋 Task Breakdown**
   - Triggers: "break down this task", "plan this project", "how to approach"
   - Breaks complex goals into manageable, actionable subtasks
   - Provides timelines, priorities, and dependencies

4. **💡 Brainstorm Facilitator**
   - Triggers: "brainstorm ideas for", "help me ideate", "creative ideas"
   - Facilitates structured brainstorming using proven techniques
   - Generates, organizes, and prioritizes ideas

5. **📊 Report Generator**
   - Triggers: "create a report", "generate report for", "write a report on"
   - Creates professional reports from raw data or topics
   - Includes executive summaries, analysis, and recommendations

### ⚡ 12 Slash Commands (Manual workflows)

| Command | Purpose |
|---------|---------|
| `/schedule` | Create optimized daily/weekly schedules |
| `/prioritize` | Prioritize tasks using proven frameworks |
| `/outline` | Create outlines for any content type |
| `/summarize` | Summarize long content (articles, meetings, docs) |
| `/agenda` | Create structured meeting agendas |
| `/minutes` | Format meeting notes → Triggers meeting-notes-formatter skill |
| `/weekly-review` | Guided weekly reflection and planning |
| `/goal-setting` | Create SMART goals with action plans |
| `/decision` | Make better decisions using frameworks |
| `/email` | Quick email drafting → Triggers email-composer skill |
| `/presentation` | Create presentation outlines and structures |
| `/journal` | Journaling prompts and templates |

### 🤖 4 Specialized Subagents

1. **content-writer** - Expert writing and editing for all content types
2. **project-coordinator** - Project planning, tracking, and management
3. **productivity-coach** - Time management and productivity optimization
4. **creative-consultant** - Idea generation and creative problem-solving

---

## 🚀 Quick Start

### Installation

```bash
# Copy starter kit to your project or home directory
cp -r productivity-skills/starter-kit/.claude ~/

# Or for a specific project
cp -r productivity-skills/starter-kit/.claude /path/to/your/project/
```

### Using Skills (Auto-triggered)

Simply describe what you need in natural language:

```
"Format my meeting notes from today's standup"
→ meeting-notes-formatter skill activates

"Write an email to my manager about taking time off"
→ email-composer skill activates

"Break down the task of planning a company retreat"
→ task-breakdown skill activates

"Brainstorm ideas for increasing customer engagement"
→ brainstorm-facilitator skill activates

"Create a status report for the Q3 website project"
→ report-generator skill activates
```

### Using Commands (Manual)

Type the command to trigger specific workflows:

```
/schedule week
→ Create optimized weekly schedule

/prioritize
→ Prioritize your task list using Eisenhower Matrix

/goal-setting
→ Create SMART goals with action plans

/weekly-review
→ Guided reflection and planning session

/decision
→ Use decision-making frameworks for tough choices
```

### Using Subagents (Consultants)

Call on specialized expertise:

```
"I need help from the content-writer agent to write a blog post about productivity"

"Can the project-coordinator help me plan my home renovation?"

"I'd like the productivity-coach to help me design my ideal week"

"I need the creative-consultant for a brainstorming session"
```

---

## 💡 Example Use Cases

### For Professionals

**Scenario: Weekly Planning**
```
You: /weekly-review

Claude: Let's do your weekly review!

What were your wins this week?
...
[Guided reflection and planning process]
...

Result: Comprehensive weekly review + plan for next week
```

**Scenario: Email Overwhelm**
```
You: Write an email to John following up on the proposal I sent last week

Claude: [email-composer activates]

Result: Professional follow-up email with multiple tone options
```

**Scenario: Big Project**
```
You: Break down "Launch new product" into actionable tasks

Claude: [task-breakdown activates]

Result: Comprehensive project plan with phases, tasks, timelines, and dependencies
```

### For Creatives

**Scenario: Content Creation**
```
You: I need to write a blog post about remote work productivity

Subagent: content-writer

Result: Complete outline, draft, and SEO optimization
```

**Scenario: Idea Generation**
```
You: Brainstorm ideas for my YouTube channel

Claude: [brainstorm-facilitator activates]

Result: 50+ organized, categorized content ideas with prioritization
```

### For Personal Use

**Scenario: Life Goals**
```
You: /goal-setting

Claude: What goal would you like to set?

You: I want to get healthier

Result: SMART goal with 4-month action plan, milestones, and accountability system
```

**Scenario: Tough Decision**
```
You: /decision

Claude: What decision are you facing?

You: Should I accept this job offer or stay at my current company?

Result: Decision analysis using multiple frameworks (matrix, 10-10-10, regret minimization)
```

---

## 🎯 Learning Path

### Week 1: Fundamentals
- Use `/schedule` to create your ideal week
- Try the email-composer for 3-5 emails
- Use task-breakdown on one project
- Start `/journal` practice (daily or weekly)

### Week 2: Deep Dive
- Complete your first `/weekly-review`
- Use `/prioritize` to tackle your task list
- Try `/goal-setting` for one important goal
- Experiment with brainstorm-facilitator

### Week 3: Advanced Usage
- Call on subagents for complex work:
  - content-writer for important writing
  - project-coordinator for a real project
  - productivity-coach for system design
  - creative-consultant for innovation

### Week 4: Customization
- Adjust skills to your workflow
- Create your own slash commands
- Develop personal templates
- Build your productivity system

---

## 📚 Detailed Skill Documentation

### Meeting Notes Formatter

**Best for:**
- Daily standups
- Client meetings
- Team sync meetings
- Interview notes
- Workshop sessions

**Input:** Raw, unstructured meeting notes or transcripts

**Output:** Professional formatted notes with:
- Executive summary
- Attendees and date
- Discussion points (organized by topic)
- Decisions made
- Action items (with owners and deadlines)
- Parking lot items
- Next steps

**Pro tip:** Include any dates, names, or deadlines mentioned - the skill will extract and organize them.

---

### Email Composer

**Best for:**
- Request emails (time off, resources, approvals)
- Follow-up emails (proposals, meetings)
- Thank you emails (after interviews, meetings, help)
- Introduction emails (networking, warm intros)
- Professional apologies (delays, mistakes)
- Status updates (project progress, changes)

**Tone options:**
- Formal (executives, first contact with clients)
- Professional (standard business)
- Friendly (colleagues you know well)
- Casual (internal team)
- Urgent (time-sensitive)
- Apologetic (addressing mistakes)

**Pro tip:** Specify the recipient relationship and desired tone for best results.

---

### Task Breakdown

**Best for:**
- Complex projects (product launches, events, renovations)
- Personal goals (learning new skills, fitness goals)
- Career transitions (job hunting, skill building)
- Creative projects (writing a book, starting a podcast)
- Process improvements (implementing new systems)

**Output includes:**
- Phased breakdown (with realistic timelines)
- Sequential and parallel tasks
- Time estimates per task
- Dependencies clearly marked
- Resource requirements
- Success criteria
- Risk identification

**Pro tip:** The more context you provide, the better the breakdown. Include deadlines, constraints, and resources available.

---

### Brainstorm Facilitator

**Techniques applied:**
- Mind mapping
- SCAMPER method
- Six Thinking Hats
- Reverse brainstorming
- Rapid ideation
- Priority matrices

**Best for:**
- Business challenges (increase sales, improve processes)
- Product ideas (new features, new offerings)
- Content creation (blog topics, video ideas)
- Problem-solving (creative solutions)
- Personal challenges (making friends, career pivot)

**Pro tip:** Don't self-censor during brainstorming. Wild ideas often lead to practical innovations.

---

### Report Generator

**Report types:**
- Project status reports
- Market research reports
- Quarterly business reviews
- Performance reports
- Post-mortem reports
- Research findings
- Executive summaries

**Audience options:**
- Executive level (high-level, strategic)
- Management (balanced detail)
- Technical (detailed, data-driven)
- Board/investors (results and projections)

**Pro tip:** Provide raw data and context; the skill will structure and professionalize it.

---

## 🛠️ Customization

### Adjusting Skills

Skills are defined in `.claude/skills/` as markdown files. You can:

1. **Modify trigger phrases** - Add your own preferred phrases
2. **Adjust output format** - Change templates to match your needs
3. **Add examples** - Include examples specific to your work
4. **Combine skills** - Create workflows that chain multiple skills

### Creating Custom Commands

Create new commands in `.claude/commands/`:

```markdown
# my-custom-command.md

You are a [role] helping users [purpose].

When the user uses this command:
1. [Step 1]
2. [Step 2]
3. [Deliver formatted output]

Example: [Show example]
```

### Building Your System

Combine these tools into your personal productivity system:

**Daily routine:**
1. Morning: `/journal` (5 min morning mindset)
2. Planning: `/schedule today` + `/prioritize`
3. Execution: Use skills as needed (email-composer, task-breakdown)
4. Evening: `/journal` (evening reflection)

**Weekly routine:**
1. Sunday: `/weekly-review` + `/schedule week`
2. Daily: `/prioritize` + Execute
3. Friday: Quick wins review + next week preview

---

## 🎓 Best Practices

### For Maximum Productivity

1. **Be specific** - "Write an email to my manager about Q4 goals" > "Write an email"
2. **Provide context** - Include relevant details, deadlines, constraints
3. **Iterate** - Refine outputs, don't expect perfection first try
4. **Build habits** - Use `/weekly-review` and `/journal` consistently
5. **Customize** - Adapt tools to your workflow, not vice versa

### Common Pitfalls to Avoid

1. ❌ **Tool collecting** - Using every skill vs. what you actually need
2. ❌ **Over-planning** - Planning forever, never executing
3. ❌ **Perfectionism** - Waiting for perfect plan/email/outline
4. ❌ **No follow-through** - Creating plans but not doing the work
5. ❌ **Ignoring energy** - Scheduling without considering energy levels

### Success Indicators

You're using this well if:
- ✅ You reference your weekly reviews regularly
- ✅ Meeting notes actually get used (not just filed away)
- ✅ Your emails are clearer and get better responses
- ✅ Projects don't feel overwhelming anymore
- ✅ You're making progress on personal goals
- ✅ Decisions feel less agonizing
- ✅ You have systems, not just intentions

---

## 🆘 Troubleshooting

**Skill not triggering?**
- Try different trigger phrases (listed in each skill file)
- Be more explicit: "Use the task-breakdown skill for..."

**Output not quite right?**
- Provide more context and details
- Specify desired format or tone
- Give an example of what you want

**Overwhelmed by options?**
- Start with just 3 tools: email-composer, task-breakdown, /weekly-review
- Add more as you master the basics
- Quality over quantity

**Not seeing results?**
- Are you executing on the plans you create?
- Review your weekly reviews - do you see patterns?
- Are you being honest in your reflections?
- Remember: Tools enable action, but you must take action

---

## 📊 Measuring Impact

Track these metrics to see if productivity is actually improving:

**Work metrics:**
- Time from task assignment to completion
- Number of projects completed vs. started
- Meeting effectiveness (action items completed)
- Email response time and clarity

**Personal metrics:**
- Goals achieved (quarterly, annually)
- Stress levels (subjective, 1-10 scale)
- Work-life balance rating
- Energy and focus levels

**System metrics:**
- Weekly review completion rate
- Task completion rate (completed / planned)
- Decision satisfaction (happy with choices made)
- Habit consistency (streaks maintained)

---

## 🚀 Next Steps

### Immediate (This week):
- [ ] Install starter kit
- [ ] Try each of the 5 skills at least once
- [ ] Complete your first `/weekly-review`
- [ ] Set up one `/goal-setting` session

### Short-term (This month):
- [ ] Establish weekly review habit
- [ ] Create your ideal week schedule
- [ ] Call on subagents for complex work
- [ ] Customize 1-2 skills or commands to your needs

### Long-term (This quarter):
- [ ] Develop personal productivity system
- [ ] Measure impact (are you achieving more with less stress?)
- [ ] Explore intermediate kit (advanced management skills)
- [ ] Share what works with others

---

## 🆙 Upgrading to Intermediate Kit

Ready for more advanced productivity and management skills?

The **Intermediate Kit** includes:
- 10 advanced management skills
- 15 professional workflow commands
- 6 specialized subagents
- Team coordination and leadership tools
- Strategic planning frameworks
- Advanced project management

See `/productivity-skills/intermediate-kit/README.md` for details.

---

## 💬 Tips from Users

> "The weekly review changed my life. I actually accomplish my goals now instead of just thinking about them." - Sarah, Product Manager

> "Task breakdown makes overwhelming projects manageable. I used it to plan my entire home renovation." - Mike, Homeowner

> "Email composer saves me 30 minutes per day. I used to agonize over every email." - Lisa, Consultant

> "Brainstorm facilitator helped me generate 6 months of content ideas in 20 minutes." - Alex, Content Creator

---

## 📖 Additional Resources

### In this repository:
- `/templates/` - Reusable templates for common tasks
- `/examples/beginner/` - Step-by-step tutorials
- `/resources/guides/` - Best practices and guides

### External resources:
- Getting Things Done (GTD) - David Allen
- Atomic Habits - James Clear
- Deep Work - Cal Newport
- The ONE Thing - Gary Keller
- Essentialism - Greg McKeown

---

## ❤️ Contributing

Have ideas for new skills or improvements?
- Submit issues or PRs to the repository
- Share your custom skills with the community
- Provide feedback on what's working (or not)

---

**Version:** 1.0.0
**Last Updated:** November 2025
**License:** MIT
**Maintained by:** Claudius Skills Project

---

Ready to transform your productivity? Install the starter kit and start with your first `/weekly-review`! 🚀
