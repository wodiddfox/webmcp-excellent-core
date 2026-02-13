---
name: webmcp-excellent-core
description: Reliable WebMCP execution for web tasks with strict scope, confirmation gates, and traceable outputs.
---

# webmcp-excellent-core

Use when
- Executable web task is required via structured tools: search/filter/submit/update.
- Stable, reproducible execution is required.

Do not use when
- Only brainstorming is requested.
- No WebMCP tool exists and only generic advice is needed.

Trigger signals
- "查找并筛选后提交"
- "按条件下单/建单/更新状态"
- "给我可追溯执行结果"

Non-trigger signals
- "先讨论，不执行"
- "只要思路"

Workflow
1) Discover tools
- Enumerate tools/resources/prompts.
- Mark read-only vs write.

2) Validate intent
- Normalize: Input -> Transformation -> Output.
- Validate required fields against schema.

3) Gate and execute
- Apply confirmation policy in references/confirmation-matrix.md.
- Execute smallest deterministic chain.
- Capture trace refs: tool, key params, result id.

4) Return
- Final result.
- Executed actions.
- Pending actions (if any).

Fallback
- Apply fallback codes in references/fallback-codes.md.

Output format
- result: one-line final outcome
- executed_actions: list of {tool, key_params, result_id}
- pending_actions: list (empty if none)
- trace_refs: list of stable references/ids
- fallback: {code, cause, next_action} (only when fallback occurs)
- limits: omit unless material
