#!/usr/bin/env python3
"""
Scoring Engine for Bug Hunting Championship

Implements CVSS-based scoring with bonuses and penalties for:
- Severity levels
- Uniqueness
- Report quality
- Time to discovery
- False positives
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum
import time


class Severity(Enum):
    """Bug severity levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


@dataclass
class BugReport:
    """Represents a discovered bug/vulnerability"""
    vuln_type: str
    location: str
    severity: str
    cvss_score: float
    description: str
    proof_of_concept: str
    remediation: str
    discovered_at: float
    team: str

    # Metadata (set by scoring engine)
    is_unique: bool = False
    is_false_positive: bool = False
    discovered_by: str = ""
    quality_score: float = 0.0
    time_bonus: float = 0.0
    total_score: float = 0.0

    def __post_init__(self):
        """Validate and normalize fields"""
        # Normalize severity
        self.severity = self.severity.lower()
        if self.severity not in [s.value for s in Severity]:
            raise ValueError(f"Invalid severity: {self.severity}")

        # Validate CVSS score
        if not 0 <= self.cvss_score <= 10:
            raise ValueError(f"Invalid CVSS score: {self.cvss_score}")


class ScoringEngine:
    """
    Calculates scores for bug discoveries using industry-standard metrics
    """

    # Base scores by severity (aligned with bug bounty programs)
    SEVERITY_SCORES = {
        Severity.CRITICAL.value: 100,
        Severity.HIGH.value: 50,
        Severity.MEDIUM.value: 25,
        Severity.LOW.value: 10,
        Severity.INFO.value: 5
    }

    # CVSS score multipliers
    CVSS_MULTIPLIERS = {
        (9.0, 10.0): 2.0,   # Critical (9.0-10.0)
        (7.0, 8.9): 1.5,    # High (7.0-8.9)
        (4.0, 6.9): 1.2,    # Medium (4.0-6.9)
        (0.1, 3.9): 1.0,    # Low (0.1-3.9)
    }

    # Bonus multipliers
    UNIQUENESS_BONUS = 0.5      # 50% bonus for first discovery
    QUALITY_BONUS_MAX = 20      # Up to 20 points for report quality
    SPEED_BONUS_MAX = 1.3       # Up to 30% bonus for fast discovery

    # Penalties
    FALSE_POSITIVE_PENALTY = -20

    def __init__(self):
        """Initialize scoring engine"""
        self.discovered_bugs: Dict[str, BugReport] = {}

    def score_bug(self, bug: BugReport) -> float:
        """
        Calculate comprehensive score for a bug report

        Args:
            bug: The bug report to score

        Returns:
            Total score for the bug
        """
        # Check if it's a false positive (simplified check)
        bug.is_false_positive = self._check_false_positive(bug)

        if bug.is_false_positive:
            bug.total_score = self.FALSE_POSITIVE_PENALTY
            return bug.total_score

        # Calculate base score
        base_score = self._calculate_base_score(bug)

        # Apply CVSS multiplier
        cvss_multiplier = self._get_cvss_multiplier(bug.cvss_score)
        score_with_cvss = base_score * cvss_multiplier

        # Calculate bonuses
        uniqueness_bonus = self._calculate_uniqueness_bonus(
            score_with_cvss, bug
        )
        quality_bonus = self._calculate_quality_bonus(bug)
        speed_bonus = self._calculate_speed_bonus(bug)

        # Total score
        bug.quality_score = quality_bonus
        bug.time_bonus = speed_bonus
        bug.total_score = (
            score_with_cvss +
            uniqueness_bonus +
            quality_bonus +
            speed_bonus
        )

        return bug.total_score

    def _calculate_base_score(self, bug: BugReport) -> float:
        """Calculate base score from severity"""
        return self.SEVERITY_SCORES.get(bug.severity, 0)

    def _get_cvss_multiplier(self, cvss_score: float) -> float:
        """Get CVSS-based multiplier"""
        for (min_score, max_score), multiplier in self.CVSS_MULTIPLIERS.items():
            if min_score <= cvss_score <= max_score:
                return multiplier
        return 1.0

    def _calculate_uniqueness_bonus(
        self,
        base_score: float,
        bug: BugReport
    ) -> float:
        """Calculate bonus for unique discovery"""
        if bug.is_unique:
            return base_score * self.UNIQUENESS_BONUS
        return 0.0

    def _calculate_quality_bonus(self, bug: BugReport) -> float:
        """
        Calculate bonus for report quality

        Evaluates:
        - Description completeness
        - Proof of concept clarity
        - Remediation guidance
        """
        quality_score = 0.0

        # Check description (up to 7 points)
        if len(bug.description) >= 50:
            quality_score += 7
        elif len(bug.description) >= 20:
            quality_score += 4
        elif len(bug.description) > 0:
            quality_score += 2

        # Check proof of concept (up to 7 points)
        if len(bug.proof_of_concept) >= 30:
            quality_score += 7
        elif len(bug.proof_of_concept) >= 10:
            quality_score += 4
        elif len(bug.proof_of_concept) > 0:
            quality_score += 2

        # Check remediation (up to 6 points)
        if len(bug.remediation) >= 30:
            quality_score += 6
        elif len(bug.remediation) >= 10:
            quality_score += 3
        elif len(bug.remediation) > 0:
            quality_score += 1

        return min(quality_score, self.QUALITY_BONUS_MAX)

    def _calculate_speed_bonus(self, bug: BugReport) -> float:
        """
        Calculate bonus for discovery speed

        Faster discoveries get higher bonuses (simulated)
        """
        # In real implementation, this would compare to round start time
        # For now, we'll use a simplified approach
        elapsed_minutes = (time.time() - bug.discovered_at) / 60

        if elapsed_minutes < 5:
            return 20  # Very fast
        elif elapsed_minutes < 15:
            return 10  # Fast
        elif elapsed_minutes < 30:
            return 5   # Moderate
        else:
            return 0   # Slow

    def _check_false_positive(self, bug: BugReport) -> bool:
        """
        Check if a bug report is likely a false positive

        This is a simplified check. Real implementation would involve
        validation, verification, and possibly human review.
        """
        # Simple heuristics for false positive detection
        false_positive_indicators = [
            len(bug.description) < 10,
            len(bug.proof_of_concept) < 5,
            bug.cvss_score == 0,
            len(bug.location) == 0,
        ]

        # If multiple indicators, likely false positive
        return sum(false_positive_indicators) >= 2

    def calculate_total_score(self, bug: BugReport) -> float:
        """
        Recalculate total score (useful after updates)

        Args:
            bug: The bug report

        Returns:
            Updated total score
        """
        return self.score_bug(bug)

    def get_severity_distribution(
        self,
        bugs: List[BugReport]
    ) -> Dict[str, int]:
        """Get distribution of bugs by severity"""
        distribution = {s.value: 0 for s in Severity}

        for bug in bugs:
            if not bug.is_false_positive:
                distribution[bug.severity] += 1

        return distribution

    def get_top_bugs(
        self,
        bugs: List[BugReport],
        n: int = 10
    ) -> List[BugReport]:
        """Get top N bugs by score"""
        valid_bugs = [b for b in bugs if not b.is_false_positive]
        return sorted(
            valid_bugs,
            key=lambda b: b.total_score,
            reverse=True
        )[:n]

    def calculate_team_score(self, bugs: List[BugReport]) -> float:
        """Calculate total score for a team's bugs"""
        total = 0.0

        for bug in bugs:
            if bug.is_false_positive:
                total += self.FALSE_POSITIVE_PENALTY
            else:
                total += self.score_bug(bug)

        return total

    def generate_scorecard(self, bugs: List[BugReport]) -> Dict:
        """Generate comprehensive scorecard for a set of bugs"""
        valid_bugs = [b for b in bugs if not b.is_false_positive]
        false_positives = [b for b in bugs if b.is_false_positive]

        return {
            "total_bugs": len(bugs),
            "valid_bugs": len(valid_bugs),
            "false_positives": len(false_positives),
            "total_score": self.calculate_team_score(bugs),
            "severity_distribution": self.get_severity_distribution(bugs),
            "top_bugs": [
                {
                    "type": b.vuln_type,
                    "severity": b.severity,
                    "score": b.total_score,
                    "location": b.location
                }
                for b in self.get_top_bugs(bugs, 5)
            ],
            "average_cvss": (
                sum(b.cvss_score for b in valid_bugs) / len(valid_bugs)
                if valid_bugs else 0
            ),
            "unique_discoveries": sum(1 for b in valid_bugs if b.is_unique),
            "false_positive_rate": (
                len(false_positives) / len(bugs) if bugs else 0
            )
        }


class CVSSCalculator:
    """
    Helper class for CVSS score calculation

    Implements simplified CVSS v3.1 calculation
    """

    @staticmethod
    def calculate(
        attack_vector: str = "network",
        attack_complexity: str = "low",
        privileges_required: str = "none",
        user_interaction: str = "none",
        scope: str = "unchanged",
        confidentiality: str = "high",
        integrity: str = "high",
        availability: str = "high"
    ) -> float:
        """
        Calculate CVSS v3.1 base score

        Args:
            Various CVSS metrics

        Returns:
            CVSS base score (0.0-10.0)
        """
        # Simplified CVSS calculation
        # Real implementation would use official CVSS formulas

        # Attack Vector
        av_scores = {"network": 0.85, "adjacent": 0.62, "local": 0.55, "physical": 0.2}
        av = av_scores.get(attack_vector.lower(), 0.85)

        # Attack Complexity
        ac_scores = {"low": 0.77, "high": 0.44}
        ac = ac_scores.get(attack_complexity.lower(), 0.77)

        # Privileges Required
        pr_scores = {"none": 0.85, "low": 0.62, "high": 0.27}
        pr = pr_scores.get(privileges_required.lower(), 0.85)

        # User Interaction
        ui_scores = {"none": 0.85, "required": 0.62}
        ui = ui_scores.get(user_interaction.lower(), 0.85)

        # Impact scores
        impact_scores = {"none": 0.0, "low": 0.22, "high": 0.56}
        c = impact_scores.get(confidentiality.lower(), 0.56)
        i = impact_scores.get(integrity.lower(), 0.56)
        a = impact_scores.get(availability.lower(), 0.56)

        # Exploitability
        exploitability = 8.22 * av * ac * pr * ui

        # Impact
        impact_base = 1 - ((1 - c) * (1 - i) * (1 - a))

        if scope == "unchanged":
            impact = 6.42 * impact_base
        else:
            impact = 7.52 * (impact_base - 0.029) - 3.25 * pow(impact_base - 0.02, 15)

        # Final score
        if impact <= 0:
            return 0.0

        if scope == "unchanged":
            score = min(impact + exploitability, 10.0)
        else:
            score = min(1.08 * (impact + exploitability), 10.0)

        return round(score, 1)


# Example usage and testing
if __name__ == "__main__":
    # Create scoring engine
    engine = ScoringEngine()

    # Example bug reports
    bugs = [
        BugReport(
            vuln_type="SQL Injection",
            location="src/db/queries.py:45",
            severity="high",
            cvss_score=8.5,
            description="Unsanitized user input in SQL query allows for data exfiltration",
            proof_of_concept="payload: ' OR '1'='1 -- will bypass authentication",
            remediation="Use parameterized queries or prepared statements",
            discovered_at=time.time(),
            team="Team 1",
            is_unique=True
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
            team="Team 1"
        ),
        BugReport(
            vuln_type="Auth Bypass",
            location="src/auth/middleware.py:78",
            severity="critical",
            cvss_score=9.8,
            description="JWT validation can be bypassed with null signature algorithm",
            proof_of_concept="Send token with alg: none in header",
            remediation="Enforce signature validation and reject 'none' algorithm",
            discovered_at=time.time(),
            team="Team 2",
            is_unique=True
        )
    ]

    # Score the bugs
    for bug in bugs:
        score = engine.score_bug(bug)
        print(f"{bug.vuln_type}: {score:.1f} points")
        print(f"  Severity: {bug.severity} (CVSS: {bug.cvss_score})")
        print(f"  Quality bonus: {bug.quality_score:.1f}")
        print(f"  Unique: {bug.is_unique}")
        print()

    # Generate scorecard
    scorecard = engine.generate_scorecard(bugs)
    print("Team Scorecard:")
    print(f"  Total Score: {scorecard['total_score']:.1f}")
    print(f"  Valid Bugs: {scorecard['valid_bugs']}")
    print(f"  False Positives: {scorecard['false_positives']}")
    print(f"  Average CVSS: {scorecard['average_cvss']:.1f}")
    print(f"  Severity Distribution: {scorecard['severity_distribution']}")

    # Test CVSS calculator
    print("\nCVSS Calculator Example:")
    cvss_score = CVSSCalculator.calculate(
        attack_vector="network",
        attack_complexity="low",
        privileges_required="none",
        user_interaction="none",
        confidentiality="high",
        integrity="high",
        availability="high"
    )
    print(f"Calculated CVSS Score: {cvss_score}")
