Perform a complete production release with all checks and notifications.

Arguments: $ARGUMENTS (optional: version type - major/minor/patch)

## Pre-Release Validation

1. **Check Git Status**
   ```bash
   git status
   ```
   - Ensure working directory is clean
   - Ensure on correct branch (main/master)
   - Ensure branch is up to date with remote

2. **Run All Tests**
   ```bash
   npm test  # or appropriate test command
   ```
   - Tests must pass (exit if failures)
   - Display test results

3. **Run Linter**
   ```bash
   npm run lint
   ```
   - Code must pass linting
   - Show any warnings

## Version Management

4. **Determine Version Bump**
   - If version specified in $ARGUMENTS, use that
   - Otherwise, analyze commits since last tag
   - Suggest version based on conventional commits:
     - `feat:` → minor
     - `fix:` → patch
     - `BREAKING CHANGE:` → major
   - Confirm with user

5. **Update Version Files**
   - Update package.json (or equivalent)
   - Update any other version files
   - Commit version changes

## Changelog and Documentation

6. **Generate Changelog Entry**
   - Get commits since last tag
   - Format as changelog entry
   - Update CHANGELOG.md
   - Commit changelog

## Git Operations

7. **Create Git Tag**
   ```bash
   git tag -a v{version} -m "Release v{version}"
   ```

8. **Push Everything**
   ```bash
   git push origin main --tags
   ```

## External Integrations (if MCP configured)

9. **Create GitHub Release** (if GitHub MCP enabled)
   - Create release on GitHub
   - Use changelog as release notes
   - Attach any build artifacts

10. **Notify Team** (if Slack MCP enabled)
    - Post to #releases channel
    - Include version and changelog highlights
    - Link to GitHub release

## Final Steps

11. **Display Summary**
    ```
    ✅ Release v{version} Complete!

    📦 Version: {version}
    🏷️  Tag: v{version}
    🔗 GitHub: {release_url}
    💬 Team notified on Slack

    Next steps:
    - Monitor deployment
    - Watch for issues
    - Update documentation if needed
    ```

## Error Handling

- If tests fail → Abort with error message
- If working directory dirty → Ask to commit or stash
- If not on main branch → Confirm or abort
- If version already exists → Ask to use different version
- For any failure → Provide clear next steps

## Safety Features

- Requires clean working directory
- Requires passing tests
- Confirms version bump
- Creates backup tag before proceeding
- Provides rollback instructions if needed
