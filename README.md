# Data Migration Multi-Agent Factory

Scaffold generated from `migration_agent_checklist.xlsx`: **10 systems**, **110 file patterns**, and **105 migration tasks**.

## Covered systems
- Cloudera
- Airflow
- SYSS
- SAP BOBJ
- PowerCenter
- Snowflake
- Teradata
- Oracle Exadata - ADW
- IBM Db2 Warehouse
- SAP BW - HANA

## Agent topology
1. Supervisor — controls state, policy gates and retries.
2. Discovery — inventories files, schemas, jobs and dependencies.
3. Platform specialists — interpret each source system.
4. Schema mapper — proposes source-to-target mappings.
5. Transformation engineer — generates SQL/Python conversion assets.
6. Synthetic data — creates referentially consistent, PII-safe test datasets.
7. Execution planner — builds dependency-aware migration waves.
8. Data quality — profiles, validates and compares source/target.
9. Reconciliation — row counts, checksums, aggregates and business rules.
10. Security/governance — secrets, policies, lineage and approval checks.
11. Evidence/audit — writes an immutable run manifest and artifacts.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
migration-agents dry-run --system Snowflake
uvicorn migration_agents.api:app --reload
```

## Important boundary
The initial implementation is a safe control-plane scaffold. It inventories and plans migrations, generates synthetic test data, and emits validation evidence. Production connectors and target-specific execution commands must be enabled explicitly after credentials, network paths, target platform, and approval policy are configured.
