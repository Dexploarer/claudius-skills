# /optimize-pipeline - CI/CD Pipeline Optimization

Analyze and optimize your CI/CD pipeline for speed and cost.

---

## Usage

```
/optimize-pipeline
/optimize-pipeline --focus [area]
/optimize-pipeline --report
```

Examples:
- `/optimize-pipeline`
- `/optimize-pipeline --focus build-time`
- `/optimize-pipeline --report`

---

## What This Command Does

1. **Analyze Current Pipeline**
   - Build duration
   - Test execution time
   - Resource usage
   - Cache effectiveness
   - Failure rate

2. **Identify Bottlenecks**
   - Slow steps
   - Resource-heavy operations
   - Sequential vs parallel
   - Cache misses

3. **Generate Optimizations**
   - **Caching Strategies**
     - Docker layer caching
     - Dependency caching
     - Build artifact caching

   - **Parallelization**
     - Parallel test execution
     - Matrix builds
     - Concurrent deployments

   - **Resource Optimization**
     - Right-size runners
     - Spot instances
     - ARM instances for builds

4. **Implement Improvements**
   - Update pipeline config
   - Add caching
   - Reorganize steps
   - Update dependencies

5. **Measure Impact**
   - Before/after comparison
   - Cost savings
   - Time savings
   - Success rate improvement

---

## Output

```
⚡ PIPELINE OPTIMIZATION REPORT

Current Performance:
• Average build: 12m 34s
• Monthly cost: $450
• Success rate: 87%

Bottlenecks Identified:
1. ⏱️  Docker build: 6m 12s (48% of total)
2. ⏱️  Integration tests: 4m 45s (38% of total)
3. ⏱️  npm install: 1m 23s (11% of total)

Recommended Optimizations:

1. Enable Docker Layer Caching
   Impact: -4m 30s per build
   Cost: Free

2. Parallelize Test Suites
   Impact: -2m 30s per build
   Cost: +$50/month (worth it)

3. Use npm ci with caching
   Impact: -45s per build
   Cost: Free

4. Switch to ARM runners
   Impact: Same speed
   Cost: -$180/month (40% savings)

Projected Results:
✅ Average build: 5m 49s (53% faster)
✅ Monthly cost: $320 (29% savings)
✅ Success rate: 87% (same)

Apply optimizations? (yes/no)
```

---

**Related Commands:**
- `/analyze-costs` - Cloud cost analysis
- `/test-parallel` - Parallel testing setup
