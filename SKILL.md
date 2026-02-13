---
name: webmcp-excellent-core
description: Execute WebMCP web actions with clear tool contracts, confirmation before write operations, deterministic execution, and concise traceable outputs.
---

# webmcp-excellent-core

Use when
- The task requires reliable web actions through structured tools (search/filter/submit/update).
- Raw click/DOM automation is unstable or hard to reproduce.

Do not use when
- The user only wants brainstorming with no executable step.
- No WebMCP-capable tools are available and manual guidance is sufficient.

Workflow
1) Discover capability
- Identify available tools/resources/prompts.
- Mark each tool as read-only or write.

2) Map intent
- Convert request to: Input -> Transformation -> Output.
- Validate required fields against tool schema.

3) Confirm write actions
- For write operations, ask for explicit confirmation once.
- For high-risk operations (payment/account/security), confirm twice.

4) Execute minimally
- Run the smallest deterministic tool chain.
- Capture references: tool name, key params, result id.

5) Return result
- Provide final outcome.
- List executed actions.
- List pending actions (if any).

Fallback
- Missing tool: return shortest manual path.
- Schema mismatch: return invalid fields + expected shape.
- Runtime failure: bounded retry, then degrade with clear next step.

Output format
- Result
- Executed actions
- Pending actions
- Trace references
- Limits (only if material)
