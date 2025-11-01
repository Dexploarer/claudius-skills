# Incident Response Runbook

Production incident response procedures for quick resolution and minimal downtime.

## Severity Levels

| Severity | Description | Response Time | Example |
|----------|-------------|---------------|---------|
| **SEV-1** | Critical - Service down | 15 minutes | Complete outage, data breach |
| **SEV-2** | High - Major impact | 1 hour | Degraded performance, partial outage |
| **SEV-3** | Medium - Minor impact | 4 hours | Non-critical feature broken |
| **SEV-4** | Low - Minimal impact | Next business day | Cosmetic issues |

## Incident Response Process

### Phase 1: Detection (0-5 minutes)

**Automatic Detection:**
- Monitoring alerts (PagerDuty, Datadog)
- Health check failures
- Error rate spikes
- Customer reports

**Initial Actions:**
1. Acknowledge the alert
2. Assess severity
3. Open incident channel in Slack: `#incident-YYYY-MM-DD-NNNN`

### Phase 2: Triage (5-15 minutes)

**Incident Commander Actions:**
1. **Declare incident**: `/incident-declare sev-1`
2. **Assemble team**:
   - Engineering lead
   - On-call engineer
   - Product manager (SEV-1/2)
   - Communications lead (SEV-1)
3. **Set up war room**: Zoom link in incident channel
4. **Start incident log**: Document timeline in real-time

**Assessment Questions:**
- What is the user impact?
- How many users affected?
- What systems are impacted?
- Is data at risk?
- Is this a security incident?

### Phase 3: Investigation (15-60 minutes)

**Investigation Checklist:**
- [ ] Check recent deployments (last 24 hours)
- [ ] Review error logs and traces
- [ ] Check infrastructure metrics (CPU, memory, disk)
- [ ] Verify third-party service status
- [ ] Check database performance
- [ ] Review security alerts

**Investigation Commands:**
\`\`\`bash
# Check recent deployments
kubectl get deployments -n production --sort-by=.metadata.creationTimestamp

# View error logs
kubectl logs -f deployment/api-service -n production --since=1h | grep ERROR

# Check resource usage
kubectl top pods -n production

# Database queries
psql -c "SELECT * FROM pg_stat_activity WHERE state = 'active';"
\`\`\`

### Phase 4: Mitigation (Immediate)

**Quick Wins (Try First):**
1. **Rollback recent deployment**:
   \`\`\`bash
   /rollback-emergency api-service
   \`\`\`

2. **Disable feature flag**:
   \`\`\`bash
   /feature-flag-toggle problematic-feature off
   \`\`\`

3. **Scale up resources**:
   \`\`\`bash
   kubectl scale deployment api-service --replicas=10 -n production
   \`\`\`

4. **Clear cache**:
   \`\`\`bash
   redis-cli FLUSHALL
   \`\`\`

5. **Restart service** (last resort):
   \`\`\`bash
   kubectl rollout restart deployment/api-service -n production
   \`\`\`

### Phase 5: Communication

**Internal Communication:**
- **15 minutes**: Initial status in #incidents
- **Every 30 minutes**: Updates in incident channel
- **Upon resolution**: Final summary

**External Communication (SEV-1/2):**
- **30 minutes**: Status page update
- **Every hour**: Customer email/tweet
- **Upon resolution**: Detailed explanation

**Communication Template:**
\`\`\`
🚨 INCIDENT UPDATE [SEV-1] [HH:MM UTC]

Status: Investigating / Identified / Monitoring / Resolved
Impact: [Description of user impact]
Affected: [% of users or specific features]
ETA: [Estimated time to resolution]
Next Update: [Time of next update]

Actions Taken:
- [Action 1]
- [Action 2]

Current Status:
[Detailed current state]
\`\`\`

### Phase 6: Resolution

**Verification Checklist:**
- [ ] Error rate back to baseline
- [ ] Latency normal
- [ ] All health checks passing
- [ ] Customer reports resolved
- [ ] Monitoring shows stable state
- [ ] No follow-up alerts

**Resolution Actions:**
1. Monitor for 15-30 minutes
2. Announce resolution in all channels
3. Update status page
4. Thank the team
5. Schedule postmortem

### Phase 7: Postmortem (Within 48 hours)

**Postmortem Template:**
\`\`\`bash
/postmortem-generate incident-2025-11-01-001
\`\`\`

**Required Sections:**
1. **Summary**: What happened in 1-2 paragraphs
2. **Timeline**: Detailed event timeline
3. **Root Cause**: Technical root cause analysis
4. **Impact**: Users affected, revenue lost, duration
5. **Resolution**: How it was fixed
6. **Action Items**: Prevent recurrence
   - [ ] Immediate fixes (this week)
   - [ ] Short-term improvements (this month)
   - [ ] Long-term enhancements (this quarter)

## Common Incident Types

### Database Issues

**Symptoms:**
- Slow queries
- Connection pool exhausted
- Deadlocks

**Investigation:**
\`\`\`sql
-- Check slow queries
SELECT pid, query, state, wait_event 
FROM pg_stat_activity 
WHERE state != 'idle' 
ORDER BY query_start;

-- Check locks
SELECT * FROM pg_locks WHERE NOT granted;
\`\`\`

**Resolution:**
- Kill long-running queries
- Add missing indexes
- Scale database resources
- Optimize problematic queries

### High Traffic Spike

**Symptoms:**
- Increased latency
- Timeouts
- CPU/memory saturation

**Resolution:**
- Scale horizontally (add pods)
- Enable caching
- Rate limiting
- CDN for static assets

### Third-Party Service Down

**Symptoms:**
- Timeouts to external APIs
- Circuit breaker open

**Resolution:**
- Check service status pages
- Enable fallback/degraded mode
- Use cached data
- Queue requests for retry

## Escalation Matrix

| Time | Action |
|------|--------|
| 0 min | On-call engineer paged |
| 15 min | Engineering lead notified |
| 30 min | VP Engineering notified (SEV-1) |
| 1 hour | CTO notified (SEV-1) |
| 2 hours | CEO notified (SEV-1) |

## Tools and Access

**Required Access:**
- AWS Console (production)
- Kubernetes cluster (kubectl)
- Database (psql, read-only)
- Monitoring (Datadog, Grafana)
- Logs (Elasticsearch/Kibana)
- PagerDuty

**Quick Links:**
- Status Page: https://status.example.com
- Grafana Dashboards: https://grafana.example.com
- Datadog APM: https://app.datadoghq.com
- Runbooks: https://runbooks.example.com

## Contact Information

| Role | Contact | Phone |
|------|---------|-------|
| On-Call Engineer | PagerDuty | - |
| Engineering Lead | @eng-lead | xxx-xxx-xxxx |
| VP Engineering | @vp-eng | xxx-xxx-xxxx |
| CTO | @cto | xxx-xxx-xxxx |

---

**Last Updated:** $(date +%Y-%m-%d)
**Version:** 2.0
**Owner:** SRE Team
