# Meeting Notes Formatter

**Trigger phrases:**
- "format my meeting notes"
- "organize these meeting notes"
- "structure my meeting"
- "clean up meeting notes"
- "format meeting transcript"

**Description:**
Automatically formats raw meeting notes into a professional, structured document with clear sections for attendees, agenda items, discussion points, action items, and next steps.

## What this skill does:

When you provide raw meeting notes, transcripts, or unstructured meeting content, this skill will:

1. **Extract key information:**
   - Meeting date and time
   - Attendees/participants
   - Meeting topic/purpose

2. **Organize content into sections:**
   - Executive Summary
   - Attendees
   - Agenda Items
   - Discussion Points (organized by topic)
   - Decisions Made
   - Action Items (with owners and deadlines)
   - Parking Lot (topics for future discussion)
   - Next Steps

3. **Format action items clearly:**
   - [ ] Task description @owner (due: date)
   - Priority indicators (High/Medium/Low)
   - Dependencies noted

4. **Improve clarity:**
   - Remove filler words and redundancy
   - Clarify vague statements
   - Add section headers
   - Use bullet points and formatting

## Example usage:

**Input:**
```
meeting with sarah and john today talked about q4 planning
discussed budget - need 50k more for marketing
john said he'll check with finance by friday
also talked about hiring - sarah wants 2 new devs
decided to push product launch to november
need to review designs next week
```

**Output:**
```markdown
# Q4 Planning Meeting

**Date:** November 1, 2025
**Attendees:** Sarah, John, [Your name]

## Executive Summary
Discussed Q4 budget requirements and hiring plans. Decided to adjust product launch timeline to November to accommodate resource needs.

## Discussion Points

### Budget
- Marketing budget shortfall identified
- Additional $50K needed for Q4 marketing initiatives

### Hiring
- Engineering team expansion required
- 2 new developer positions to be opened

### Product Launch
- Timeline adjusted to November
- Design review scheduled for next week

## Decisions Made
- ✅ Product launch moved to November
- ✅ Proceed with hiring 2 developers
- ✅ Request additional $50K marketing budget

## Action Items
- [ ] Check with finance department on marketing budget @john (due: Friday, Nov 3)
- [ ] Review product designs @team (due: Next week)
- [ ] Post developer job listings @sarah (due: TBD)

## Next Steps
- Finance approval on budget
- Design review meeting
- Begin developer recruitment process
```

## Best Practices:

1. **Be comprehensive** - Include all important details
2. **Use consistent formatting** - Maintain professional structure
3. **Assign ownership** - Every action item needs an owner
4. **Set deadlines** - Include due dates when mentioned
5. **Prioritize clarity** - Make notes scannable and actionable

## Tips for better results:

- Provide as much context as possible (even if messy)
- Include any dates, names, or specific numbers mentioned
- Mention if certain items are urgent or high priority
- Include any follow-up meetings or deadlines discussed

## Output format:

The skill will always produce markdown-formatted notes that you can:
- Copy to Notion, Confluence, or other tools
- Save as a .md file
- Share via email or Slack
- Convert to PDF for distribution

---

**Skill Type:** Productivity - Meeting Management
**Complexity:** Beginner
**Estimated time:** 30 seconds - 2 minutes
