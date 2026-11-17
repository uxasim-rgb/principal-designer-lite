---
tags: [principal-designer-lite]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Design the bulk approve flow for our expense approval queue. The list is paginated (50 per page), managers can 'select all matching' across pages, some expenses in a selection aren't eligible (over their limit or already approved), permissions can change mid-session, and the backend can partly succeed. Give me the flow and the states.
