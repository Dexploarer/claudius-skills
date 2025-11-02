# Multi-Tenant Architecture Designer

**Category:** SaaS Architecture
**Level:** Advanced
**Auto-trigger:** When user mentions multi-tenancy, SaaS architecture, tenant isolation, or B2B SaaS

---

## Description

Designs and implements multi-tenant SaaS architectures including tenant isolation strategies, data partitioning, tenant-specific customization, and billing integration.

---

## Activation Phrases

- "Set up multi-tenant architecture"
- "Implement tenant isolation"
- "Create SaaS data model"
- "Configure tenant routing"

---

## Isolation Strategies

### 1. Database Per Tenant
- **Pros**: Maximum isolation, easier compliance
- **Cons**: Higher operational overhead

### 2. Schema Per Tenant
- **Pros**: Good isolation, shared infrastructure
- **Cons**: Schema management complexity

### 3. Shared Schema with Tenant ID
- **Pros**: Most cost-effective, easiest to scale
- **Cons**: Requires careful query filtering

---

## Code Example

```typescript
// Tenant-aware middleware
export function tenantMiddleware() {
  return async (req, res, next) => {
    // Extract tenant from subdomain or header
    const host = req.get('host');
    const tenant = host.split('.')[0];

    // Attach tenant context
    req.tenant = await getTenant(tenant);

    // Set tenant context for database queries
    await setTenantContext(req.tenant.id);

    next();
  };
}

// Tenant-scoped query
async function getUsers(tenantId: string) {
  return db.users.findMany({
    where: { tenantId }  // Always filter by tenant
  });
}
```

---

**Last Updated:** 2025-11-02
