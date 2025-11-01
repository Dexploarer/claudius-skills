# Security Workflow - Intermediate Kit

> **Security best practices and OWASP Top 10 prevention**

---

## 🛡️ Security Checklist

- [ ] Authentication implemented securely
- [ ] Authorization checks in place
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] CSRF protection
- [ ] Rate limiting configured
- [ ] HTTPS enforced
- [ ] Secrets in environment variables
- [ ] Dependencies audited (`/security-audit`)

---

## 🔐 OWASP Top 10 Prevention

### 1. Broken Access Control
- Implement proper authorization
- Check permissions on every request
- Use role-based access control (RBAC)

### 2. Cryptographic Failures
- Use bcrypt for passwords (cost factor 12+)
- HTTPS for all connections
- Encrypt sensitive data at rest

### 3. Injection
- Use parameterized queries
- Validate and sanitize all inputs
- Use ORMs with proper escaping

### 4. Insecure Design
- Threat modeling
- Security requirements
- Use `security-auditor` agent

### 5. Security Misconfiguration
- Disable default credentials
- Remove unnecessary features
- Keep software updated

### 6. Vulnerable Components
- Run `/security-audit` regularly
- Update dependencies (`/dependency-update`)
- Monitor for CVEs

### 7. Authentication Failures
- Implement MFA where possible
- Use strong password requirements
- Implement rate limiting on auth endpoints

### 8. Software and Data Integrity
- Verify package integrity
- Use lock files (package-lock.json)
- Code signing where applicable

### 9. Logging & Monitoring
- Log authentication events
- Monitor for suspicious activity
- Set up alerts (Sentry, Datadog)

### 10. Server-Side Request Forgery
- Validate URLs
- Use allowlists for external requests
- Disable unnecessary protocols

---

## 🔧 Security Commands

```bash
/security-audit           # Comprehensive audit
/dependency-update        # Update vulnerable deps
```

## 🔧 Security Agents

```
"Use security-auditor to audit the authentication system"
```

---

**Last Updated:** 2025-11-01
