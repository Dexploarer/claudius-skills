/**
 * Scoring Engine for Bug Hunting Championship
 *
 * Implements CVSS-based scoring with bonuses and penalties for:
 * - Severity levels
 * - Uniqueness
 * - Report quality
 * - Time to discovery
 * - False positives
 */

export enum Severity {
  CRITICAL = "critical",
  HIGH = "high",
  MEDIUM = "medium",
  LOW = "low",
  INFO = "info",
}

export interface BugReport {
  vuln_type: string;
  location: string;
  severity: Severity;
  cvss_score: number;
  description: string;
  proof_of_concept: string;
  remediation: string;
  discovered_at: number;
  team: string;

  // Metadata (set by scoring engine)
  is_unique?: boolean;
  is_false_positive?: boolean;
  discovered_by?: string;
  quality_score?: number;
  time_bonus?: number;
  total_score?: number;
}

export interface SeverityDistribution {
  [Severity.CRITICAL]: number;
  [Severity.HIGH]: number;
  [Severity.MEDIUM]: number;
  [Severity.LOW]: number;
  [Severity.INFO]: number;
}

export interface TopBug {
  type: string;
  severity: Severity;
  score: number;
  location: string;
}

export interface Scorecard {
  total_bugs: number;
  valid_bugs: number;
  false_positives: number;
  total_score: number;
  severity_distribution: SeverityDistribution;
  top_bugs: TopBug[];
  average_cvss: number;
  unique_discoveries: number;
  false_positive_rate: number;
}

export class ScoringEngine {
  // Base scores by severity (aligned with bug bounty programs)
  private static readonly SEVERITY_SCORES: Record<Severity, number> = {
    [Severity.CRITICAL]: 100,
    [Severity.HIGH]: 50,
    [Severity.MEDIUM]: 25,
    [Severity.LOW]: 10,
    [Severity.INFO]: 5,
  };

  // CVSS score multipliers
  private static readonly CVSS_MULTIPLIERS: Array<{ range: [number, number]; multiplier: number }> = [
    { range: [9.0, 10.0], multiplier: 2.0 },   // Critical (9.0-10.0)
    { range: [7.0, 8.9], multiplier: 1.5 },    // High (7.0-8.9)
    { range: [4.0, 6.9], multiplier: 1.2 },    // Medium (4.0-6.9)
    { range: [0.1, 3.9], multiplier: 1.0 },    // Low (0.1-3.9)
  ];

  // Bonus multipliers
  private static readonly UNIQUENESS_BONUS = 0.5;      // 50% bonus for first discovery
  private static readonly QUALITY_BONUS_MAX = 20;      // Up to 20 points for report quality
  private static readonly SPEED_BONUS_MAX = 1.3;       // Up to 30% bonus for fast discovery

  // Penalties
  private static readonly FALSE_POSITIVE_PENALTY = -20;

  private discovered_bugs: Map<string, BugReport> = new Map();

  /**
   * Calculate comprehensive score for a bug report
   */
  public score_bug(bug: BugReport): number {
    // Check if it's a false positive (simplified check)
    bug.is_false_positive = this._check_false_positive(bug);

    if (bug.is_false_positive) {
      bug.total_score = ScoringEngine.FALSE_POSITIVE_PENALTY;
      return bug.total_score;
    }

    // Calculate base score
    const base_score = this._calculate_base_score(bug);

    // Apply CVSS multiplier
    const cvss_multiplier = this._get_cvss_multiplier(bug.cvss_score);
    const score_with_cvss = base_score * cvss_multiplier;

    // Calculate bonuses
    const uniqueness_bonus = this._calculate_uniqueness_bonus(score_with_cvss, bug);
    const quality_bonus = this._calculate_quality_bonus(bug);
    const speed_bonus = this._calculate_speed_bonus(bug);

    // Total score
    bug.quality_score = quality_bonus;
    bug.time_bonus = speed_bonus;
    bug.total_score = score_with_cvss + uniqueness_bonus + quality_bonus + speed_bonus;

    return bug.total_score;
  }

  private _calculate_base_score(bug: BugReport): number {
    return ScoringEngine.SEVERITY_SCORES[bug.severity] || 0;
  }

  private _get_cvss_multiplier(cvss_score: number): number {
    for (const { range, multiplier } of ScoringEngine.CVSS_MULTIPLIERS) {
      if (cvss_score >= range[0] && cvss_score <= range[1]) {
        return multiplier;
      }
    }
    return 1.0;
  }

  private _calculate_uniqueness_bonus(base_score: number, bug: BugReport): number {
    if (bug.is_unique) {
      return base_score * ScoringEngine.UNIQUENESS_BONUS;
    }
    return 0.0;
  }

  /**
   * Calculate bonus for report quality
   *
   * Evaluates:
   * - Description completeness
   * - Proof of concept clarity
   * - Remediation guidance
   */
  private _calculate_quality_bonus(bug: BugReport): number {
    let quality_score = 0.0;

    // Check description (up to 7 points)
    if (bug.description.length >= 50) {
      quality_score += 7;
    } else if (bug.description.length >= 20) {
      quality_score += 4;
    } else if (bug.description.length > 0) {
      quality_score += 2;
    }

    // Check proof of concept (up to 7 points)
    if (bug.proof_of_concept.length >= 30) {
      quality_score += 7;
    } else if (bug.proof_of_concept.length >= 10) {
      quality_score += 4;
    } else if (bug.proof_of_concept.length > 0) {
      quality_score += 2;
    }

    // Check remediation (up to 6 points)
    if (bug.remediation.length >= 30) {
      quality_score += 6;
    } else if (bug.remediation.length >= 10) {
      quality_score += 3;
    } else if (bug.remediation.length > 0) {
      quality_score += 1;
    }

    return Math.min(quality_score, ScoringEngine.QUALITY_BONUS_MAX);
  }

  /**
   * Calculate bonus for discovery speed
   *
   * Faster discoveries get higher bonuses
   */
  private _calculate_speed_bonus(bug: BugReport): number {
    // In real implementation, this would compare to round start time
    const elapsed_minutes = (Date.now() - bug.discovered_at) / 60000;

    if (elapsed_minutes < 5) {
      return 20;  // Very fast
    } else if (elapsed_minutes < 15) {
      return 10;  // Fast
    } else if (elapsed_minutes < 30) {
      return 5;   // Moderate
    } else {
      return 0;   // Slow
    }
  }

  /**
   * Check if a bug report is likely a false positive
   *
   * This is a simplified check. Real implementation would involve
   * validation, verification, and possibly human review.
   */
  private _check_false_positive(bug: BugReport): boolean {
    // Simple heuristics for false positive detection
    const false_positive_indicators = [
      bug.description.length < 10,
      bug.proof_of_concept.length < 5,
      bug.cvss_score === 0,
      bug.location.length === 0,
    ];

    // If multiple indicators, likely false positive
    return false_positive_indicators.filter(Boolean).length >= 2;
  }

  /**
   * Recalculate total score (useful after updates)
   */
  public calculate_total_score(bug: BugReport): number {
    return this.score_bug(bug);
  }

  /**
   * Get distribution of bugs by severity
   */
  public get_severity_distribution(bugs: BugReport[]): SeverityDistribution {
    const distribution: SeverityDistribution = {
      [Severity.CRITICAL]: 0,
      [Severity.HIGH]: 0,
      [Severity.MEDIUM]: 0,
      [Severity.LOW]: 0,
      [Severity.INFO]: 0,
    };

    for (const bug of bugs) {
      if (!bug.is_false_positive) {
        distribution[bug.severity]++;
      }
    }

    return distribution;
  }

  /**
   * Get top N bugs by score
   */
  public get_top_bugs(bugs: BugReport[], n: number = 10): BugReport[] {
    const valid_bugs = bugs.filter(b => !b.is_false_positive);
    return valid_bugs
      .sort((a, b) => (b.total_score || 0) - (a.total_score || 0))
      .slice(0, n);
  }

  /**
   * Calculate total score for a team's bugs
   */
  public calculate_team_score(bugs: BugReport[]): number {
    let total = 0.0;

    for (const bug of bugs) {
      if (bug.is_false_positive) {
        total += ScoringEngine.FALSE_POSITIVE_PENALTY;
      } else {
        total += this.score_bug(bug);
      }
    }

    return total;
  }

  /**
   * Generate comprehensive scorecard for a set of bugs
   */
  public generate_scorecard(bugs: BugReport[]): Scorecard {
    const valid_bugs = bugs.filter(b => !b.is_false_positive);
    const false_positives = bugs.filter(b => b.is_false_positive);

    return {
      total_bugs: bugs.length,
      valid_bugs: valid_bugs.length,
      false_positives: false_positives.length,
      total_score: this.calculate_team_score(bugs),
      severity_distribution: this.get_severity_distribution(bugs),
      top_bugs: this.get_top_bugs(bugs, 5).map(b => ({
        type: b.vuln_type,
        severity: b.severity,
        score: b.total_score || 0,
        location: b.location,
      })),
      average_cvss:
        valid_bugs.length > 0
          ? valid_bugs.reduce((sum, b) => sum + b.cvss_score, 0) / valid_bugs.length
          : 0,
      unique_discoveries: valid_bugs.filter(b => b.is_unique).length,
      false_positive_rate: bugs.length > 0 ? false_positives.length / bugs.length : 0,
    };
  }
}

/**
 * Helper class for CVSS score calculation
 *
 * Implements simplified CVSS v3.1 calculation
 */
export class CVSSCalculator {
  /**
   * Calculate CVSS v3.1 base score
   */
  public static calculate(options: {
    attack_vector?: string;
    attack_complexity?: string;
    privileges_required?: string;
    user_interaction?: string;
    scope?: string;
    confidentiality?: string;
    integrity?: string;
    availability?: string;
  } = {}): number {
    const {
      attack_vector = "network",
      attack_complexity = "low",
      privileges_required = "none",
      user_interaction = "none",
      scope = "unchanged",
      confidentiality = "high",
      integrity = "high",
      availability = "high",
    } = options;

    // Attack Vector
    const av_scores: Record<string, number> = {
      network: 0.85,
      adjacent: 0.62,
      local: 0.55,
      physical: 0.2,
    };
    const av = av_scores[attack_vector.toLowerCase()] || 0.85;

    // Attack Complexity
    const ac_scores: Record<string, number> = { low: 0.77, high: 0.44 };
    const ac = ac_scores[attack_complexity.toLowerCase()] || 0.77;

    // Privileges Required
    const pr_scores: Record<string, number> = { none: 0.85, low: 0.62, high: 0.27 };
    const pr = pr_scores[privileges_required.toLowerCase()] || 0.85;

    // User Interaction
    const ui_scores: Record<string, number> = { none: 0.85, required: 0.62 };
    const ui = ui_scores[user_interaction.toLowerCase()] || 0.85;

    // Impact scores
    const impact_scores: Record<string, number> = { none: 0.0, low: 0.22, high: 0.56 };
    const c = impact_scores[confidentiality.toLowerCase()] || 0.56;
    const i = impact_scores[integrity.toLowerCase()] || 0.56;
    const a = impact_scores[availability.toLowerCase()] || 0.56;

    // Exploitability
    const exploitability = 8.22 * av * ac * pr * ui;

    // Impact
    const impact_base = 1 - (1 - c) * (1 - i) * (1 - a);

    let impact: number;
    if (scope === "unchanged") {
      impact = 6.42 * impact_base;
    } else {
      impact = 7.52 * (impact_base - 0.029) - 3.25 * Math.pow(impact_base - 0.02, 15);
    }

    // Final score
    if (impact <= 0) {
      return 0.0;
    }

    let score: number;
    if (scope === "unchanged") {
      score = Math.min(impact + exploitability, 10.0);
    } else {
      score = Math.min(1.08 * (impact + exploitability), 10.0);
    }

    return Math.round(score * 10) / 10;
  }
}
