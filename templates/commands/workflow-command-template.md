<!-- Workflow Command Template -->
<!-- File: .claude/commands/{workflow-name}.md -->

Execute a complex, multi-step workflow with validation, rollback, and progress tracking.

## What This Workflow Does

This command orchestrates a complete workflow including:
- Pre-flight validation
- Multi-step execution
- Progress tracking
- Error recovery
- Post-execution verification
- Rollback capability

## Usage

```bash
# Run complete workflow
/{workflow-name}

# Run with specific configuration
/{workflow-name} --env production

# Dry run (show what would happen)
/{workflow-name} --dry-run

# Resume from checkpoint
/{workflow-name} --resume
```

## Workflow Overview

```
Phase 1: Pre-Flight Checks (2 min)
  ├─ Validate environment
  ├─ Check dependencies
  └─ Verify permissions

Phase 2: Preparation (5 min)
  ├─ Backup current state
  ├─ Create checkpoint
  └─ Initialize resources

Phase 3: Execution (15 min)
  ├─ Step 1: [Action 1]
  ├─ Step 2: [Action 2]
  ├─ Step 3: [Action 3]
  └─ Step 4: [Action 4]

Phase 4: Verification (3 min)
  ├─ Run health checks
  ├─ Validate outputs
  └─ Confirm success

Phase 5: Cleanup (2 min)
  ├─ Remove temporary files
  ├─ Update state
  └─ Generate report

Total estimated time: ~27 minutes
```

## Instructions

### Pre-Flight Checks Phase

**Step 1: Display Workflow Banner**

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           {WORKFLOW NAME} - Production Ready             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

Version: v{version}
Environment: {environment}
Started: {timestamp}
Execution ID: {unique-id}

════════════════════════════════════════════════════════════
```

**Step 2: Parse Arguments and Options**

```markdown
Handle arguments:
  - Environment: $1 or $ARGS (staging/production)
  - Options: Parse flags
    - --dry-run: Preview only
    - --force: Skip confirmations
    - --resume: Resume from last checkpoint
    - --rollback: Rollback to previous state
    - --verbose: Detailed logging
```

**Step 3: Validate Environment**

```bash
## Environment Validation

Checking environment...

✓ Node.js version: v18.16.0 (required: >=18.0.0)
✓ Git version: 2.40.0 (required: >=2.30.0)
✓ Docker: Running (required)
✓ Database: Connected (required)
✓ Redis: Connected (optional - warning if missing)
✓ Storage: 15GB free (required: >=10GB)
✓ Memory: 8GB available (required: >=4GB)

All environment checks passed! ✓

If any check fails:
  ❌ [Tool] version X.X.X (required: >=Y.Y.Y)

  Please upgrade:
    [installation instructions]

  Cannot proceed until requirements are met.
  Exiting...
```

**Step 4: Check Permissions**

```bash
## Permission Checks

Verifying access...

✓ File system: Write access to /target/directory
✓ Database: Admin permissions
✓ API: Valid authentication token
✓ Repository: Push access to origin

If permission denied:
  ❌ Missing permission: [permission name]

  Required: [specific permission]

  To grant access:
    [instructions for granting access]
```

**Step 5: Verify Working State**

```bash
## Working State Check

Analyzing current state...

Git status:
  Branch: main
  Status: Clean working tree ✓
  Commits ahead: 0
  Uncommitted changes: 0

Database:
  Migrations: Up to date ✓
  Pending migrations: 0
  Schema version: v2.5.0

Dependencies:
  Outdated packages: 0 ✓
  Security vulnerabilities: 0 ✓

If state is not clean:
  ⚠️  Warning: Uncommitted changes detected

  Files modified:
    - src/file1.ts
    - src/file2.ts

  Options:
    1. Stash changes: git stash
    2. Commit changes: git commit
    3. Discard changes: git restore
    4. Continue anyway: --force flag

  How would you like to proceed?
```

**Step 6: Show Workflow Plan**

```
═══════════════════════════════════════════════════════════
WORKFLOW PLAN
═══════════════════════════════════════════════════════════

Environment: PRODUCTION
Estimated duration: 27 minutes

Tasks to be executed:
  1. ✓ Backup current database (2 min)
  2. ✓ Run database migrations (5 min)
  3. ✓ Build application (8 min)
  4. ✓ Run test suite (10 min)
  5. ✓ Deploy to production (5 min)
  6. ✓ Run smoke tests (3 min)
  7. ✓ Update documentation (2 min)

Critical operations:
  ⚠️  Database migration (cannot be auto-rolled back)
  ⚠️  Production deployment (affects live users)

Rollback plan:
  - Database: Restore from backup
  - Application: Revert to previous deployment
  - Estimated rollback time: 10 minutes

═══════════════════════════════════════════════════════════

Ready to proceed? (yes/no):

If --dry-run:
  Show: "DRY RUN MODE - No changes will be made"
  Display all commands that would be run
  Exit without executing
```

### Preparation Phase

**Step 7: Create Checkpoint**

```bash
## Creating Checkpoint

Creating restore point...

Checkpoint ID: ckpt-20250101-120000
Timestamp: 2025-01-01 12:00:00 UTC

Saving state:
  ✓ Database snapshot: backup-20250101.sql (125 MB)
  ✓ Current deployment: v2.4.5
  ✓ Configuration: .env.production
  ✓ Git commit: abc123def

Checkpoint created successfully!

To restore:
  /{workflow-name} --rollback ckpt-20250101-120000

Checkpoint expires: 2025-01-08 (7 days)
```

**Step 8: Initialize Resources**

```bash
## Resource Initialization

Setting up execution environment...

  ✓ Creating temporary directory: /tmp/workflow-abc123
  ✓ Loading configuration: production.yml
  ✓ Initializing logger: workflow-20250101.log
  ✓ Starting progress tracker
  ✓ Setting up error handlers

Resources ready! ✓
```

### Execution Phase

**Step 9: Execute Workflow Steps**

```bash
═══════════════════════════════════════════════════════════
EXECUTION PHASE
═══════════════════════════════════════════════════════════

Progress: [●●●○○○○○○○○○○○○○○○○○] 15% (2/7 tasks)

Current Task: Building application
Started: 12:05:30
Elapsed: 2m 15s
Remaining: ~12m 45s

────────────────────────────────────────────────────────────

For each step:

┌─────────────────────────────────────────────────────────┐
│ STEP {N}: {STEP NAME}                                   │
└─────────────────────────────────────────────────────────┘

Status: In Progress...
Started: {timestamp}

[Show real-time output from step]

If step succeeds:
  ✅ STEP {N} completed successfully
  Duration: {duration}
  Output: {summary}

  Checkpoint: Saving progress...
  ✓ Checkpoint saved: step-{n}-complete

If step fails:
  ❌ STEP {N} failed

  Error: {error message}

  Attempted rollback: {rollback status}

  Options:
    1. Retry this step: /{workflow-name} --resume
    2. Skip this step: /{workflow-name} --resume --skip {n}
    3. Rollback completely: /{workflow-name} --rollback
    4. View logs: cat /path/to/workflow.log

  What would you like to do?

If step has warnings:
  ⚠️  STEP {N} completed with warnings

  Warnings:
    - {warning 1}
    - {warning 2}

  Continue anyway? (yes/no):
```

**Step 10: Handle Long-Running Operations**

```bash
## Long Operation Progress

Task: Running test suite
Progress: [●●●●●●●●●●●●○○○○○○○○] 60% (120/200 tests)

Stats:
  ✓ Passed: 118
  ❌ Failed: 2
  ⏭️  Skipped: 5
  ⏸️  Pending: 75

Current: integration/user-auth.test.ts
Elapsed: 6m 15s
Estimated remaining: 4m 10s

Failed tests:
  1. user-service.test.ts: User registration validation
  2. auth-middleware.test.ts: Token expiration handling

Continuing...

Option to cancel:
  Press Ctrl+C to stop (will create checkpoint)
```

### Verification Phase

**Step 11: Run Health Checks**

```bash
═══════════════════════════════════════════════════════════
VERIFICATION PHASE
═══════════════════════════════════════════════════════════

Running post-deployment checks...

## System Health
  ✓ Application: Responding (200 OK)
  ✓ Database: Connected (latency: 12ms)
  ✓ Cache: Operational (hit rate: 94%)
  ✓ Queue: Processing (0 failed jobs)

## Functional Tests
  ✓ User login: Working
  ✓ API endpoints: 25/25 passing
  ✓ Database queries: Optimized
  ✓ File uploads: Working

## Performance Benchmarks
  ✓ Response time (p95): 185ms (target: <200ms)
  ✓ Throughput: 1,250 req/sec (target: >1,000)
  ✓ Error rate: 0.02% (target: <0.1%)

## Security Scan
  ✓ Vulnerabilities: 0 critical, 0 high
  ✓ SSL/TLS: Valid certificate
  ✓ Headers: Secure
  ✓ Dependencies: Up to date

All checks passed! ✓

If checks fail:
  ❌ Health check failed: {check name}

  Status: {status code/error}
  Expected: {expected value}
  Actual: {actual value}

  This indicates a problem with the deployment.

  Options:
    1. Investigate: View logs and metrics
    2. Rollback: Return to previous version
    3. Ignore: Mark as acceptable risk (not recommended)

  Recommended action: ROLLBACK

  Proceed with rollback? (yes/no):
```

**Step 12: Generate Report**

```bash
═══════════════════════════════════════════════════════════
WORKFLOW COMPLETE
═══════════════════════════════════════════════════════════

✅ All tasks completed successfully!

Summary:
  Started: 2025-01-01 12:00:00 UTC
  Finished: 2025-01-01 12:28:35 UTC
  Duration: 28 minutes 35 seconds

Tasks Executed:
  ✓ 1. Database backup (2m 15s)
  ✓ 2. Run migrations (4m 50s)
  ✓ 3. Build application (8m 20s)
  ✓ 4. Run tests (10m 5s)
  ✓ 5. Deploy to production (1m 45s)
  ✓ 6. Smoke tests (45s)
  ✓ 7. Update docs (35s)

Changes Applied:
  - Database: Migrated to v2.6.0 (3 new tables)
  - Deployment: v2.4.5 → v2.5.0
  - Configuration: Updated 5 environment variables
  - Dependencies: Updated 12 packages

Metrics:
  - Files changed: 147
  - Lines added: 2,341
  - Lines removed: 892
  - Test coverage: 87.5% (+2.1%)

Resources:
  - Database backup: /backups/backup-20250101.sql
  - Deployment log: /logs/deploy-20250101.log
  - Report: /reports/workflow-20250101.html

Next Steps:
  💡 Monitor application for 15 minutes
  💡 Check error logs: /logs/production.log
  💡 Review metrics: https://monitoring.app/dashboard
  💡 Notify team: #deployments channel

Rollback Information:
  Checkpoint ID: ckpt-20250101-120000
  To rollback: /{workflow-name} --rollback ckpt-20250101-120000
  Expires: 2025-01-08 (7 days)

═══════════════════════════════════════════════════════════

📊 Full report: /reports/workflow-20250101.html

Report includes:
  - Detailed timeline
  - Resource usage graphs
  - Test results
  - Performance metrics
  - Change log

Generate PDF report? (yes/no):
```

### Cleanup Phase

**Step 13: Clean Up Temporary Resources**

```bash
## Cleanup

Removing temporary resources...

  ✓ Deleted: /tmp/workflow-abc123
  ✓ Cleared: Build cache (1.2 GB freed)
  ✓ Removed: Old checkpoints (2)
  ✓ Archived: Logs to /archive/2025/01/

Cleanup complete! ✓
```

## Error Recovery

### Handle Individual Step Failure

```markdown
If a step fails during execution:

1. Capture error details
2. Save checkpoint at failure point
3. Attempt automatic recovery (if configured)
4. If recovery fails, show options:

═══════════════════════════════════════════════════════════
❌ WORKFLOW FAILED
═══════════════════════════════════════════════════════════

Failed at: Step 3 - Build application
Error: Build failed with 5 errors
Time: 2025-01-01 12:08:15 UTC
Duration before failure: 8m 15s

Error Details:
  src/api/users.ts:45 - Type 'string' not assignable to type 'number'
  src/api/auth.ts:102 - Cannot find module '@/utils/crypto'
  [... 3 more errors]

Full error log: /logs/workflow-error-20250101.log

Checkpoint created: ckpt-20250101-120815-failure

Recovery Options:

  1. RETRY - Fix errors and retry from this step
     Command: /{workflow-name} --resume

  2. SKIP - Skip this step and continue (risky)
     Command: /{workflow-name} --resume --skip 3

  3. ROLLBACK - Undo all changes
     Command: /{workflow-name} --rollback

  4. DEBUG - Open interactive debugging session
     Command: /{workflow-name} --debug --from-checkpoint ckpt-20250101-120815-failure

  5. ABORT - Stop and clean up
     Note: Changes made so far will remain

═══════════════════════════════════════════════════════════

Recommended action: ROLLBACK (automatic rollback in 60 seconds)

Press Enter to rollback now, or choose an option (1-5):
```

### Implement Rollback

```bash
═══════════════════════════════════════════════════════════
ROLLBACK IN PROGRESS
═══════════════════════════════════════════════════════════

Rolling back to checkpoint: ckpt-20250101-120000
Created: 2025-01-01 12:00:00 UTC

Reversing changes:

  Step 3/3: Restoring database from backup
    ✓ Stopping application
    ✓ Dropping new tables
    ✓ Restoring: backup-20250101.sql
    ✓ Verifying data integrity
    ✓ Starting application

  Step 2/3: Reverting deployment
    ✓ Switching to previous version: v2.4.5
    ✓ Updating configuration
    ✓ Restarting services

  Step 1/3: Cleaning up
    ✓ Removing temporary files
    ✓ Clearing caches
    ✓ Resetting state

Rollback complete! ✓

Verification:
  ✓ Application: Running on v2.4.5
  ✓ Database: Restored to previous state
  ✓ All systems operational

System has been restored to state from 2025-01-01 12:00:00 UTC

═══════════════════════════════════════════════════════════
```

## Advanced Features

### Parallel Execution

```markdown
If steps can run in parallel:

═══════════════════════════════════════════════════════════
PARALLEL EXECUTION
═══════════════════════════════════════════════════════════

Running tasks in parallel (4 threads):

  Task 1: Build frontend      [●●●●●●●●●○○○○○○] 60%
  Task 2: Build backend       [●●●●●●●●●●●●○○○] 80%
  Task 3: Generate docs       [●●●●●●●●●●●●●●●] 100% ✓
  Task 4: Optimize images     [●●●●○○○○○○○○○○○] 27%

Overall progress: 67% (3.2/4 tasks)
Elapsed: 5m 20s
Estimated remaining: 2m 45s

All tasks complete!
Total time: 8m 5s (saved 12m with parallelization)
```

### Conditional Steps

```markdown
## Conditional Execution

Based on environment or state:

If environment is "production":
  - Require manual approval
  - Run extra security scans
  - Send notifications to ops team
  - Create detailed audit log

If environment is "staging":
  - Skip manual approval
  - Run basic health checks
  - Send notifications to dev team

If database has pending migrations:
  - Show migration plan
  - Require confirmation
  - Create backup automatically

If tests are failing:
  - Stop workflow
  - Show which tests failed
  - Suggest fixes
```

### Interactive Mode

```markdown
## Interactive Decision Points

At critical points, ask for confirmation:

⚠️  CRITICAL OPERATION AHEAD

You are about to:
  - Drop database table: legacy_users (1.2M rows)
  - This operation CANNOT be undone automatically
  - Estimated time: 2 minutes

Backup status:
  ✓ Manual backup created: backup-20250101.sql
  ✓ Automated backup: 2 hours old
  ✓ Remote backup: 1 day old

Have you verified the backup? (yes/no):

If yes:
  Type the table name to confirm: legacy_users

  If typed correctly:
    Proceeding with table drop...

  If typed incorrectly:
    Confirmation failed. Aborting operation.
```

## Monitoring and Observability

### Real-Time Metrics

```bash
═══════════════════════════════════════════════════════════
WORKFLOW METRICS (Live)
═══════════════════════════════════════════════════════════

System Resources:
  CPU Usage:     [●●●●●○○○○○] 52%
  Memory:        [●●●●●●●○○○] 72% (5.8/8 GB)
  Disk I/O:      [●●●○○○○○○○] 28 MB/s
  Network:       [●●○○○○○○○○] 15 MB/s

Workflow Progress:
  Elapsed:       15m 32s
  Remaining:     ~11m 28s
  Current Step:  4/7 (Run test suite)
  Success Rate:  100% (3/3 completed steps)

Performance:
  Avg Step Time: 5m 10s
  Slowest Step:  3. Build application (8m 20s)
  Fastest Step:  6. Smoke tests (45s)

Updated every 5 seconds...
Press 'q' to hide metrics panel
```

### Detailed Logging

```bash
## Logging

Save detailed logs:
  - Workflow execution: /logs/workflow-20250101-120000.log
  - Error logs: /logs/errors-20250101.log
  - Performance: /logs/performance-20250101.json
  - Audit trail: /logs/audit-20250101.log

Log levels:
  - DEBUG: All operations and decisions
  - INFO: Major steps and milestones
  - WARN: Non-critical issues
  - ERROR: Failures and problems

If --verbose flag:
  Show all logs in console
  Include timing for each operation
  Display full command output
```

## Integration Points

### Notifications

```markdown
Send notifications at key points:

Starting workflow:
  - Slack: #deployments
  - Email: ops-team@company.com
  - PagerDuty: Info alert

Critical operation:
  - Slack: @channel in #deployments
  - Email: ops-leads@company.com

Failure:
  - Slack: @oncall with full error
  - PagerDuty: High-priority incident
  - Email: All stakeholders

Success:
  - Slack: Success message with metrics
  - Email: Summary report
```

### External Tools

```markdown
Integrate with:

## CI/CD
- Trigger from: GitHub Actions, GitLab CI, Jenkins
- Report back: Build status, test results
- Update: Deployment records

## Monitoring
- Log to: DataDog, New Relic, Sentry
- Create: Dashboard annotations
- Track: Custom metrics

## Project Management
- Update: JIRA tickets
- Close: Related issues
- Create: Deployment record
```

## Best Practices

✅ **Always include:**
- Pre-flight checks
- Dry-run mode
- Progress indicators
- Error recovery
- Rollback capability
- Detailed logging
- Final verification

✅ **For production workflows:**
- Require manual approval
- Create automatic backups
- Implement health checks
- Set up monitoring
- Plan for rollback
- Document everything
- Test in staging first

✅ **For safety:**
- Validate all inputs
- Confirm destructive operations
- Create checkpoints
- Save audit logs
- Implement timeouts
- Handle interruptions
- Provide escape hatches

## Customization

Add your specific workflow steps:

```markdown
## Custom Steps

### Step: Run Custom Scripts
Execute project-specific scripts:
  - Pre-deployment hooks
  - Data migrations
  - Cache warming
  - Feature flag updates

### Step: Integration Tests
Run against real services:
  - API integration tests
  - Database integration tests
  - Third-party service tests

### Step: Approval Gates
Wait for manual approval:
  - Show pending approval UI
  - Send notification to approvers
  - Wait for response (timeout: 1 hour)
  - Proceed or abort based on response
```

## Notes

This workflow template provides:
- Professional-grade orchestration
- Production-ready error handling
- Comprehensive monitoring
- Safe execution with rollback
- Detailed reporting
- Team collaboration features

Use this for complex, critical operations where safety and observability are paramount.
