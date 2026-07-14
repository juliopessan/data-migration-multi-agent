# Codex operating instructions

## Mission
Build and evolve a safe, auditable multi-agent data migration factory. Preserve deterministic execution for migration-critical operations; use LLMs only for analysis, mapping suggestions, code generation, and exception explanation.

## Engineering rules
- Never execute destructive source-system operations.
- Every generated transformation requires validation, lineage, and approval metadata.
- Synthetic data must not be derived by copying production PII; generate from schema and statistical constraints only.
- Secrets stay in environment variables or a secret manager.
- Add tests for every adapter and orchestration state transition.
- Keep platform-specific behavior behind adapters.
- Produce machine-readable evidence in `outputs/<pipeline>/<run_id>/`.

## Definition of done
`pytest` passes; dry-run completes; artifacts include inventory, mapping, plan, validation and audit records; no credentials or production data are committed.
