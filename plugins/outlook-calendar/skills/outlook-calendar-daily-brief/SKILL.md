---
name: outlook-calendar-daily-brief
description: Create a polished, human-readable day brief from Outlook Calendar events. Use when the user asks for a summary of today, tomorrow, a specific day, "my schedule", "my day", an agenda, or a calendar brief and the Outlook Calendar connector from this plugin is available.
---

# Outlook Calendar Daily Brief

## Overview

Use this skill to turn one day of Outlook Calendar events into a readable daily brief instead of a raw event dump. Favor a short executive summary over exhaustive event-by-event narration, and call out Outlook-specific status semantics, work-location cues, and shared-calendar limits when they change how busy the day really is.

## Workflow

1. Resolve the date window explicitly in the user's timezone.
2. Fetch the day's events from the Outlook Calendar connector for the relevant calendar.
3. Build a compact brief around the actual workday shape, not just a chronological list.
4. Distinguish true busy time from `Tentative`, `Free`, `Out of Office`, or `Working Elsewhere` blocks when the source data exposes those statuses.
5. If the day has meaningful work-location or out-of-office context, mention it near the top because Outlook users often use that information to interpret the schedule.
6. When shared-calendar visibility is partial, say that clearly instead of implying the agenda is complete.

## Relevant Focus

- Prefer one-day schedule reads over broad multi-day scans.
- If the user is asking about "today", emphasize what is still upcoming and which meetings may require prep.
- If the user is asking about "tomorrow" or another future day, emphasize density, conflict zones, large open blocks, and unusual holds.
- If the day contains many tentative holds, soft blocks, or work-location markers, explain the day as "firm" versus "fluid" rather than treating every block equally.

## Data Source Rules

- Use the Outlook Calendar connector from this plugin, not web search and not a manually reconstructed schedule.
- Query with explicit day boundaries in the user's timezone.
- Preserve titles exactly when the connector returns them.
- If the connector only exposes busy windows for a calendar, build the brief around availability patterns and say that event-level detail was not available.

## Default Shape

Use this structure unless the user asks for something narrower:

- date header
- short top summary lines
- `Day Shape`
- `Agenda`
- optional `What Needs Attention`
- `Useful Readout`
- optional `Remaining Today`

Keep the tone compact and practical. Do not use a fenced code block for the agenda.

## Formatting Rules

- Keep the agenda table to two columns only: `Time` and `Meeting`.
- Use compact times and include the timezone in the section header or summary, not on every row.
- Treat all-day status markers such as PTO or OOF as context even when they are not meetings.
- When the source data includes Outlook status, mention it only when it changes the user's real availability.
- Mention work-location or building context only when it affects meeting logistics or how the day should be interpreted.
- Keep overlap explanations in `What Needs Attention`, not inline in every agenda row.
- If the day contains only tentative holds or shared-calendar busy markers, say that plainly.

## Outlook-Specific Notes

- `Working Elsewhere` and `Free` should not be treated as the same thing as a hard busy meeting.
- `Tentative` often means the slot may still be usable, but only if the user accepts that ambiguity.
- Shared calendars may expose only free/busy signals, not full titles or notes.

## Fallback

If the Outlook Calendar connector is unavailable or returns no events unexpectedly, say that Microsoft Outlook access may be unavailable or scoped to the wrong calendar and ask the user to reconnect or clarify the intended calendar.
