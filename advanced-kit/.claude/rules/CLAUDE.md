# Advanced Kit - Enterprise-Level Rules

> **Level 4: Enterprise/Master Claude Code Configuration**
> Enterprise-grade tools for distributed systems, compliance, and platform engineering.

---

## 🎯 Purpose

The Advanced Kit provides **enterprise-grade capabilities** for technical leaders and architects:
- 15 enterprise skills (microservices, compliance, observability, platform engineering)
- 20 advanced automation commands (deployment, incident response, compliance)
- 10 specialist consultant subagents (architects, SRE, compliance, security)
- Production-critical hooks with compliance enforcement
- Full observability stack integration
- Multi-cloud and platform engineering support

**Target Audience:** Enterprise architects, staff engineers, platform teams, SREs, compliance officers building production-critical systems at scale

---

## 📚 Available Capabilities

### Enterprise Skills (15 Total)
All skills located in: `advanced-kit/.claude/skills/`

#### Architecture & Design (4 skills):

1. **microservices-orchestrator** - Design and manage microservices architectures
   - Auto-invoked: "design microservices", "split into microservices", "service architecture"
   - Features: Service decomposition, bounded contexts, API contracts, service mesh
   - Reference: `@advanced-kit/.claude/skills/microservices-orchestrator.md`

2. **api-gateway-configurator** - Configure API gateways
   - Auto-invoked: "configure API gateway", "set up Kong", "API gateway patterns"
   - Features: Kong, Tyk, AWS API Gateway, rate limiting, authentication
   - Reference: `@advanced-kit/.claude/skills/api-gateway-configurator.md`

3. **event-driven-architect** - Design event-driven systems
   - Auto-invoked: "design event-driven", "Kafka architecture", "event sourcing"
   - Features: Kafka, RabbitMQ, event sourcing, CQRS, saga patterns
   - Reference: `@advanced-kit/.claude/skills/event-driven-architect.md`

4. **service-mesh-integrator** - Configure service meshes
   - Auto-invoked: "configure service mesh", "set up Istio", "Linkerd setup"
   - Features: Istio, Linkerd, Consul, traffic management, security policies
   - Reference: `@advanced-kit/.claude/skills/service-mesh-integrator.md`

#### Compliance & Governance (4 skills):

5. **compliance-auditor** - SOC2, HIPAA, GDPR, PCI-DSS compliance
   - Auto-invoked: "compliance audit", "SOC2 check", "HIPAA compliance", "GDPR audit"
   - Features: Automated compliance scanning, evidence collection, gap analysis
   - Reference: `@advanced-kit/.claude/skills/compliance-auditor.md`

6. **architecture-decision-recorder** - Create and manage ADRs
   - Auto-invoked: "create ADR", "document decision", "architecture decision"
   - Features: ADR templates, decision documentation, traceability
   - Reference: `@advanced-kit/.claude/skills/architecture-decision-recorder.md`

7. **sla-monitor-generator** - SLA/SLO/SLI monitoring
   - Auto-invoked: "create SLO", "define SLA", "error budget", "reliability targets"
   - Features: SLO/SLI definitions, error budgets, alerting rules
   - Reference: `@advanced-kit/.claude/skills/sla-monitor-generator.md`

8. **disaster-recovery-planner** - DR strategy and automation
   - Auto-invoked: "disaster recovery plan", "DR strategy", "backup strategy"
   - Features: RTO/RPO calculation, backup automation, failover procedures
   - Reference: `@advanced-kit/.claude/skills/disaster-recovery-planner.md`

#### Observability & Performance (4 skills):

9. **distributed-tracing-setup** - Configure distributed tracing
   - Auto-invoked: "set up tracing", "configure Jaeger", "distributed tracing"
   - Features: Jaeger, Zipkin, Datadog APM, AWS X-Ray, OpenTelemetry
   - Reference: `@advanced-kit/.claude/skills/distributed-tracing-setup.md`

10. **metrics-pipeline-builder** - Build metrics pipelines
    - Auto-invoked: "metrics pipeline", "Prometheus setup", "Grafana dashboards"
    - Features: Prometheus, Grafana, Datadog, CloudWatch, custom metrics
    - Reference: `@advanced-kit/.claude/skills/metrics-pipeline-builder.md`

11. **log-aggregation-configurator** - Centralized logging
    - Auto-invoked: "centralize logs", "ELK stack", "log aggregation"
    - Features: ELK, Loki, Splunk, Fluentd, structured logging
    - Reference: `@advanced-kit/.claude/skills/log-aggregation-configurator.md`

12. **chaos-engineering-setup** - Chaos testing framework
    - Auto-invoked: "chaos engineering", "resilience testing", "chaos experiment"
    - Features: Chaos Monkey, Litmus, chaos experiments, resilience patterns
    - Reference: `@advanced-kit/.claude/skills/chaos-engineering-setup.md`

#### Platform Engineering (3 skills):

13. **internal-platform-builder** - Build internal developer platforms
    - Auto-invoked: "build platform", "developer platform", "internal platform"
    - Features: Platform architecture, self-service, golden paths
    - Reference: `@advanced-kit/.claude/skills/internal-platform-builder.md`

14. **developer-portal-generator** - Create developer portals
    - Auto-invoked: "developer portal", "Backstage setup", "API catalog"
    - Features: Backstage, documentation portals, API catalogs
    - Reference: `@advanced-kit/.claude/skills/developer-portal-generator.md`

15. **golden-path-creator** - Define and enforce golden paths
    - Auto-invoked: "golden path", "platform standards", "best practices"
    - Features: Standard templates, scaffolding, enforcement patterns
    - Reference: `@advanced-kit/.claude/skills/golden-path-creator.md`

---

### Advanced Commands (20 Total)
All commands located in: `advanced-kit/.claude/commands/`

#### Deployment & Release (5 commands):

- `/release-orchestrator` - Multi-service coordinated releases
  - Usage: `/release-orchestrator <services>` → Orchestrate multi-service release
  - Reference: `@advanced-kit/.claude/commands/release-orchestrator.md`

- `/canary-deploy` - Canary deployment automation
  - Usage: `/canary-deploy <service>` → Progressive canary rollout
  - Reference: `@advanced-kit/.claude/commands/canary-deploy.md`

- `/blue-green-deploy` - Blue-green deployment
  - Usage: `/blue-green-deploy <service>` → Zero-downtime deployment
  - Reference: `@advanced-kit/.claude/commands/blue-green-deploy.md`

- `/rollback-emergency` - Emergency rollback procedures
  - Usage: `/rollback-emergency <service>` → Immediate rollback
  - Reference: `@advanced-kit/.claude/commands/rollback-emergency.md`

- `/feature-flag-toggle` - Feature flag management
  - Usage: `/feature-flag-toggle <flag>` → Toggle feature flags
  - Reference: `@advanced-kit/.claude/commands/feature-flag-toggle.md`

#### Compliance & Audit (4 commands):

- `/compliance-scan` - Full compliance audit
  - Usage: `/compliance-scan [framework]` → SOC2/HIPAA/GDPR/PCI audit
  - Reference: `@advanced-kit/.claude/commands/compliance-scan.md`

- `/adr-create` - Create architecture decision record
  - Usage: `/adr-create <title>` → Document architectural decision
  - Reference: `@advanced-kit/.claude/commands/adr-create.md`

- `/sla-report` - Generate SLA compliance report
  - Usage: `/sla-report [service]` → SLA/SLO compliance reporting
  - Reference: `@advanced-kit/.claude/commands/sla-report.md`

- `/security-posture` - Comprehensive security assessment
  - Usage: `/security-posture` → Full security posture audit
  - Reference: `@advanced-kit/.claude/commands/security-posture.md`

#### Incident Response (4 commands):

- `/incident-declare` - Declare and track incidents
  - Usage: `/incident-declare <severity>` → Start incident response
  - Reference: `@advanced-kit/.claude/commands/incident-declare.md`

- `/runbook-execute` - Execute incident runbooks
  - Usage: `/runbook-execute <runbook>` → Execute predefined runbook
  - Reference: `@advanced-kit/.claude/commands/runbook-execute.md`

- `/postmortem-generate` - Generate postmortem templates
  - Usage: `/postmortem-generate <incident-id>` → Create postmortem doc
  - Reference: `@advanced-kit/.claude/commands/postmortem-generate.md`

- `/oncall-schedule` - Manage on-call schedules
  - Usage: `/oncall-schedule` → View/manage on-call rotation
  - Reference: `@advanced-kit/.claude/commands/oncall-schedule.md`

#### Platform Operations (7 commands):

- `/environment-clone` - Clone entire environments
  - Usage: `/environment-clone <source> <target>` → Clone environment
  - Reference: `@advanced-kit/.claude/commands/environment-clone.md`

- `/data-migration` - Orchestrate data migrations
  - Usage: `/data-migration <plan>` → Execute data migration
  - Reference: `@advanced-kit/.claude/commands/data-migration.md`

- `/traffic-replay` - Replay production traffic
  - Usage: `/traffic-replay <source>` → Replay traffic for testing
  - Reference: `@advanced-kit/.claude/commands/traffic-replay.md`

- `/load-test-suite` - Comprehensive load testing
  - Usage: `/load-test-suite <target>` → Execute load tests
  - Reference: `@advanced-kit/.claude/commands/load-test-suite.md`

- `/dependency-graph` - Service dependency visualization
  - Usage: `/dependency-graph` → Generate dependency graph
  - Reference: `@advanced-kit/.claude/commands/dependency-graph.md`

- `/tech-debt-audit` - Analyze and prioritize tech debt
  - Usage: `/tech-debt-audit` → Assess technical debt
  - Reference: `@advanced-kit/.claude/commands/tech-debt-audit.md`

- `/cost-analysis` - Multi-cloud cost analysis
  - Usage: `/cost-analysis [cloud]` → Analyze cloud costs
  - Reference: `@advanced-kit/.claude/commands/cost-analysis.md`

---

### Specialist Subagents (10 Total)
All agents located in: `advanced-kit/.claude/agents/`

#### Architecture & Design Consultants (4 agents):

1. **enterprise-architect** - System architecture design expert
   - Invocation: "Use enterprise-architect to design the architecture"
   - Expertise: Distributed systems, scalability, design patterns
   - Tools: Read, Grep, Glob
   - Reference: `@advanced-kit/.claude/agents/enterprise-architect.md`

2. **distributed-systems-architect** - Microservices and distributed patterns
   - Invocation: "Use distributed-systems-architect for microservices design"
   - Expertise: Microservices, event-driven, CQRS, saga patterns
   - Tools: Read, Grep, Glob
   - Reference: `@advanced-kit/.claude/agents/distributed-systems-architect.md`

3. **data-architect** - Data modeling and pipelines
   - Invocation: "Use data-architect to design the data architecture"
   - Expertise: Data warehouses, lakes, pipelines, modeling
   - Tools: Read, Grep, Glob
   - Reference: `@advanced-kit/.claude/agents/data-architect.md`

4. **platform-engineer** - Internal platform specialist
   - Invocation: "Use platform-engineer to build the developer platform"
   - Expertise: Platform engineering, golden paths, self-service
   - Tools: Read, Write, Bash, Grep
   - Reference: `@advanced-kit/.claude/agents/platform-engineer.md`

#### Operations & Reliability Consultants (4 agents):

5. **sre-consultant** - SRE best practices expert
   - Invocation: "Use sre-consultant for SLO design"
   - Expertise: SRE, SLO/SLI, error budgets, reliability
   - Tools: Read, Grep, Bash
   - Reference: `@advanced-kit/.claude/agents/sre-consultant.md`

6. **incident-commander** - Incident response expert
   - Invocation: "Use incident-commander for incident response"
   - Expertise: Incident management, runbooks, postmortems
   - Tools: Read, Bash, Grep
   - Reference: `@advanced-kit/.claude/agents/incident-commander.md`

7. **chaos-engineer** - Resilience testing specialist
   - Invocation: "Use chaos-engineer to design chaos experiments"
   - Expertise: Chaos engineering, resilience, failure modes
   - Tools: Read, Bash, Grep
   - Reference: `@advanced-kit/.claude/agents/chaos-engineer.md`

8. **finops-analyst** - Cloud cost optimization expert
   - Invocation: "Use finops-analyst to reduce cloud costs"
   - Expertise: FinOps, cost optimization, multi-cloud
   - Tools: Read, Grep, Bash
   - Reference: `@advanced-kit/.claude/agents/finops-analyst.md`

#### Compliance & Security Consultants (2 agents):

9. **compliance-officer** - Regulatory compliance expert
   - Invocation: "Use compliance-officer for SOC2 compliance"
   - Expertise: SOC2, HIPAA, GDPR, PCI-DSS, auditing
   - Tools: Read, Grep
   - Reference: `@advanced-kit/.claude/agents/compliance-officer.md`

10. **security-architect** - Security architecture expert
    - Invocation: "Use security-architect for zero-trust design"
    - Expertise: Zero-trust, threat modeling, defense-in-depth
    - Tools: Read, Grep
    - Reference: `@advanced-kit/.claude/agents/security-architect.md`

---

### Production-Critical Hooks
Configuration: `advanced-kit/.claude/settings.json`

**PreToolUse Hooks (Enterprise Safety):**
- ✅ Production deployment multi-stage approval
- ✅ PII/PHI detection in code and commits
- ✅ Compliance policy enforcement (SOC2, HIPAA, GDPR)
- ✅ Cost threshold warnings (cloud spend gates)
- ✅ Breaking change detection (API versioning)
- ✅ License compliance checking
- ✅ Security policy enforcement
- ✅ Data retention policy validation
- ✅ Secret detection (enhanced enterprise patterns)
- ✅ Force push prevention (main/master/production branches)

**PostToolUse Hooks (Observability):**
- Deployment success/failure notifications
- Performance regression detection
- Cost anomaly alerts
- SLA breach warnings
- Security incident creation
- Audit log generation
- Metric emission to observability platform

**SessionStart/End Hooks:**
- Environment context loading
- Compliance mode activation
- Session audit logging
- Cost tracking and reporting

---

## 🎓 Enterprise Workflow

### Recommended Usage Pattern:

1. **Architecture Design Phase**
   ```
   You: "Design microservices architecture for e-commerce platform"

   Claude:
   → Uses enterprise-architect agent first
   → Activates microservices-orchestrator skill
   → Creates /adr-create for decisions
   → Suggests service-mesh-integrator
   ```

2. **Compliance Setup**
   ```
   You: "We need SOC2 Type II compliance"

   Commands:
   /compliance-scan soc2 → Initial assessment
   /security-posture → Security audit

   Agent:
   Use compliance-officer agent → Gap analysis

   Skill:
   compliance-auditor → Continuous monitoring
   ```

3. **Platform Engineering**
   ```
   You: "Build internal developer platform"

   Agent:
   Use platform-engineer agent → Platform design

   Skills:
   internal-platform-builder → Platform architecture
   developer-portal-generator → Portal setup
   golden-path-creator → Standards definition

   Commands:
   /environment-clone → Template environments
   ```

4. **Incident Response**
   ```
   You: "Production database is down"

   Commands:
   /incident-declare severity-1 → Start incident

   Agent:
   Use incident-commander agent → Response coordination

   Commands:
   /runbook-execute db-failover → Execute runbook
   /rollback-emergency api-service → Rollback if needed
   /postmortem-generate INC-123 → Post-incident review
   ```

---

## 📖 Framework Support

### Enterprise Frameworks:
- **Microservices** - Service decomposition, bounded contexts
- **Event-Driven** - Kafka, RabbitMQ, event sourcing, CQRS
- **Service Mesh** - Istio, Linkerd, Consul, traffic management
- **API Gateway** - Kong, Tyk, AWS API Gateway, rate limiting
- **Serverless** - AWS Lambda, Azure Functions, event-driven
- **GraphQL Federation** - Federated GraphQL architectures
- **CQRS/Event Sourcing** - Command/query separation, event stores
- **Platform Engineering** - Internal platforms, golden paths

### Cloud Platforms:
- **AWS** - Multi-account, organizations, control tower
- **GCP** - Projects, folders, organization policies
- **Azure** - Subscriptions, management groups
- **Multi-Cloud** - Hybrid cloud, disaster recovery
- **Edge Computing** - CDN, edge functions, IoT

### Observability Stacks:
- **Prometheus + Grafana** - Metrics and dashboards
- **ELK Stack** - Elasticsearch, Logstash, Kibana
- **Datadog** - Full-stack monitoring and APM
- **Jaeger/Zipkin** - Distributed tracing
- **OpenTelemetry** - Vendor-neutral instrumentation

---

## 🚀 Quick Start

### For Enterprise Architects:
```bash
# 1. Design architecture
Use enterprise-architect to design our system

# 2. Document decisions
/adr-create "Microservices architecture decision"

# 3. Set up observability
Use distributed-tracing-setup skill
Use metrics-pipeline-builder skill

# 4. Compliance check
/compliance-scan soc2
```

### For Platform Teams:
```bash
# 1. Platform design
Use platform-engineer agent

# 2. Create golden paths
Use golden-path-creator skill

# 3. Developer portal
Use developer-portal-generator skill

# 4. Environment templates
/environment-clone prod template
```

### For SRE Teams:
```bash
# 1. Define SLOs
Use sre-consultant agent
Use sla-monitor-generator skill

# 2. Set up monitoring
Use metrics-pipeline-builder skill
Use log-aggregation-configurator skill

# 3. Chaos testing
Use chaos-engineer agent
Use chaos-engineering-setup skill

# 4. Incident readiness
/runbook-execute test-mode
```

---

## 🔐 Compliance Features

### SOC2 Type II:
- Automated evidence collection
- Access control validation
- Change management tracking
- Continuous monitoring
- Audit logging

### HIPAA:
- PHI detection and protection
- Encryption enforcement
- Access audit trails
- BAA management
- Breach notification

### GDPR:
- PII identification
- Data subject rights automation
- Consent management
- Data retention policies
- Cross-border transfers

### PCI-DSS:
- Cardholder data detection
- Network segmentation
- Encryption verification
- Access control
- Security scanning

---

## 💡 Best Practices

### For Architecture:
- Always start with enterprise-architect agent
- Document all decisions with /adr-create
- Use dependency-graph before refactoring
- Implement service mesh for microservices
- Design for observability from day one

### For Compliance:
- Run /compliance-scan weekly
- Automate evidence collection
- Use compliance-officer for gap analysis
- Enforce policies through hooks
- Maintain audit trails

### For Operations:
- Define SLOs for all critical services
- Create runbooks for all incidents
- Practice chaos experiments quarterly
- Monitor costs with finops-analyst
- Maintain up-to-date dependency graphs

### For Platform Engineering:
- Define clear golden paths
- Enable self-service through automation
- Build developer portals for documentation
- Template environments with /environment-clone
- Measure platform adoption and satisfaction

---

## 📊 Progression Path

**Current Level:** Advanced (Enterprise)

**What You've Mastered:**
- ✅ Enterprise architecture patterns
- ✅ Distributed systems design
- ✅ Compliance frameworks (SOC2, HIPAA, GDPR)
- ✅ Full-stack observability
- ✅ Platform engineering
- ✅ SRE practices
- ✅ Incident response
- ✅ Multi-cloud operations

**What You Can Build:**
- Large-scale distributed systems
- Compliant healthcare/fintech platforms
- Internal developer platforms
- Multi-cloud architectures
- Self-healing systems
- Enterprise SaaS platforms

**Continuous Learning:**
- Advanced chaos engineering patterns
- ML-powered observability
- Advanced cost optimization
- Automated compliance remediation
- Plugin ecosystem development

---

## 🔗 Detailed Rule References

### Comprehensive Documentation:
- **Skills Reference:** `@advanced-kit/.claude/rules/skills-reference.md`
- **Commands Reference:** `@advanced-kit/.claude/rules/commands-reference.md`
- **Agents Reference:** `@advanced-kit/.claude/rules/agents-reference.md`
- **Hooks Reference:** `@advanced-kit/.claude/rules/hooks-reference.md`
- **MCP Reference:** `@advanced-kit/.claude/rules/mcp-reference.md`

### Framework-Specific Rules:
- Microservices: `@advanced-kit/.claude/rules/frameworks/microservices.md`
- Event-Driven: `@advanced-kit/.claude/rules/frameworks/event-driven.md`
- Service Mesh: `@advanced-kit/.claude/rules/frameworks/service-mesh.md`
- API Gateway: `@advanced-kit/.claude/rules/frameworks/api-gateway.md`
- Serverless: `@advanced-kit/.claude/rules/frameworks/serverless.md`
- GraphQL Federation: `@advanced-kit/.claude/rules/frameworks/graphql-federation.md`
- CQRS/ES: `@advanced-kit/.claude/rules/frameworks/cqrs-event-sourcing.md`
- Platform Engineering: `@advanced-kit/.claude/rules/frameworks/platform-engineering.md`

### Workflow Rules:
- Architecture Design: `@advanced-kit/.claude/rules/workflows/architecture-design.md`
- Compliance: `@advanced-kit/.claude/rules/workflows/compliance.md`
- Incident Response: `@advanced-kit/.claude/rules/workflows/incident-response.md`
- Disaster Recovery: `@advanced-kit/.claude/rules/workflows/disaster-recovery.md`
- Release Management: `@advanced-kit/.claude/rules/workflows/release-management.md`
- Observability: `@advanced-kit/.claude/rules/workflows/observability.md`
- Cost Optimization: `@advanced-kit/.claude/rules/workflows/cost-optimization.md`
- Security Governance: `@advanced-kit/.claude/rules/workflows/security-governance.md`
- Data Governance: `@advanced-kit/.claude/rules/workflows/data-governance.md`
- Platform Operations: `@advanced-kit/.claude/rules/workflows/platform-operations.md`
- Chaos Engineering: `@advanced-kit/.claude/rules/workflows/chaos-engineering.md`
- Multi-Cloud: `@advanced-kit/.claude/rules/workflows/multi-cloud.md`

### Domain-Specific Rules:
- FinTech: `@advanced-kit/.claude/rules/domains/fintech.md`
- Healthcare: `@advanced-kit/.claude/rules/domains/healthcare.md`
- E-Commerce: `@advanced-kit/.claude/rules/domains/ecommerce.md`
- SaaS Platforms: `@advanced-kit/.claude/rules/domains/saas-platforms.md`
- Data Platforms: `@advanced-kit/.claude/rules/domains/data-platforms.md`
- IoT/Edge: `@advanced-kit/.claude/rules/domains/iot-edge.md`

---

## 🔗 Related Resources

**Project Root:**
- Main Overview: `@CLAUDE.md`
- Project README: `@README.md`
- Advanced Pack Design: `@ADVANCED_PACK_DESIGN.md`

**Previous Levels:**
- Starter Kit: `@starter-kit/.claude/rules/CLAUDE.md`
- Intermediate Kit: `@intermediate-kit/.claude/rules/CLAUDE.md`
- Advanced Examples: `@examples/advanced/.claude/rules/CLAUDE.md`

**Templates:**
- Skill Template: `@templates/skill-template.md`
- Command Template: `@templates/command-template.md`
- Subagent Template: `@templates/subagent-template.md`

**Advanced Pack Documentation:**
- Main README: `@advanced-kit/README.md`
- Architecture Guide: `@advanced-kit/ARCHITECTURE.md`
- Compliance Guide: `@advanced-kit/COMPLIANCE_GUIDE.md`
- Quick Reference: `@advanced-kit/QUICK_REFERENCE.md`

**Runbooks:**
- Incident Response: `@advanced-kit/RUNBOOKS/incident-response.md`
- Disaster Recovery: `@advanced-kit/RUNBOOKS/disaster-recovery.md`
- Security Incident: `@advanced-kit/RUNBOOKS/security-incident.md`
- Data Breach: `@advanced-kit/RUNBOOKS/data-breach.md`

---

**Level:** Advanced (Enterprise/Master)
**Last Updated:** 2025-11-01
**Capabilities:** 15 skills, 20 commands, 10 agents, 15+ hooks
**Enterprise Support:** SOC2, HIPAA, GDPR, PCI-DSS
**Cloud Support:** AWS, GCP, Azure, Multi-Cloud
**Observability:** Full-Stack Monitoring, Tracing, Logging

---

**Enterprise-grade. Production-ready. Compliance-first. 🚀**
