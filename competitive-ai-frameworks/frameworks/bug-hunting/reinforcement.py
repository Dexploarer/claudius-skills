#!/usr/bin/env python3
"""
Reinforcement Learning System for Strategy Adaptation

Implements a reinforcement learning algorithm that adapts team strategies
based on their performance across rounds.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
import math
import json


@dataclass
class StrategyUpdate:
    """Represents an update to strategy weights"""
    vulnerability_type: str
    old_weight: float
    new_weight: float
    reason: str
    reward: float


class ReinforcementLearner:
    """
    Implements reinforcement learning for bug hunting strategy adaptation

    Uses a variant of Q-learning adapted for competitive bug hunting:
    - Rewards successful vulnerability discoveries
    - Penalizes false positives
    - Adjusts weights based on uniqueness and severity
    - Implements exploration vs exploitation trade-off
    """

    # Learning parameters
    LEARNING_RATE = 0.15          # How quickly to adapt (alpha)
    DISCOUNT_FACTOR = 0.9         # Future reward importance (gamma)
    EXPLORATION_RATE = 0.1        # Chance to try new strategies (epsilon)
    MIN_WEIGHT = 0.1              # Minimum weight for any vulnerability type
    MAX_WEIGHT = 2.0              # Maximum weight for any vulnerability type

    # Reward structure
    REWARD_CRITICAL = 100
    REWARD_HIGH = 50
    REWARD_MEDIUM = 25
    REWARD_LOW = 10
    PENALTY_FALSE_POSITIVE = -20
    BONUS_UNIQUE = 50
    BONUS_FIRST_DISCOVERY = 25

    def __init__(
        self,
        learning_rate: float = LEARNING_RATE,
        discount_factor: float = DISCOUNT_FACTOR,
        exploration_rate: float = EXPLORATION_RATE
    ):
        """
        Initialize reinforcement learner

        Args:
            learning_rate: How quickly to update weights (0-1)
            discount_factor: Importance of future rewards (0-1)
            exploration_rate: Probability of random exploration (0-1)
        """
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

        # Track history for each vulnerability type
        self.vuln_history: Dict[str, List[float]] = {}

        # Track strategy performance
        self.strategy_performance: Dict[str, Dict] = {}

    def update_weights(
        self,
        current_weights: Dict[str, float],
        bugs_found: List['BugReport'],
        score: float,
        false_positives: int
    ) -> Dict[str, float]:
        """
        Update strategy weights based on round performance

        Args:
            current_weights: Current vulnerability type weights
            bugs_found: List of bugs discovered this round
            score: Total score achieved
            false_positives: Number of false positives

        Returns:
            Updated weights dictionary
        """
        new_weights = current_weights.copy()
        updates: List[StrategyUpdate] = []

        # Calculate rewards for each vulnerability type
        vuln_rewards = self._calculate_vuln_rewards(bugs_found)

        # Update weights for each vulnerability type
        for vuln_type, current_weight in current_weights.items():
            # Get reward for this vulnerability type
            reward = vuln_rewards.get(vuln_type, 0)

            # Calculate baseline (average performance)
            baseline = self._get_baseline_reward(vuln_type)

            # Calculate weight update using policy gradient method
            # new_weight = old_weight + learning_rate * (reward - baseline) * frequency
            frequency = self._get_discovery_frequency(vuln_type, bugs_found)

            # Calculate update
            delta = self.learning_rate * (reward - baseline) * frequency

            # Apply update with exploration
            if self._should_explore():
                # Add random exploration
                delta += self._random_exploration_delta()

            new_weight = current_weight + delta

            # Clip to valid range
            new_weight = max(self.MIN_WEIGHT, min(self.MAX_WEIGHT, new_weight))

            # Record update
            if abs(new_weight - current_weight) > 0.01:
                updates.append(StrategyUpdate(
                    vulnerability_type=vuln_type,
                    old_weight=current_weight,
                    new_weight=new_weight,
                    reason=self._generate_update_reason(
                        vuln_type, reward, baseline, frequency
                    ),
                    reward=reward
                ))

            new_weights[vuln_type] = new_weight

            # Update history
            if vuln_type not in self.vuln_history:
                self.vuln_history[vuln_type] = []
            self.vuln_history[vuln_type].append(reward)

        # Normalize weights (optional, keeps total weight consistent)
        # new_weights = self._normalize_weights(new_weights)

        return new_weights

    def _calculate_vuln_rewards(
        self,
        bugs_found: List['BugReport']
    ) -> Dict[str, float]:
        """Calculate rewards for each vulnerability type"""
        rewards = {}

        for bug in bugs_found:
            if bug.is_false_positive:
                # Penalize false positives
                if bug.vuln_type not in rewards:
                    rewards[bug.vuln_type] = 0
                rewards[bug.vuln_type] += self.PENALTY_FALSE_POSITIVE
                continue

            # Base reward by severity
            if bug.severity == "critical":
                base_reward = self.REWARD_CRITICAL
            elif bug.severity == "high":
                base_reward = self.REWARD_HIGH
            elif bug.severity == "medium":
                base_reward = self.REWARD_MEDIUM
            else:
                base_reward = self.REWARD_LOW

            # Apply bonuses
            reward = base_reward

            if bug.is_unique:
                reward += self.BONUS_UNIQUE

            # Add to vulnerability type total
            if bug.vuln_type not in rewards:
                rewards[bug.vuln_type] = 0
            rewards[bug.vuln_type] += reward

        return rewards

    def _get_baseline_reward(self, vuln_type: str) -> float:
        """
        Calculate baseline reward for a vulnerability type

        Uses moving average of historical rewards
        """
        if vuln_type not in self.vuln_history or not self.vuln_history[vuln_type]:
            return 0.0

        history = self.vuln_history[vuln_type]

        # Use recent history (last 5 rounds) for baseline
        recent_history = history[-5:]
        return sum(recent_history) / len(recent_history)

    def _get_discovery_frequency(
        self,
        vuln_type: str,
        bugs_found: List['BugReport']
    ) -> float:
        """
        Calculate how frequently this vulnerability type was discovered

        Returns value between 0 and 1
        """
        if not bugs_found:
            return 0.0

        count = sum(1 for bug in bugs_found if bug.vuln_type == vuln_type)
        return count / len(bugs_found)

    def _should_explore(self) -> bool:
        """Determine if we should explore (vs exploit)"""
        import random
        return random.random() < self.exploration_rate

    def _random_exploration_delta(self) -> float:
        """Generate random exploration delta"""
        import random
        # Random value between -0.1 and 0.1
        return (random.random() - 0.5) * 0.2

    def _generate_update_reason(
        self,
        vuln_type: str,
        reward: float,
        baseline: float,
        frequency: float
    ) -> str:
        """Generate human-readable reason for weight update"""
        if reward > baseline + 10:
            return f"High success rate with {vuln_type} (reward: {reward:.1f})"
        elif reward < baseline - 10:
            return f"Poor performance with {vuln_type} (reward: {reward:.1f})"
        elif frequency > 0.3:
            return f"Frequent discoveries of {vuln_type}"
        elif frequency < 0.05:
            return f"Rare discoveries of {vuln_type}"
        else:
            return f"Maintaining strategy for {vuln_type}"

    def _normalize_weights(self, weights: Dict[str, float]) -> Dict[str, float]:
        """
        Normalize weights to sum to a specific value

        This ensures total effort remains constant
        """
        total = sum(weights.values())
        target_total = len(weights)  # Average weight of 1.0

        if total == 0:
            return weights

        factor = target_total / total
        return {k: v * factor for k, v in weights.items()}

    def get_strategy_recommendations(
        self,
        current_weights: Dict[str, float],
        performance_history: List[float]
    ) -> List[str]:
        """
        Generate strategy recommendations based on performance

        Args:
            current_weights: Current strategy weights
            performance_history: Historical performance scores

        Returns:
            List of strategic recommendations
        """
        recommendations = []

        # Analyze performance trend
        if len(performance_history) >= 3:
            recent_avg = sum(performance_history[-3:]) / 3
            overall_avg = sum(performance_history) / len(performance_history)

            if recent_avg < overall_avg * 0.8:
                recommendations.append(
                    "Performance declining - consider diversifying vulnerability focus"
                )
            elif recent_avg > overall_avg * 1.2:
                recommendations.append(
                    "Performance improving - continue current strategy direction"
                )

        # Analyze weight distribution
        sorted_weights = sorted(
            current_weights.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Check if too focused
        top_3_weight = sum(w for _, w in sorted_weights[:3])
        total_weight = sum(current_weights.values())

        if top_3_weight / total_weight > 0.7:
            recommendations.append(
                f"Heavily focused on: {', '.join(v for v, _ in sorted_weights[:3])}. " +
                "Consider broadening coverage."
            )

        # Check for neglected areas
        neglected = [v for v, w in current_weights.items() if w < 0.3]
        if neglected:
            recommendations.append(
                f"Low coverage areas: {', '.join(neglected[:3])}. " +
                "These might have untapped potential."
            )

        # Check for high-performing areas
        high_performers = [
            (v, self._get_baseline_reward(v))
            for v in current_weights.keys()
        ]
        high_performers = [
            v for v, r in high_performers if r > 50
        ]

        if high_performers:
            recommendations.append(
                f"High success areas: {', '.join(high_performers[:3])}. " +
                "Consider increasing focus here."
            )

        return recommendations if recommendations else [
            "Strategy performing adequately - continue current approach"
        ]

    def export_learning_data(self, filepath: str):
        """Export learning history and data to JSON"""
        data = {
            "parameters": {
                "learning_rate": self.learning_rate,
                "discount_factor": self.discount_factor,
                "exploration_rate": self.exploration_rate
            },
            "vulnerability_history": self.vuln_history,
            "strategy_performance": self.strategy_performance
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def import_learning_data(self, filepath: str):
        """Import learning history from JSON"""
        with open(filepath, 'r') as f:
            data = json.load(f)

        self.vuln_history = data.get("vulnerability_history", {})
        self.strategy_performance = data.get("strategy_performance", {})


class AdaptiveExploration:
    """
    Implements adaptive exploration rate

    Decreases exploration as the system learns, but increases when
    performance plateaus or declines.
    """

    def __init__(
        self,
        initial_rate: float = 0.3,
        min_rate: float = 0.05,
        decay_factor: float = 0.95
    ):
        """
        Initialize adaptive exploration

        Args:
            initial_rate: Starting exploration rate
            min_rate: Minimum exploration rate
            decay_factor: How quickly exploration decays
        """
        self.current_rate = initial_rate
        self.min_rate = min_rate
        self.decay_factor = decay_factor
        self.performance_history: List[float] = []

    def update(self, performance: float) -> float:
        """
        Update exploration rate based on performance

        Args:
            performance: Latest performance score

        Returns:
            Updated exploration rate
        """
        self.performance_history.append(performance)

        # Check if performance is plateauing or declining
        if len(self.performance_history) >= 5:
            recent = self.performance_history[-5:]
            variance = self._calculate_variance(recent)

            if variance < 10:  # Performance plateauing
                # Increase exploration to find new strategies
                self.current_rate = min(0.3, self.current_rate * 1.1)
            elif recent[-1] < recent[0]:  # Performance declining
                # Increase exploration significantly
                self.current_rate = min(0.4, self.current_rate * 1.2)
            else:
                # Normal decay
                self.current_rate = max(
                    self.min_rate,
                    self.current_rate * self.decay_factor
                )

        return self.current_rate

    def _calculate_variance(self, values: List[float]) -> float:
        """Calculate variance of values"""
        if not values:
            return 0.0

        mean = sum(values) / len(values)
        return sum((x - mean) ** 2 for x in values) / len(values)


# Example usage and testing
if __name__ == "__main__":
    from scoring_engine import BugReport
    import time

    print("Reinforcement Learning System Test")
    print("="*60)

    # Create learner
    learner = ReinforcementLearner()

    # Initial weights
    initial_weights = {
        "sql_injection": 1.0,
        "xss": 1.0,
        "csrf": 0.8,
        "auth_bypass": 0.7,
        "idor": 0.6
    }

    print("\nInitial Weights:")
    for vuln, weight in initial_weights.items():
        print(f"  {vuln}: {weight:.2f}")

    # Simulate Round 1: Good performance on SQL injection
    bugs_round1 = [
        BugReport(
            vuln_type="sql_injection",
            location="src/db/query.py:45",
            severity="critical",
            cvss_score=9.5,
            description="SQL injection vulnerability",
            proof_of_concept="' OR 1=1--",
            remediation="Use parameterized queries",
            discovered_at=time.time(),
            team="Test Team",
            is_unique=True
        ),
        BugReport(
            vuln_type="sql_injection",
            location="src/api/users.py:123",
            severity="high",
            cvss_score=8.0,
            description="Another SQL injection",
            proof_of_concept="UNION SELECT",
            remediation="Sanitize input",
            discovered_at=time.time(),
            team="Test Team",
            is_unique=True
        )
    ]

    print("\n\nRound 1 Results:")
    print(f"  Found {len(bugs_round1)} bugs (both SQL injection)")

    updated_weights1 = learner.update_weights(
        initial_weights,
        bugs_round1,
        score=250,
        false_positives=0
    )

    print("\nUpdated Weights After Round 1:")
    for vuln, weight in updated_weights1.items():
        change = weight - initial_weights[vuln]
        arrow = "↑" if change > 0 else "↓" if change < 0 else "→"
        print(f"  {vuln}: {weight:.2f} {arrow}")

    # Simulate Round 2: False positives in XSS
    bugs_round2 = [
        BugReport(
            vuln_type="xss",
            location="src/template.html:12",
            severity="medium",
            cvss_score=6.0,
            description="XSS vulnerability",
            proof_of_concept="<script>alert(1)</script>",
            remediation="Escape output",
            discovered_at=time.time(),
            team="Test Team",
            is_false_positive=True  # False positive!
        )
    ]

    print("\n\nRound 2 Results:")
    print(f"  Found {len(bugs_round2)} bugs (1 false positive)")

    updated_weights2 = learner.update_weights(
        updated_weights1,
        bugs_round2,
        score=-20,
        false_positives=1
    )

    print("\nUpdated Weights After Round 2:")
    for vuln, weight in updated_weights2.items():
        change = weight - updated_weights1[vuln]
        arrow = "↑" if change > 0 else "↓" if change < 0 else "→"
        print(f"  {vuln}: {weight:.2f} {arrow}")

    # Get recommendations
    print("\n\nStrategy Recommendations:")
    recommendations = learner.get_strategy_recommendations(
        updated_weights2,
        [100, 250, -20]
    )
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec}")

    print("\n" + "="*60)
