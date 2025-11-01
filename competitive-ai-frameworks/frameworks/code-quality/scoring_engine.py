#!/usr/bin/env python3
"""
Scoring Engine for Code Quality Championship

Scores improvements across three dimensions:
- Performance (runtime, memory, bundle size)
- Maintainability (complexity, tests, documentation)
- Best Practices (style, security, accessibility)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum


class ImprovementCategory(Enum):
    """Categories of code quality improvements"""
    PERFORMANCE = "performance"
    MAINTAINABILITY = "maintainability"
    BEST_PRACTICES = "best_practices"


class ImprovementType(Enum):
    """Specific types of improvements"""
    # Performance
    ALGORITHM_OPTIMIZATION = "algorithm_optimization"
    MEMORY_LEAK_FIX = "memory_leak_fix"
    BUNDLE_SIZE_REDUCTION = "bundle_size_reduction"
    CACHING = "caching"
    LAZY_LOADING = "lazy_loading"

    # Maintainability
    COMPLEXITY_REDUCTION = "complexity_reduction"
    TEST_COVERAGE = "test_coverage"
    DOCUMENTATION = "documentation"
    REFACTORING = "refactoring"
    CODE_DUPLICATION = "code_duplication"

    # Best Practices
    LINTING_FIX = "linting_fix"
    SECURITY_FIX = "security_fix"
    ACCESSIBILITY = "accessibility"
    TYPE_SAFETY = "type_safety"
    ERROR_HANDLING = "error_handling"


@dataclass
class QualityImprovement:
    """Represents a code quality improvement"""
    improvement_type: str
    category: str
    location: str
    description: str

    # Before/after metrics
    before_value: float
    after_value: float
    unit: str  # "ms", "%", "KB", "complexity", etc.

    # Additional context
    impact_description: str
    team: str

    # Calculated by scoring engine
    improvement_percent: float = 0.0
    base_score: float = 0.0
    multiplier: float = 1.0
    bonus_points: float = 0.0
    total_score: float = 0.0

    def __post_init__(self):
        """Calculate improvement percentage"""
        if self.before_value > 0:
            # For metrics where lower is better (complexity, time, bundle size)
            if self.unit in ['ms', 'KB', 'MB', 'complexity', 'errors']:
                self.improvement_percent = (
                    (self.before_value - self.after_value) /
                    self.before_value * 100
                )
            # For metrics where higher is better (coverage, score)
            else:
                self.improvement_percent = (
                    (self.after_value - self.before_value) /
                    max(self.before_value, 1) * 100
                )


class CodeQualityScoringEngine:
    """
    Calculates scores for code quality improvements
    """

    # Base scores by improvement type
    BASE_SCORES = {
        # Performance (high impact = high base score)
        ImprovementType.ALGORITHM_OPTIMIZATION.value: 50,
        ImprovementType.MEMORY_LEAK_FIX.value: 30,
        ImprovementType.BUNDLE_SIZE_REDUCTION.value: 40,
        ImprovementType.CACHING.value: 25,
        ImprovementType.LAZY_LOADING.value: 30,

        # Maintainability
        ImprovementType.COMPLEXITY_REDUCTION.value: 35,
        ImprovementType.TEST_COVERAGE.value: 40,
        ImprovementType.DOCUMENTATION.value: 25,
        ImprovementType.REFACTORING.value: 30,
        ImprovementType.CODE_DUPLICATION.value: 20,

        # Best Practices
        ImprovementType.LINTING_FIX.value: 15,
        ImprovementType.SECURITY_FIX.value: 45,
        ImprovementType.ACCESSIBILITY.value: 35,
        ImprovementType.TYPE_SAFETY.value: 25,
        ImprovementType.ERROR_HANDLING.value: 20,
    }

    # Improvement multipliers based on percentage improvement
    IMPROVEMENT_MULTIPLIERS = {
        (90, 100): 2.0,    # Massive improvement (90-100%)
        (70, 89): 1.7,     # Major improvement (70-89%)
        (50, 69): 1.4,     # Significant improvement (50-69%)
        (30, 49): 1.2,     # Moderate improvement (30-49%)
        (10, 29): 1.0,     # Minor improvement (10-29%)
        (0, 9): 0.5,       # Minimal improvement (<10%)
    }

    # Bonus points
    IMPACT_BONUS_MAX = 20      # Up to 20 points for high impact
    DOCUMENTATION_BONUS = 10   # Bonus for well-documented changes
    BREAKING_CHANGE_PENALTY = -50  # Penalty for breaking changes

    def __init__(self):
        """Initialize scoring engine"""
        self.improvements_tracked: List[QualityImprovement] = []

    def score_improvement(
        self,
        improvement: QualityImprovement
    ) -> float:
        """
        Calculate comprehensive score for an improvement

        Args:
            improvement: The code quality improvement to score

        Returns:
            Total score for the improvement
        """
        # Get base score
        base_score = self._get_base_score(improvement)

        # Apply improvement multiplier
        multiplier = self._get_improvement_multiplier(
            improvement.improvement_percent
        )
        score_with_multiplier = base_score * multiplier

        # Calculate bonuses
        impact_bonus = self._calculate_impact_bonus(improvement)

        # Total score
        improvement.base_score = base_score
        improvement.multiplier = multiplier
        improvement.bonus_points = impact_bonus
        improvement.total_score = (
            score_with_multiplier + impact_bonus
        )

        # Track improvement
        self.improvements_tracked.append(improvement)

        return improvement.total_score

    def _get_base_score(self, improvement: QualityImprovement) -> float:
        """Get base score for improvement type"""
        return self.BASE_SCORES.get(
            improvement.improvement_type,
            20  # Default base score
        )

    def _get_improvement_multiplier(self, improvement_percent: float) -> float:
        """Get multiplier based on improvement percentage"""
        for (min_pct, max_pct), multiplier in self.IMPROVEMENT_MULTIPLIERS.items():
            if min_pct <= improvement_percent <= max_pct:
                return multiplier
        return 0.5  # Minimal improvement

    def _calculate_impact_bonus(
        self,
        improvement: QualityImprovement
    ) -> float:
        """
        Calculate bonus for improvement impact

        Considers:
        - Description quality
        - User-facing impact
        - Scope of improvement
        """
        bonus = 0.0

        # Bonus for detailed description
        if len(improvement.description) > 50:
            bonus += 5
        if len(improvement.impact_description) > 30:
            bonus += 5

        # Bonus for high-impact improvements
        if improvement.improvement_percent > 80:
            bonus += 10
        elif improvement.improvement_percent > 50:
            bonus += 5

        return min(bonus, self.IMPACT_BONUS_MAX)

    def calculate_team_score(
        self,
        improvements: List[QualityImprovement]
    ) -> float:
        """Calculate total score for a team's improvements"""
        total = 0.0

        for improvement in improvements:
            total += self.score_improvement(improvement)

        return total

    def calculate_category_scores(
        self,
        improvements: List[QualityImprovement]
    ) -> Dict[str, float]:
        """Calculate scores broken down by category"""
        category_scores = {
            ImprovementCategory.PERFORMANCE.value: 0.0,
            ImprovementCategory.MAINTAINABILITY.value: 0.0,
            ImprovementCategory.BEST_PRACTICES.value: 0.0,
        }

        for improvement in improvements:
            if improvement.category in category_scores:
                category_scores[improvement.category] += (
                    improvement.total_score
                )

        return category_scores

    def get_top_improvements(
        self,
        improvements: List[QualityImprovement],
        n: int = 10
    ) -> List[QualityImprovement]:
        """Get top N improvements by score"""
        return sorted(
            improvements,
            key=lambda i: i.total_score,
            reverse=True
        )[:n]

    def generate_scorecard(
        self,
        improvements: List[QualityImprovement]
    ) -> Dict:
        """Generate comprehensive scorecard"""
        category_scores = self.calculate_category_scores(improvements)
        total_score = sum(category_scores.values())

        # Count improvements by type
        type_counts = {}
        for improvement in improvements:
            imp_type = improvement.improvement_type
            type_counts[imp_type] = type_counts.get(imp_type, 0) + 1

        return {
            "total_improvements": len(improvements),
            "total_score": total_score,
            "category_breakdown": category_scores,
            "improvement_types": type_counts,
            "top_improvements": [
                {
                    "type": imp.improvement_type,
                    "location": imp.location,
                    "improvement": f"{imp.improvement_percent:.1f}%",
                    "score": imp.total_score
                }
                for imp in self.get_top_improvements(improvements, 5)
            ],
            "average_improvement_percent": (
                sum(i.improvement_percent for i in improvements) /
                len(improvements) if improvements else 0
            )
        }


class MetricsCalculator:
    """
    Helper class for calculating various code quality metrics
    """

    @staticmethod
    def calculate_complexity_improvement(
        before_complexity: int,
        after_complexity: int
    ) -> float:
        """Calculate complexity reduction percentage"""
        if before_complexity == 0:
            return 0.0
        return (before_complexity - after_complexity) / before_complexity * 100

    @staticmethod
    def calculate_coverage_improvement(
        before_coverage: float,
        after_coverage: float
    ) -> float:
        """Calculate test coverage increase"""
        return after_coverage - before_coverage

    @staticmethod
    def calculate_performance_improvement(
        before_ms: float,
        after_ms: float
    ) -> float:
        """Calculate performance improvement percentage"""
        if before_ms == 0:
            return 0.0
        return (before_ms - after_ms) / before_ms * 100

    @staticmethod
    def calculate_bundle_size_improvement(
        before_kb: float,
        after_kb: float
    ) -> float:
        """Calculate bundle size reduction percentage"""
        if before_kb == 0:
            return 0.0
        return (before_kb - after_kb) / before_kb * 100

    @staticmethod
    def estimate_time_to_first_byte_improvement(
        bundle_reduction_kb: float,
        connection_speed_kbps: float = 1000  # 1 Mbps default
    ) -> float:
        """Estimate TTFB improvement from bundle reduction"""
        # Convert KB to Kb and calculate time saved
        bundle_reduction_kb_bits = bundle_reduction_kb * 8
        time_saved_seconds = bundle_reduction_kb_bits / connection_speed_kbps
        return time_saved_seconds * 1000  # Convert to ms


# Example usage and testing
if __name__ == "__main__":
    # Create scoring engine
    engine = CodeQualityScoringEngine()

    # Example improvements
    improvements = [
        # Performance improvement
        QualityImprovement(
            improvement_type=ImprovementType.ALGORITHM_OPTIMIZATION.value,
            category=ImprovementCategory.PERFORMANCE.value,
            location="src/utils/search.js:45",
            description="Replaced O(n²) bubble sort with O(n log n) quicksort for large arrays",
            before_value=250.0,
            after_value=5.0,
            unit="ms",
            impact_description="Search results now appear instantly for large datasets",
            team="Performance Optimizers"
        ),

        # Maintainability improvement
        QualityImprovement(
            improvement_type=ImprovementType.COMPLEXITY_REDUCTION.value,
            category=ImprovementCategory.MAINTAINABILITY.value,
            location="src/services/order.py:120",
            description="Extracted payment processing into separate functions, reducing cyclomatic complexity",
            before_value=18.0,
            after_value=4.0,
            unit="complexity",
            impact_description="Function is now easily understandable and testable",
            team="Maintainability Engineers"
        ),

        # Best practices improvement
        QualityImprovement(
            improvement_type=ImprovementType.SECURITY_FIX.value,
            category=ImprovementCategory.BEST_PRACTICES.value,
            location="src/api/routes.js:67",
            description="Added input validation and parameterized queries to prevent SQL injection",
            before_value=1.0,
            after_value=0.0,
            unit="vulnerabilities",
            impact_description="Critical security vulnerability eliminated",
            team="Best Practices Auditors"
        ),

        # Test coverage improvement
        QualityImprovement(
            improvement_type=ImprovementType.TEST_COVERAGE.value,
            category=ImprovementCategory.MAINTAINABILITY.value,
            location="src/services/payment.py",
            description="Added comprehensive test suite covering all payment flows and edge cases",
            before_value=15.0,
            after_value=92.0,
            unit="%",
            impact_description="Payment processing is now fully tested and reliable",
            team="Maintainability Engineers"
        ),

        # Bundle size reduction
        QualityImprovement(
            improvement_type=ImprovementType.BUNDLE_SIZE_REDUCTION.value,
            category=ImprovementCategory.PERFORMANCE.value,
            location="package.json",
            description="Replaced moment.js with date-fns and implemented tree shaking",
            before_value=500.0,
            after_value=45.0,
            unit="KB",
            impact_description="Initial page load 91% faster on slow connections",
            team="Performance Optimizers"
        )
    ]

    # Score all improvements
    print("Code Quality Improvements Scoring")
    print("=" * 60)

    for imp in improvements:
        score = engine.score_improvement(imp)
        print(f"\n{imp.improvement_type}")
        print(f"  Location: {imp.location}")
        print(f"  Improvement: {imp.before_value}{imp.unit} → {imp.after_value}{imp.unit}")
        print(f"  Percentage: {imp.improvement_percent:.1f}%")
        print(f"  Base Score: {imp.base_score:.0f}")
        print(f"  Multiplier: {imp.multiplier:.1f}x")
        print(f"  Bonus: +{imp.bonus_points:.0f}")
        print(f"  Total Score: {imp.total_score:.1f} points")

    # Generate scorecard
    print("\n" + "=" * 60)
    scorecard = engine.generate_scorecard(improvements)
    print("\nTeam Scorecard:")
    print(f"  Total Score: {scorecard['total_score']:.1f}")
    print(f"  Total Improvements: {scorecard['total_improvements']}")
    print(f"  Average Improvement: {scorecard['average_improvement_percent']:.1f}%")

    print("\nCategory Breakdown:")
    for category, score in scorecard['category_breakdown'].items():
        print(f"  {category}: {score:.1f} points")

    print("\nTop 5 Improvements:")
    for i, imp in enumerate(scorecard['top_improvements'], 1):
        print(f"  {i}. {imp['type']}: {imp['improvement']} improvement ({imp['score']:.1f} pts)")
