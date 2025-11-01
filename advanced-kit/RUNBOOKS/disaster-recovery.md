# Disaster Recovery Runbook

Procedures for recovering from catastrophic failures and disasters.

## Disaster Scenarios

### Scenario 1: Complete Region Failure (AWS us-east-1)

**RTO:** 2 hours
**RPO:** 15 minutes

**Recovery Steps:**

1. **Declare Disaster** (0-5 min)
   \`\`\`bash
   # Activate DR team
   page-team dr-team "Region failure - activating DR"
   
   # Update status page
   status-page update "Major outage - switching to backup region"
   \`\`\`

2. **Switch DNS to DR Region** (5-15 min)
   \`\`\`bash
   # Route53 failover
   aws route53 change-resource-record-sets \
     --hosted-zone-id Z123456 \
     --change-batch file://failover-to-us-west-2.json
   
   # Verify DNS propagation
   dig api.example.com
   \`\`\`

3. **Restore Database** (15-60 min)
   \`\`\`bash
   # Promote read replica to primary
   aws rds promote-read-replica --db-instance-identifier dr-db-us-west-2
   
   # Verify replication lag
   psql -h dr-db -c "SELECT now() - pg_last_xact_replay_timestamp();"
   \`\`\`

4. **Scale DR Resources** (60-90 min)
   \`\`\`bash
   # Scale up DR environment
   kubectl scale deployment --all --replicas=10 -n production
   
   # Verify all pods running
   kubectl get pods -n production
   \`\`\`

5. **Verify Service** (90-120 min)
   - Run smoke tests
   - Check critical flows
   - Monitor error rates
   - Communicate recovery

### Scenario 2: Data Corruption

**RTO:** 4 hours
**RPO:** 1 hour

**Recovery Steps:**

1. **Stop Writes**
   - Put application in read-only mode
   - Prevent further corruption

2. **Identify Corruption Point**
   \`\`\`bash
   # Check transaction logs
   psql -c "SELECT * FROM audit_log WHERE timestamp > NOW() - INTERVAL '24 hours' ORDER BY timestamp DESC;"
   \`\`\`

3. **Restore from Backup**
   \`\`\`bash
   # List available backups
   aws rds describe-db-snapshots \
     --db-instance-identifier prod-db
   
   # Restore to point-in-time
   aws rds restore-db-instance-to-point-in-time \
     --source-db-instance-identifier prod-db \
     --target-db-instance-identifier prod-db-restored \
     --restore-time 2025-11-01T10:00:00Z
   \`\`\`

4. **Validate Data Integrity**
   - Run data validation queries
   - Compare with known good state
   - Verify critical records

5. **Switch to Restored Database**
   - Update application config
   - Rolling restart
   - Monitor for issues

### Scenario 3: Security Breach

**See:** `security-incident.md`

## Backup Verification

**Weekly Tests:**
\`\`\`bash
#!/bin/bash
# Test database backup restoration

# 1. Restore latest backup to test instance
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier test-restore \
  --db-snapshot-identifier latest-snapshot

# 2. Run validation queries
psql -h test-restore -c "SELECT COUNT(*) FROM users;"
psql -h test-restore -c "SELECT MAX(created_at) FROM orders;"

# 3. Cleanup
aws rds delete-db-instance \
  --db-instance-identifier test-restore \
  --skip-final-snapshot
\`\`\`

## RTO/RPO Tracking

| System | RTO | RPO | Last Test | Status |
|--------|-----|-----|-----------|--------|
| Database | 2 hours | 15 min | 2025-10-25 | ✅ Pass |
| API Services | 1 hour | 0 min | 2025-10-25 | ✅ Pass |
| Frontend | 30 min | 0 min | 2025-10-25 | ✅ Pass |

## DR Testing Schedule

- **Monthly:** Database restore test
- **Quarterly:** Full DR failover drill
- **Annually:** Complete disaster simulation

---

**Last Updated:** $(date +%Y-%m-%d)
**Version:** 2.0
**Owner:** SRE Team
