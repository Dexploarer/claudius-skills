# Tutorial: Building Your Weekly Productivity System

**Level:** Beginner
**Time Required:** 1-2 hours initial setup, then 30 min/week ongoing
**Skills Used:** Multiple starter-kit skills
**Goal:** Establish a sustainable weekly productivity routine

---

## What You'll Learn

By the end of this tutorial, you'll have:
- ✅ A structured weekly planning system
- ✅ Clear priorities and task lists
- ✅ Habit of weekly reviews
- ✅ Improved work-life balance
- ✅ Measurable productivity gains

**Prerequisites:** Starter kit installed (`productivity-skills/starter-kit/.claude/`)

---

## The Problem

**Sound familiar?**
- Weeks fly by without clear progress
- Always busy but never accomplish big goals
- Unclear what to work on each day
- React to urgent vs. important
- Feel overwhelmed and disorganized

**The solution:** A simple, consistent weekly system.

---

## The System (Overview)

```
Sunday Evening
└─ Weekly Review (30 min)
   ├─ Reflect on past week
   ├─ Plan next week
   └─ Set top 3 priorities

Monday-Friday
└─ Daily Routine (10 min/day)
   ├─ Review daily schedule
   ├─ Prioritize tasks
   └─ Execute with focus

Friday Afternoon
└─ Week Wrap-up (15 min)
   ├─ Celebrate wins
   ├─ Archive completed tasks
   └─ Preview next week
```

---

## Part 1: Your First Weekly Review (30 minutes)

### Step 1: Open Claude Code

```bash
cd ~  # Or your project directory
claude code
```

### Step 2: Start Weekly Review

Type in Claude Code:
```
/weekly-review
```

**Expected output:**
```
Let's do your weekly review!

I'll guide you through reflecting on this week and planning next week.

First, what were your wins this week? (Big or small accomplishments)
```

### Step 3: Answer Each Prompt

**Example conversation:**

```
You: /weekly-review

Claude: What were your wins this week?

You: Finished the client proposal, hit the gym 3 times, had a good 1-on-1 with my manager

Claude: Great! What challenges did you face?

You: Team meeting ran way over time, got distracted by emails constantly, didn't finish the report I planned to

Claude: What did you learn?

You: I need to protect my focus time better and maybe batch my email checking

Claude: How was your energy and balance this week? (1-10)

You: Energy was about 7/10, work-life balance was 6/10 - I stayed late twice

Claude: What are your top 3 priorities for next week?

You: 1) Finish the report, 2) Plan Q4 marketing strategy, 3) Fix the production bug

[Claude generates comprehensive weekly review document]
```

### Step 4: Review the Output

You'll receive a formatted review like:

```markdown
# Weekly Review - Week of October 28, 2025

## This Week in Review

### ✅ Wins & Accomplishments
- ✅ Completed client proposal
- ✅ Hit gym 3 times
- ✅ Productive 1-on-1 with manager

### 📈 Challenges & Learnings
- ⚠️ Team meeting ran over (need better agenda)
- 📚 Constant email interruptions (batch checking needed)
- 🎯 Report not finished (time estimation was off)

### ⚡ Energy & Well-being
- Overall energy: 7/10
- Work-life balance: 6/10
- Drained by: Email context switching, late nights
- Energized by: Gym routine, good 1-on-1 conversations

## Next Week's Focus (Nov 4-8)

### Top 3 Priorities
1. **Finish quarterly report** (due Friday)
2. **Plan Q4 marketing strategy** (meeting Wed)
3. **Fix production bug** (blocking customers)

### Big Rocks Scheduled
| Day | Focus Block | Task |
|-----|-------------|------|
| Mon | 9-11 AM | Report deep work session |
| Tue | 9-12 PM | Report completion |
| Wed | 2-4 PM | Q4 strategy prep |
| Thu | 9-11 AM | Bug fix |
| Fri | 9-11 AM | Buffer/catch-up |

### Adjustments for Next Week

**Start doing:**
- Batch email checking (10 AM, 2 PM, 4 PM only)
- Block focus time on calendar
- Leave work by 6 PM (set alarm)

**Stop doing:**
- Checking Slack constantly
- Saying yes to every meeting
- Working through lunch
```

### Step 5: Save Your Review

Copy the output to your note-taking system:
- Notion
- Obsidian
- Apple Notes
- Google Docs
- Markdown file

**Recommended:** Create a folder called "Weekly Reviews" and save as `2025-11-04.md`

---

## Part 2: Schedule Your Ideal Week (20 minutes)

Now that you know your priorities, let's create your ideal schedule.

### Step 6: Create Weekly Schedule

Type in Claude Code:
```
/schedule week
```

**Provide context when prompted:**

```
Claude: Let me help you create an optimized weekly schedule.

What are your fixed commitments? (Meetings, appointments, etc.)

You: Team standup Monday 10 AM, 1-on-1 with manager Tuesday 2 PM, team meeting Wednesday 3 PM

Claude: What times are you most focused and energized?

You: Mornings 9-12, definitely. I'm useless after 3 PM

Claude: What are your top priorities that need focused time?

You: Finishing the quarterly report (needs 6-8 hours), Q4 strategy planning (needs 4 hours), bug fix (needs 3 hours)

[Claude generates optimized weekly schedule]
```

### Step 7: Review Your Schedule

You'll receive:

```markdown
# Your Ideal Week - November 4-8, 2025

## Monday

### 🌅 Morning (6:00 AM - 12:00 PM)
6:00-7:00   Morning routine + exercise
7:00-8:00   Breakfast + email triage
8:00-9:00   Plan day + priority setting
9:00-11:00  🎯 DEEP WORK: Quarterly Report (Block 1)
10:00-10:30 MEETING: Team Standup
10:30-12:00 🎯 DEEP WORK: Quarterly Report (Block 1 cont'd)

### 🌞 Afternoon (12:00 PM - 6:00 PM)
12:00-1:00  Lunch break (leave desk!)
1:00-2:00   Email batch #2 + admin tasks
2:00-4:00   🎯 DEEP WORK: Quarterly Report (Block 2)
4:00-4:30   Email batch #3
4:30-5:30   Shallow work (Slack, small tasks)
5:30-6:00   Plan tomorrow + review today

### 🌙 Evening (6:00 PM+)
6:00+       OFF - No work!

**Daily Focus:** Quarterly Report (Goal: 50% complete)

---

## Tuesday

[Similar structure with different priorities]

**Daily Focus:** Finish Quarterly Report

---

## Wednesday

**Daily Focus:** Q4 Strategy Planning

---

## Thursday

**Daily Focus:** Bug Fix

---

## Friday

**Daily Focus:** Wrap-up + Buffer

---

## Weekly Habits

**Every Morning (30 min):**
- [ ] Review calendar
- [ ] Check top 3 priorities for today
- [ ] Schedule most important work first

**Every Afternoon (15 min):**
- [ ] Review what got done
- [ ] Plan tomorrow's top 3
- [ ] Clear desk and close tabs

**Email Batching:**
- 📧 8:00 AM - Morning triage
- 📧 1:00 PM - Midday check
- 📧 4:00 PM - End-of-day wrap-up

**Focus Time Protection:**
- 🚫 No meetings 9-12 (deep work)
- 🔕 Phone on Do Not Disturb during deep work
- 💻 Email/Slack closed during deep work
- 🎧 Headphones = "Do Not Disturb"
```

### Step 8: Block Time on Your Calendar

**Action:** Actually schedule these blocks:
1. Open your calendar (Google Calendar, Outlook, etc.)
2. Block "Deep Work" times as busy
3. Add "Email Batch" reminders
4. Set end-of-day alarm (6 PM)

**Pro tip:** Color-code your blocks:
- 🔴 Deep work (focus time)
- 🔵 Meetings (collaboration)
- 🟢 Email/admin (shallow work)
- ⚪ Breaks (rest and recharge)

---

## Part 3: Daily Task Management (10 min/day)

### Step 9: Prioritize Daily Tasks

Each morning, use the prioritize command:

```
/prioritize
```

**Example workflow:**

```
You: /prioritize

Claude: What tasks do you need to prioritize?

You:
- Finish quarterly report
- Fix production bug
- Respond to 15 emails
- Review design mockups
- Update documentation
- Schedule team meeting
- Call vendor about invoice issue

Claude: Let me help you prioritize these using the Eisenhower Matrix...

[Claude analyzes and categorizes]

Result:

# Task Prioritization - Monday, Nov 4

## Do First (This morning)
1. ⚡ Fix production bug (Urgent + Important: affecting customers)
2. ⚡ Finish quarterly report (Important + Deadline: due Friday)

## Schedule (This afternoon/this week)
3. 📅 Review design mockups (Important, not urgent)
4. 📅 Update documentation (Important for team)

## Delegate/Batch (30 min block)
5. ↗️ Respond to emails (batch at 1 PM)
6. ↗️ Call vendor (delegate to accounting?)

## Eliminate/Defer
7. ❌ Schedule team meeting (can wait until next week)

**Recommendation:**
- Block 9-11 AM for production bug (your peak focus time)
- Block 11:30-12:30 for quarterly report
- Batch emails at 1 PM
- Review mockups at 2 PM
- Update docs tomorrow (not critical today)
```

### Step 10: Execute Your Day

Now actually do the work! Some tips:

**For focus work:**
- Close email and Slack
- Put phone in another room
- Use Pomodoro timer (25 min work, 5 min break)
- Work on ONE thing at a time

**For shallow work:**
- Batch similar tasks together
- Set a timer (don't let it expand)
- Process quickly, don't perfect

**For breaks:**
- Actually take them!
- Walk, stretch, hydrate
- Don't scroll social media (doesn't restore energy)

---

## Part 4: Using Skills Throughout the Week

### For Emails (use email-composer)

**Scenario:** Need to follow up with client

```
You: Write an email following up with Sarah about the proposal I sent last week

Claude: [email-composer skill activates]

Subject: Re: Q4 Marketing Proposal - Quick Follow-up

Hi Sarah,

I wanted to follow up on the marketing proposal I sent over last week. I know you're juggling multiple priorities, so I wanted to bring this back to your attention.

The key points we discussed:
- $50K budget allocation for Q4 campaigns
- Focus on digital channels (LinkedIn, Google Ads)
- Expected 30% increase in qualified leads

I'm happy to jump on a quick call to discuss any questions or concerns. Would sometime this week work for you?

Looking forward to your thoughts.

Best,
[Your name]
```

**Time saved:** 10-15 minutes per email

---

### For Meetings (use meeting-notes-formatter)

**Scenario:** Just finished a messy meeting, need clean notes

```
You: Format my meeting notes:

meeting with john and sarah discussed q4 budget
need 50k more john will check with finance
sarah wants 2 new hires decided to push launch to november

Claude: [meeting-notes-formatter activates]

# Q4 Planning Meeting

**Date:** November 4, 2025
**Attendees:** John, Sarah, [Your name]

## Discussion Points

### Budget
- Additional $50K needed for Q4
- John to confirm with finance team

### Hiring
- 2 new positions approved (Sarah's team)
- Recruiting to begin immediately

### Product Launch
- Timeline adjusted to November (from October)
- Allows for proper resource allocation

## Decisions Made
- ✅ Proceed with 2 new hires
- ✅ Request additional $50K budget
- ✅ Launch date moved to November

## Action Items
- [ ] Check with finance on budget @john (due: This week)
- [ ] Post job listings @sarah (due: ASAP)
- [ ] Update launch timeline in project plan @you (due: Today)

## Next Steps
- Await budget approval from finance
- Begin recruitment process
- Communicate timeline change to stakeholders
```

**Time saved:** 15-20 minutes of note cleanup

---

### For Projects (use task-breakdown)

**Scenario:** Got assigned a big, vague project

```
You: Break down "Plan company holiday party for 100 people in December" into actionable tasks

Claude: [task-breakdown activates]

[Receives comprehensive breakdown with phases, tasks, timelines, and dependencies - see earlier examples]
```

**Time saved:** 1-2 hours of planning overhead

---

## Part 5: End-of-Week Wrap-up (15 minutes)

### Step 11: Friday Afternoon Review

Every Friday around 4 PM:

```
You: Help me wrap up this week

Claude: Let's review your week!

Looking at your priorities:
1. ✅ Finish quarterly report - DONE
2. ✅ Plan Q4 marketing strategy - DONE
3. ✅ Fix production bug - DONE

What else did you accomplish this week?

You: Also launched the new feature, had 3 productive 1-on-1s, and cleaned up 50 old tasks

Claude: Excellent! Here's your week summary:

# Week in Review - Nov 4-8, 2025

## Major Wins 🎉
- ✅ All 3 top priorities completed!
- ✅ Launched new feature
- ✅ 3 productive 1-on-1s
- ✅ Cleared 50 old tasks from backlog

## Key Metrics
- Tasks completed: 23/25 (92%)
- Deep work hours: 15 hours (goal: 15) ✅
- Meetings: 6 hours (goal: max 8) ✅
- Email batch discipline: 4/5 days ✅

## What Worked Well
- Morning deep work blocks were highly productive
- Email batching reduced interruptions
- Leaving work by 6 PM improved evening energy

## What to Improve
- Still got pulled into 2 unscheduled meetings
- Thursday afternoon lost focus (too many small tasks)

## Next Week Preview
- Lighter week (no major deadlines)
- Good time to tackle backlog items
- Schedule some strategic thinking time

**Status: GREAT WEEK! 🚀**
```

---

## Part 6: Making It Stick (Building the Habit)

### Week 1-2: Establishment
- [ ] Do weekly review (even if imperfect)
- [ ] Use /prioritize daily
- [ ] Try email-composer for important emails
- [ ] Block focus time on calendar

### Week 3-4: Refinement
- [ ] Adjust schedule based on learnings
- [ ] Optimize email batching times
- [ ] Identify best deep work hours
- [ ] Track completion rates

### Month 2+: Optimization
- [ ] Review monthly trends
- [ ] Customize skills to your workflow
- [ ] Add new tools as needed
- [ ] Remove tools that don't help

---

## Success Metrics

Track these to see if it's working:

**Weekly:**
- % of top 3 priorities completed (target: 80%+)
- Deep work hours (target: 15+ hours/week)
- Meeting hours (target: <10 hours/week for ICs)
- Daily planning consistency (target: 5/5 days)

**Monthly:**
- Goals achieved (vs. goals set)
- Stress level trend (subjective, 1-10)
- Work-life balance (subjective, 1-10)
- System satisfaction (would you recommend it?)

**Sample progress:**

```
Month 1: Learning the system
- Top 3 completion: 60%
- Deep work: 8 hours/week
- Still figuring it out

Month 2: Getting consistent
- Top 3 completion: 75%
- Deep work: 12 hours/week
- System feels natural

Month 3: Optimized
- Top 3 completion: 85%
- Deep work: 15 hours/week
- Can't imagine working without it
```

---

## Common Challenges & Solutions

### "I missed my weekly review"
**Solution:** Do it Monday morning instead. Better late than never. Build the habit of "the week doesn't start until I've reviewed."

### "My schedule never goes as planned"
**Solution:** That's normal. The schedule is a guide, not a prison. The value is in having priorities and protecting focus time, not rigid adherence.

### "I have too many meetings to block focus time"
**Solution:** Start with 2 hours/week. Block Mon/Wed/Fri 9-10 AM as "busy" for focus time. Gradually increase.

### "I fall off the wagon after 2-3 weeks"
**Solution:** Set a recurring calendar reminder for Sunday evening weekly review. Make it non-negotiable like a meeting.

### "This feels like a lot of overhead"
**Solution:** The first 2 weeks take effort to establish. By week 3-4, it becomes automatic. The 30-60 min/week investment saves 5-10 hours of wasted effort.

---

## Next Steps

### This Week:
- [ ] Do your first weekly review (/weekly-review)
- [ ] Create your ideal week schedule (/schedule week)
- [ ] Block focus time on your calendar
- [ ] Try /prioritize for 3 days

### This Month:
- [ ] Complete 4 weekly reviews (build the habit)
- [ ] Measure your productivity metrics
- [ ] Adjust the system to your needs
- [ ] Explore other starter-kit tools

### This Quarter:
- [ ] Review 3-month progress
- [ ] Set bigger goals with /goal-setting
- [ ] Consider intermediate kit for advanced needs
- [ ] Share the system with colleagues

---

## Real Results from Users

> "After 2 months using this system, I've completed more goals than in the previous year. The weekly review keeps me honest." - Mike, Product Manager

> "I was skeptical at first, but the email batching alone saved me 5 hours per week. Game-changer." - Sarah, Consultant

> "The task breakdown skill helped me plan my entire wedding in 2 hours. Would have taken me weeks of stress." - Lisa, Bride-to-be

---

## Additional Resources

**Skills reference:**
- [Meeting Notes Formatter](../../starter-kit/.claude/skills/meeting-notes-formatter.md)
- [Email Composer](../../starter-kit/.claude/skills/email-composer.md)
- [Task Breakdown](../../starter-kit/.claude/skills/task-breakdown.md)

**Related tutorials:**
- Goal Setting Tutorial (coming soon)
- Decision-Making Tutorial (coming soon)
- Creative Project Tutorial (coming soon)

**Books to deepen your practice:**
- *Getting Things Done* - David Allen
- *Atomic Habits* - James Clear
- *Deep Work* - Cal Newport

---

**Tutorial complete!** You now have a productivity system that actually works.

Start with your first `/weekly-review` this Sunday. Your future self will thank you. 🚀

---

**Questions or feedback?** Open an issue in the repository or share what's working for you!
