# Query Patterns (Draft)

Use these patterns when querying a GitHub MCP server for triage workflows.

## Issues

- `is:issue is:open sort:updated-desc` for fresh inbound triage
- `is:issue is:open label:bug no:assignee` for unowned bugs
- `is:issue is:open label:regression` for release risk scanning

## Pull Requests

- `is:pr is:open review:required` for review queue triage
- `is:pr is:open status:failure` for broken CI
- `is:pr is:open updated:<7d` for stale active work

## Triage heuristics

Capture at least these fields in your final output:

- `owner`
- `current_state`
- `blocking_reason`
- `risk_level`
- `next_action`
