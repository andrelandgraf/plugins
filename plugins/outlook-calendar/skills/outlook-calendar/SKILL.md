---
name: outlook-calendar
description: Manage Outlook Calendar scheduling, availability, event details, and shared-calendar context through connected Microsoft Outlook data. Use when the user wants to inspect a schedule, compare candidate slots, review conflicts, understand meeting status semantics, or prepare an exact event change before applying it.
---

# Outlook Calendar

## Overview

Use this skill to turn Outlook Calendar data into clear scheduling decisions. Keep answers grounded in exact dates, times, and calendar evidence, and translate Microsoft-specific calendar semantics into plain English when they matter.

## Preferred Deliverables

- Availability summaries with exact candidate slots, timezone, and relevant conflicts.
- Scheduling Assistant style summaries that explain when Outlook is showing free/busy only versus full event detail.
- Event change proposals that show the current event details and the intended update.
- Meeting-status explanations that decode Outlook concepts such as `Busy`, `Tentative`, `Free`, `Out of Office`, and `Working Elsewhere`.
- Meeting-readiness summaries that incorporate attendee response state, organizer intent, and whether a Teams link, room, or work-location detail already exists.
- Final event details that are ready to create, reschedule, or cancel after confirmation.

## Workflow

1. Read the relevant calendar state first so the request is grounded in actual events, attendee responses, calendars, and time windows.
2. Normalize relative time language into explicit dates, times, and timezone-aware ranges before reasoning about availability.
3. Start from Outlook's scheduling surfaces, not generic calendar abstractions. Account for attendee response state, organizer vs attendee role, shared-calendar visibility, work hours, work location, and room/resource context when available.
4. Surface Outlook-specific status semantics before proposing changes. Call out whether a block is `Tentative`, `Free`, `Out of Office`, `Working Elsewhere`, or only visible as shared-calendar busy time.
5. When the request depends on workday norms, prefer Outlook-native cues such as work hours, location plans, and Scheduling Assistant visibility over generic assumptions about "focus time".
6. When notes, Teams links, rooms, or missing details matter, inspect the event payload before proposing a change and say when the source data appears partial.
7. When the request is ambiguous, summarize the best candidate slots or the exact event diff before drafting any write.
8. Treat missing title, attendees, location, Teams link, or timezone as confirmation points rather than assumptions.
9. Only create, update, move, or cancel events when the user has clearly asked for that action or confirmed the exact event details.

## Outlook Product Differences

- Outlook users often reason from the Scheduling Assistant, not from fully open peer calendars. When visibility is partial, present the answer as a free/busy recommendation rather than pretending to know the meeting titles.
- `Tentative` matters more in Outlook culture than in many Google Calendar workflows. It often means "soft hold" or "not yet accepted", so keep it distinct from true busy time.
- Work location and work hours are first-class scheduling signals in Outlook and can appear alongside availability. Use them to explain why a slot is awkward or strong, especially for hybrid teams.
- RSVP state is part of the scheduling story. For prep and rescheduling requests, mention whether key attendees have accepted, tentatively accepted, declined, or not responded.
- Teams and room/resource context are part of the event object, not an afterthought. Preserve those logistics unless the user wants them changed.

## Write Safety

- Preserve event titles, attendees, start and end times, locations, Teams links, status, and notes from the source data unless the user requests a change.
- Treat deletes, cancellations, attendee-impacting changes, and broad schedule edits as high-impact actions. Restate the affected event before applying them.
- If multiple calendars or similarly named events are in play, identify the intended one explicitly before editing.
- If the request references relative dates like "tomorrow afternoon," restate the exact interpreted date, time, and timezone before drafting the change.
- If a meeting is online, preserve the existing Teams or online-meeting setup unless the user asks to change it.

## Output Conventions

- Present scheduling summaries with exact weekday, date, time, and timezone.
- When sharing availability, explain why a slot works or conflicts instead of listing raw times without context.
- When Outlook status matters, translate it into user language, such as "tentative hold", "true busy", "out of office", or "visible only as shared-calendar busy time".
- When attendee responses matter, name them directly instead of flattening everything into "available" or "unavailable".
- When proposing a new or updated event, format the response as title, attendees, start, end, timezone, location or Teams link, status if relevant, and purpose.
- Keep option lists short and explain the tradeoff for each candidate slot.
- When reporting conflicts, name the overlapping events and how much time is affected.
- When the source data is incomplete, say whether the limitation seems to come from shared-calendar permissions or missing meeting metadata.

## Example Requests

- "Check my Outlook Calendar availability this Thursday afternoon and suggest the best two meeting slots."
- "Use Scheduling Assistant logic to find a time for this meeting that avoids people's out-of-office blocks and likely remote-only days."
- "Move the project review to next week and keep the same attendees and Teams link."
- "Summarize my calendar for tomorrow, including which holds are only tentative."
- "Draft the exact event details for a 30 minute sync with the vendor at 2 PM Pacific on Friday."
- "Explain whether this shared Outlook calendar slot is really free or just marked working elsewhere."

## Light Fallback

If Outlook Calendar data is missing or incomplete, say that Microsoft Outlook access may be unavailable or pointed at the wrong calendar, then ask the user to reconnect or clarify the intended calendar or event.
