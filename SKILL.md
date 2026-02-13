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
1) Discover capability
- Enumerate tools/resources/prompts.
- Mark read-only vs write.

2) Map intent
- Normalize: Input -> Transformation -> Output.
- Validate required fields against schema.

3) Confirm write actions
- Write: 1 confirmation.
- High-risk (payment/account/security): 2 confirmations.

4) Execute minimally
- Run smallest deterministic chain.
- Capture trace refs: tool, key params, result id.

5) Return result
- Final result
- Executed actions
- Pending actions (if any)

Fallback
- Missing tool: shortest manual path.
- Schema mismatch: invalid fields + expected shape.
- Runtime failure: bounded retry then clear downgrade path.

Output format
- Result
- Executed actions
- Pending actions
- Trace references
- Limits (only if material)
