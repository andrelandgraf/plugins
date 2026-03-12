---
name: repo-triage
description: Triage GitHub issues and pull requests, build a prioritized queue, and propose next actions with clear risk/testing notes.
metadata:
  short-description: GitHub repo issue/PR triage
---

# Repo Triage Skill

Use this skill when the task is to understand the state of a repository's issue or PR queue and produce an actionable triage outcome.

## What this skill is for

- Prioritizing incoming issues by impact, confidence, and unblockability
- Grouping PRs by review state and risk
- Producing a clean handoff summary for engineering leads or oncall rotations

## Workflow

1. Collect the requested issue/PR set using the GitHub MCP tools.
2. Normalize references and labels (see `references/query_patterns.md`).
3. Build a triage table with: status, owner, risk, blockers, and recommended next action.
4. Call out missing tests, missing repros, and stale branches explicitly.
5. End with the top 3 actions the user can take next.

## Output conventions

- Keep summaries concise and decision-oriented.
- Prefer explicit evidence (links, PR numbers, failing checks) over speculation.
- If the request is review-centric, delegate to the plugin's PR review sub-agent prompt.

## Optional helper script

If the user provides text blobs (issue lists, changelogs, pasted PR summaries), use `scripts/extract_refs.py` to normalize GitHub issue and PR references before triage.
