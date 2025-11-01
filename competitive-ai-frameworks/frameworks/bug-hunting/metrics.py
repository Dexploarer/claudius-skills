#!/usr/bin/env python3
"""
Metrics Tracker for Bug Hunting Championship

Tracks and analyzes performance metrics across rounds for strategy optimization
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
import json
import time


@dataclass
class TeamMetrics:
    """Comprehensive metrics for a team across all rounds"""
    team_id: str
    team_name: str

    # Score metrics
    total_score: float = 0.0
    scores_per_round: List[float] = field(default_factory=list)
    average_score: float = 0.0
    score_trend: str = "stable"  # "improving", "declining", "stable"

    # Bug discovery metrics
    total_bugs: int = 0
    bugs_per_round: List[int] = field(default_factory=list)
    unique_bugs: int = 0
    duplicate_bugs: int = 0

    # Severity metrics
    critical_bugs: int = 0
    high_bugs: int = 0
    medium_bugs: int = 0
    low_bugs: int = 0

    # Quality metrics
    false_positives: int = 0
    false_positive_rate: float = 0.0
    average_report_quality: float = 0.0
    quality_score_total: float = 0.0
    quality_score_samples: int = 0

    # Efficiency metrics
    average_time_to_discovery: float = 0.0
    time_to_discovery_per_round: List[float] = field(default_factory=list)
    bugs_per_minute: float = 0.0

    # Vulnerability type distribution
    vuln_types: Dict[str, int] = field(default_factory=dict)

    # Comparative metrics
    rank_per_round: List[int] = field(default_factory=list)
    times_ranked_first: int = 0
    times_ranked_last: int = 0


class MetricsTracker:
    """
    Tracks and analyzes team performance metrics across championship rounds
    """

    def __init__(self):
        """Initialize metrics tracker"""
        self.team_metrics: Dict[str, TeamMetrics] = {}
        self.round_data: List[Dict] = []
        self.start_time: Optional[float] = None

    def initialize_team(self, team_id: str, team_name: str):
        """Initialize tracking for a team"""
        self.team_metrics[team_id] = TeamMetrics(
            team_id=team_id,
            team_name=team_name
        )

    def record_round(
        self,
        round_number: int,
        team_results: Dict[str, 'TeamRoundResult']
    ):
        """
        Record results from a round

        Args:
            round_number: The round number
            team_results: Dictionary of team results
        """
        # Initialize teams if needed
        for team_id, result in team_results.items():
            if team_id not in self.team_metrics:
                self.initialize_team(team_id, result.team_name)

        # Calculate rankings for this round
        rankings = self._calculate_rankings(team_results)

        # Update metrics for each team
        for team_id, result in team_results.items():
            metrics = self.team_metrics[team_id]

            # Score metrics
            metrics.total_score += result.score
            metrics.scores_per_round.append(result.score)
            metrics.average_score = (
                metrics.total_score / len(metrics.scores_per_round)
            )

            # Bug discovery metrics (filter out false positives)
            valid_bugs = [bug for bug in result.bugs_found if not bug.is_false_positive]
            valid_bug_count = len(valid_bugs)

            metrics.total_bugs += valid_bug_count
            metrics.bugs_per_round.append(valid_bug_count)
            metrics.unique_bugs += result.unique_discoveries
            metrics.duplicate_bugs += max(
                0,
                valid_bug_count - result.unique_discoveries
            )

            # Severity metrics
            for bug in valid_bugs:
                if bug.severity == "critical":
                    metrics.critical_bugs += 1
                elif bug.severity == "high":
                    metrics.high_bugs += 1
                elif bug.severity == "medium":
                    metrics.medium_bugs += 1
                elif bug.severity == "low":
                    metrics.low_bugs += 1

                # Track vulnerability types
                if bug.vuln_type not in metrics.vuln_types:
                    metrics.vuln_types[bug.vuln_type] = 0
                metrics.vuln_types[bug.vuln_type] += 1

            # Quality metrics
            metrics.false_positives += result.false_positives
            total_reports = metrics.total_bugs + metrics.false_positives
            if total_reports > 0:
                metrics.false_positive_rate = (
                    metrics.false_positives / total_reports
                )

            # Calculate cumulative average report quality
            quality_scores = [bug.quality_score for bug in valid_bugs]
            if quality_scores:
                metrics.quality_score_total += sum(quality_scores)
                metrics.quality_score_samples += len(quality_scores)
                metrics.average_report_quality = (
                    metrics.quality_score_total / metrics.quality_score_samples
                )

            # Efficiency metrics - cumulative average
            if result.avg_time_to_discovery is not None and result.avg_time_to_discovery > 0:
                metrics.time_to_discovery_per_round.append(result.avg_time_to_discovery)
                metrics.average_time_to_discovery = (
                    sum(metrics.time_to_discovery_per_round)
                    / len(metrics.time_to_discovery_per_round)
                )

            # Ranking metrics
            rank = rankings[team_id]
            metrics.rank_per_round.append(rank)
            if rank == 1:
                metrics.times_ranked_first += 1
            elif rank == len(team_results):
                metrics.times_ranked_last += 1

        # Calculate trends
        self._calculate_trends()

        # Store round data
        self.round_data.append({
            "round": round_number,
            "results": team_results,
            "rankings": rankings
        })

    def _calculate_rankings(
        self,
        team_results: Dict[str, 'TeamRoundResult']
    ) -> Dict[str, int]:
        """Calculate team rankings for a round"""
        # Sort teams by score
        sorted_teams = sorted(
            team_results.items(),
            key=lambda x: x[1].score,
            reverse=True
        )

        # Assign ranks
        rankings = {}
        for rank, (team_id, _) in enumerate(sorted_teams, 1):
            rankings[team_id] = rank

        return rankings

    def _calculate_trends(self):
        """Calculate performance trends for all teams"""
        for metrics in self.team_metrics.values():
            if len(metrics.scores_per_round) < 2:
                metrics.score_trend = "stable"
                continue

            # Calculate trend using simple linear regression
            scores = metrics.scores_per_round
            n = len(scores)
            x = list(range(n))
            y = scores

            # Calculate slope
            x_mean = sum(x) / n
            y_mean = sum(y) / n
            numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
            denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

            if denominator == 0:
                slope = 0
            else:
                slope = numerator / denominator

            # Classify trend
            if slope > 5:  # Significant improvement
                metrics.score_trend = "improving"
            elif slope < -5:  # Significant decline
                metrics.score_trend = "declining"
            else:
                metrics.score_trend = "stable"

    def get_team_metrics(self, team_id: str) -> Optional[TeamMetrics]:
        """Get metrics for a specific team"""
        return self.team_metrics.get(team_id)

    def get_all_metrics(self) -> Dict[str, TeamMetrics]:
        """Get metrics for all teams"""
        return self.team_metrics

    def get_leaderboard(self) -> List[Tuple[str, TeamMetrics]]:
        """
        Get current leaderboard

        Returns:
            List of (team_id, metrics) tuples sorted by total score
        """
        return sorted(
            self.team_metrics.items(),
            key=lambda x: x[1].total_score,
            reverse=True
        )

    def get_best_performing_team(self) -> Optional[Tuple[str, TeamMetrics]]:
        """Get the best performing team overall"""
        leaderboard = self.get_leaderboard()
        return leaderboard[0] if leaderboard else None

    def get_most_improved_team(self) -> Optional[Tuple[str, TeamMetrics]]:
        """Get the team that improved the most"""
        improving_teams = [
            (team_id, metrics)
            for team_id, metrics in self.team_metrics.items()
            if metrics.score_trend == "improving"
        ]

        if not improving_teams:
            return None

        # Calculate improvement rate
        def improvement_rate(metrics: TeamMetrics) -> float:
            if len(metrics.scores_per_round) < 2:
                return 0.0
            return (
                metrics.scores_per_round[-1] -
                metrics.scores_per_round[0]
            ) / len(metrics.scores_per_round)

        return max(
            improving_teams,
            key=lambda x: improvement_rate(x[1])
        )

    def get_specialist_teams(self) -> Dict[str, Tuple[str, TeamMetrics]]:
        """
        Identify specialist teams

        Returns:
            Dictionary mapping specialties to (team_id, metrics)
        """
        specialists = {}

        # Most critical bugs
        if self.team_metrics:
            specialists["critical_hunter"] = max(
                self.team_metrics.items(),
                key=lambda x: x[1].critical_bugs
            )

            # Best accuracy (lowest false positive rate)
            teams_with_bugs = [
                (tid, m) for tid, m in self.team_metrics.items()
                if m.total_bugs > 0
            ]
            if teams_with_bugs:
                specialists["most_accurate"] = min(
                    teams_with_bugs,
                    key=lambda x: x[1].false_positive_rate
                )

            # Most unique discoveries
            specialists["best_coverage"] = max(
                self.team_metrics.items(),
                key=lambda x: x[1].unique_bugs
            )

            # Highest quality reports
            specialists["best_reporter"] = max(
                self.team_metrics.items(),
                key=lambda x: x[1].average_report_quality
            )

        return specialists

    def generate_comparative_analysis(self) -> Dict[str, any]:
        """
        Generate comparative analysis across all teams

        Returns:
            Comprehensive comparison data
        """
        if not self.team_metrics:
            return {}

        leaderboard = self.get_leaderboard()
        best_team = leaderboard[0]
        specialists = self.get_specialist_teams()
        most_improved = self.get_most_improved_team()

        # Calculate overall statistics
        all_scores = [m.total_score for m in self.team_metrics.values()]
        all_bugs = [m.total_bugs for m in self.team_metrics.values()]

        return {
            "overall_winner": {
                "team_id": best_team[0],
                "team_name": best_team[1].team_name,
                "total_score": best_team[1].total_score,
                "total_bugs": best_team[1].total_bugs,
                "critical_bugs": best_team[1].critical_bugs
            },
            "specialists": {
                specialty: {
                    "team_id": team_id,
                    "team_name": metrics.team_name,
                    "value": getattr(
                        metrics,
                        {
                            "critical_hunter": "critical_bugs",
                            "most_accurate": "false_positive_rate",
                            "best_coverage": "unique_bugs",
                            "best_reporter": "average_report_quality"
                        }[specialty]
                    )
                }
                for specialty, (team_id, metrics) in specialists.items()
            },
            "most_improved": {
                "team_id": most_improved[0],
                "team_name": most_improved[1].team_name,
                "trend": most_improved[1].score_trend,
                "improvement": (
                    most_improved[1].scores_per_round[-1] -
                    most_improved[1].scores_per_round[0]
                ) if len(most_improved[1].scores_per_round) >= 2 else 0
            } if most_improved else None,
            "statistics": {
                "average_score": sum(all_scores) / len(all_scores),
                "total_bugs_found": sum(all_bugs),
                "average_bugs_per_team": sum(all_bugs) / len(all_bugs),
                "total_rounds": len(self.round_data)
            },
            "leaderboard": [
                {
                    "rank": i + 1,
                    "team_id": team_id,
                    "team_name": metrics.team_name,
                    "score": metrics.total_score,
                    "bugs": metrics.total_bugs,
                    "trend": metrics.score_trend
                }
                for i, (team_id, metrics) in enumerate(leaderboard)
            ]
        }

    def export_metrics(self, filepath: str):
        """Export metrics to JSON file"""
        data = {
            "teams": {
                team_id: {
                    "name": metrics.team_name,
                    "total_score": metrics.total_score,
                    "scores_per_round": metrics.scores_per_round,
                    "total_bugs": metrics.total_bugs,
                    "bugs_per_round": metrics.bugs_per_round,
                    "severity_breakdown": {
                        "critical": metrics.critical_bugs,
                        "high": metrics.high_bugs,
                        "medium": metrics.medium_bugs,
                        "low": metrics.low_bugs
                    },
                    "false_positive_rate": metrics.false_positive_rate,
                    "unique_bugs": metrics.unique_bugs,
                    "vuln_types": metrics.vuln_types,
                    "score_trend": metrics.score_trend,
                    "rank_per_round": metrics.rank_per_round
                }
                for team_id, metrics in self.team_metrics.items()
            },
            "comparative_analysis": self.generate_comparative_analysis()
        }

        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
        except (IOError, PermissionError) as e:
            print(f"Error exporting metrics to {filepath}: {e}")

    def print_summary(self):
        """Print a summary of metrics"""
        print("\n" + "="*60)
        print("  CHAMPIONSHIP METRICS SUMMARY")
        print("="*60 + "\n")

        leaderboard = self.get_leaderboard()

        for i, (team_id, metrics) in enumerate(leaderboard, 1):
            medal = ["🥇", "🥈", "🥉"][i-1] if i <= 3 else "  "
            print(f"{medal} {metrics.team_name}")
            print(f"   Total Score: {metrics.total_score:.1f}")
            print(f"   Bugs Found: {metrics.total_bugs} " +
                  f"(Critical: {metrics.critical_bugs}, " +
                  f"High: {metrics.high_bugs})")
            print(f"   Unique Discoveries: {metrics.unique_bugs}")
            print(f"   False Positive Rate: {metrics.false_positive_rate:.1%}")
            print(f"   Trend: {metrics.score_trend.upper()}")
            print(f"   Times Ranked #1: {metrics.times_ranked_first}")
            print()

        # Specialists
        specialists = self.get_specialist_teams()
        print("="*60)
        print("  SPECIALIST AWARDS")
        print("="*60 + "\n")

        awards = {
            "critical_hunter": "🎯 Critical Bug Hunter",
            "most_accurate": "🎪 Most Accurate (Fewest False Positives)",
            "best_coverage": "🔍 Best Coverage (Most Unique Discoveries)",
            "best_reporter": "📝 Best Reporter (Highest Quality Reports)"
        }

        for specialty, title in awards.items():
            if specialty in specialists:
                team_id, metrics = specialists[specialty]
                print(f"{title}")
                print(f"   Winner: {metrics.team_name}")
                print()


# Example usage
if __name__ == "__main__":
    from scoring_engine import BugReport
    import time

    # Create tracker
    tracker = MetricsTracker()

    # Simulate some rounds
    # (In real usage, this would be called by the coordinator)

    print("Metrics Tracker Test")
    print("="*60)

    # Example: Would be integrated with actual round results
    tracker.print_summary()
