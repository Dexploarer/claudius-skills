# /setup-dashboards - Observability Dashboards

Set up comprehensive monitoring dashboards for your application.

---

## Usage

```
/setup-dashboards [platform]
/setup-dashboards --service [service-name]
```

Examples:
- `/setup-dashboards grafana`
- `/setup-dashboards prometheus`
- `/setup-dashboards --service api-gateway`

---

## What This Command Does

1. **Dashboard Platform Setup**
   - Install Grafana/Kibana/Datadog
   - Configure data sources
   - Set up authentication

2. **Create Dashboards**
   - **Application Dashboard**
     - Request rate
     - Error rate
     - Latency (p50, p95, p99)
     - Success rate

   - **Infrastructure Dashboard**
     - CPU usage
     - Memory usage
     - Disk I/O
     - Network traffic

   - **Business Metrics Dashboard**
     - User signups
     - Transactions
     - Revenue
     - Active users

3. **Set Up Alerts**
   - High error rate (>1%)
   - High latency (p99 >1s)
   - Resource exhaustion
   - Service down

4. **Configure Integrations**
   - Slack notifications
   - PagerDuty escalation
   - Email alerts
   - Webhook callbacks

---

## Output

```
📊 DASHBOARDS CONFIGURED

Platform: Grafana
URL: https://grafana.example.com

Dashboards Created:
✓ Application Metrics (/d/app-metrics)
✓ Infrastructure (/d/infrastructure)
✓ Business KPIs (/d/business)
✓ Error Tracking (/d/errors)

Alerts Configured:
✓ High Error Rate → #alerts-critical
✓ Service Down → PagerDuty
✓ High Latency → #alerts-warning

Next Steps:
1. Review dashboards
2. Customize thresholds
3. Test alert routing
```

---

**Related Commands:**
- `/trace-request` - Distributed tracing
- `/analyze-logs` - Log analysis
