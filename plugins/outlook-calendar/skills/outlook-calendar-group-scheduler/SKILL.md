---
name: outlook-calendar-group-scheduler
description: Find and rank good meeting times for multiple people using connected Outlook Calendar data. Use when the user wants to schedule a group meeting, compare candidate slots across several attendees, or find the best compromise time while respecting Outlook availability semantics.
---

# Outlook Calendar Group Scheduler

Use this skill when the scheduling problem is the task.

## Outlook Product Framing

- Think like Scheduling Assistant first: free/busy visibility, work hours, and work location are often more reliable than full event detail.
- Treat attendee response state and organizer logistics as part of scheduling, not just the final event body.
- When rooms or resources are visible, treat them as Outlook-style scheduling constraints rather than a separate "room finder" workflow.

## Workflow

1. Ground the scheduling problem first: date window, duration, timezone, required attendees, optional attendees, and any hard constraints such as "this week", "afternoons only", or "avoid lunch".
2. Normalize the request into explicit candidate windows before ranking anything.
3. Rank slots, do not enumerate everything. Optimize for a short list of strong options.
4. Treat `Busy` and `Out of Office` as harder constraints than `Tentative` or `Working Elsewhere` unless the user says otherwise.
5. Prefer slots that minimize conflict cost, fit within work hours, and avoid avoidable hybrid-work friction such as forcing an in-office room meeting onto remote-heavy attendees.
6. When rooms, resources, or building context are available, prefer slots that keep the meeting logistically coherent instead of treating time as the only variable.
7. If shared-calendar visibility is partial, say when a recommendation is based on free/busy signals rather than full event detail.

## Ranking Heuristics

- Favor required-attendee fit over optional-attendee fit.
- Favor slots that avoid very early or very late local times for distributed attendees.
- Favor slots that stay inside work hours and avoid consuming the only large free block in someone's day unless the meeting is clearly important.
- Favor a small number of high-confidence options over a long weak list.
- When two slots are similar, prefer the one that causes less calendar fragmentation.
- When one attendee is only `Tentative` or `Working Elsewhere`, describe that as a softer constraint instead of silently treating it as unavailable.
- When one option aligns better with attendees' work locations or room logistics, explain that advantage explicitly.

## Output Conventions

- Return 2-4 candidate slots by default.
- For each slot, say why it works and who, if anyone, would be inconvenienced.
- If there is no clean option, say what tradeoff the best slot is making.
- If the recommendation depends on partial shared-calendar visibility, say so directly.
