# Task Breakdown Assistant

**Trigger phrases:**
- "break down this task"
- "create subtasks for"
- "how to approach"
- "plan this project"
- "break this into steps"
- "task planning"

**Description:**
Breaks down complex tasks or projects into manageable, actionable subtasks with clear dependencies, time estimates, and priorities. Helps prevent overwhelm and provides a clear path forward.

## What this skill does:

When you provide a high-level task or goal, this skill will:

1. **Analyze the task:**
   - Identify the end goal and deliverables
   - Recognize complexity and scope
   - Determine required resources/skills

2. **Create a structured breakdown:**
   - Sequential steps with clear order
   - Dependencies between tasks
   - Time estimates (realistic)
   - Priority levels
   - Resource requirements

3. **Provide actionable subtasks:**
   - Each subtask is concrete and doable
   - Clear success criteria
   - Next action always obvious
   - Estimated effort (time/difficulty)

4. **Organize for execution:**
   - Group related tasks
   - Identify parallel vs. sequential work
   - Highlight blockers and dependencies
   - Suggest milestone checkpoints

## Example usage:

**Example 1: Project Task**

**Input:**
```
I need to plan our company's annual retreat for 50 people
```

**Output:**
```markdown
# Company Annual Retreat - Task Breakdown

**Goal:** Successfully plan and execute annual company retreat for 50 people
**Timeline:** 8-12 weeks (recommended)
**Complexity:** High

## Phase 1: Planning & Research (Week 1-2)

### High Priority
- [ ] Define retreat objectives and goals (2 hours)
  - Team building, strategic planning, celebration, or mix?
  - Get input from leadership team
  - Success criteria: Clear 2-3 sentence purpose statement

- [ ] Set budget and get approval (1 day)
  - Estimate per-person cost ($200-500 typical)
  - Total budget: $10,000-25,000
  - Get executive approval
  - Dependency: None

- [ ] Form planning committee (1 hour)
  - 3-4 people from different departments
  - Assign roles (logistics, activities, communications)
  - Success criteria: Committee identified and first meeting scheduled

### Medium Priority
- [ ] Research venue options (3-5 hours)
  - 50-60 person capacity
  - Within budget
  - Preferred locations/regions
  - Create shortlist of 3-5 venues
  - Dependency: Budget approval

- [ ] Survey employees for preferences (2 hours)
  - Dietary restrictions
  - Accessibility needs
  - Activity preferences
  - Date availability
  - Success criteria: >80% response rate

## Phase 2: Booking & Logistics (Week 3-4)

### High Priority
- [ ] Book venue (1 week)
  - Visit top 2-3 options if possible
  - Negotiate pricing and terms
  - Sign contract
  - Pay deposit
  - Dependency: Budget approval, venue research

- [ ] Arrange transportation (2-3 hours)
  - Charter bus, car rentals, or individual travel?
  - Get quotes
  - Book transportation
  - Dependency: Venue confirmed

- [ ] Book accommodations (2 hours)
  - If overnight retreat
  - Room blocks at nearby hotels
  - Confirm group rates
  - Dependency: Venue confirmed

### Medium Priority
- [ ] Plan catering/meals (3-4 hours)
  - Breakfast, lunch, dinner, snacks
  - Account for dietary restrictions
  - Get quotes from 2-3 caterers
  - Make selection and book
  - Dependency: Attendee survey results

- [ ] Secure insurance/liability coverage (1 hour)
  - Event insurance
  - Activity liability waivers if needed
  - Dependency: Venue confirmed

## Phase 3: Program Development (Week 5-7)

### High Priority
- [ ] Create retreat agenda (4-5 hours)
  - Balance work sessions and fun activities
  - Include breaks and free time
  - Assign session owners
  - Success criteria: Minute-by-minute schedule

- [ ] Plan team-building activities (3-4 hours)
  - Choose 2-3 activities
  - Book facilitators/vendors if needed
  - Prepare materials
  - Dependency: Budget, venue confirmed

### Medium Priority
- [ ] Prepare work session content (5-10 hours)
  - Strategic planning materials
  - Presentation decks
  - Workshop supplies
  - Success criteria: All content ready 1 week before

- [ ] Create attendee packet (2 hours)
  - Schedule
  - Map/directions
  - WiFi info
  - Emergency contacts
  - Packing list

## Phase 4: Communications (Week 6-8)

### High Priority
- [ ] Send save-the-date (30 min)
  - 6-8 weeks before event
  - Basic details and logistics
  - Dependency: Venue and date confirmed

- [ ] Collect RSVPs and final headcount (ongoing)
  - Track responses
  - Follow up with non-responders
  - Adjust catering/logistics as needed

### Medium Priority
- [ ] Send pre-retreat email (1 hour)
  - 2 weeks before: Detailed agenda
  - 1 week before: Final logistics
  - Day before: Last-minute reminders

- [ ] Create Slack/Teams channel (15 min)
  - Centralized communication
  - Share updates and info
  - Day-of coordination

## Phase 5: Execution & Wrap-up (Week 8+)

### Day Before
- [ ] Final vendor confirmations (1 hour)
  - Catering, activities, transportation
  - Headcount updates

- [ ] Pack supplies and materials (2 hours)
  - Name tags, signs, handouts
  - Emergency kit
  - Tech equipment (projector, mics, etc.)

### Day Of
- [ ] Setup and registration (2-3 hours before)
  - Venue setup
  - Registration table
  - Test A/V equipment

- [ ] Event management (all day)
  - Stick to schedule
  - Address issues as they arise
  - Take photos/videos

### Post-Event (Week after)
- [ ] Send thank you email (30 min)
  - Recap highlights
  - Share photos
  - Thank attendees and vendors

- [ ] Collect feedback (1 hour)
  - Survey about what worked/didn't
  - Analyze results
  - Document lessons learned

- [ ] Process expenses and reconcile budget (2-3 hours)
  - Submit invoices
  - Close out contracts
  - Final budget report

## Summary

**Total estimated effort:** 35-50 hours
**Timeline:** 8-12 weeks
**Key milestones:**
- Week 2: Budget approved, venue shortlisted
- Week 4: Venue booked, logistics confirmed
- Week 7: Full agenda finalized
- Week 8+: Event execution

**Critical path:**
1. Budget approval → Venue booking → Everything else
2. Attendee survey → Catering decisions
3. Agenda creation → Content preparation

**Resources needed:**
- Planning committee (3-4 people)
- Budget ($10k-25k)
- Executive buy-in
- 35-50 hours of planning time
```

**Example 2: Personal Task**

**Input:**
```
Break down "learn Spanish" for me
```

**Output:**
```markdown
# Learn Spanish - Task Breakdown

**Goal:** Achieve conversational Spanish proficiency
**Timeline:** 6-12 months for basic conversation
**Complexity:** Medium-High (long-term commitment)

## Phase 1: Foundation (Month 1-2)

### Week 1-2: Setup & Basics
- [ ] Choose learning method (1 hour)
  - App (Duolingo, Babbel), tutor, class, or mix?
  - Research and commit to primary method
  - Budget: $0-50/month

- [ ] Learn Spanish alphabet and pronunciation (3-5 hours)
  - Focus on sounds that don't exist in English
  - Practice daily (15 min/day)
  - Success: Can pronounce any Spanish word

- [ ] Master basic greetings and phrases (2-3 hours)
  - Hello, goodbye, thank you, please
  - "My name is...", "Do you speak English?"
  - Practice with audio

### Week 3-4: Core Grammar
- [ ] Learn present tense conjugation (5-7 hours)
  - Regular -ar, -er, -ir verbs
  - Common irregular verbs (ser, estar, tener, ir)
  - Practice: 15 min daily

- [ ] Build core vocabulary - 100 words (7-10 hours)
  - Numbers 1-100
  - Days, months, colors
  - Common nouns (food, family, objects)
  - Create flashcards or use Anki

## Phase 2: Building Skills (Month 3-6)

### Grammar expansion
- [ ] Learn past tenses (10-15 hours)
  - Preterite vs. imperfect
  - When to use each
  - Practice with stories

- [ ] Master ser vs. estar (3-5 hours)
  - Permanent vs. temporary states
  - Common uses
  - Exercises

- [ ] Learn future and conditional (8-10 hours)
  - Conjugation patterns
  - Common uses
  - Practice sentences

### Vocabulary growth
- [ ] Expand to 500+ words (ongoing)
  - Learn 10 new words daily
  - Focus on high-frequency words
  - Use spaced repetition

- [ ] Learn topic-specific vocabulary
  - [ ] Restaurant/food (2 hours)
  - [ ] Travel/directions (2 hours)
  - [ ] Work/business (2 hours)
  - [ ] Hobbies/interests (2 hours)

### Listening practice
- [ ] Watch Spanish content with subtitles (30 min daily)
  - Start: Spanish audio + English subtitles
  - Progress to: Spanish audio + Spanish subtitles
  - Netflix shows, YouTube channels

- [ ] Listen to Spanish podcasts (15 min daily)
  - Start with slow/learner podcasts
  - Progress to native content

## Phase 3: Conversation (Month 6-12)

### Speaking practice
- [ ] Find conversation partner (1-2 hours to find)
  - iTalki, Tandem app, local meetups
  - 30 min practice 2-3x per week
  - Success: Regular conversation schedule

- [ ] Talk to yourself in Spanish (daily)
  - Narrate daily activities
  - Practice what you learned
  - 10-15 min daily

- [ ] Join Spanish conversation group (weekly)
  - Local meetup or online
  - Force yourself to speak
  - 1 hour per week

### Immersion
- [ ] Change phone/apps to Spanish (5 min)
  - Forces daily exposure
  - Learn tech vocabulary

- [ ] Read simple Spanish content (15-30 min daily)
  - Children's books
  - News articles (start with simplified news)
  - Progress to novels

- [ ] Write in Spanish (15 min daily)
  - Journal entries
  - Social media posts
  - Get corrections from tutor/partner

## Ongoing (Throughout)

### Daily habits (total: 1-2 hours daily)
- [ ] Duolingo or app (15-20 min)
- [ ] Flashcard review (10-15 min)
- [ ] Listen to podcast/music (15-30 min)
- [ ] Read something in Spanish (15-30 min)
- [ ] Speak/practice (15-30 min)

### Weekly commitments
- [ ] Conversation practice (1-2 hours)
- [ ] Grammar study (2-3 hours)
- [ ] Watch Spanish content (2-3 hours)

### Monthly checkpoints
- [ ] Vocabulary assessment (how many words do I know?)
- [ ] Speaking self-assessment (record yourself)
- [ ] Adjust study plan based on progress
- [ ] Celebrate wins!

## Summary

**Daily time commitment:** 1-2 hours
**Weekly time commitment:** 8-15 hours
**Key milestones:**
- Month 2: Can introduce yourself, order food, ask basic questions
- Month 6: Can have basic conversations, understand simple content
- Month 12: Conversational proficiency in familiar topics

**Resources needed:**
- Language learning app ($0-15/month)
- Conversation tutor ($10-30/hour, 2-4x month)
- Spanish media (Netflix, podcasts - free)
- Textbook or grammar reference ($20-40 one-time)

**Critical success factors:**
1. Daily consistency (even 15 min is better than nothing)
2. Speaking practice (can't learn without using it)
3. Immersion (surround yourself with Spanish)
4. Patience (language learning is a marathon)
```

## Task categories supported:

### Work Projects:
- Event planning
- Product launches
- Marketing campaigns
- Process improvements
- Training programs

### Personal Goals:
- Learning new skills
- Health/fitness goals
- Moving/relocation
- Home renovation
- Career transitions

### Creative Projects:
- Writing a book
- Starting a podcast
- Building a website
- Learning an instrument

## Best Practices:

1. **Start with the end in mind:**
   - What does "done" look like?
   - What are the deliverables?

2. **Be realistic with time:**
   - Add buffer time (things take longer than expected)
   - Account for dependencies and blockers

3. **Break tasks into 2-hour chunks:**
   - If a task is bigger than 2 hours, break it down more
   - Makes progress trackable

4. **Identify the critical path:**
   - What must be done first?
   - What blocks other tasks?

## Output includes:

- ✅ Prioritized task list
- ⏱️ Time estimates
- 🔗 Dependencies clearly marked
- 📅 Suggested timeline/phases
- 🎯 Success criteria for each task
- 💰 Resource requirements
- 🚧 Potential blockers/risks

---

**Skill Type:** Productivity - Planning
**Complexity:** Beginner
**Estimated time:** 1-5 minutes depending on task complexity
