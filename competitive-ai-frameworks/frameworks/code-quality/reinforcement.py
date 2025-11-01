#!/usr/bin/env python3
"""
Reinforcement Learning System for Code Quality Championship

Adapts team strategies based on improvement success rates across rounds.
"""

from typing import Dict, List
from dataclasses import dataclass
import json
import random


@dataclass
class StrategyUpdate:
    """Represents an update to strategy weights"""
    improvement_type: str
    old_weight: float
    new_weight: float
    reason: str
    reward: float


class QualityReinforcementLearner:
    """
    Implements reinforcement learning for code quality strategy adaptation
    """

    # Learning parameters
    LEARNING_RATE = 0.15
    DISCOUNT_FACTOR = 0.9
    EXPLORATION_RATE = 0.1
    MIN_WEIGHT = 0.1
    MAX_WEIGHT = 2.0

    # Reward structure (based on score improvements)
    REWARD_MASSIVE_IMPROVEMENT = 100    # 90%+ improvement
    REWARD_MAJOR_IMPROVEMENT = 60       # 70-89% improvement
    REWARD_SIGNIFICANT = 35             # 50-69% improvement
    REWARD_MODERATE = 20                # 30-49% improvement
    REWARD_MINOR = 10                   # 10-29% improvement
    PENALTY_MINIMAL = -5                # <10% improvement

    def __init__(
        self,
        learning_rate: float = LEARNING_RATE,
        discount_factor: float = DISCOUNT_FACTOR,
        exploration_rate: float = EXPLORATION_RATE
    ):
        """Initialize reinforcement learner"""
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.improvement_history: Dict[str, List[float]] = {}

    def update_weights(
        self,
        current_weights: Dict[str, float],
        improvements: List[Dict],
        total_score: float
    ) -> Dict[str, float]:
        """
        Update strategy weights based on round performance

        Args:
            current_weights: Current improvement type weights
            improvements: List of improvements made this round
            total_score: Total score achieved

        Returns:
            Updated weights dictionary
        """
        new_weights = current_weights.copy()

        # Calculate rewards for each improvement type
        type_rewards = self._calculate_improvement_rewards(improvements)

        # Update weights for each improvement type
        for imp_type, current_weight in current_weights.items():
            # Get reward for this improvement type
            reward = type_rewards.get(imp_type, 0)

            # Calculate baseline (average historical performance)
            baseline = self._get_baseline_reward(imp_type)

            # Calculate improvement frequency
            frequency = self._get_improvement_frequency(imp_type, improvements)

            # Calculate weight update
            delta = self.learning_rate * (reward - baseline) * frequency

            # Apply exploration
            if self._should_explore():
                delta += self._random_exploration_delta()

            new_weight = current_weight + delta

            # Clip to valid range
            new_weight = max(self.MIN_WEIGHT, min(self.MAX_WEIGHT, new_weight))

            new_weights[imp_type] = new_weight

            # Update history
            if imp_type not in self.improvement_history:
                self.improvement_history[imp_type] = []
            self.improvement_history[imp_type].append(reward)

        return new_weights

    def _calculate_improvement_rewards(
        self,
        improvements: List[Dict]
    ) -> Dict[str, float]:
        """Calculate rewards for each improvement type"""
        rewards = {}

        for improvement in improvements:
            imp_type = improvement.get('improvement_type')
            imp_percent = improvement.get('improvement_percent', 0)

            # Calculate reward based on improvement percentage
            if imp_percent >= 90:
                reward = self.REWARD_MASSIVE_IMPROVEMENT
            elif imp_percent >= 70:
                reward = self.REWARD_MAJOR_IMPROVEMENT
            elif imp_percent >= 50:
                reward = self.REWARD_SIGNIFICANT
            elif imp_percent >= 30:
                reward = self.REWARD_MODERATE
            elif imp_percent >= 10:
                reward = self.REWARD_MINOR
            else:
                reward = self.PENALTY_MINIMAL

            # Accumulate rewards by type
            if imp_type not in rewards:
                rewards[imp_type] = 0
            rewards[imp_type] += reward

        return rewards

    def _get_baseline_reward(self, imp_type: str) -> float:
        """Get baseline reward from historical performance"""
        if imp_type not in self.improvement_history or not self.improvement_history[imp_type]:
            return 0.0

        history = self.improvement_history[imp_type]
        recent_history = history[-5:]  # Last 5 rounds
        return sum(recent_history) / len(recent_history)

    def _get_improvement_frequency(
        self,
        imp_type: str,
        improvements: List[Dict]
    ) -> float:
        """Calculate frequency of this improvement type"""
        if not improvements:
            return 0.0

        count = sum(1 for imp in improvements if imp.get('improvement_type') == imp_type)
        return count / len(improvements)

    def _should_explore(self) -> bool:
        """Determine if we should explore (vs exploit)"""
        return random.random() < self.exploration_rate

    def _random_exploration_delta(self) -> float:
        """Generate random exploration delta"""
        return (random.random() - 0.5) * 0.2

    def get_strategy_recommendations(
        self,
        current_weights: Dict[str, float],
        performance_history: List[float]
    ) -> List[str]:
        """Generate strategy recommendations"""
        recommendations = []

        # Analyze performance trend
        if len(performance_history) >= 3:
            recent_avg = sum(performance_history[-3:]) / 3
            overall_avg = sum(performance_history) / len(performance_history)

            if recent_avg < overall_avg * 0.8:
                recommendations.append(
                    "Performance declining - consider diversifying improvement focus"
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
            top_types = [t for t, _ in sorted_weights[:3]]
            recommendations.append(
                f"Heavily focused on: {', '.join(top_types)}. "
                "Consider broadening scope for more improvements."
            )

        # Find neglected areas with potential
        neglected = [t for t, w in current_weights.items() if w < 0.3]
        if neglected:
            recommendations.append(
                f"Low focus areas: {', '.join(neglected[:3])}. "
                "These might have untapped potential."
            )

        # Find high-performing areas
        high_performers = [
            (t, self._get_baseline_reward(t))
            for t in current_weights.keys()
        ]
        high_performers = [
            t for t, r in high_performers if r > 40
        ]

        if high_performers:
            recommendations.append(
                f"High success areas: {', '.join(high_performers[:3])}. "
                "Consider increasing focus here."
            )

        return recommendations if recommendations else [
            "Strategy performing adequately - continue current approach"
        ]

    def export_learning_data(self, filepath: str):
        """Export learning history to JSON"""
        data = {
            "parameters": {
                "learning_rate": self.learning_rate,
                "discount_factor": self.discount_factor,
                "exploration_rate": self.exploration_rate
            },
            "improvement_history": self.improvement_history
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)


# Example usage
if __name__ == "__main__":
    print("Code Quality Reinforcement Learning Test")
    print("=" * 60)

    # Create learner
    learner = QualityReinforcementLearner()

    # Initial weights for Performance team
    initial_weights = {
        "algorithm_optimization": 1.0,
        "memory_leak_fix": 0.9,
        "bundle_size_reduction": 0.8,
        "caching": 0.7,
        "lazy_loading": 0.8
    }

    print("\nInitial Weights:")
    for imp_type, weight in initial_weights.items():
        print(f"  {imp_type}: {weight:.2f}")

    # Simulate Round 1: Good performance on algorithm optimization
    improvements_round1 = [
        {
            "improvement_type": "algorithm_optimization",
            "improvement_percent": 95.0,
            "score": 85
        },
        {
            "improvement_type": "algorithm_optimization",
            "improvement_percent": 88.0,
            "score": 72
        },
        {
            "improvement_type": "bundle_size_reduction",
            "improvement_percent": 45.0,
            "score": 35
        }
    ]

    print("\n\nRound 1 Results:")
    print(f"  {len(improvements_round1)} improvements made")
    print("  Strong performance on algorithm optimization")

    updated_weights1 = learner.update_weights(
        initial_weights,
        improvements_round1,
        total_score=192
    )

    print("\nUpdated Weights After Round 1:")
    for imp_type, weight in updated_weights1.items():
        change = weight - initial_weights[imp_type]
        arrow = "↑" if change > 0 else "↓" if change < 0 else "→"
        print(f"  {imp_type}: {weight:.2f} {arrow}")

    # Simulate Round 2: Poor performance on caching
    improvements_round2 = [
        {
            "improvement_type": "caching",
            "improvement_percent": 8.0,  # Minimal improvement
            "score": 5
        },
        {
            "improvement_type": "memory_leak_fix",
            "improvement_percent": 72.0,
            "score": 58
        }
    ]

    print("\n\nRound 2 Results:")
    print(f"  {len(improvements_round2)} improvements made")
    print("  Caching had minimal impact, memory fixes worked well")

    updated_weights2 = learner.update_weights(
        updated_weights1,
        improvements_round2,
        total_score=63
    )

    print("\nUpdated Weights After Round 2:")
    for imp_type, weight in updated_weights2.items():
        change = weight - updated_weights1[imp_type]
        arrow = "↑" if change > 0 else "↓" if change < 0 else "→"
        print(f"  {imp_type}: {weight:.2f} {arrow}")

    # Get recommendations
    print("\n\nStrategy Recommendations:")
    recommendations = learner.get_strategy_recommendations(
        updated_weights2,
        [100, 192, 63]
    )
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec}")

    print("\n" + "=" * 60)
