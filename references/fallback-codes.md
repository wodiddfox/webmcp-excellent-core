# Fallback Codes

- F1_MISSING_TOOL: no required tool available
- F2_SCHEMA_MISMATCH: input does not match required schema
- F3_RUNTIME_FAILURE: execution failed after bounded retries

For each fallback, return:
- code
- cause
- next action
