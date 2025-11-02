# /trace-request - Distributed Tracing Command

Set up and analyze distributed tracing for microservices.

---

## Usage

```
/trace-request [service] [endpoint]
/trace-request --analyze [trace-id]
/trace-request --setup
```

Examples:
- `/trace-request api-gateway /api/users`
- `/trace-request --analyze abc123def`
- `/trace-request --setup opentelemetry`

---

## What This Command Does

### Setup Mode (`--setup`)
1. Install tracing dependencies (OpenTelemetry, Jaeger, etc.)
2. Configure trace exporters
3. Add instrumentation to services
4. Set up sampling strategies
5. Configure trace collectors

### Trace Mode
1. Instrument specific endpoint
2. Add custom spans and attributes
3. Set up context propagation
4. Configure error tracking

### Analysis Mode (`--analyze`)
1. Fetch trace by ID
2. Visualize trace spans
3. Identify bottlenecks
4. Show latency breakdown
5. Detect errors and anomalies

---

## Output

```
🔍 DISTRIBUTED TRACE ANALYSIS

Trace ID: abc123def456
Duration: 245ms
Status: OK
Services: 4

Span Breakdown:
├─ api-gateway (15ms)
│  └─ auth-service (45ms)
│     ├─ user-service (120ms) ⚠️ SLOW
│     │  └─ database (95ms) ⚠️ BOTTLENECK
│     └─ cache-service (5ms)

Performance Issues:
⚠️  user-service: 120ms (expected <50ms)
⚠️  database query: 95ms (missing index?)

Recommendations:
1. Add database index on user_id
2. Implement query caching
3. Consider read replica
```

---

**Related Commands:**
- `/monitor-service` - Service health monitoring
- `/analyze-logs` - Log analysis
- `/performance-report` - Generate performance report
