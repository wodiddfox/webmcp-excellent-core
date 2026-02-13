---
name: webmcp-excellent-core
description: Execute WebMCP actions with strict scope, write-confirmation gates, deterministic flow, and traceable outputs for production web tasks.
---

# webmcp-excellent-core

Use when
- User asks for executable web tasks through structured tools: search/filter/submit/update.
- Reliability and reproducibility are required (not best-effort clicking).

Do not use when
- Request is only ideation/brainstorming with no executable action.
- No WebMCP-capable tool exists and user only needs generic advice.

Trigger signals
- "帮我在网页里查找并筛选后提交"
- "按条件下单/创建工单/更新状态"
- "需要可追溯的执行结果"

Non-trigger signals
- "先聊聊方案，不要执行"
- "只给思路，不做操作"

Workflow
1) Discover capability
- List available tools/resources/prompts.
- Mark each tool: read-only or write.

2) Map intent
- Normalize to Input -> Transformation -> Output.
- Validate required fields against tool schema.

3) Confirm write actions
- Write actions: explicit confirmation once.
- High-risk (payment/account/security): double confirmation.

4) Execute minimally
- Run the smallest deterministic tool chain.
- Capture trace refs: tool name, key params, result id.

5) Return result
- Final outcome
- Executed actions
- Pending actions (if any)

Fallback
- Missing tool: shortest manual path.
- Schema mismatch: invalid fields + expected shape.
- Runtime failure: bounded retry, then degrade with clear next step.

Output format
- Result
- Executed actions
- Pending actions
- Trace references
- Limits (only if material)
