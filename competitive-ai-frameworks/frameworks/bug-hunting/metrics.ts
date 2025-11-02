/**
 * Metrics Tracker for Bug Hunting Championship
 *
 * Tracks and analyzes performance metrics across rounds for strategy optimization
 */

import type { BugReport } from './scoring_engine';
import * as fs from 'fs';

export interface TeamRoundResult {
  team_name: string;
  bugs_found: BugReport[];
  score: number;
  false_positives: number;
  unique_discoveries: number;
  avg_time_to_discovery: number;
  strategy_weights: Record<string, number>;
}

export interface TeamMetrics {
  team_id: string;
  team_name: string;

  // Score metrics
  total_score: number;
  scores_per_round: number[];
  average_score: number;
  score_trend: 'improving' | 'declining' | 'stable';

  // Bug discovery metrics
  total_bugs: number;
  bugs_per_round: number[];
  unique_bugs: number;
  duplicate_bugs: number;

  // Severity metrics
  critical_bugs: number;
  high_bugs: number;
  medium_bugs: number;
  low_bugs: number;

  // Quality metrics
  false_positives: number;
  false_positive_rate: number;
  average_report_quality: number;
  quality_score_total: number;
  quality_score_samples: number;

  // Efficiency metrics
  average_time_to_discovery: number;
  time_to_discovery_per_round: number[];
  bugs_per_minute: number;

  // Vulnerability type distribution
  vuln_types: Record<string, number>;

  // Comparative metrics
  rank_per_round: number[];
  times_ranked_first: number;
  times_ranked_last: number;
}

export interface RoundData {
  round: number;
  results: Record<string, TeamRoundResult>;
  rankings: Record<string, number>;
}

export interface ComparativeAnalysis {
  overall_winner: {
    team_id: string;
    team_name: string;
    total_score: number;
    total_bugs: number;
    critical_bugs: number;
  };
  specialists: Record<string, {
    team_id: string;
    team_name: string;
    value: number;
  }>;
  most_improved: {
    team_id: string;
    team_name: string;
    trend: string;
    improvement: number;
  } | null;
  statistics: {
    average_score: number;
    total_bugs_found: number;
    average_bugs_per_team: number;
    total_rounds: number;
  };
  leaderboard: Array<{
    rank: number;
    team_id: string;
    team_name: string;
    score: number;
    bugs: number;
    trend: string;
  }>;
}

export class MetricsTracker {
  private team_metrics: Map<string, TeamMetrics> = new Map();
  private round_data: RoundData[] = [];
  private start_time: number | null = null;

  /**
   * Initialize tracking for a team
   */
  public initialize_team(team_id: string, team_name: string): void {
    this.team_metrics.set(team_id, {
      team_id,
      team_name,
      total_score: 0.0,
      scores_per_round: [],
      average_score: 0.0,
      score_trend: 'stable',
      total_bugs: 0,
      bugs_per_round: [],
      unique_bugs: 0,
      duplicate_bugs: 0,
      critical_bugs: 0,
      high_bugs: 0,
      medium_bugs: 0,
      low_bugs: 0,
      false_positives: 0,
      false_positive_rate: 0.0,
      average_report_quality: 0.0,
      quality_score_total: 0.0,
      quality_score_samples: 0,
      average_time_to_discovery: 0.0,
      time_to_discovery_per_round: [],
      bugs_per_minute: 0.0,
      vuln_types: {},
      rank_per_round: [],
      times_ranked_first: 0,
      times_ranked_last: 0,
    });
  }

  /**
   * Record results from a round
   */
  public record_round(
    round_number: number,
    team_results: Record<string, TeamRoundResult>
  ): void {
    // Initialize teams if needed
    for (const [team_id, result] of Object.entries(team_results)) {
      if (!this.team_metrics.has(team_id)) {
        this.initialize_team(team_id, result.team_name);
      }
    }

    // Calculate rankings for this round
    const rankings = this._calculate_rankings(team_results);

    // Update metrics for each team
    for (const [team_id, result] of Object.entries(team_results)) {
      const metrics = this.team_metrics.get(team_id)!;

      // Score metrics
      metrics.total_score += result.score;
      metrics.scores_per_round.push(result.score);
      metrics.average_score = metrics.total_score / metrics.scores_per_round.length;

      // Bug discovery metrics (filter out false positives)
      const valid_bugs = result.bugs_found.filter(bug => !bug.is_false_positive);
      const valid_bug_count = valid_bugs.length;

      metrics.total_bugs += valid_bug_count;
      metrics.bugs_per_round.push(valid_bug_count);
      metrics.unique_bugs += result.unique_discoveries;
      metrics.duplicate_bugs += Math.max(0, valid_bug_count - result.unique_discoveries);

      // Severity metrics
      for (const bug of valid_bugs) {
        if (bug.severity === 'critical') {
          metrics.critical_bugs++;
        } else if (bug.severity === 'high') {
          metrics.high_bugs++;
        } else if (bug.severity === 'medium') {
          metrics.medium_bugs++;
        } else if (bug.severity === 'low') {
          metrics.low_bugs++;
        }

        // Track vulnerability types
        if (!metrics.vuln_types[bug.vuln_type]) {
          metrics.vuln_types[bug.vuln_type] = 0;
        }
        metrics.vuln_types[bug.vuln_type]++;
      }

      // Quality metrics
      metrics.false_positives += result.false_positives;
      const total_reports = metrics.total_bugs + metrics.false_positives;
      if (total_reports > 0) {
        metrics.false_positive_rate = metrics.false_positives / total_reports;
      }

      // Calculate cumulative average report quality
      const quality_scores = valid_bugs.map(bug => bug.quality_score || 0);
      if (quality_scores.length > 0) {
        metrics.quality_score_total += quality_scores.reduce((a, b) => a + b, 0);
        metrics.quality_score_samples += quality_scores.length;
        metrics.average_report_quality = metrics.quality_score_total / metrics.quality_score_samples;
      }

      // Efficiency metrics - cumulative average
      if (result.avg_time_to_discovery != null && result.avg_time_to_discovery > 0) {
        metrics.time_to_discovery_per_round.push(result.avg_time_to_discovery);
        metrics.average_time_to_discovery =
          metrics.time_to_discovery_per_round.reduce((a, b) => a + b, 0) /
          metrics.time_to_discovery_per_round.length;
      }

      // Ranking metrics
      const rank = rankings[team_id];
      metrics.rank_per_round.push(rank);
      if (rank === 1) {
        metrics.times_ranked_first++;
      } else if (rank === Object.keys(team_results).length) {
        metrics.times_ranked_last++;
      }
    }

    // Calculate trends
    this._calculate_trends();

    // Store round data
    this.round_data.push({
      round: round_number,
      results: team_results,
      rankings,
    });
  }

  /**
   * Calculate team rankings for a round
   */
  private _calculate_rankings(
    team_results: Record<string, TeamRoundResult>
  ): Record<string, number> {
    // Sort teams by score
    const sorted_teams = Object.entries(team_results).sort(
      (a, b) => b[1].score - a[1].score
    );

    // Assign ranks
    const rankings: Record<string, number> = {};
    sorted_teams.forEach(([team_id], index) => {
      rankings[team_id] = index + 1;
    });

    return rankings;
  }

  /**
   * Calculate performance trends for all teams
   */
  private _calculate_trends(): void {
    for (const metrics of this.team_metrics.values()) {
      if (metrics.scores_per_round.length < 2) {
        metrics.score_trend = 'stable';
        continue;
      }

      // Calculate trend using simple linear regression
      const scores = metrics.scores_per_round;
      const n = scores.length;
      const x = Array.from({ length: n }, (_, i) => i);
      const y = scores;

      // Calculate slope
      const x_mean = x.reduce((a, b) => a + b, 0) / n;
      const y_mean = y.reduce((a, b) => a + b, 0) / n;
      const numerator = x.reduce((sum, xi, i) => sum + (xi - x_mean) * (y[i] - y_mean), 0);
      const denominator = x.reduce((sum, xi) => sum + Math.pow(xi - x_mean, 2), 0);

      const slope = denominator === 0 ? 0 : numerator / denominator;

      // Classify trend
      if (slope > 5) {
        metrics.score_trend = 'improving';
      } else if (slope < -5) {
        metrics.score_trend = 'declining';
      } else {
        metrics.score_trend = 'stable';
      }
    }
  }

  /**
   * Get metrics for a specific team
   */
  public get_team_metrics(team_id: string): TeamMetrics | null {
    return this.team_metrics.get(team_id) || null;
  }

  /**
   * Get metrics for all teams
   */
  public get_all_metrics(): Map<string, TeamMetrics> {
    return this.team_metrics;
  }

  /**
   * Get current leaderboard
   */
  public get_leaderboard(): Array<[string, TeamMetrics]> {
    return Array.from(this.team_metrics.entries()).sort(
      (a, b) => b[1].total_score - a[1].total_score
    );
  }

  /**
   * Get the best performing team overall
   */
  public get_best_performing_team(): [string, TeamMetrics] | null {
    const leaderboard = this.get_leaderboard();
    return leaderboard.length > 0 ? leaderboard[0] : null;
  }

  /**
   * Get the team that improved the most
   */
  public get_most_improved_team(): [string, TeamMetrics] | null {
    const improving_teams = Array.from(this.team_metrics.entries()).filter(
      ([, metrics]) => metrics.score_trend === 'improving'
    );

    if (improving_teams.length === 0) {
      return null;
    }

    // Calculate improvement rate
    const improvement_rate = (metrics: TeamMetrics): number => {
      if (metrics.scores_per_round.length < 2) {
        return 0.0;
      }
      const last = metrics.scores_per_round[metrics.scores_per_round.length - 1];
      const first = metrics.scores_per_round[0];
      return (last - first) / metrics.scores_per_round.length;
    };

    return improving_teams.reduce((best, current) =>
      improvement_rate(current[1]) > improvement_rate(best[1]) ? current : best
    );
  }

  /**
   * Identify specialist teams
   */
  public get_specialist_teams(): Record<string, [string, TeamMetrics]> {
    const specialists: Record<string, [string, TeamMetrics]> = {};

    if (this.team_metrics.size === 0) {
      return specialists;
    }

    const entries = Array.from(this.team_metrics.entries());

    // Most critical bugs
    specialists['critical_hunter'] = entries.reduce((best, current) =>
      current[1].critical_bugs > best[1].critical_bugs ? current : best
    );

    // Best accuracy (lowest false positive rate)
    const teams_with_bugs = entries.filter(([, m]) => m.total_bugs > 0);
    if (teams_with_bugs.length > 0) {
      specialists['most_accurate'] = teams_with_bugs.reduce((best, current) =>
        current[1].false_positive_rate < best[1].false_positive_rate ? current : best
      );
    }

    // Most unique discoveries
    specialists['best_coverage'] = entries.reduce((best, current) =>
      current[1].unique_bugs > best[1].unique_bugs ? current : best
    );

    // Highest quality reports
    specialists['best_reporter'] = entries.reduce((best, current) =>
      current[1].average_report_quality > best[1].average_report_quality ? current : best
    );

    return specialists;
  }

  /**
   * Generate comparative analysis across all teams
   */
  public generate_comparative_analysis(): ComparativeAnalysis {
    if (this.team_metrics.size === 0) {
      return {} as ComparativeAnalysis;
    }

    const leaderboard = this.get_leaderboard();
    const [best_team_id, best_team] = leaderboard[0];
    const specialists = this.get_specialist_teams();
    const most_improved = this.get_most_improved_team();

    // Calculate overall statistics
    const all_scores = Array.from(this.team_metrics.values()).map(m => m.total_score);
    const all_bugs = Array.from(this.team_metrics.values()).map(m => m.total_bugs);

    const specialist_map: Record<string, keyof TeamMetrics> = {
      critical_hunter: 'critical_bugs',
      most_accurate: 'false_positive_rate',
      best_coverage: 'unique_bugs',
      best_reporter: 'average_report_quality',
    };

    return {
      overall_winner: {
        team_id: best_team_id,
        team_name: best_team.team_name,
        total_score: best_team.total_score,
        total_bugs: best_team.total_bugs,
        critical_bugs: best_team.critical_bugs,
      },
      specialists: Object.fromEntries(
        Object.entries(specialists).map(([specialty, [team_id, metrics]]) => [
          specialty,
          {
            team_id,
            team_name: metrics.team_name,
            value: metrics[specialist_map[specialty]] as number,
          },
        ])
      ),
      most_improved: most_improved
        ? {
            team_id: most_improved[0],
            team_name: most_improved[1].team_name,
            trend: most_improved[1].score_trend,
            improvement:
              most_improved[1].scores_per_round.length >= 2
                ? most_improved[1].scores_per_round[most_improved[1].scores_per_round.length - 1] -
                  most_improved[1].scores_per_round[0]
                : 0,
          }
        : null,
      statistics: {
        average_score: all_scores.reduce((a, b) => a + b, 0) / all_scores.length,
        total_bugs_found: all_bugs.reduce((a, b) => a + b, 0),
        average_bugs_per_team: all_bugs.reduce((a, b) => a + b, 0) / all_bugs.length,
        total_rounds: this.round_data.length,
      },
      leaderboard: leaderboard.map(([team_id, metrics], i) => ({
        rank: i + 1,
        team_id,
        team_name: metrics.team_name,
        score: metrics.total_score,
        bugs: metrics.total_bugs,
        trend: metrics.score_trend,
      })),
    };
  }

  /**
   * Export metrics to JSON file
   */
  public export_metrics(filepath: string): void {
    const data = {
      teams: Object.fromEntries(
        Array.from(this.team_metrics.entries()).map(([team_id, metrics]) => [
          team_id,
          {
            name: metrics.team_name,
            total_score: metrics.total_score,
            scores_per_round: metrics.scores_per_round,
            total_bugs: metrics.total_bugs,
            bugs_per_round: metrics.bugs_per_round,
            severity_breakdown: {
              critical: metrics.critical_bugs,
              high: metrics.high_bugs,
              medium: metrics.medium_bugs,
              low: metrics.low_bugs,
            },
            false_positive_rate: metrics.false_positive_rate,
            unique_bugs: metrics.unique_bugs,
            vuln_types: metrics.vuln_types,
            score_trend: metrics.score_trend,
            rank_per_round: metrics.rank_per_round,
          },
        ])
      ),
      comparative_analysis: this.generate_comparative_analysis(),
    };

    try {
      fs.writeFileSync(filepath, JSON.stringify(data, null, 2));
    } catch (error) {
      console.error(`Error exporting metrics to ${filepath}:`, error);
    }
  }

  /**
   * Print a summary of metrics
   */
  public print_summary(): void {
    console.log('\n' + '='.repeat(60));
    console.log('  CHAMPIONSHIP METRICS SUMMARY');
    console.log('='.repeat(60) + '\n');

    const leaderboard = this.get_leaderboard();

    leaderboard.forEach(([team_id, metrics], i) => {
      const medals = ['🥇', '🥈', '🥉'];
      const medal = i < 3 ? medals[i] : '  ';
      console.log(`${medal} ${metrics.team_name}`);
      console.log(`   Total Score: ${metrics.total_score.toFixed(1)}`);
      console.log(
        `   Bugs Found: ${metrics.total_bugs} ` +
        `(Critical: ${metrics.critical_bugs}, High: ${metrics.high_bugs})`
      );
      console.log(`   Unique Discoveries: ${metrics.unique_bugs}`);
      console.log(`   False Positive Rate: ${(metrics.false_positive_rate * 100).toFixed(1)}%`);
      console.log(`   Trend: ${metrics.score_trend.toUpperCase()}`);
      console.log(`   Times Ranked #1: ${metrics.times_ranked_first}`);
      console.log();
    });

    // Specialists
    const specialists = this.get_specialist_teams();
    console.log('='.repeat(60));
    console.log('  SPECIALIST AWARDS');
    console.log('='.repeat(60) + '\n');

    const awards: Record<string, string> = {
      critical_hunter: '🎯 Critical Bug Hunter',
      most_accurate: '🎪 Most Accurate (Fewest False Positives)',
      best_coverage: '🔍 Best Coverage (Most Unique Discoveries)',
      best_reporter: '📝 Best Reporter (Highest Quality Reports)',
    };

    for (const [specialty, title] of Object.entries(awards)) {
      if (specialists[specialty]) {
        const [team_id, metrics] = specialists[specialty];
        console.log(title);
        console.log(`   Winner: ${metrics.team_name}`);
        console.log();
      }
    }
  }
}
