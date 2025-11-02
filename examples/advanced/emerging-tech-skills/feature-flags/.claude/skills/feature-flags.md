# Feature Flag Management System

**Category:** DevOps & Release Management
**Level:** Advanced
**Auto-trigger:** When user mentions feature flags, feature toggles, gradual rollouts, or A/B testing

---

## Description

Implements feature flag systems for gradual rollouts, A/B testing, and safe deployments. Supports server-side and client-side flags, targeting rules, and analytics integration.

---

## Activation Phrases

- "Set up feature flags"
- "Create feature toggle system"
- "Implement gradual rollout"
- "Set up A/B testing"
- "Configure feature management"

---

## Code Example

```typescript
// feature-flags.ts
interface FeatureFlag {
  key: string;
  enabled: boolean;
  rolloutPercentage?: number;
  targeting?: {
    userIds?: string[];
    groups?: string[];
    countries?: string[];
  };
}

class FeatureFlagService {
  private flags: Map<string, FeatureFlag> = new Map();

  async isEnabled(
    flagKey: string,
    context: {
      userId?: string;
      group?: string;
      country?: string;
    }
  ): Promise<boolean> {

    const flag = this.flags.get(flagKey);
    if (!flag) return false;
    if (!flag.enabled) return false;

    // Check targeting rules
    if (flag.targeting) {
      if (flag.targeting.userIds?.includes(context.userId || '')) {
        return true;
      }
      if (flag.targeting.groups?.includes(context.group || '')) {
        return true;
      }
      if (flag.targeting.countries?.includes(context.country || '')) {
        return true;
      }
    }

    // Check rollout percentage
    if (flag.rolloutPercentage !== undefined) {
      const hash = this.hashUserId(context.userId || '');
      return hash < flag.rolloutPercentage;
    }

    return flag.enabled;
  }

  private hashUserId(userId: string): number {
    let hash = 0;
    for (let i = 0; i < userId.length; i++) {
      hash = ((hash << 5) - hash) + userId.charCodeAt(i);
    }
    return Math.abs(hash % 100);
  }
}
```

---

**Last Updated:** 2025-11-02
