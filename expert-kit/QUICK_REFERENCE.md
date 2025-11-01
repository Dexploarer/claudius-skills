# Expert Pack - Quick Reference

Fast lookup guide for all enterprise capabilities.

---

## 🎯 Quick Commands

### Architecture & Design
```bash
/adr-create <title>              # Create Architecture Decision Record
/dependency-graph                # Visualize service dependencies
Use enterprise-architect        # Consult architecture expert
Use distributed-systems-architect  # Microservices expert
```

### Deployment & Release
```bash
/release-orchestrator <services> # Multi-service coordinated release
/canary-deploy <service>        # Progressive canary rollout
/blue-green-deploy <service>    # Zero-downtime deployment
/rollback-emergency <service>   # Emergency rollback
/feature-flag-toggle <flag>     # Toggle feature flags
```

### Compliance & Security
```bash
/compliance-scan [framework]    # SOC2/HIPAA/GDPR/PCI audit
/security-posture              # Security assessment
/sla-report [service]          # SLA compliance report
Use compliance-officer         # Compliance expert
Use security-architect         # Security expert
```

### Incident Response
```bash
/incident-declare <severity>   # Start incident response
/runbook-execute <runbook>     # Execute incident runbook
/postmortem-generate <id>      # Create postmortem
/oncall-schedule              # Manage on-call rotation
Use incident-commander        # Incident response expert
```

### Platform Operations
```bash
/environment-clone <src> <dst> # Clone entire environment
/data-migration <plan>         # Orchestrate data migration
/traffic-replay <source>       # Replay production traffic
/load-test-suite <target>      # Comprehensive load tests
/cost-analysis [cloud]         # Multi-cloud cost analysis
/tech-debt-audit              # Technical debt assessment
Use platform-engineer         # Platform expert
Use finops-analyst           # Cost optimization expert
```

---

## 🔧 Skills Quick Reference

### Architecture (4 skills)
| Skill | Trigger Phrases |
|-------|----------------|
| `microservices-orchestrator` | "design microservices", "service architecture" |
| `api-gateway-configurator` | "configure API gateway", "set up Kong" |
| `event-driven-architect` | "event-driven", "Kafka architecture" |
| `service-mesh-integrator` | "configure service mesh", "Istio setup" |

### Compliance (4 skills)
| Skill | Trigger Phrases |
|-------|----------------|
| `compliance-auditor` | "compliance audit", "SOC2 check", "HIPAA" |
| `architecture-decision-recorder` | "create ADR", "document decision" |
| `sla-monitor-generator` | "create SLO", "define SLA", "error budget" |
| `disaster-recovery-planner` | "disaster recovery", "DR strategy" |

### Observability (4 skills)
| Skill | Trigger Phrases |
|-------|----------------|
| `distributed-tracing-setup` | "set up tracing", "configure Jaeger" |
| `metrics-pipeline-builder` | "metrics pipeline", "Prometheus setup" |
| `log-aggregation-configurator` | "centralize logs", "ELK stack" |
| `chaos-engineering-setup` | "chaos engineering", "resilience testing" |

### Platform (3 skills)
| Skill | Trigger Phrases |
|-------|----------------|
| `internal-platform-builder` | "build platform", "developer platform" |
| `developer-portal-generator` | "developer portal", "Backstage setup" |
| `golden-path-creator` | "golden path", "platform standards" |

---

## 👥 Agents Quick Reference

### Architecture Consultants
- `enterprise-architect` - System architecture design
- `distributed-systems-architect` - Microservices patterns
- `data-architect` - Data modeling and pipelines
- `platform-engineer` - Internal platform building

### Operations Consultants
- `sre-consultant` - SRE best practices, SLOs
- `incident-commander` - Incident response
- `chaos-engineer` - Resilience testing
- `finops-analyst` - Cloud cost optimization

### Compliance Consultants
- `compliance-officer` - SOC2, HIPAA, GDPR, PCI
- `security-architect` - Zero-trust, threat modeling

---

## 📋 Common Workflows

### 1. Design New Architecture
```
1. Use enterprise-architect to design the architecture
2. /adr-create "Architecture Decision Title"
3. Use microservices-orchestrator skill
4. /dependency-graph
5. Use distributed-tracing-setup skill
```

### 2. Achieve SOC2 Compliance
```
1. /compliance-scan soc2
2. Use compliance-officer agent
3. Use security-architect agent
4. /security-posture
5. /adr-create "Security Controls"
6. Use sla-monitor-generator skill
```

### 3. Handle Production Incident
```
1. /incident-declare severity-1
2. Use incident-commander agent
3. /runbook-execute <incident-type>
4. /rollback-emergency (if needed)
5. /postmortem-generate INC-XXX
```

### 4. Deploy New Service
```
1. Use distributed-systems-architect agent
2. /adr-create "New Service Design"
3. Use service-mesh-integrator skill
4. /canary-deploy new-service
5. /sla-report new-service
```

### 5. Build Internal Platform
```
1. Use platform-engineer agent
2. Use internal-platform-builder skill
3. Use golden-path-creator skill
4. Use developer-portal-generator skill
5. /environment-clone prod template
```

### 6. Cost Optimization
```
1. Use finops-analyst agent
2. /cost-analysis all
3. /tech-debt-audit
4. Review recommendations
5. Implement optimizations
```

---

## 🔐 Compliance Frameworks

### SOC2 Type II
```bash
/compliance-scan soc2
Use compliance-officer agent
```
**Focus:** Security, availability, processing integrity, confidentiality, privacy

### HIPAA
```bash
/compliance-scan hipaa
```
**Focus:** PHI protection, encryption, access controls, audit trails

### GDPR
```bash
/compliance-scan gdpr
```
**Focus:** PII protection, consent, data subject rights, retention

### PCI-DSS
```bash
/compliance-scan pci
```
**Focus:** Cardholder data protection, encryption, network segmentation

---

## 📊 Observability Stack

### Distributed Tracing
```
Use distributed-tracing-setup skill
Tools: Jaeger, Zipkin, Datadog APM, AWS X-Ray
```

### Metrics & Monitoring
```
Use metrics-pipeline-builder skill
Tools: Prometheus, Grafana, Datadog, CloudWatch
```

### Centralized Logging
```
Use log-aggregation-configurator skill
Tools: ELK Stack, Loki, Splunk, Fluentd
```

### Chaos Engineering
```
Use chaos-engineer agent
Use chaos-engineering-setup skill
Tools: Chaos Monkey, Litmus
```

---

## 🚨 Emergency Commands

```bash
# Production incident
/incident-declare severity-1
Use incident-commander agent

# Emergency rollback
/rollback-emergency <service>

# Disable failing feature
/feature-flag-toggle <flag> off

# Check system health
/sla-report

# View dependencies
/dependency-graph
```

---

## 💰 Cost Management

```bash
# Analyze costs
/cost-analysis aws

# Get optimization advice
Use finops-analyst agent

# Review resource usage
/tech-debt-audit
```

---

## 🎯 Success Metrics

### Architecture Quality
- ADRs documented for all major decisions
- Service dependencies visualized
- SLOs defined for all critical services
- Architecture reviews completed

### Compliance
- Compliance scan score > 85%
- No critical security findings
- All PHI/PII protected
- Audit logs comprehensive

### Operations
- Incident MTTR < 30 minutes
- Deployment frequency: Daily
- Change failure rate < 5%
- Availability > 99.9%

### Cost Efficiency
- Cloud costs optimized (< budget)
- Resource utilization > 70%
- No idle resources
- Reserved instance coverage > 80%

---

## 🔗 Documentation Locations

### Main Docs
- **README:** `expert-kit/README.md`
- **Rules:** `expert-kit/.claude/rules/CLAUDE.md`
- **Architecture:** `expert-kit/ARCHITECTURE.md`
- **Compliance:** `expert-kit/COMPLIANCE_GUIDE.md`

### Runbooks
- `expert-kit/RUNBOOKS/incident-response.md`
- `expert-kit/RUNBOOKS/disaster-recovery.md`
- `expert-kit/RUNBOOKS/security-incident.md`

### Rules & Workflows
- **Frameworks:** `expert-kit/.claude/rules/frameworks/`
- **Workflows:** `expert-kit/.claude/rules/workflows/`
- **Domains:** `expert-kit/.claude/rules/domains/`

---

## 📞 Getting Help

```bash
# List all skills
list skills

# List all commands
/help

# View specific agent
Read expert-kit/.claude/agents/<agent-name>.md

# View specific skill
Read expert-kit/.claude/skills/<skill-name>.md

# View command details
Read expert-kit/.claude/commands/<command-name>.md
```

---

## ⚡ Pro Tips

1. **Always start with enterprise-architect** for new designs
2. **Document decisions with /adr-create** immediately
3. **Run /compliance-scan** weekly in regulated industries
4. **Use /dependency-graph** before major refactoring
5. **Test with chaos-engineer** before production
6. **Monitor costs with finops-analyst** monthly
7. **Update runbooks after every incident**
8. **Review SLOs with sre-consultant** quarterly

---

**Quick Start:** `Use enterprise-architect to review our architecture`

**Emergency:** `/incident-declare severity-1`

**Documentation:** `expert-kit/README.md`
