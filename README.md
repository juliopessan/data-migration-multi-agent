# Data Migration Multi-Agent Factory

Enterprise AI-first migration platform targeting **Microsoft Fabric** and **Databricks**.

## Highlights
- Python SDK with pluggable agents and connectors
- Markdown/YAML agent definitions
- Mandatory adaptive onboarding agent
- Microsoft Fabric and Databricks as first-class targets
- Synthetic data generation with referential integrity
- Native telemetry (tokens, latency, cost, quality)
- Budget gates and economic policies
- Optional Headroom optimization layer
- Approval workflow and audit evidence

## Architecture
Runtime (Python SDK)
- Agent Runtime
- Plugin Registry
- Workflow Engine
- Budget Engine
- Telemetry

Declarative Layer
- prompt.md
- agent.yaml
- policies.yaml
- schemas

## Workflow
Onboarding → Discovery → Mapping → Target Planning → Synthetic Data → Validation → Reconciliation → Approval → Execution

## Financial-first design
Every LLM call is measured before and after execution.

Tracked metrics:
- input/output tokens
- cached tokens
- estimated cost
- latency
- compression ratio
- cost per migration
- cost per migrated object

Compression is optional. If Headroom does not achieve the configured savings threshold or quality gates fail, the runtime automatically falls back to the original context.

## Roadmap
- Source connectors
- Fabric deployment engine
- Databricks deployment engine
- GitHub Actions CI
- OpenTelemetry
- Azure Monitor
- Application Insights
- Benchmark suite
