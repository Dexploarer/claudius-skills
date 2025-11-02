# /setup-data-pipeline - Data Pipeline Setup

Set up ETL/ELT data pipelines with orchestration and monitoring.

---

## Usage

```
/setup-data-pipeline [type] [name]
/setup-data-pipeline --scheduler [airflow|prefect|dagster]
```

Examples:
- `/setup-data-pipeline etl user-analytics`
- `/setup-data-pipeline streaming clickstream`
- `/setup-data-pipeline --scheduler airflow`

---

## What This Command Does

1. **Pipeline Orchestration Setup**
   - **Airflow:** Complex workflows, scheduling
   - **Prefect:** Pythonic, dynamic pipelines
   - **Dagster:** Asset-based, data quality
   - **Temporal:** Durable execution

2. **Data Sources Integration**
   - Databases (PostgreSQL, MySQL, MongoDB)
   - APIs (REST, GraphQL)
   - Files (S3, GCS, Azure Blob)
   - Streams (Kafka, Kinesis, Pub/Sub)

3. **Transformation Layer**
   - dbt for SQL transformations
   - PySpark for large datasets
   - Pandas for smaller datasets
   - Data validation (Great Expectations)

4. **Data Quality**
   - Schema validation
   - Data profiling
   - Anomaly detection
   - Quality metrics

5. **Monitoring & Alerting**
   - Pipeline health
   - Data freshness
   - Quality metrics
   - SLA tracking

---

## Pipeline Types

### Batch ETL
- Scheduled runs (hourly, daily)
- Extract → Transform → Load
- Incremental updates
- Backfill support

### Streaming Pipeline
- Real-time processing
- Kafka/Kinesis consumers
- Stream transformations
- Exactly-once semantics

### Reverse ETL
- Warehouse → Operational systems
- Customer data to CRM
- Analytics to business tools
- Scheduled syncs

---

## Output

```
📊 DATA PIPELINE CONFIGURED

Pipeline: user-analytics-etl
Orchestrator: Apache Airflow
Schedule: Daily at 2 AM UTC

Components:
✓ DAG created: user_analytics_dag.py
✓ Extractors: PostgreSQL, Stripe API, S3
✓ Transformations: dbt models (12 models)
✓ Destination: Snowflake data warehouse
✓ Quality checks: 8 validation rules

Monitoring:
✓ Airflow UI: http://localhost:8080
✓ dbt docs: http://localhost:8081
✓ Alerts: #data-pipeline-alerts

Next Steps:
1. Review DAG in Airflow UI
2. Test pipeline with sample data
3. Schedule production run
4. Monitor first execution

Documentation: ./pipelines/user-analytics/README.md
```

---

**Related Commands:**
- `/validate-data` - Data quality checks
- `/backfill-pipeline` - Historical data processing
