# Security Incident Response Runbook

Procedures for responding to security incidents and data breaches.

## Incident Types

- **Data Breach**: Unauthorized access to sensitive data
- **DDoS Attack**: Distributed denial of service
- **Account Compromise**: User or admin account takeover
- **Malware**: Malicious code detected
- **Vulnerability Exploitation**: Exploit of security flaw

## Security Incident Response

### Phase 1: Detection & Containment (0-30 min)

**1. Detect and Verify**
- Security alert received
- Verify incident is genuine
- Assess severity

**2. Contain Immediately**
\`\`\`bash
# Block suspicious IP
aws wafv2 update-ip-set \
  --id xxx --addresses "1.2.3.4/32"

# Revoke compromised credentials
aws iam delete-access-key --access-key-id AKIAIOSFODNN7EXAMPLE

# Isolate affected systems
kubectl cordon affected-node
\`\`\`

**3. Preserve Evidence**
- Take memory dumps
- Capture logs
- Snapshot affected systems
- Document everything

### Phase 2: Investigation (30 min - 4 hours)

**Forensic Analysis:**
\`\`\`bash
# Collect logs
aws cloudtrail lookup-events \
  --start-time 2025-11-01T00:00:00Z

# Check access logs
grep "suspicious-pattern" /var/log/nginx/access.log

# Database audit logs
psql -c "SELECT * FROM audit_log WHERE user_id = 'suspicious-user';"
\`\`\`

**Determine:**
- What was accessed?
- When did it occur?
- How did they get in?
- Is it still ongoing?
- What data was exposed?

### Phase 3: Eradication (4-24 hours)

**Remove Threat:**
- Patch vulnerabilities
- Remove malware
- Close security gaps
- Rotate all credentials

**Hardening:**
- Update security rules
- Enhance monitoring
- Add detection rules

### Phase 4: Notification (Required by Law)

**Internal:** Immediate
**Customers:** 72 hours (GDPR)
**Regulators:** As required

**Breach Notification Template:**
\`\`\`
Subject: Security Incident Notification

Dear [Customer],

We are writing to inform you of a security incident that may have affected your data.

What Happened:
[Brief description]

What Data Was Affected:
[Types of data]

What We're Doing:
[Actions taken]

What You Should Do:
[Recommended actions]

Contact:
security@example.com
\`\`\`

### Phase 5: Recovery

- Restore from clean backups
- Re-deploy systems
- Enhanced monitoring
- Conduct security review

### Phase 6: Postmortem

**Required Analysis:**
1. Root cause
2. Timeline of events
3. Data exposed
4. Gaps in security
5. Improvements needed

## Common Security Incidents

### SQL Injection Detected

**Immediate Actions:**
1. Block offending IPs via WAF
2. Review database logs
3. Check for data exfiltration
4. Patch vulnerable code

### Credential Leak

**Immediate Actions:**
1. Revoke leaked credentials
2. Rotate all related secrets
3. Check for unauthorized access
4. Scan for usage of credentials

### DDoS Attack

**Mitigation:**
1. Enable AWS Shield
2. Activate CloudFlare "Under Attack" mode
3. Implement rate limiting
4. Scale infrastructure

## Tools and Access

- **AWS GuardDuty**: Threat detection
- **Security Information**: Splunk, Datadog
- **WAF**: AWS WAF, CloudFlare
- **Forensics**: Memory dumps, disk images

---

**Last Updated:** $(date +%Y-%m-%d)
**Version:** 2.0
**Owner:** Security Team
