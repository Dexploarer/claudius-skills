# Data Breach Response Runbook

Specific procedures for handling data breaches with regulatory compliance.

## Data Breach Definition

A data breach is confirmed when:
- Unauthorized access to PII/PHI occurred
- Data was exfiltrated
- Encryption keys were compromised
- Reasonable belief of unauthorized access

## Immediate Actions (0-1 hour)

### 1. Activate Breach Team

**Core Team:**
- Security Lead (Incident Commander)
- Legal Counsel
- Privacy Officer
- CTO
- Communications Lead

### 2. Contain the Breach

\`\`\`bash
# Isolate affected systems
kubectl delete pod compromised-pod -n production

# Block attacker
aws wafv2 update-ip-set --id xxx --addresses "attacker-ip/32"

# Revoke access
aws iam delete-access-key --access-key-id COMPROMISED_KEY
\`\`\`

### 3. Preserve Evidence

- Snapshot all affected systems
- Collect logs (30 days retention minimum)
- Document timeline
- Take screenshots
- Record all actions

## Investigation (1-24 hours)

### Determine Scope

**Questions to Answer:**
1. What data was accessed?
   - PII (names, emails, addresses)
   - PHI (medical records, diagnoses)
   - Financial (credit cards, bank accounts)
   - Credentials (passwords, API keys)

2. How many individuals affected?
   - Exact count if possible
   - Reasonable estimate if not

3. Time period of unauthorized access?
   - First access timestamp
   - Last access timestamp
   - Duration of exposure

4. Method of breach?
   - SQL injection
   - Credential theft
   - Vulnerability exploitation
   - Insider threat

### Evidence Collection

\`\`\`bash
# Database audit
psql -c "SELECT * FROM audit_log WHERE action = 'SELECT' 
         AND table_name IN ('users', 'patients', 'payment_methods')
         AND timestamp BETWEEN '2025-11-01' AND '2025-11-02';"

# Access logs
grep "SELECT.*FROM users" /var/log/postgresql/postgresql.log

# Application logs
grep "unauthorized" /var/log/app/application.log
\`\`\`

## Notification Requirements

### Timeline

| Regulation | Notification Deadline | Authority | Affected Individuals |
|------------|----------------------|-----------|---------------------|
| GDPR | 72 hours | Data Protection Authority | Without undue delay |
| HIPAA | 60 days | HHS OCR | 60 days |
| CCPA | Without unreasonable delay | Attorney General | California residents |
| PCI-DSS | Immediately | Card brands, processor | Cardholders |

### GDPR Breach Notification

**To Supervisory Authority (72 hours):**
\`\`\`markdown
1. Nature of personal data breach
2. Name and contact details of DPO
3. Likely consequences of the breach
4. Measures taken or proposed

Submit to: [Your country's data protection authority]
\`\`\`

**To Data Subjects:**
\`\`\`markdown
When required:
- High risk to rights and freedoms
- Clear language, plain terms
- Describe the breach
- Contact point for information
- Measures taken and recommended
\`\`\`

### HIPAA Breach Notification

**To HHS (60 days):**
- Breach Notification Form
- Detailed description
- Types of PHI involved
- Number of individuals
- Mitigation actions

**To Affected Individuals (60 days):**
- First-class mail
- Description of breach
- Types of PHI
- Steps individuals should take
- What organization is doing

**To Media (if >500 affected):**
- Notice to prominent media outlets
- Same information as individuals

## Remediation

### Technical Measures

1. **Close the vulnerability**
   - Patch systems
   - Update code
   - Fix configurations

2. **Enhance security**
   - Additional monitoring
   - Stronger access controls
   - Encryption improvements

3. **Credential rotation**
   - All API keys
   - All passwords
   - All certificates

### User Actions

**For Affected Users:**
- Password reset required
- Enable MFA
- Credit monitoring (1 year free)
- Identity theft protection

## Post-Breach Actions

### 1. Credit Monitoring Service

Contract with credit monitoring provider:
- 12-24 months free monitoring
- Identity theft insurance
- Credit report access

### 2. Call Center

Set up breach response hotline:
- Dedicated phone number
- FAQs prepared
- Trained staff
- Extended hours

### 3. Enhanced Monitoring

- Increase logging
- Add security alerts
- Regular security scans
- Penetration testing

## Legal Considerations

### Potential Liabilities

- GDPR: Up to €20M or 4% of annual revenue
- HIPAA: Up to $1.5M per violation
- CCPA: Up to $7,500 per intentional violation
- Class action lawsuits
- Regulatory investigations

### Legal Holds

- Preserve all evidence
- Don't delete anything
- Document everything
- Legal review required

## Documentation Template

\`\`\`markdown
# Data Breach Report

**Incident ID:** DBR-2025-11-01-001
**Date Discovered:** [Date and time]
**Date Contained:** [Date and time]

## Summary
[Brief description]

## Affected Data
- Data types: [PII, PHI, etc.]
- Number of records: [Count]
- Time period: [Date range]

## Root Cause
[Technical explanation]

## Individuals Affected
- Total count: [Number]
- Geographic distribution: [Countries/states]
- Notification method: [Email/Mail/etc]

## Remediation
- Immediate: [Actions taken]
- Short-term: [This month]
- Long-term: [This quarter]

## Notifications
- Regulators: [Date notified]
- Affected individuals: [Date notified]
- Media: [If applicable]

## Lessons Learned
[What we learned and how we'll prevent future breaches]
\`\`\`

---

**Last Updated:** $(date +%Y-%m-%d)
**Version:** 2.0
**Owner:** Security & Privacy Team
**Legal Review:** Required before use
