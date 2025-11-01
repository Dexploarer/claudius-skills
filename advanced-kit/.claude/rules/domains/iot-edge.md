# iot edge Domain Guide

IoT and edge computing architectures for connected devices

## Domain Overview

This guide provides expert guidance for building iot and edge computing architectures for connected devices.

## Key Characteristics

### Business Requirements
- **Regulatory Compliance:** [Specific regulations]
- **Security Requirements:** [Domain-specific security needs]
- **Performance Requirements:** [Latency, throughput targets]
- **Scalability Requirements:** [Growth expectations]

### Technical Challenges
1. **Challenge 1:** [Specific to domain]
2. **Challenge 2:** [Specific to domain]
3. **Challenge 3:** [Specific to domain]

## Compliance Requirements

### Required Frameworks

iot-edge applications must comply with:

- **IOT-EDGE Regulations:** [Specific regulations]
- **Data Protection:** [GDPR, CCPA, etc.]
- **Security Standards:** [ISO 27001, SOC2, etc.]
- **Industry Standards:** [Domain-specific standards]

### Compliance Checklist

#### Data Protection
- [ ] Data encryption at rest (AES-256)
- [ ] Data encryption in transit (TLS 1.3)
- [ ] Access controls and audit logging
- [ ] Data retention policies documented
- [ ] Breach notification procedures

#### Security Controls
- [ ] Multi-factor authentication required
- [ ] Role-based access control (RBAC)
- [ ] Regular security scanning
- [ ] Penetration testing (annual)
- [ ] Incident response plan

#### Audit Requirements
- [ ] Comprehensive audit logging
- [ ] Log retention (7+ years)
- [ ] Regular compliance audits
- [ ] Evidence collection automated
- [ ] Audit reports generated

## Architecture Patterns

### Pattern 1: [Domain-Specific Pattern]

**Use Case:** [When to use this pattern]

**Architecture:**
```
[High-level architecture diagram description]
```

**Key Components:**
1. **Component A:** [Purpose and implementation]
2. **Component B:** [Purpose and implementation]
3. **Component C:** [Purpose and implementation]

**Data Flow:**
1. [Step 1 of data flow]
2. [Step 2 of data flow]
3. [Step 3 of data flow]

### Pattern 2: [Another Domain Pattern]

[Similar structure]

## Technology Stack Recommendations

### Backend
| Component | Recommendation | Rationale |
|-----------|---------------|-----------|
| Language | [Language] | [Why it's suitable] |
| Framework | [Framework] | [Why it's suitable] |
| Database | [Database] | [Why it's suitable] |

### Frontend
| Component | Recommendation | Rationale |
|-----------|---------------|-----------|
| Framework | [Framework] | [Why it's suitable] |
| State Management | [Tool] | [Why it's suitable] |
| UI Library | [Library] | [Why it's suitable] |

### Infrastructure
| Component | Recommendation | Rationale |
|-----------|---------------|-----------|
| Cloud Provider | [Provider] | [Why it's suitable] |
| Orchestration | [Tool] | [Why it's suitable] |
| Monitoring | [Tool] | [Why it's suitable] |

## Security Best Practices

### Authentication & Authorization
```yaml
authentication:
  method: OAuth2 + JWT
  mfa: required
  session_timeout: 15 minutes
  
authorization:
  model: RBAC
  least_privilege: true
  regular_reviews: quarterly
```

### Data Protection
- ✅ Encrypt all sensitive data (AES-256)
- ✅ Use HSM for key management
- ✅ Implement data masking for PII
- ✅ Regular data classification reviews
- ✅ Data loss prevention (DLP) tools

### Network Security
- ✅ Web Application Firewall (WAF)
- ✅ DDoS protection
- ✅ Network segmentation
- ✅ VPC with private subnets
- ✅ Regular vulnerability scanning

## Data Management

### Data Architecture

**Data Sources:**
- [Source 1]: [Description and volume]
- [Source 2]: [Description and volume]

**Data Storage:**
- **Operational:** [Database choice and rationale]
- **Analytical:** [Data warehouse choice]
- **Archival:** [Long-term storage solution]

**Data Pipeline:**
```
Source → Ingestion → Processing → Storage → Analytics
         (Kafka)    (Spark)      (S3/DB)   (Snowflake)
```

### Data Governance

**Policies:**
- Data classification (Public, Internal, Confidential, Restricted)
- Access control policies
- Retention policies
- Data quality standards

**Processes:**
- Weekly data quality checks
- Monthly access reviews
- Quarterly policy reviews
- Annual comprehensive audit

## Performance Optimization

### Scalability Strategies

**Horizontal Scaling:**
- Stateless application design
- Load balancing across instances
- Auto-scaling based on metrics
- Database read replicas

**Caching:**
- CDN for static assets
- Application-level caching (Redis)
- Database query caching
- API response caching

**Performance Targets:**
- API latency: p95 < 200ms, p99 < 500ms
- Page load time: < 2 seconds
- Database queries: < 100ms average
- Throughput: [Specific to domain] requests/second

## Monitoring and Observability

### Key Metrics

**Business Metrics:**
- [Domain-specific KPI 1]
- [Domain-specific KPI 2]
- [Domain-specific KPI 3]

**Technical Metrics:**
- Request rate and error rate
- Latency (p50, p95, p99)
- Database connection pool
- Queue depth and lag

**Security Metrics:**
- Failed authentication attempts
- Unauthorized access attempts
- Data access patterns
- Anomaly detection

### Alerting Rules

```yaml
alerts:
  - name: HighErrorRate
    condition: error_rate > 1%
    severity: critical
    
  - name: UnauthorizedAccess
    condition: auth_failures > 10 in 5m
    severity: high
    
  - name: DataAnomaly
    condition: unusual_data_access_pattern
    severity: medium
```

## Testing Strategy

### Domain-Specific Tests

**Compliance Tests:**
- Verify data encryption
- Validate access controls
- Test audit logging
- Verify data retention

**Security Tests:**
- Penetration testing
- Vulnerability scanning
- Authentication testing
- Authorization testing

**Performance Tests:**
- Load testing ([X] concurrent users)
- Stress testing ([Y] concurrent users)
- Soak testing (24+ hours)
- Spike testing (sudden traffic)

## Deployment Considerations

### Pre-Production Checklist

#### Security
- [ ] Security scan passed
- [ ] Secrets rotated
- [ ] Access controls verified
- [ ] WAF rules configured

#### Compliance
- [ ] Compliance scan passed
- [ ] Audit logging enabled
- [ ] Data retention configured
- [ ] Backup tested

#### Performance
- [ ] Load testing completed
- [ ] Auto-scaling configured
- [ ] Caching enabled
- [ ] CDN configured

### Production Deployment

**Strategy:** [Recommended deployment pattern]

**Monitoring:** [Specific metrics to watch]

**Rollback Plan:** [How to rollback if issues]

## Common Pitfalls

### Pitfall 1: [Domain-Specific Issue]

**Problem:** [Description]

**Impact:** [Business and technical impact]

**Solution:** [How to avoid or fix]

### Pitfall 2: [Domain-Specific Issue]

[Similar structure]

## Case Studies

### Success Story 1

**Company:** [Example company]
**Challenge:** [What they faced]
**Solution:** [How they solved it]
**Results:** [Outcomes and metrics]

### Success Story 2

[Similar structure]

## Resources

### Documentation
- [Relevant standard or spec]
- [Industry best practices guide]
- [Regulatory guidance]

### Tools
- [Recommended tool 1]
- [Recommended tool 2]
- [Recommended tool 3]

### Community
- [Industry forum or group]
- [Slack community]
- [Conference or meetup]

## Related Skills

- `compliance-auditor` - Compliance automation
- `security-architect` agent - Security design
- `data-architect` agent - Data modeling

## Related Workflows

- `compliance.md` - Compliance implementation
- `security-governance.md` - Security practices
- `data-governance.md` - Data management

---

**Domain:** iot-edge
**Last Updated:** 2025-11-01
**Status:** Production-Ready
**Compliance Frameworks:** [List applicable frameworks]
