# Onboarding and Target Strategy

## Decision

The workflow MUST start with a proactive onboarding agent. No discovery, code generation, synthetic-data generation, or migration execution may start until the onboarding gate reaches `ready` or an authorized user explicitly accepts documented assumptions.

## Why this is required

A migration factory cannot infer critical business and platform constraints safely from source metadata alone. The onboarding agent establishes the migration contract, removes ambiguity, and creates an auditable baseline for downstream agents.

## Target platforms

Microsoft Fabric and Databricks are first-class targets.

### Microsoft Fabric target profile

The onboarding agent must determine:

- Fabric capacity, tenant, region, workspace and deployment stage.
- OneLake and Lakehouse/Warehouse destination pattern.
- Shortcut, copy, mirroring or pipeline ingestion strategy.
- Delta table, Warehouse table and semantic-model requirements.
- Data Factory pipeline and notebook orchestration preferences.
- Purview, sensitivity labels, RLS/OLS and tenant governance constraints.
- Direct Lake, Import or DirectQuery consumption requirements.

### Databricks target profile

The onboarding agent must determine:

- Cloud, region, account, workspace and network topology.
- Unity Catalog metastore, catalogs, schemas and external locations.
- Delta Lake table strategy and medallion-layer requirements.
- Serverless, SQL Warehouse, job cluster or existing-cluster execution.
- Auto Loader, Lakeflow/Jobs, DLT or notebook orchestration preferences.
- Secrets, service principals, managed identities and private connectivity.
- Data quality expectations, lineage and cluster-policy constraints.

## Proactive questioning model

Questions should be adaptive, not a static questionnaire. Each answer can open, skip or reprioritize subsequent questions. The agent should:

1. Ask one coherent question group at a time.
2. Explain why the information matters.
3. Offer constrained options where possible.
4. Detect contradictions and request resolution.
5. Propose defaults, but label them as assumptions.
6. Summarize the current migration contract after each section.
7. Stop the workflow when blocking information is missing.

## Required onboarding domains

1. Business scope and migration objectives.
2. Source systems and object inventory.
3. Target selection: Databricks, Fabric or dual-target.
4. Workload classification: batch, streaming, BI, ML, operational or hybrid.
5. Data volume, growth, latency, retention and SLA.
6. Security, privacy, residency and regulatory constraints.
7. Connectivity, credentials and network restrictions.
8. Data-quality baseline and reconciliation thresholds.
9. Historical-load, CDC and cutover strategy.
10. Synthetic-data requirements and prohibited production-data usage.
11. Testing environments and acceptance criteria.
12. Rollback, hypercare, ownership and approval model.

## Readiness gates

The onboarding agent produces a readiness score and blocking findings.

- `blocked`: missing mandatory information, unresolved security risk or no target contract.
- `needs_review`: assumptions exist or conflicting answers require approval.
- `ready`: mandatory domains are complete and acceptance criteria are explicit.

## Output contract

The agent emits a versioned `MigrationIntake` artifact containing:

- source systems and selected objects;
- target platform profile;
- workload and non-functional requirements;
- security and governance controls;
- synthetic-data policy;
- migration waves and priorities;
- reconciliation thresholds;
- assumptions, risks and unresolved questions;
- approval status and approver identity.

All downstream agents consume this artifact rather than independently reinterpreting user intent.
