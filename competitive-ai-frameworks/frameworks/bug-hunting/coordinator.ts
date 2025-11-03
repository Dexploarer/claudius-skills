#!/usr/bin/env ts-node
/**
 * Bug Hunting Championship Coordinator
 *
 * Orchestrates three competing AI teams in a bug hunting competition with
 * reinforcement learning-based strategy adaptation.
 */

import * as fs from 'fs';
import * as path from 'path';
import { exec } from 'child_process';
import { promisify } from 'util';
import { ScoringEngine, BugReport, Severity } from './scoring_engine';
import { MetricsTracker, TeamRoundResult } from './metrics';
import { ReinforcementLearner } from './reinforcement';

const execAsync = promisify(exec);

export interface TeamConfig {
  name: string;
  strategy: string;
  subagent_file: string;
  focus_areas: string[];
  tools: string[];
  initial_weights: Record<string, number>;
}

export interface RoundResults {
  round_number: number;
  timestamp: string;
  teams: Record<string, TeamRoundResult>;
  duration_seconds: number;
  target_path: string;
}

export class BugHuntingCoordinator {
  private target_path: string;
  private rounds: number;
  private output_dir: string;
  private visualize: boolean;

  private scoring_engine: ScoringEngine;
  private metrics_tracker: MetricsTracker;
  private rl_learner: ReinforcementLearner;

  private session_id: string;
  private teams: Record<string, TeamConfig>;
  private all_rounds: RoundResults[] = [];

  constructor(
    target_path: string,
    rounds: number = 5,
    output_dir: string = './results',
    visualize: boolean = false
  ) {
    this.target_path = target_path;
    this.rounds = rounds;
    this.output_dir = output_dir;
    this.visualize = visualize;

    // Initialize components
    this.scoring_engine = new ScoringEngine();
    this.metrics_tracker = new MetricsTracker();
    this.rl_learner = new ReinforcementLearner();

    // Setup output directory
    if (!fs.existsSync(this.output_dir)) {
      fs.mkdirSync(this.output_dir, { recursive: true });
    }
    this.session_id = new Date().toISOString().replace(/[:.]/g, '-').slice(0, -5);

    // Initialize teams
    this.teams = this._initialize_teams();
  }

  /**
   * Initialize the three competing teams with their strategies
   */
  private _initialize_teams(): Record<string, TeamConfig> {
    return {
      team1: {
        name: 'Automated Scanners',
        strategy: 'automated',
        subagent_file: '.claude/subagents/team1-automated-scanner.md',
        focus_areas: [
          'pattern_matching',
          'static_analysis',
          'dependency_scanning',
          'known_vulnerabilities',
        ],
        tools: ['grep', 'ripgrep', 'ast_parser', 'dependency_checker', 'cve_database'],
        initial_weights: {
          sql_injection: 1.0,
          xss: 1.0,
          csrf: 0.8,
          auth_bypass: 0.7,
          path_traversal: 0.9,
          command_injection: 0.8,
          xxe: 0.6,
          deserialization: 0.5,
        },
      },
      team2: {
        name: 'Manual Reviewers',
        strategy: 'manual',
        subagent_file: '.claude/subagents/team2-manual-reviewer.md',
        focus_areas: [
          'business_logic',
          'authentication',
          'authorization',
          'logic_flaws',
          'access_control',
        ],
        tools: ['code_review', 'logic_analyzer', 'flow_tracker', 'context_analyzer'],
        initial_weights: {
          business_logic: 1.0,
          auth_bypass: 1.0,
          privilege_escalation: 0.9,
          idor: 0.8,
          race_conditions: 0.6,
          session_management: 0.8,
          cryptographic_issues: 0.7,
          input_validation: 0.7,
        },
      },
      team3: {
        name: 'Fuzzers & Behavioral Analysts',
        strategy: 'fuzzing',
        subagent_file: '.claude/subagents/team3-fuzzer.md',
        focus_areas: [
          'input_fuzzing',
          'edge_cases',
          'runtime_behavior',
          'race_conditions',
          'memory_issues',
        ],
        tools: ['fuzzer', 'behavior_monitor', 'race_detector', 'memory_profiler'],
        initial_weights: {
          buffer_overflow: 1.0,
          race_conditions: 1.0,
          dos_vulnerabilities: 0.7,
          memory_leaks: 0.6,
          integer_overflow: 0.8,
          null_pointer: 0.5,
          edge_case_crashes: 0.9,
          resource_exhaustion: 0.6,
        },
      },
    };
  }

  /**
   * Run the complete championship across all rounds
   */
  public async run_championship(): Promise<Record<string, any>> {
    console.log('\n' + '='.repeat(60));
    console.log('  BUG HUNTING CHAMPIONSHIP');
    console.log('='.repeat(60));
    console.log(`Target: ${this.target_path}`);
    console.log(`Rounds: ${this.rounds}`);
    console.log(`Teams: ${Object.keys(this.teams).length}`);
    console.log('='.repeat(60) + '\n');

    for (let round_num = 1; round_num <= this.rounds; round_num++) {
      console.log('\n' + '─'.repeat(60));
      console.log(`  ROUND ${round_num}/${this.rounds}`);
      console.log('─'.repeat(60) + '\n');

      const round_results = await this._run_round(round_num);
      this.all_rounds.push(round_results);

      // Display round summary
      this._display_round_summary(round_results);

      // Apply reinforcement learning
      if (round_num < this.rounds) {
        this._apply_reinforcement_learning(round_results);
        console.log('\n✓ Team strategies adapted based on performance\n');
      }
    }

    // Generate final results
    const final_results = this._generate_final_results();

    // Display championship results
    this._display_championship_results(final_results);

    // Save results
    this._save_results(final_results);

    // Visualize if requested
    if (this.visualize) {
      this._visualize_results(final_results);
    }

    return final_results;
  }

  /**
   * Execute a single round of competition
   */
  private async _run_round(round_num: number): Promise<RoundResults> {
    const start_time = Date.now();
    const team_results: Record<string, TeamRoundResult> = {};

    // Track discovered bugs across all teams for uniqueness detection
    const all_bugs: Map<string, BugReport> = new Map();

    for (const [team_id, team_config] of Object.entries(this.teams)) {
      console.log(`  ▶ ${team_config.name} hunting...`);

      // Execute team's bug hunting
      const bugs = await this._execute_team_hunt(team_config, round_num);

      // Score the bugs
      const scored_bugs: BugReport[] = [];
      for (const bug of bugs) {
        this.scoring_engine.score_bug(bug);

        // Check uniqueness
        const bug_signature = this._get_bug_signature(bug);
        if (!all_bugs.has(bug_signature)) {
          all_bugs.set(bug_signature, bug);
          bug.is_unique = true;
          bug.discovered_by = team_id;
        } else {
          bug.is_unique = false;
        }

        scored_bugs.push(bug);
      }

      // Calculate team metrics
      const team_result = this._calculate_team_metrics(
        team_config,
        scored_bugs,
        round_num,
        start_time
      );
      team_results[team_id] = team_result;
    }

    const duration = (Date.now() - start_time) / 1000;

    return {
      round_number: round_num,
      timestamp: new Date().toISOString(),
      teams: team_results,
      duration_seconds: duration,
      target_path: this.target_path,
    };
  }

  /**
   * Execute bug hunting for a specific team
   */
  private async _execute_team_hunt(
    team: TeamConfig,
    round_num: number
  ): Promise<BugReport[]> {
    console.log(`\n🤖 Launching ${team.name} (Round ${round_num})...`);

    try {
      // Fallback to static analysis
      const bugs = await this._fallback_analysis(team);
      return bugs;
    } catch (error) {
      console.error(`⚠️  Error during ${team.name} hunt:`, error);
      return [];
    }
  }

  /**
   * Fallback analysis using static analysis tools
   */
  private async _fallback_analysis(team: TeamConfig): Promise<BugReport[]> {
    const bugs: BugReport[] = [];
    const discovery_time = Date.now();

    try {
      if (team.strategy === 'automated') {
        bugs.push(...(await this._scan_sql_injection(team.name, discovery_time)));
        bugs.push(...(await this._scan_xss(team.name, discovery_time)));
        bugs.push(...(await this._scan_command_injection(team.name, discovery_time)));
      } else if (team.strategy === 'manual') {
        bugs.push(...(await this._scan_auth_issues(team.name, discovery_time)));
        bugs.push(...(await this._scan_idor(team.name, discovery_time)));
      } else {
        bugs.push(...(await this._scan_race_conditions(team.name, discovery_time)));
      }
    } catch (error) {
      console.error(`   ⚠️  Error during fallback analysis:`, error);
    }

    console.log(`   ✓ Found ${bugs.length} potential vulnerabilities`);
    return bugs;
  }

  /**
   * Scan for SQL injection vulnerabilities
   */
  private async _scan_sql_injection(team_name: string, discovery_time: number): Promise<BugReport[]> {
    const bugs: BugReport[] = [];

    try {
      const { stdout } = await execAsync(
        `grep -rn -E '(execute|query|cursor\\.execute)\\s*\\(\\s*["\'].*\\+.*["\']|f".*SELECT.*\\{.*\\}"' ${this.target_path}`,
        { timeout: 10000 }
      ).catch(() => ({ stdout: '' }));

      const lines = stdout.trim().split('\n').slice(0, 3);
      for (const line of lines) {
        if (line.includes(':')) {
          const [location] = line.split(':', 2);
          bugs.push({
            vuln_type: 'SQL Injection',
            location: location.replace(`${this.target_path}/`, ''),
            severity: Severity.HIGH,
            cvss_score: 8.5,
            description: 'Potential SQL injection via string concatenation in query',
            proof_of_concept: 'User input appears to be concatenated directly into SQL query',
            remediation: 'Use parameterized queries or prepared statements',
            discovered_at: discovery_time,
            team: team_name,
          });
        }
      }
    } catch (error) {
      // Ignore grep errors
    }

    return bugs;
  }

  /**
   * Scan for XSS vulnerabilities
   */
  private async _scan_xss(team_name: string, discovery_time: number): Promise<BugReport[]> {
    const bugs: BugReport[] = [];

    try {
      const { stdout } = await execAsync(
        `grep -rn -E '\\.innerHTML\\s*=|document\\.write\\(|render_template_string\\(.*\\+' ${this.target_path}`,
        { timeout: 10000 }
      ).catch(() => ({ stdout: '' }));

      const lines = stdout.trim().split('\n').slice(0, 2);
      for (const line of lines) {
        if (line.includes(':')) {
          const [location] = line.split(':', 2);
          bugs.push({
            vuln_type: 'Cross-Site Scripting (XSS)',
            location: location.replace(`${this.target_path}/`, ''),
            severity: Severity.MEDIUM,
            cvss_score: 6.5,
            description: 'Potential XSS vulnerability via unsafe output rendering',
            proof_of_concept: 'User-controlled data may be rendered without escaping',
            remediation: 'Use auto-escaping templates or sanitize user input',
            discovered_at: discovery_time,
            team: team_name,
          });
        }
      }
    } catch (error) {
      // Ignore grep errors
    }

    return bugs;
  }

  /**
   * Scan for command injection vulnerabilities
   */
  private async _scan_command_injection(team_name: string, discovery_time: number): Promise<BugReport[]> {
    const bugs: BugReport[] = [];

    try {
      const { stdout } = await execAsync(
        `grep -rn -E '(subprocess\\.run|subprocess\\.call|os\\.system|exec|eval)\\(.*shell\\s*=\\s*True' ${this.target_path}`,
        { timeout: 10000 }
      ).catch(() => ({ stdout: '' }));

      const lines = stdout.trim().split('\n').slice(0, 2);
      for (const line of lines) {
        if (line.includes(':')) {
          const [location] = line.split(':', 2);
          bugs.push({
            vuln_type: 'Command Injection',
            location: location.replace(`${this.target_path}/`, ''),
            severity: Severity.CRITICAL,
            cvss_score: 9.0,
            description: 'Shell command execution with shell=True allows command injection',
            proof_of_concept: 'Unsanitized input in shell command can execute arbitrary commands',
            remediation: 'Avoid shell=True, use argument lists, validate input',
            discovered_at: discovery_time,
            team: team_name,
          });
        }
      }
    } catch (error) {
      // Ignore grep errors
    }

    return bugs;
  }

  /**
   * Scan for authentication issues
   */
  private async _scan_auth_issues(team_name: string, discovery_time: number): Promise<BugReport[]> {
    const bugs: BugReport[] = [];

    try {
      const { stdout } = await execAsync(
        `grep -rn -E "algorithms\\s*=\\s*\\[.*['\"]none['\"]" ${this.target_path}`,
        { timeout: 10000 }
      ).catch(() => ({ stdout: '' }));

      const lines = stdout.trim().split('\n').slice(0, 1);
      for (const line of lines) {
        if (line.includes(':')) {
          const [location] = line.split(':', 2);
          bugs.push({
            vuln_type: 'Authentication Bypass',
            location: location.replace(`${this.target_path}/`, ''),
            severity: Severity.CRITICAL,
            cvss_score: 9.8,
            description: 'JWT validation accepts \'none\' algorithm allowing signature bypass',
            proof_of_concept: 'Attacker can forge tokens with null signature',
            remediation: 'Remove \'none\' from allowed algorithms list',
            discovered_at: discovery_time,
            team: team_name,
          });
        }
      }
    } catch (error) {
      // Ignore grep errors
    }

    return bugs;
  }

  /**
   * Scan for IDOR vulnerabilities
   */
  private async _scan_idor(team_name: string, discovery_time: number): Promise<BugReport[]> {
    const bugs: BugReport[] = [];

    try {
      const { stdout } = await execAsync(
        `grep -rn -E '@app\\.route.*<(int:)?user_id>.*def.*\\(.*user_id' ${this.target_path}`,
        { timeout: 10000 }
      ).catch(() => ({ stdout: '' }));

      const lines = stdout.trim().split('\n').slice(0, 2);
      for (const line of lines) {
        if (line.includes(':')) {
          const [location] = line.split(':', 2);
          bugs.push({
            vuln_type: 'IDOR (Insecure Direct Object Reference)',
            location: location.replace(`${this.target_path}/`, ''),
            severity: Severity.HIGH,
            cvss_score: 7.5,
            description: 'Direct object reference without authorization check',
            proof_of_concept: 'User can access other users\' data by changing ID parameter',
            remediation: 'Verify user ownership before returning data',
            discovered_at: discovery_time,
            team: team_name,
          });
        }
      }
    } catch (error) {
      // Ignore grep errors
    }

    return bugs;
  }

  /**
   * Scan for race conditions
   */
  private async _scan_race_conditions(team_name: string, discovery_time: number): Promise<BugReport[]> {
    const bugs: BugReport[] = [];

    try {
      const { stdout } = await execAsync(
        `grep -rn -A5 -E 'if.*balance.*>=.*amount' ${this.target_path}`,
        { timeout: 10000 }
      ).catch(() => ({ stdout: '' }));

      if (stdout.includes('balance -')) {
        const lines = stdout.trim().split('\n');
        if (lines.length > 0) {
          const location = lines[0].split(':')[0];
          bugs.push({
            vuln_type: 'Race Condition (TOCTOU)',
            location: location.replace(`${this.target_path}/`, ''),
            severity: Severity.CRITICAL,
            cvss_score: 9.1,
            description: 'Time-of-check to time-of-use race condition in balance check',
            proof_of_concept: 'Concurrent requests can bypass balance validation',
            remediation: 'Use database transactions with proper locking',
            discovered_at: discovery_time,
            team: team_name,
          });
        }
      }
    } catch (error) {
      // Ignore grep errors
    }

    return bugs;
  }

  /**
   * Generate a unique signature for a bug to detect duplicates
   */
  private _get_bug_signature(bug: BugReport): string {
    return `${bug.vuln_type}:${bug.location}:${bug.severity}`;
  }

  /**
   * Calculate comprehensive metrics for a team's performance
   */
  private _calculate_team_metrics(
    team: TeamConfig,
    bugs: BugReport[],
    round_num: number,
    round_start_time: number
  ): TeamRoundResult {
    let total_score = 0;
    let false_positives = 0;
    let unique_count = 0;
    const discovery_times: number[] = [];

    for (const bug of bugs) {
      if (bug.is_false_positive) {
        false_positives++;
        total_score -= 20; // Penalty
      } else {
        const bug_score = bug.total_score || 0;
        total_score += bug_score;

        if (bug.is_unique) {
          unique_count++;
        }

        // Track discovery time (delta from round start)
        const time_delta = Math.max((bug.discovered_at - round_start_time) / 1000, 0.0);
        discovery_times.push(time_delta);
      }
    }

    const avg_time =
      discovery_times.length > 0
        ? discovery_times.reduce((a, b) => a + b, 0) / discovery_times.length
        : 0;

    return {
      team_name: team.name,
      bugs_found: bugs,
      score: total_score,
      false_positives,
      unique_discoveries: unique_count,
      avg_time_to_discovery: avg_time,
      strategy_weights: { ...team.initial_weights },
    };
  }

  /**
   * Display summary of round results
   */
  private _display_round_summary(results: RoundResults): void {
    console.log(`\n  Round ${results.round_number} Summary:`);
    console.log('  ' + '─'.repeat(56) + '\n');

    // Sort teams by score
    const sorted_teams = Object.entries(results.teams).sort(
      (a, b) => b[1].score - a[1].score
    );

    sorted_teams.forEach(([team_id, result], index) => {
      const medals = ['🥇', '🥈', '🥉'];
      const medal = index < 3 ? medals[index] : '  ';
      console.log(`  ${medal} ${result.team_name.padEnd(30)} Score: ${result.score.toFixed(0).padStart(6)}`);
      console.log(
        `     Bugs: ${result.bugs_found.length.toString().padStart(2)}  |  ` +
        `Unique: ${result.unique_discoveries.toString().padStart(2)}  |  ` +
        `False+: ${result.false_positives.toString().padStart(2)}`
      );
    });

    console.log(`\n  Duration: ${results.duration_seconds.toFixed(1)}s\n`);
  }

  /**
   * Apply reinforcement learning to adapt team strategies
   */
  private _apply_reinforcement_learning(results: RoundResults): void {
    for (const [team_id, team_result] of Object.entries(results.teams)) {
      // Update weights based on performance
      const updated_weights = this.rl_learner.update_weights(
        team_result.strategy_weights,
        team_result.bugs_found,
        team_result.score,
        team_result.false_positives
      );

      // Apply updated weights to team
      this.teams[team_id].initial_weights = updated_weights;
    }
  }

  /**
   * Generate comprehensive final results
   */
  private _generate_final_results(): Record<string, any> {
    // Aggregate scores across all rounds
    const team_totals: Record<string, number> = {};
    const team_stats: Record<string, any> = {};

    for (const team_id of Object.keys(this.teams)) {
      team_totals[team_id] = 0;
      team_stats[team_id] = {
        total_bugs: 0,
        unique_bugs: 0,
        false_positives: 0,
        critical_bugs: 0,
        high_bugs: 0,
        scores_per_round: [],
      };
    }

    for (const round_result of this.all_rounds) {
      for (const [team_id, result] of Object.entries(round_result.teams)) {
        team_totals[team_id] += result.score;
        const stats = team_stats[team_id];
        stats.total_bugs += result.bugs_found.length;
        stats.unique_bugs += result.unique_discoveries;
        stats.false_positives += result.false_positives;
        stats.scores_per_round.push(result.score);

        // Count severity
        for (const bug of result.bugs_found) {
          if (bug.severity === 'critical') {
            stats.critical_bugs++;
          } else if (bug.severity === 'high') {
            stats.high_bugs++;
          }
        }
      }
    }

    // Determine winner
    const [winner_id, winner_score] = Object.entries(team_totals).reduce((a, b) =>
      a[1] > b[1] ? a : b
    );
    const winner = this.teams[winner_id];

    return {
      championship_id: this.session_id,
      target: this.target_path,
      rounds: this.rounds,
      winner: {
        id: winner_id,
        name: winner.name,
        strategy: winner.strategy,
        total_score: winner_score,
        stats: team_stats[winner_id],
      },
      all_teams: Object.fromEntries(
        Object.entries(team_totals).map(([team_id, score]) => [
          team_id,
          {
            name: this.teams[team_id].name,
            total_score: score,
            stats: team_stats[team_id],
          },
        ])
      ),
      rounds: this.all_rounds,
    };
  }

  /**
   * Display final championship results
   */
  private _display_championship_results(results: Record<string, any>): void {
    console.log('\n' + '='.repeat(60));
    console.log('  FINAL CHAMPIONSHIP RESULTS');
    console.log('='.repeat(60) + '\n');

    // Sort teams by total score
    const sorted_teams = Object.entries(results.all_teams).sort(
      (a: any, b: any) => b[1].total_score - a[1].total_score
    );

    sorted_teams.forEach(([team_id, team_data]: [string, any], index) => {
      const medals = ['🥇', '🥈', '🥉'];
      const medal = index < 3 ? medals[index] : '  ';
      console.log(
        `${medal} ${team_data.name.padEnd(30)} Total: ${team_data.total_score.toFixed(0).padStart(7)}`
      );
      const stats = team_data.stats;
      console.log(
        `   Critical: ${stats.critical_bugs.toString().padStart(2)}  |  ` +
        `High: ${stats.high_bugs.toString().padStart(2)}  |  ` +
        `Total Bugs: ${stats.total_bugs.toString().padStart(3)}  |  ` +
        `FP: ${stats.false_positives.toString().padStart(2)}`
      );
      console.log();
    });

    console.log('='.repeat(60) + '\n');
  }

  /**
   * Save results to JSON file
   */
  private _save_results(results: Record<string, any>): void {
    const output_file = path.join(this.output_dir, `championship_${this.session_id}.json`);

    try {
      fs.writeFileSync(output_file, JSON.stringify(results, null, 2));
      console.log(`Results saved to: ${output_file}`);
    } catch (error) {
      console.error(`Error saving results to ${output_file}:`, error);
    }
  }

  /**
   * Generate visualizations of results
   */
  private _visualize_results(results: Record<string, any>): void {
    console.log('\nVisualization would be generated here...');
    console.log('  - Score progression per round');
    console.log('  - Bug severity distribution');
    console.log('  - Team comparison charts');
  }
}

// Main entry point
if (require.main === module) {
  const args = process.argv.slice(2);
  const target_path = args.find(arg => !arg.startsWith('--')) || process.cwd();
  const rounds = parseInt(args.find(arg => arg.startsWith('--rounds='))?.split('=')[1] || '5');
  const output_dir = args.find(arg => arg.startsWith('--output='))?.split('=')[1] || './results';
  const visualize = args.includes('--visualize');

  // Validate target exists
  if (!fs.existsSync(target_path)) {
    console.error(`Error: Target path does not exist: ${target_path}`);
    process.exit(1);
  }

  // Create coordinator
  const coordinator = new BugHuntingCoordinator(target_path, rounds, output_dir, visualize);

  // Run championship
  coordinator
    .run_championship()
    .then(() => {
      process.exit(0);
    })
    .catch(error => {
      console.error('Error running championship:', error);
      process.exit(1);
    });
}
