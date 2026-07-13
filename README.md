# Data Migration Multi-Agent Factory

[![CI](https://github.com/juliopessan/data-migration-multi-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/juliopessan/data-migration-multi-agent/actions/workflows/ci.yml)

An AI-first, financially governed migration SDK for preparing and validating enterprise data workloads targeting **Microsoft Fabric** and **Databricks**.

Developer tools: see [RTK Integration](RTK.md) for repository helpers to install and initialize the `rtk` CLI for token-optimized command output and developer workflows.

The platform combines a typed Python runtime, declarative agent definitions, extensible plugins, synthetic test data, native telemetry, token budgets, and optional Headroom context compression.

## Design principles

- **Onboarding first:** discovery cannot start until business, technical, security, target, testing, and acceptance requirements are complete.
- **Python owns execution:** contracts, state, validation, retries, budgets, telemetry, approvals, and integrations are implemented as testable Python components.
- **Markdown and YAML own behavior:** prompts, questions, policies, examples, and platform configuration remain declarative and versionable.
- **Fabric and Databricks are first-class targets:** each platform receives an independent target contract and deployment plan.
- **Cost is a runtime constraint:** token and cost limits are enforced before model calls, not discovered on an invoice later.
- **Quality outranks compression:** Headroom is optional and compression is accepted only when savings clear configured economic and quality gates.

## Architecture

```text
User
  -> Proactive Onboarding Agent
  -> Versioned MigrationIntake
  -> Readiness Gate
  -> Discovery and Source Plugins
  -> Mapping and Transformation Agents
  -> Fabric / Databricks Target Adapters
  -> Synthetic Data and Migration Simulation
  -> Validation and Reconciliation
  -> Human Approval
  -> Controlled Execution

Every agent call
  -> Redaction
  -> Token and Cost Budget Gate
  -> Optional Headroom Optimization
  -> LLM Gateway
  -> Native Telemetry
  -> Quality Gate
```

## SDK layout

```text
src/
├── migration_sdk/
│   ├── core/             # agent contracts, runtime and plugin registry
│   ├── contracts/        # immutable migration and target contracts
│   ├── economics/        # token and cost budget policies
│   ├── optimization/     # optional Headroom adapter
│   ├── plugins/          # onboarding and future installable agents
│   ├── targets/          # Microsoft Fabric and Databricks adapters
│   └── telemetry/        # token, cost, latency and run events
└── migration_agents/     # API, CLI and migration control-plane scaffold
```

## Current source coverage

The initial catalog was generated from `migration_agent_checklist.xlsx` and covers Cloudera, Airflow, SSIS, SAP BusinessObjects, Informatica PowerCenter, Snowflake, Teradata, Oracle Exadata/ADW, IBM Db2 Warehouse, and SAP BW/HANA.

Connectors are being implemented incrementally behind stable source-plugin contracts.

## Target platforms

### Microsoft Fabric

Target planning covers OneLake landing zones, Lakehouse or Warehouse selection, Fabric Data Factory pipelines, notebooks, SQL assets, semantic models, Purview, lineage, reconciliation, and workspace/capacity constraints.

### Databricks

Target planning covers Unity Catalog, Delta Lake, catalogs and schemas, external locations, Lakeflow jobs and pipelines, notebooks, compute policy, lineage, access controls, and reconciliation.

Dual-target initiatives maintain separate contracts so that Fabric and Databricks decisions do not leak into each other.

## Proactive onboarding

The onboarding agent asks only the next relevant questions and produces one of three readiness states:

- `blocked`: mandatory, security, or residency information is unresolved.
- `needs_review`: explicit assumptions require human approval.
- `ready`: discovery may begin.

The workflow cannot continue without a selected target and an approved synthetic-data policy.

## Financial governance and Headroom

Native telemetry records token usage, estimated cost, latency, model, agent, workflow stage, source system, and target platform. Prompt content is not captured by default.

Budget policies can fail closed when per-call or per-run token and cost limits are exceeded. Headroom is loaded lazily and remains optional:

```bash
pip install -e ".[headroom]"
```

Compression is used only when measured savings exceed the configured threshold. A holdout group and reconciliation gates protect quality, while the original context remains the fallback.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[dev]"

ruff check .
mypy src
pytest -q
python -m build
```

Run the existing control plane:

```bash
migration-agents dry-run --system Snowflake
uvicorn migration_agents.api:app --reload
```

## CI quality gates

GitHub Actions validates Python 3.11 and 3.12 with:

- Ruff linting and import checks;
- strict mypy type checking;
- pytest unit tests;
- source and wheel builds;
- clean wheel installation and import smoke tests.

## Safety boundary

The repository currently provides a safe control plane for onboarding, discovery planning, mappings, synthetic test data, target planning, telemetry, and validation evidence. Production extraction, deployment, and cutover require explicit credentials, network configuration, policy approval, and human authorization.

## Roadmap

Near-term work includes the workflow state machine, OpenTelemetry exporters, source connector contracts, Snowflake and Oracle discovery, deeper Fabric and Databricks planners, secrets redaction middleware, synthetic data integration, and migration-cost dashboards.
