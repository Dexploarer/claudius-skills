#!/usr/bin/env python3
"""
Bug Hunting Championship Coordinator

Orchestrates three competing AI teams in a bug hunting competition with
reinforcement learning-based strategy adaptation.
"""

import argparse
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import subprocess
import sys

from scoring_engine import ScoringEngine, BugReport
from metrics import MetricsTracker
from reinforcement import ReinforcementLearner


@dataclass
class TeamConfig:
    """Configuration for a competing team"""
    name: str
    strategy: str
    subagent_file: str
    focus_areas: List[str]
    tools: List[str]
    initial_weights: Dict[str, float]


@dataclass
class RoundResults:
    """Results from a single round of competition"""
    round_number: int
    timestamp: str
    teams: Dict[str, 'TeamRoundResult']
    duration_seconds: float
    target_path: str


@dataclass
class TeamRoundResult:
    """Individual team's results for a round"""
    team_name: str
    bugs_found: List[BugReport]
    score: float
    false_positives: int
    unique_discoveries: int
    avg_time_to_discovery: float
    strategy_weights: Dict[str, float]


class BugHuntingCoordinator:
    """
    Coordinates competitive bug hunting between three AI teams
    with reinforcement learning strategy adaptation.
    """

    def __init__(
        self,
        target_path: Path,
        rounds: int = 5,
        output_dir: Optional[Path] = None,
        visualize: bool = False
    ):
        self.target_path = Path(target_path)
        self.rounds = rounds
        self.output_dir = output_dir or Path("./results")
        self.visualize = visualize

        # Initialize components
        self.scoring_engine = ScoringEngine()
        self.metrics_tracker = MetricsTracker()
        self.rl_learner = ReinforcementLearner()

        # Setup output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Initialize teams
        self.teams = self._initialize_teams()

        # Track all results
        self.all_rounds: List[RoundResults] = []

    def _initialize_teams(self) -> Dict[str, TeamConfig]:
        """Initialize the three competing teams with their strategies"""
        return {
            "team1": TeamConfig(
                name="Automated Scanners",
                strategy="automated",
                subagent_file=".claude/subagents/team1-automated-scanner.md",
                focus_areas=[
                    "pattern_matching",
                    "static_analysis",
                    "dependency_scanning",
                    "known_vulnerabilities"
                ],
                tools=[
                    "grep", "ripgrep", "ast_parser",
                    "dependency_checker", "cve_database"
                ],
                initial_weights={
                    "sql_injection": 1.0,
                    "xss": 1.0,
                    "csrf": 0.8,
                    "auth_bypass": 0.7,
                    "path_traversal": 0.9,
                    "command_injection": 0.8,
                    "xxe": 0.6,
                    "deserialization": 0.5
                }
            ),
            "team2": TeamConfig(
                name="Manual Reviewers",
                strategy="manual",
                subagent_file=".claude/subagents/team2-manual-reviewer.md",
                focus_areas=[
                    "business_logic",
                    "authentication",
                    "authorization",
                    "logic_flaws",
                    "access_control"
                ],
                tools=[
                    "code_review", "logic_analyzer",
                    "flow_tracker", "context_analyzer"
                ],
                initial_weights={
                    "business_logic": 1.0,
                    "auth_bypass": 1.0,
                    "privilege_escalation": 0.9,
                    "idor": 0.8,
                    "race_conditions": 0.6,
                    "session_management": 0.8,
                    "cryptographic_issues": 0.7,
                    "input_validation": 0.7
                }
            ),
            "team3": TeamConfig(
                name="Fuzzers & Behavioral Analysts",
                strategy="fuzzing",
                subagent_file=".claude/subagents/team3-fuzzer.md",
                focus_areas=[
                    "input_fuzzing",
                    "edge_cases",
                    "runtime_behavior",
                    "race_conditions",
                    "memory_issues"
                ],
                tools=[
                    "fuzzer", "behavior_monitor",
                    "race_detector", "memory_profiler"
                ],
                initial_weights={
                    "buffer_overflow": 1.0,
                    "race_conditions": 1.0,
                    "dos_vulnerabilities": 0.7,
                    "memory_leaks": 0.6,
                    "integer_overflow": 0.8,
                    "null_pointer": 0.5,
                    "edge_case_crashes": 0.9,
                    "resource_exhaustion": 0.6
                }
            )
        }

    def run_championship(self) -> Dict[str, Any]:
        """
        Run the complete championship across all rounds

        Returns:
            Final results including winner, statistics, and insights
        """
        print(f"\n{'='*60}")
        print(f"  BUG HUNTING CHAMPIONSHIP")
        print(f"{'='*60}")
        print(f"Target: {self.target_path}")
        print(f"Rounds: {self.rounds}")
        print(f"Teams: {len(self.teams)}")
        print(f"{'='*60}\n")

        for round_num in range(1, self.rounds + 1):
            print(f"\n{'─'*60}")
            print(f"  ROUND {round_num}/{self.rounds}")
            print(f"{'─'*60}\n")

            round_results = self._run_round(round_num)
            self.all_rounds.append(round_results)

            # Display round summary
            self._display_round_summary(round_results)

            # Apply reinforcement learning
            if round_num < self.rounds:
                self._apply_reinforcement_learning(round_results)
                print("\n✓ Team strategies adapted based on performance\n")

        # Generate final results
        final_results = self._generate_final_results()

        # Display championship results
        self._display_championship_results(final_results)

        # Save results
        self._save_results(final_results)

        # Visualize if requested
        if self.visualize:
            self._visualize_results(final_results)

        return final_results

    def _run_round(self, round_num: int) -> RoundResults:
        """Execute a single round of competition"""
        start_time = time.time()
        team_results = {}

        # Track discovered bugs across all teams for uniqueness detection
        all_bugs: Dict[str, BugReport] = {}

        for team_id, team_config in self.teams.items():
            print(f"  ▶ {team_config.name} hunting...")

            # Execute team's bug hunting
            bugs = self._execute_team_hunt(team_config, round_num)

            # Score the bugs
            scored_bugs = []
            for bug in bugs:
                score = self.scoring_engine.score_bug(bug)

                # Check uniqueness
                bug_signature = self._get_bug_signature(bug)
                if bug_signature not in all_bugs:
                    all_bugs[bug_signature] = bug
                    bug.is_unique = True
                    bug.discovered_by = team_id
                else:
                    bug.is_unique = False

                scored_bugs.append(bug)

            # Calculate team metrics
            team_result = self._calculate_team_metrics(
                team_config,
                scored_bugs,
                round_num
            )
            team_results[team_id] = team_result

        duration = time.time() - start_time

        return RoundResults(
            round_number=round_num,
            timestamp=datetime.now().isoformat(),
            teams=team_results,
            duration_seconds=duration,
            target_path=str(self.target_path)
        )

    def _execute_team_hunt(
        self,
        team: TeamConfig,
        round_num: int
    ) -> List[BugReport]:
        """
        Execute bug hunting for a specific team using Claude Code subagent

        In a real implementation, this would invoke the Claude Code subagent
        defined in team.subagent_file. For this framework, we'll simulate
        the interaction.
        """
        # In production, this would be:
        # result = subprocess.run([
        #     "claude",
        #     "agent",
        #     team.subagent_file,
        #     "--target", str(self.target_path),
        #     "--weights", json.dumps(team.initial_weights),
        #     "--round", str(round_num)
        # ], capture_output=True, text=True)

        # For now, we'll create a prompt that would be used with the subagent
        prompt = self._generate_team_prompt(team, round_num)

        # Simulated bug discovery (in reality, Claude Code would execute this)
        bugs = self._simulate_bug_discovery(team, prompt)

        return bugs

    def _generate_team_prompt(self, team: TeamConfig, round_num: int) -> str:
        """Generate the prompt for a team's bug hunting session"""
        return f"""
You are {team.name}, competing in Round {round_num} of the Bug Hunting Championship.

Your Strategy: {team.strategy}

Your Focus Areas:
{chr(10).join(f"  - {area}" for area in team.focus_areas)}

Your Tools:
{chr(10).join(f"  - {tool}" for tool in team.tools)}

Your Current Detection Weights:
{json.dumps(team.initial_weights, indent=2)}

Target: {self.target_path}

Your Mission:
1. Search for security vulnerabilities and bugs in the target codebase
2. Focus on your specialty areas: {', '.join(team.focus_areas)}
3. Prioritize high-severity issues (CVSS 7.0+)
4. Provide detailed, actionable reports for each bug
5. Minimize false positives (they hurt your score)
6. Be thorough but efficient

For each bug you find, report:
- Vulnerability type (e.g., SQL Injection, XSS, Auth Bypass)
- Location (file:line)
- Severity (Critical/High/Medium/Low)
- CVSS score (0-10)
- Proof of concept
- Remediation steps

Remember: You're competing against two other teams. Unique discoveries
earn bonus points. Quality matters more than quantity.

Begin your hunt!
"""

    def _simulate_bug_discovery(
        self,
        team: TeamConfig,
        prompt: str
    ) -> List[BugReport]:
        """
        Simulate bug discovery based on team strategy

        In production, this would be replaced by actual Claude Code execution
        """
        # This is a placeholder - real implementation would invoke Claude Code
        bugs = []

        # Simulate different discovery patterns for each team
        if team.strategy == "automated":
            # Automated scanners find more medium/low bugs quickly
            bugs = [
                BugReport(
                    vuln_type="SQL Injection",
                    location="src/db/queries.py:45",
                    severity="high",
                    cvss_score=8.5,
                    description="Unsanitized user input in SQL query",
                    proof_of_concept="payload: ' OR '1'='1",
                    remediation="Use parameterized queries",
                    discovered_at=time.time(),
                    team=team.name
                ),
                BugReport(
                    vuln_type="XSS",
                    location="src/templates/user_profile.html:12",
                    severity="medium",
                    cvss_score=6.5,
                    description="Unescaped user input in template",
                    proof_of_concept="<script>alert('XSS')</script>",
                    remediation="Use template auto-escaping",
                    discovered_at=time.time(),
                    team=team.name
                )
            ]
        elif team.strategy == "manual":
            # Manual reviewers find critical business logic bugs
            bugs = [
                BugReport(
                    vuln_type="Authentication Bypass",
                    location="src/auth/middleware.py:78",
                    severity="critical",
                    cvss_score=9.8,
                    description="JWT validation can be bypassed with null signature",
                    proof_of_concept="Send token with null signature algorithm",
                    remediation="Enforce signature validation",
                    discovered_at=time.time(),
                    team=team.name
                ),
                BugReport(
                    vuln_type="IDOR",
                    location="src/api/users.py:123",
                    severity="high",
                    cvss_score=7.5,
                    description="User can access other users' data via ID manipulation",
                    proof_of_concept="GET /api/users/123 returns any user's data",
                    remediation="Implement proper authorization checks",
                    discovered_at=time.time(),
                    team=team.name
                )
            ]
        else:  # fuzzing
            # Fuzzers find race conditions and edge cases
            bugs = [
                BugReport(
                    vuln_type="Race Condition",
                    location="src/payment/processor.py:234",
                    severity="critical",
                    cvss_score=9.1,
                    description="Double-spend vulnerability in payment processing",
                    proof_of_concept="Send two concurrent payment requests",
                    remediation="Implement transaction locking",
                    discovered_at=time.time(),
                    team=team.name
                ),
                BugReport(
                    vuln_type="Integer Overflow",
                    location="src/utils/calculator.py:56",
                    severity="medium",
                    cvss_score=5.8,
                    description="Integer overflow in quantity calculation",
                    proof_of_concept="quantity = 2^32",
                    remediation="Add bounds checking",
                    discovered_at=time.time(),
                    team=team.name
                )
            ]

        return bugs

    def _get_bug_signature(self, bug: BugReport) -> str:
        """Generate a unique signature for a bug to detect duplicates"""
        return f"{bug.vuln_type}:{bug.location}:{bug.severity}"

    def _calculate_team_metrics(
        self,
        team: TeamConfig,
        bugs: List[BugReport],
        round_num: int
    ) -> TeamRoundResult:
        """Calculate comprehensive metrics for a team's performance"""
        total_score = 0
        false_positives = 0
        unique_count = 0
        discovery_times = []

        for bug in bugs:
            if bug.is_false_positive:
                false_positives += 1
                total_score -= 20  # Penalty
            else:
                bug_score = self.scoring_engine.calculate_total_score(bug)
                total_score += bug_score

                if bug.is_unique:
                    unique_count += 1

                # Track discovery time (simulated)
                discovery_times.append(bug.discovered_at)

        avg_time = (
            sum(discovery_times) / len(discovery_times)
            if discovery_times else 0
        )

        return TeamRoundResult(
            team_name=team.name,
            bugs_found=bugs,
            score=total_score,
            false_positives=false_positives,
            unique_discoveries=unique_count,
            avg_time_to_discovery=avg_time,
            strategy_weights=team.initial_weights.copy()
        )

    def _display_round_summary(self, results: RoundResults):
        """Display summary of round results"""
        print(f"\n  Round {results.round_number} Summary:")
        print(f"  {'─'*56}\n")

        # Sort teams by score
        sorted_teams = sorted(
            results.teams.items(),
            key=lambda x: x[1].score,
            reverse=True
        )

        for rank, (team_id, result) in enumerate(sorted_teams, 1):
            medal = ["🥇", "🥈", "🥉"][rank-1] if rank <= 3 else "  "
            print(f"  {medal} {result.team_name:<30} Score: {result.score:>6.0f}")
            print(f"     Bugs: {len(result.bugs_found):>2}  |  " +
                  f"Unique: {result.unique_discoveries:>2}  |  " +
                  f"False+: {result.false_positives:>2}")

        print(f"\n  Duration: {results.duration_seconds:.1f}s\n")

    def _apply_reinforcement_learning(self, results: RoundResults):
        """Apply reinforcement learning to adapt team strategies"""
        for team_id, team_result in results.teams.items():
            # Update weights based on performance
            updated_weights = self.rl_learner.update_weights(
                current_weights=team_result.strategy_weights,
                bugs_found=team_result.bugs_found,
                score=team_result.score,
                false_positives=team_result.false_positives
            )

            # Apply updated weights to team
            self.teams[team_id].initial_weights = updated_weights

    def _generate_final_results(self) -> Dict[str, Any]:
        """Generate comprehensive final results"""
        # Aggregate scores across all rounds
        team_totals = {team_id: 0 for team_id in self.teams.keys()}
        team_stats = {
            team_id: {
                "total_bugs": 0,
                "unique_bugs": 0,
                "false_positives": 0,
                "critical_bugs": 0,
                "high_bugs": 0,
                "scores_per_round": []
            }
            for team_id in self.teams.keys()
        }

        for round_result in self.all_rounds:
            for team_id, result in round_result.teams.items():
                team_totals[team_id] += result.score
                stats = team_stats[team_id]
                stats["total_bugs"] += len(result.bugs_found)
                stats["unique_bugs"] += result.unique_discoveries
                stats["false_positives"] += result.false_positives
                stats["scores_per_round"].append(result.score)

                # Count severity
                for bug in result.bugs_found:
                    if bug.severity == "critical":
                        stats["critical_bugs"] += 1
                    elif bug.severity == "high":
                        stats["high_bugs"] += 1

        # Determine winner
        winner_id = max(team_totals.items(), key=lambda x: x[1])[0]
        winner = self.teams[winner_id]

        return {
            "championship_id": self.session_id,
            "target": str(self.target_path),
            "rounds": self.rounds,
            "winner": {
                "id": winner_id,
                "name": winner.name,
                "strategy": winner.strategy,
                "total_score": team_totals[winner_id],
                "stats": team_stats[winner_id]
            },
            "all_teams": {
                team_id: {
                    "name": self.teams[team_id].name,
                    "total_score": score,
                    "stats": team_stats[team_id]
                }
                for team_id, score in team_totals.items()
            },
            "rounds": [asdict(r) for r in self.all_rounds],
            "insights": self._generate_insights(team_totals, team_stats, winner_id)
        }

    def _generate_insights(
        self,
        team_totals: Dict[str, float],
        team_stats: Dict[str, Dict],
        winner_id: str
    ) -> Dict[str, Any]:
        """Generate insights about winning strategies"""
        winner_stats = team_stats[winner_id]
        winner_config = self.teams[winner_id]

        return {
            "winning_strategy": winner_config.strategy,
            "key_strengths": winner_config.focus_areas,
            "critical_bugs_ratio": (
                winner_stats["critical_bugs"] /
                max(winner_stats["total_bugs"], 1)
            ),
            "false_positive_rate": (
                winner_stats["false_positives"] /
                max(winner_stats["total_bugs"], 1)
            ),
            "recommended_approach": self._synthesize_best_practices(
                team_stats,
                {k: v for k, v in self.teams.items()}
            )
        }

    def _synthesize_best_practices(
        self,
        team_stats: Dict[str, Dict],
        teams: Dict[str, TeamConfig]
    ) -> List[str]:
        """Synthesize best practices from all teams"""
        practices = []

        # Find team with lowest false positive rate
        best_accuracy = min(
            team_stats.items(),
            key=lambda x: x[1]["false_positives"] / max(x[1]["total_bugs"], 1)
        )
        practices.append(
            f"Use {teams[best_accuracy[0]].name}'s approach " +
            f"for accuracy: {teams[best_accuracy[0]].strategy}"
        )

        # Find team with most critical bugs
        best_severity = max(
            team_stats.items(),
            key=lambda x: x[1]["critical_bugs"]
        )
        practices.append(
            f"Apply {teams[best_severity[0]].name}'s techniques " +
            f"for critical bug discovery"
        )

        # Find team with most unique discoveries
        best_coverage = max(
            team_stats.items(),
            key=lambda x: x[1]["unique_bugs"]
        )
        practices.append(
            f"Leverage {teams[best_coverage[0]].name}'s coverage " +
            f"for comprehensive scanning"
        )

        return practices

    def _display_championship_results(self, results: Dict[str, Any]):
        """Display final championship results"""
        print(f"\n{'='*60}")
        print(f"  FINAL CHAMPIONSHIP RESULTS")
        print(f"{'='*60}\n")

        # Sort teams by total score
        sorted_teams = sorted(
            results["all_teams"].items(),
            key=lambda x: x[1]["total_score"],
            reverse=True
        )

        for rank, (team_id, team_data) in enumerate(sorted_teams, 1):
            medal = ["🥇", "🥈", "🥉"][rank-1] if rank <= 3 else "  "
            print(f"{medal} {team_data['name']:<30} " +
                  f"Total: {team_data['total_score']:>7.0f}")
            stats = team_data['stats']
            print(f"   Critical: {stats['critical_bugs']:>2}  |  " +
                  f"High: {stats['high_bugs']:>2}  |  " +
                  f"Total Bugs: {stats['total_bugs']:>3}  |  " +
                  f"FP: {stats['false_positives']:>2}")
            print()

        print(f"{'─'*60}\n")
        print("Winning Strategy Analysis:")
        print(f"  Strategy: {results['insights']['winning_strategy']}")
        print(f"  Key Strengths: {', '.join(results['insights']['key_strengths'])}")
        print(f"  Critical Bug Ratio: {results['insights']['critical_bugs_ratio']:.1%}")
        print(f"  False Positive Rate: {results['insights']['false_positive_rate']:.1%}")

        print(f"\n{'─'*60}\n")
        print("Recommended Combined Approach:")
        for i, practice in enumerate(results['insights']['recommended_approach'], 1):
            print(f"  {i}. {practice}")

        print(f"\n{'='*60}\n")

    def _save_results(self, results: Dict[str, Any]):
        """Save results to JSON file"""
        output_file = self.output_dir / f"championship_{self.session_id}.json"

        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)

        print(f"Results saved to: {output_file}")

    def _visualize_results(self, results: Dict[str, Any]):
        """Generate visualizations of results"""
        # This would generate charts using matplotlib or similar
        # Placeholder for now
        print("\nVisualization would be generated here...")
        print("  - Score progression per round")
        print("  - Bug severity distribution")
        print("  - Team comparison charts")


def main():
    """Main entry point for the bug hunting coordinator"""
    parser = argparse.ArgumentParser(
        description="Bug Hunting Championship Coordinator"
    )
    parser.add_argument(
        "--target",
        type=Path,
        required=True,
        help="Path to target codebase"
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=5,
        help="Number of rounds to run (default: 5)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("./results"),
        help="Output directory for results (default: ./results)"
    )
    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Generate visualizations of results"
    )

    args = parser.parse_args()

    # Validate target exists
    if not args.target.exists():
        print(f"Error: Target path does not exist: {args.target}")
        sys.exit(1)

    # Create coordinator
    coordinator = BugHuntingCoordinator(
        target_path=args.target,
        rounds=args.rounds,
        output_dir=args.output,
        visualize=args.visualize
    )

    # Run championship
    try:
        results = coordinator.run_championship()
        sys.exit(0)
    except Exception as e:
        print(f"Error running championship: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
