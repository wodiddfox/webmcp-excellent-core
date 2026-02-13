---
name: webmcp-excellent-core
description: Production-grade WebMCP skill with strict contracts, confirmation gates, fallback policy, and traceable outputs. Goal: 面向生产环境的WebMCP通用技能执行底座
---

# webmcp-excellent-core

Goal
- 面向生产环境的WebMCP通用技能执行底座

Trigger policy
- Trigger when user requests structured web actions (search/filter/submit/update) with reliability requirements.
- Do not trigger for pure brainstorming that has no executable step.

Risk policy
- low: read-only data retrieval
- medium: state change in non-critical workflows
- high: payment/account/security sensitive operations

Execution contract
1) Capability discovery
- Detect available WebMCP tools/resources/prompts.
- Build tool map: read-only vs write.

2) Intent mapping
- Convert request into Input -> Transformation -> Output.
- Validate against target tool input schema.

3) Safety gate
- For any write action: explicit confirmation required.
- For high-risk flows: require double confirmation (summary + final intent).

4) Deterministic execution
- Execute minimal required tool chain.
- Collect action references (tool name, key params, result id).

5) Result packaging
- Return concise final outcome.
- Return what was executed and what was not executed.
- Return fallback/manual path when partial failure occurs.

Fallback policy
- Missing tool: provide compatible manual path with minimum steps.
- Schema mismatch: list invalid fields and expected schema shape.
- Runtime/tool failure: bounded retry, then degrade with explicit next action.

Output contract
- Final result
- Executed actions (tool + key params)
- Pending actions (if any)
- References/IDs for traceability
- Limits/uncertainty (only when needed)

Acceptance gate (must pass)
- Trigger clarity
- Tool contract completeness
- Confirmation points for write actions
- Deterministic core path
- Explicit fallback behavior
