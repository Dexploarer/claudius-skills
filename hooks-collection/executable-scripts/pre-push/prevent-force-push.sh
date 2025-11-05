#!/usr/bin/env bash
# Pre-push hook: Prevent Force Push
# Prevents dangerous force pushes to protected branches

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../helpers/common.sh"

print_header "🚫 Force Push Protection"

# Read pre-push hook arguments
# Format: <local ref> <local sha1> <remote ref> <remote sha1>
while read local_ref local_sha remote_ref remote_sha; do
    # Extract branch name from ref
    local_branch=$(echo "$local_ref" | sed 's/refs\/heads\///')
    remote_branch=$(echo "$remote_ref" | sed 's/refs\/heads\///')

    print_info "Checking push to: $remote_branch"

    # Check if this is a force push
    # A force push occurs when the remote commit is not an ancestor of the local commit
    # and we're trying to update the remote ref

    if [[ "$remote_sha" != "0000000000000000000000000000000000000000" ]]; then
        # Remote branch exists, check if it's a fast-forward
        if ! git merge-base --is-ancestor "$remote_sha" "$local_sha" 2>/dev/null; then
            # This is a non-fast-forward push (force push)

            if is_protected_branch "$remote_branch"; then
                print_header "⛔ FORCE PUSH BLOCKED"

                cat << EOF

You're attempting to force push to a protected branch!

Branch: ${BOLD}$remote_branch${NC}
Risk Level: ${RED}${BOLD}HIGH${NC}

⚠️  WHY THIS IS DANGEROUS:

• Overwrites remote history permanently
• Can lose other developers' work
• Breaks team's git history
• Very difficult to recover from
• May cause deployment issues
• Team members will have conflicts

🔒 PROTECTED BRANCHES:

• main
• master
• develop
• production
• staging

✅ SAFER ALTERNATIVES:

1. Merge instead of rebase:
   git checkout $remote_branch
   git pull origin $remote_branch
   git merge $local_branch
   git push origin $remote_branch

2. Create a new branch:
   git checkout -b ${remote_branch}-v2
   git push origin ${remote_branch}-v2

3. Coordinate with team:
   • Notify team before force push
   • Ensure no one has pending work on this branch
   • Use --force-with-lease (safer than --force)
   • Wait for approval from team lead

4. If you must force push:
   • Temporarily disable this hook
   • Or contact repository admin

EOF

                print_error "Force push to protected branch blocked!"
                exit 1

            else
                # Non-protected branch, show warning but allow
                print_warning "Force push detected to: $remote_branch"

                cat << EOF

⚠️  Force Push Warning

You're force pushing to: ${YELLOW}${BOLD}$remote_branch${NC}

This is allowed but please verify:
✓ No one else is using this branch
✓ You have a backup of important commits
✓ You understand you're rewriting history
✓ This is your personal feature branch

EOF

                if ! ask_yes_no "Proceed with force push?"; then
                    print_error "Force push cancelled by user"
                    exit 1
                fi

                print_warning "Proceeding with force push..."
            fi
        fi
    fi

    # Additional checks for protected branches
    if is_protected_branch "$remote_branch"; then
        print_info "Pushing to protected branch: $remote_branch"

        # Check if there are uncommitted changes
        if ! git diff-index --quiet HEAD --; then
            print_warning "You have uncommitted changes!"
            if ! ask_yes_no "Continue with push?"; then
                exit 1
            fi
        fi

        # Check if we're ahead of remote
        if [[ "$remote_sha" != "0000000000000000000000000000000000000000" ]]; then
            commits_ahead=$(git rev-list --count "$remote_sha..$local_sha")
            commits_behind=$(git rev-list --count "$local_sha..$remote_sha")

            if [[ $commits_behind -gt 0 ]]; then
                print_warning "You are $commits_behind commit(s) behind remote"
                print_warning "Consider pulling changes first"
            fi

            if [[ $commits_ahead -gt 0 ]]; then
                print_info "You are $commits_ahead commit(s) ahead of remote"
            fi
        fi
    fi

done

print_success "Push checks passed!"
exit 0
