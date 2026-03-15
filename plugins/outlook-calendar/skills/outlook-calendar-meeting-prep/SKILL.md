---
name: outlook-calendar-meeting-prep
description: Build a practical meeting prep brief from a connected Outlook Calendar event and its nearby context. Use when the user wants to prepare for an upcoming meeting, understand what to read beforehand, pull in linked notes, or get a concise brief on what the meeting appears to require.
---

# Outlook Calendar Meeting Prep

Use this skill when the user wants a prep brief, not just the event details.

## Workflow

1. Start from the event itself: title, description, attendees, response state, recurrence context, Teams details, and any obvious linked materials.
2. If the event points to connected docs, decks, threads, or notes and they are cheap to follow, inspect them before writing the brief.
3. Build the prep brief around what the meeting appears to be for, what decisions or inputs seem likely, and what context is attached versus missing.
4. Highlight what the user should read or prepare first rather than dumping every detail.
5. Stay close to the event and its linked context. Do broader research only if the user explicitly asks for it.
6. If the event comes from a shared calendar with limited detail, say what is confirmed versus what remains opaque.

## Outlook-Specific Focus

- Call out whether attendees have accepted, tentatively accepted, declined, or not responded when that changes the prep picture.
- Mention the presence of a Teams meeting link, room resource, or organizer note when those shape logistics.
- Treat organizer notes, response tracking, and last-minute RSVP drift as part of the meeting story, because Outlook users often rely on the invitation itself as the operational source of truth.
- Separate confirmed context from inferred context, especially when the event description is sparse.

## Output Conventions

- Lead with what this meeting appears to be about.
- Call out the most relevant notes, attachments, links, or Teams details.
- Separate confirmed context from missing context or open questions.
- End with a short "what to do before this meeting" list when there is enough evidence to support it.
