# Serverless Architecture Patterns

**Category:** Serverless & Cloud Native
**Level:** Advanced
**Auto-trigger:** When user mentions serverless patterns, Lambda architecture, or FaaS design

---

## Description

Implements serverless architecture patterns including event-driven functions, choreography vs orchestration, serverless data patterns, and multi-cloud serverless deployments.

---

## Activation Phrases

- "Set up serverless architecture"
- "Create Lambda function"
- "Implement serverless pattern"
- "Configure event-driven serverless"
- "Set up Step Functions"

---

## Common Patterns

### 1. Event-Driven Processing
- S3 → Lambda → DynamoDB
- EventBridge → Multiple Lambdas
- SQS → Lambda (async processing)

### 2. API Gateway Pattern
- API Gateway → Lambda → Database
- GraphQL → Lambda → Multiple sources

### 3. Stream Processing
- Kinesis/Kafka → Lambda → Analytics
- DynamoDB Streams → Lambda → Aggregations

### 4. Orchestration
- Step Functions for workflows
- EventBridge for choreography

---

**Last Updated:** 2025-11-02
