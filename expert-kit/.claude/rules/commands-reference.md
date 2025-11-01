# Expert Pack Commands Reference

Complete reference for all 20 advanced automation commands.

## Deployment & Release Commands (5)

### /release-orchestrator
**Purpose:** Multi-service coordinated releases
**Usage:** `/release-orchestrator <service1>,<service2>,<service3>`
**Features:** Dependency ordering, health checks, automatic rollback

### /canary-deploy
**Purpose:** Progressive canary deployment
**Usage:** `/canary-deploy <service> <version>`
**Features:** Traffic splitting, metric monitoring, automatic rollback

### /blue-green-deploy
**Purpose:** Zero-downtime blue-green deployment
**Usage:** `/blue-green-deploy <service> <version>`
**Features:** Instant cutover, quick rollback, zero downtime

### /rollback-emergency
**Purpose:** Emergency rollback to previous version
**Usage:** `/rollback-emergency <service>`
**Features:** Fast rollback, health verification, minimal downtime

### /feature-flag-toggle
**Purpose:** Toggle feature flags
**Usage:** `/feature-flag-toggle <flag> [on|off]`
**Features:** Runtime toggling, gradual rollouts, quick disable

## Compliance & Audit Commands (4)

### /compliance-scan
**Purpose:** Full compliance audit
**Usage:** `/compliance-scan [soc2|hipaa|gdpr|pci|all]`
**Features:** Multi-framework scanning, detailed reports, remediation plans

### /adr-create
**Purpose:** Create Architecture Decision Record
**Usage:** `/adr-create <title>`
**Features:** Numbered ADRs, templates, decision tracking

### /sla-report
**Purpose:** Generate SLA compliance reports
**Usage:** `/sla-report [service]`
**Features:** Uptime tracking, performance metrics, SLO compliance

### /security-posture
**Purpose:** Comprehensive security assessment
**Usage:** `/security-posture`
**Features:** Vulnerability scanning, configuration review, recommendations

## Incident Response Commands (4)

### /incident-declare
**Purpose:** Declare production incident
**Usage:** `/incident-declare <severity>`
**Features:** Team notification, war room setup, timeline tracking

### /runbook-execute
**Purpose:** Execute incident runbooks
**Usage:** `/runbook-execute <runbook-name>`
**Features:** Automated procedures, verification steps, logging

### /postmortem-generate
**Purpose:** Generate postmortem template
**Usage:** `/postmortem-generate <incident-id>`
**Features:** Timeline generation, action items, learning capture

### /oncall-schedule
**Purpose:** Manage on-call schedules
**Usage:** `/oncall-schedule`
**Features:** Rotation management, escalation policies, coverage

## Platform Operations Commands (7)

### /environment-clone
**Purpose:** Clone complete environment
**Usage:** `/environment-clone <source> <target>`
**Features:** Full config copy, data migration, validation

### /data-migration
**Purpose:** Orchestrate data migration
**Usage:** `/data-migration <plan>`
**Features:** Safe migration, validation, rollback capability

### /traffic-replay
**Purpose:** Replay production traffic
**Usage:** `/traffic-replay <source>`
**Features:** Traffic capture, replay to staging, validation

### /load-test-suite
**Purpose:** Comprehensive load testing
**Usage:** `/load-test-suite <target>`
**Features:** Ramp-up testing, sustained load, reporting

### /dependency-graph
**Purpose:** Service dependency visualization
**Usage:** `/dependency-graph`
**Features:** Graphical visualization, impact analysis, export

### /tech-debt-audit
**Purpose:** Analyze technical debt
**Usage:** `/tech-debt-audit`
**Features:** Code analysis, prioritization, ROI calculation

### /cost-analysis
**Purpose:** Multi-cloud cost analysis
**Usage:** `/cost-analysis [aws|gcp|azure|all]`
**Features:** Cost breakdown, optimization tips, forecasting

---

**Total Commands:** 20
**Categories:** Deployment (5), Compliance (4), Incident (4), Platform (7)
**Last Updated:** $(date +%Y-%m-%d)
