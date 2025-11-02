# /audit-security - Security Audit Command

Comprehensive security audit of your application and infrastructure.

---

## Usage

```
/audit-security
/audit-security --focus [area]
/audit-security --report
```

Examples:
- `/audit-security`
- `/audit-security --focus dependencies`
- `/audit-security --report pdf`

---

## What This Command Does

1. **Code Security Scan**
   - SAST (Static Application Security Testing)
   - Detect SQL injection vulnerabilities
   - XSS vulnerabilities
   - CSRF protection check
   - Hardcoded secrets

2. **Dependency Audit**
   - Known CVEs
   - Outdated packages
   - License compliance
   - Transitive dependencies

3. **Configuration Audit**
   - Security headers
   - CORS configuration
   - SSL/TLS settings
   - Authentication setup
   - Authorization rules

4. **Infrastructure Audit**
   - Open ports
   - Firewall rules
   - IAM permissions
   - Secrets management
   - Encryption at rest/transit

5. **Compliance Check**
   - GDPR requirements
   - SOC2 controls
   - HIPAA compliance
   - PCI-DSS standards

---

## Output

```
🔒 SECURITY AUDIT REPORT

Scan Date: 2025-11-02
Severity Levels: Critical (2) | High (5) | Medium (12) | Low (8)

Critical Issues:
❌ SQL Injection in /api/users endpoint
❌ Hardcoded AWS credentials in config.js

High Priority:
⚠️  Missing CSRF protection
⚠️  Weak password policy
⚠️  Outdated dependencies with CVEs
⚠️  Overly permissive IAM roles
⚠️  Missing security headers

Recommendations:
1. Immediate: Remove hardcoded credentials
2. High: Implement parameterized queries
3. High: Add CSRF tokens
4. Medium: Update dependencies
5. Medium: Enforce password complexity

Compliance Status:
✓ GDPR: 85% compliant
⚠️  SOC2: 70% compliant
❌ PCI-DSS: Not compliant (if applicable)
```

---

**Related Commands:**
- `/fix-vulnerabilities` - Auto-fix security issues
- `/generate-security-report` - Detailed report
