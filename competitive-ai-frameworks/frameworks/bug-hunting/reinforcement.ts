/**
 * Reinforcement Learning System for Strategy Adaptation
 *
 * Implements a reinforcement learning algorithm that adapts team strategies
 * based on their performance across rounds.
 */

import type { BugReport } from './scoring_engine';
import * as fs from 'fs';

export interface StrategyUpdate {
  vulnerability_type: string;
  old_weight: number;
  new_weight: number;
  reason: string;
  reward: number;
}

export class ReinforcementLearner {
  // Learning parameters
  private static readonly LEARNING_RATE = 0.15;          // How quickly to adapt (alpha)
  private static readonly DISCOUNT_FACTOR = 0.9;         // Future reward importance (gamma)
  private static readonly EXPLORATION_RATE = 0.1;        // Chance to try new strategies (epsilon)
  private static readonly MIN_WEIGHT = 0.1;              // Minimum weight for any vulnerability type
  private static readonly MAX_WEIGHT = 2.0;              // Maximum weight for any vulnerability type

  // Reward structure
  private static readonly REWARD_CRITICAL = 100;
  private static readonly REWARD_HIGH = 50;
  private static readonly REWARD_MEDIUM = 25;
  private static readonly REWARD_LOW = 10;
  private static readonly PENALTY_FALSE_POSITIVE = -20;
  private static readonly BONUS_UNIQUE = 50;
  private static readonly BONUS_FIRST_DISCOVERY = 25;

  private learning_rate: number;
  private discount_factor: number;
  private exploration_rate: number;

  // Track history for each vulnerability type
  private vuln_history: Map<string, number[]> = new Map();

  // Track strategy performance
  private strategy_performance: Map<string, any> = new Map();

  constructor(
    learning_rate: number = ReinforcementLearner.LEARNING_RATE,
    discount_factor: number = ReinforcementLearner.DISCOUNT_FACTOR,
    exploration_rate: number = ReinforcementLearner.EXPLORATION_RATE
  ) {
    this.learning_rate = learning_rate;
    this.discount_factor = discount_factor;
    this.exploration_rate = exploration_rate;
  }

  /**
   * Update strategy weights based on round performance
   */
  public update_weights(
    current_weights: Record<string, number>,
    bugs_found: BugReport[],
    score: number,
    false_positives: number
  ): Record<string, number> {
    const new_weights: Record<string, number> = { ...current_weights };
    const updates: StrategyUpdate[] = [];

    // Calculate rewards for each vulnerability type
    const vuln_rewards = this._calculate_vuln_rewards(bugs_found);

    // Update weights for each vulnerability type
    for (const [vuln_type, current_weight] of Object.entries(current_weights)) {
      // Get reward for this vulnerability type
      const reward = vuln_rewards[vuln_type] || 0;

      // Calculate baseline (average performance)
      const baseline = this._get_baseline_reward(vuln_type);

      // Calculate weight update using policy gradient method
      const frequency = this._get_discovery_frequency(vuln_type, bugs_found);

      // Calculate update
      let delta = this.learning_rate * (reward - baseline) * frequency;

      // Apply update with exploration
      if (this._should_explore()) {
        delta += this._random_exploration_delta();
      }

      let new_weight = current_weight + delta;

      // Clip to valid range
      new_weight = Math.max(
        ReinforcementLearner.MIN_WEIGHT,
        Math.min(ReinforcementLearner.MAX_WEIGHT, new_weight)
      );

      // Record update
      if (Math.abs(new_weight - current_weight) > 0.01) {
        updates.push({
          vulnerability_type: vuln_type,
          old_weight: current_weight,
          new_weight: new_weight,
          reason: this._generate_update_reason(vuln_type, reward, baseline, frequency),
          reward: reward,
        });
      }

      new_weights[vuln_type] = new_weight;

      // Update history
      if (!this.vuln_history.has(vuln_type)) {
        this.vuln_history.set(vuln_type, []);
      }
      this.vuln_history.get(vuln_type)!.push(reward);
    }

    return new_weights;
  }

  /**
   * Calculate rewards for each vulnerability type
   */
  private _calculate_vuln_rewards(bugs_found: BugReport[]): Record<string, number> {
    const rewards: Record<string, number> = {};

    for (const bug of bugs_found) {
      if (bug.is_false_positive) {
        rewards[bug.vuln_type] = (rewards[bug.vuln_type] || 0) + ReinforcementLearner.PENALTY_FALSE_POSITIVE;
        continue;
      }

      // Base reward by severity
      let base_reward: number;
      if (bug.severity === 'critical') {
        base_reward = ReinforcementLearner.REWARD_CRITICAL;
      } else if (bug.severity === 'high') {
        base_reward = ReinforcementLearner.REWARD_HIGH;
      } else if (bug.severity === 'medium') {
        base_reward = ReinforcementLearner.REWARD_MEDIUM;
      } else {
        base_reward = ReinforcementLearner.REWARD_LOW;
      }

      // Apply bonuses
      let reward = base_reward;
      if (bug.is_unique) {
        reward += ReinforcementLearner.BONUS_UNIQUE;
      }

      // Add to vulnerability type total
      rewards[bug.vuln_type] = (rewards[bug.vuln_type] || 0) + reward;
    }

    return rewards;
  }

  /**
   * Calculate baseline reward for a vulnerability type
   */
  private _get_baseline_reward(vuln_type: string): number {
    const history = this.vuln_history.get(vuln_type);
    if (!history || history.length === 0) {
      return 0.0;
    }

    // Use recent history (last 5 rounds) for baseline
    const recent_history = history.slice(-5);
    return recent_history.reduce((a, b) => a + b, 0) / recent_history.length;
  }

  /**
   * Calculate how frequently this vulnerability type was discovered
   */
  private _get_discovery_frequency(vuln_type: string, bugs_found: BugReport[]): number {
    if (bugs_found.length === 0) {
      return 0.0;
    }

    const count = bugs_found.filter(bug => bug.vuln_type === vuln_type).length;
    return count / bugs_found.length;
  }

  /**
   * Determine if we should explore (vs exploit)
   */
  private _should_explore(): boolean {
    return Math.random() < this.exploration_rate;
  }

  /**
   * Generate random exploration delta
   */
  private _random_exploration_delta(): number {
    // Random value between -0.1 and 0.1
    return (Math.random() - 0.5) * 0.2;
  }

  /**
   * Generate human-readable reason for weight update
   */
  private _generate_update_reason(
    vuln_type: string,
    reward: number,
    baseline: number,
    frequency: number
  ): string {
    if (reward > baseline + 10) {
      return `High success rate with ${vuln_type} (reward: ${reward.toFixed(1)})`;
    } else if (reward < baseline - 10) {
      return `Poor performance with ${vuln_type} (reward: ${reward.toFixed(1)})`;
    } else if (frequency > 0.3) {
      return `Frequent discoveries of ${vuln_type}`;
    } else if (frequency < 0.05) {
      return `Rare discoveries of ${vuln_type}`;
    } else {
      return `Maintaining strategy for ${vuln_type}`;
    }
  }

  /**
   * Normalize weights to sum to a specific value
   */
  private _normalize_weights(weights: Record<string, number>): Record<string, number> {
    const total = Object.values(weights).reduce((a, b) => a + b, 0);
    const target_total = Object.keys(weights).length; // Average weight of 1.0

    if (total === 0) {
      return weights;
    }

    const factor = target_total / total;
    return Object.fromEntries(
      Object.entries(weights).map(([k, v]) => [k, v * factor])
    );
  }

  /**
   * Generate strategy recommendations based on performance
   */
  public get_strategy_recommendations(
    current_weights: Record<string, number>,
    performance_history: number[]
  ): string[] {
    const recommendations: string[] = [];

    // Analyze performance trend
    if (performance_history.length >= 3) {
      const recent_avg =
        performance_history.slice(-3).reduce((a, b) => a + b, 0) / 3;
      const overall_avg =
        performance_history.reduce((a, b) => a + b, 0) / performance_history.length;

      if (recent_avg < overall_avg * 0.8) {
        recommendations.push(
          'Performance declining - consider diversifying vulnerability focus'
        );
      } else if (recent_avg > overall_avg * 1.2) {
        recommendations.push(
          'Performance improving - continue current strategy direction'
        );
      }
    }

    // Analyze weight distribution
    const sorted_weights = Object.entries(current_weights).sort((a, b) => b[1] - a[1]);

    // Check if too focused
    const top_3_weight = sorted_weights.slice(0, 3).reduce((sum, [, w]) => sum + w, 0);
    const total_weight = Object.values(current_weights).reduce((a, b) => a + b, 0);

    if (total_weight > 0 && top_3_weight / total_weight > 0.7) {
      recommendations.push(
        `Heavily focused on: ${sorted_weights.slice(0, 3).map(([v]) => v).join(', ')}. ` +
        'Consider broadening coverage.'
      );
    }

    // Check for neglected areas
    const neglected = Object.entries(current_weights)
      .filter(([, w]) => w < 0.3)
      .map(([v]) => v);
    if (neglected.length > 0) {
      recommendations.push(
        `Low coverage areas: ${neglected.slice(0, 3).join(', ')}. ` +
        'These might have untapped potential.'
      );
    }

    // Check for high-performing areas
    const high_performers = Object.keys(current_weights).filter(
      v => this._get_baseline_reward(v) > 50
    );

    if (high_performers.length > 0) {
      recommendations.push(
        `High success areas: ${high_performers.slice(0, 3).join(', ')}. ` +
        'Consider increasing focus here.'
      );
    }

    return recommendations.length > 0
      ? recommendations
      : ['Strategy performing adequately - continue current approach'];
  }

  /**
   * Export learning history and data to JSON
   */
  public export_learning_data(filepath: string): void {
    const data = {
      parameters: {
        learning_rate: this.learning_rate,
        discount_factor: this.discount_factor,
        exploration_rate: this.exploration_rate,
      },
      vulnerability_history: Object.fromEntries(this.vuln_history),
      strategy_performance: Object.fromEntries(this.strategy_performance),
    };

    try {
      fs.writeFileSync(filepath, JSON.stringify(data, null, 2));
    } catch (error) {
      console.error(`Error exporting learning data to ${filepath}:`, error);
    }
  }

  /**
   * Import learning history from JSON
   */
  public import_learning_data(filepath: string): void {
    const data = JSON.parse(fs.readFileSync(filepath, 'utf-8'));
    this.vuln_history = new Map(Object.entries(data.vulnerability_history || {}));
    this.strategy_performance = new Map(Object.entries(data.strategy_performance || {}));
  }
}

/**
 * Implements adaptive exploration rate
 */
export class AdaptiveExploration {
  private current_rate: number;
  private min_rate: number;
  private decay_factor: number;
  private performance_history: number[] = [];

  constructor(
    initial_rate: number = 0.3,
    min_rate: number = 0.05,
    decay_factor: number = 0.95
  ) {
    this.current_rate = initial_rate;
    this.min_rate = min_rate;
    this.decay_factor = decay_factor;
  }

  /**
   * Update exploration rate based on performance
   */
  public update(performance: number): number {
    this.performance_history.push(performance);

    // Check if performance is plateauing or declining
    if (this.performance_history.length >= 5) {
      const recent = this.performance_history.slice(-5);
      const variance = this._calculate_variance(recent);

      if (variance < 10) {
        // Performance plateauing - increase exploration
        this.current_rate = Math.min(0.3, this.current_rate * 1.1);
      } else if (recent[recent.length - 1] < recent[0]) {
        // Performance declining - increase exploration significantly
        this.current_rate = Math.min(0.4, this.current_rate * 1.2);
      } else {
        // Normal decay
        this.current_rate = Math.max(this.min_rate, this.current_rate * this.decay_factor);
      }
    }

    return this.current_rate;
  }

  /**
   * Calculate variance of values
   */
  private _calculate_variance(values: number[]): number {
    if (values.length === 0) {
      return 0.0;
    }

    const mean = values.reduce((a, b) => a + b, 0) / values.length;
    return values.reduce((sum, x) => sum + Math.pow(x - mean, 2), 0) / values.length;
  }
}
