#!/usr/bin/env python3
"""
Agent Pool Management System

Manages all available agents across frameworks, enabling flexible team composition,
recommendations, and roster management.
"""

from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Set, Tuple
from datetime import datetime
from enum import Enum
import json
from pathlib import Path


class ExperienceLevel(Enum):
    """Agent experience levels"""
    NOVICE = 1
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    EXPERT = 5
    MASTER = 6
    GRANDMASTER = 7
    LEGEND = 8
    MYTHIC = 9
    GODLIKE = 10


class Specialization(Enum):
    """Agent specialization types"""
    # Security
    AUTOMATED_SCANNING = "automated_scanning"
    MANUAL_REVIEW = "manual_review"
    FUZZING = "fuzzing"
    ML_DETECTION = "ml_detection"
    CRYPTO_ANALYSIS = "crypto_analysis"

    # Performance
    FRONTEND_OPTIMIZATION = "frontend_optimization"
    BACKEND_OPTIMIZATION = "backend_optimization"
    DATABASE_TUNING = "database_tuning"
    ALGORITHM_OPTIMIZATION = "algorithm_optimization"
    NETWORK_OPTIMIZATION = "network_optimization"

    # Architecture
    MICROSERVICES_DESIGN = "microservices_design"
    MONOLITH_DESIGN = "monolith_design"
    EVENT_DRIVEN_DESIGN = "event_driven_design"
    SERVERLESS_DESIGN = "serverless_design"

    # API Design
    REST_DESIGN = "rest_design"
    GRAPHQL_DESIGN = "graphql_design"
    GRPC_DESIGN = "grpc_design"

    # Quality
    CODE_REVIEW = "code_review"
    TEST_STRATEGY = "test_strategy"
    DOCUMENTATION = "documentation"
    MAINTAINABILITY = "maintainability"


@dataclass
class Agent:
    """Individual competing agent"""
    id: str
    name: str
    specialization: Specialization
    skills: List[str]
    framework_compatibility: List[str]
    experience_level: ExperienceLevel
    win_rate: float = 0.0
    elo_rating: int = 1500
    games_played: int = 0
    description: str = ""
    strengths: List[str] = None
    weaknesses: List[str] = None
    cost: int = 1  # For budget-based team composition

    def __post_init__(self):
        if self.strengths is None:
            self.strengths = []
        if self.weaknesses is None:
            self.weaknesses = []


@dataclass
class AgentRating:
    """Agent performance ratings and statistics"""
    agent_id: str
    elo_rating: int = 1500
    games_played: int = 0
    win_count: int = 0
    loss_count: int = 0
    draw_count: int = 0
    peak_rating: int = 1500
    lowest_rating: int = 1500
    rating_history: List[Tuple[datetime, int]] = None
    framework_performance: Dict[str, float] = None  # Framework -> win rate

    def __post_init__(self):
        if self.rating_history is None:
            self.rating_history = []
        if self.framework_performance is None:
            self.framework_performance = {}

    @property
    def win_percentage(self) -> float:
        """Calculate overall win percentage"""
        total = self.win_count + self.loss_count + self.draw_count
        return (self.win_count / total * 100) if total > 0 else 0.0


@dataclass
class Team:
    """Team composed of multiple agents"""
    id: str
    name: str
    agents: List[Agent]
    strategy: str = "balanced"
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    @property
    def total_cost(self) -> int:
        """Calculate total team cost"""
        return sum(agent.cost for agent in self.agents)

    @property
    def avg_elo(self) -> float:
        """Calculate average ELO rating"""
        return sum(agent.elo_rating for agent in self.agents) / len(self.agents) if self.agents else 0

    @property
    def combined_skills(self) -> Set[str]:
        """Get all unique skills across team"""
        skills = set()
        for agent in self.agents:
            skills.update(agent.skills)
        return skills


class AgentPool:
    """
    Manages all available agents across frameworks.

    Provides:
    - Agent registration and discovery
    - Team composition recommendations
    - Performance tracking
    - Roster management
    """

    def __init__(self, persistence_path: Optional[Path] = None):
        self.agents: Dict[str, Agent] = {}
        self.ratings: Dict[str, AgentRating] = {}
        self.teams: Dict[str, Team] = {}
        self.persistence_path = persistence_path or Path("./persistence/agent_pool.json")

        # Load existing data if available
        self._load_data()

    def register_agent(self, agent: Agent) -> None:
        """Register a new agent to the pool"""
        self.agents[agent.id] = agent

        if agent.id not in self.ratings:
            self.ratings[agent.id] = AgentRating(
                agent_id=agent.id,
                elo_rating=agent.elo_rating,
                games_played=agent.games_played
            )

        self._save_data()

    def get_agent(self, agent_id: str) -> Optional[Agent]:
        """Get agent by ID"""
        return self.agents.get(agent_id)

    def list_agents(
        self,
        framework: Optional[str] = None,
        specialization: Optional[Specialization] = None,
        min_experience: Optional[ExperienceLevel] = None,
        min_elo: Optional[int] = None
    ) -> List[Agent]:
        """
        List agents with optional filters

        Args:
            framework: Filter by framework compatibility
            specialization: Filter by specialization
            min_experience: Minimum experience level
            min_elo: Minimum ELO rating

        Returns:
            List of matching agents
        """
        agents = list(self.agents.values())

        if framework:
            agents = [a for a in agents if framework in a.framework_compatibility]

        if specialization:
            agents = [a for a in agents if a.specialization == specialization]

        if min_experience:
            agents = [a for a in agents if a.experience_level.value >= min_experience.value]

        if min_elo:
            agents = [a for a in agents if a.elo_rating >= min_elo]

        return sorted(agents, key=lambda a: a.elo_rating, reverse=True)

    def recommend_team(
        self,
        framework: str,
        budget: int = 4,
        strategy: str = "balanced",
        target_specializations: Optional[List[Specialization]] = None
    ) -> Team:
        """
        AI-powered team recommendation

        Args:
            framework: Target framework
            budget: Maximum number of agents
            strategy: Team composition strategy
            target_specializations: Desired specializations to include

        Returns:
            Recommended team
        """
        # Get compatible agents
        compatible = self.list_agents(framework=framework)

        if not compatible:
            raise ValueError(f"No agents compatible with framework '{framework}'")

        selected_agents = []

        if strategy == "balanced":
            selected_agents = self._select_balanced_team(compatible, budget, target_specializations)
        elif strategy == "aggressive":
            selected_agents = self._select_high_rating_team(compatible, budget)
        elif strategy == "specialist":
            selected_agents = self._select_specialist_team(compatible, budget, target_specializations)
        elif strategy == "diverse":
            selected_agents = self._select_diverse_team(compatible, budget)
        else:
            # Default to balanced
            selected_agents = self._select_balanced_team(compatible, budget, target_specializations)

        team = Team(
            id=f"team_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            name=f"Recommended {strategy.title()} Team",
            agents=selected_agents,
            strategy=strategy
        )

        return team

    def _select_balanced_team(
        self,
        agents: List[Agent],
        budget: int,
        target_specializations: Optional[List[Specialization]] = None
    ) -> List[Agent]:
        """Select balanced team with diverse specializations"""
        selected = []
        used_specializations = set()

        # If target specializations provided, prioritize them
        if target_specializations:
            for spec in target_specializations:
                if len(selected) >= budget:
                    break

                # Find best agent with this specialization
                spec_agents = [a for a in agents if a.specialization == spec]
                if spec_agents:
                    best = max(spec_agents, key=lambda a: a.elo_rating)
                    selected.append(best)
                    used_specializations.add(spec)
                    agents = [a for a in agents if a.id != best.id]

        # Fill remaining slots with diverse agents
        while len(selected) < budget and agents:
            # Prefer agents with new specializations
            unused_spec_agents = [
                a for a in agents
                if a.specialization not in used_specializations
            ]

            if unused_spec_agents:
                best = max(unused_spec_agents, key=lambda a: a.elo_rating)
                selected.append(best)
                used_specializations.add(best.specialization)
                agents = [a for a in agents if a.id != best.id]
            else:
                # All specializations covered, pick highest rated
                best = max(agents, key=lambda a: a.elo_rating)
                selected.append(best)
                agents = [a for a in agents if a.id != best.id]

        return selected

    def _select_high_rating_team(self, agents: List[Agent], budget: int) -> List[Agent]:
        """Select team with highest ELO ratings"""
        sorted_agents = sorted(agents, key=lambda a: a.elo_rating, reverse=True)
        return sorted_agents[:budget]

    def _select_specialist_team(
        self,
        agents: List[Agent],
        budget: int,
        specializations: Optional[List[Specialization]] = None
    ) -> List[Agent]:
        """Select team focused on specific specializations"""
        if not specializations:
            # If no specs provided, pick most common specialization
            spec_counts = {}
            for agent in agents:
                spec = agent.specialization
                spec_counts[spec] = spec_counts.get(spec, 0) + 1

            most_common = max(spec_counts.items(), key=lambda x: x[1])[0]
            specializations = [most_common]

        selected = []
        for spec in specializations:
            if len(selected) >= budget:
                break

            spec_agents = [a for a in agents if a.specialization == spec]
            spec_agents.sort(key=lambda a: a.elo_rating, reverse=True)

            # Take top agents of this specialization
            slots_for_spec = min(budget - len(selected), len(spec_agents))
            selected.extend(spec_agents[:slots_for_spec])

        return selected

    def _select_diverse_team(self, agents: List[Agent], budget: int) -> List[Agent]:
        """Select team with maximum diversity in skills and specializations"""
        selected = []
        covered_skills = set()
        used_specializations = set()

        # Sort by skill coverage first, then ELO
        def diversity_score(agent: Agent) -> float:
            new_skills = len(set(agent.skills) - covered_skills)
            spec_bonus = 0 if agent.specialization in used_specializations else 100
            return new_skills * 10 + agent.elo_rating / 100 + spec_bonus

        while len(selected) < budget and agents:
            best = max(agents, key=diversity_score)
            selected.append(best)
            covered_skills.update(best.skills)
            used_specializations.add(best.specialization)
            agents = [a for a in agents if a.id != best.id]

        return selected

    def create_team(
        self,
        name: str,
        agent_ids: List[str],
        strategy: str = "custom"
    ) -> Team:
        """Create custom team from agent IDs"""
        agents = []
        for agent_id in agent_ids:
            agent = self.get_agent(agent_id)
            if not agent:
                raise ValueError(f"Agent '{agent_id}' not found")
            agents.append(agent)

        team = Team(
            id=f"team_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            name=name,
            agents=agents,
            strategy=strategy
        )

        self.teams[team.id] = team
        self._save_data()

        return team

    def get_team(self, team_id: str) -> Optional[Team]:
        """Get team by ID"""
        return self.teams.get(team_id)

    def list_teams(self) -> List[Team]:
        """List all registered teams"""
        return list(self.teams.values())

    def update_agent_rating(
        self,
        agent_id: str,
        new_rating: int,
        win: bool = False,
        loss: bool = False,
        draw: bool = False,
        framework: Optional[str] = None
    ) -> None:
        """Update agent's ELO rating and statistics"""
        if agent_id not in self.ratings:
            raise ValueError(f"No rating record for agent '{agent_id}'")

        rating = self.ratings[agent_id]
        rating.elo_rating = new_rating
        rating.games_played += 1

        if win:
            rating.win_count += 1
        elif loss:
            rating.loss_count += 1
        elif draw:
            rating.draw_count += 1

        # Update peak/lowest
        if new_rating > rating.peak_rating:
            rating.peak_rating = new_rating
        if new_rating < rating.lowest_rating:
            rating.lowest_rating = new_rating

        # Add to history
        rating.rating_history.append((datetime.now(), new_rating))

        # Update framework-specific performance
        if framework:
            if framework not in rating.framework_performance:
                rating.framework_performance[framework] = 0.0

            # Update rolling average win rate
            current_rate = rating.framework_performance[framework]
            games_in_framework = sum(
                1 for _ in rating.rating_history  # Simplified; should track per-framework
            )

            if win:
                new_rate = ((current_rate * (games_in_framework - 1)) + 1) / games_in_framework
            elif loss:
                new_rate = ((current_rate * (games_in_framework - 1)) + 0) / games_in_framework
            else:  # draw
                new_rate = ((current_rate * (games_in_framework - 1)) + 0.5) / games_in_framework

            rating.framework_performance[framework] = new_rate

        # Update agent object
        if agent_id in self.agents:
            agent = self.agents[agent_id]
            agent.elo_rating = new_rating
            agent.games_played = rating.games_played
            agent.win_rate = rating.win_percentage / 100

        self._save_data()

    def get_leaderboard(
        self,
        framework: Optional[str] = None,
        limit: int = 20
    ) -> List[Tuple[int, Agent, AgentRating]]:
        """
        Get leaderboard rankings

        Args:
            framework: Optional framework filter
            limit: Number of top agents to return

        Returns:
            List of (rank, agent, rating) tuples
        """
        agents = self.list_agents(framework=framework) if framework else list(self.agents.values())

        # Sort by ELO rating
        ranked = sorted(agents, key=lambda a: a.elo_rating, reverse=True)

        # Return with rankings
        return [
            (rank, agent, self.ratings.get(agent.id))
            for rank, agent in enumerate(ranked[:limit], start=1)
        ]

    def get_agent_stats(self, agent_id: str) -> Dict:
        """Get comprehensive statistics for an agent"""
        agent = self.get_agent(agent_id)
        rating = self.ratings.get(agent_id)

        if not agent or not rating:
            raise ValueError(f"Agent '{agent_id}' not found")

        return {
            "agent": asdict(agent),
            "rating": {
                "current_elo": rating.elo_rating,
                "peak_elo": rating.peak_rating,
                "lowest_elo": rating.lowest_rating,
                "games_played": rating.games_played,
                "wins": rating.win_count,
                "losses": rating.loss_count,
                "draws": rating.draw_count,
                "win_rate": rating.win_percentage,
                "framework_performance": rating.framework_performance
            },
            "strengths": agent.strengths,
            "weaknesses": agent.weaknesses,
            "compatible_frameworks": agent.framework_compatibility
        }

    def _save_data(self) -> None:
        """Save agent pool data to disk"""
        try:
            self.persistence_path.parent.mkdir(parents=True, exist_ok=True)

            data = {
                "agents": {
                    agent_id: {
                        **asdict(agent),
                        "specialization": agent.specialization.value,
                        "experience_level": agent.experience_level.value
                    }
                    for agent_id, agent in self.agents.items()
                },
                "ratings": {
                    agent_id: {
                        **asdict(rating),
                        "rating_history": [
                            (ts.isoformat(), rating_val)
                            for ts, rating_val in rating.rating_history
                        ]
                    }
                    for agent_id, rating in self.ratings.items()
                },
                "teams": {
                    team_id: {
                        "id": team.id,
                        "name": team.name,
                        "agent_ids": [agent.id for agent in team.agents],
                        "strategy": team.strategy,
                        "created_at": team.created_at.isoformat()
                    }
                    for team_id, team in self.teams.items()
                }
            }

            with open(self.persistence_path, 'w') as f:
                json.dump(data, f, indent=2)

        except Exception as e:
            print(f"Warning: Could not save agent pool data: {e}")

    def _load_data(self) -> None:
        """Load agent pool data from disk"""
        if not self.persistence_path.exists():
            return

        try:
            with open(self.persistence_path, 'r') as f:
                data = json.load(f)

            # Load agents
            for agent_id, agent_data in data.get("agents", {}).items():
                # Reconstruct enums
                agent_data["specialization"] = Specialization(agent_data["specialization"])
                agent_data["experience_level"] = ExperienceLevel(agent_data["experience_level"])

                agent = Agent(**agent_data)
                self.agents[agent_id] = agent

            # Load ratings
            for agent_id, rating_data in data.get("ratings", {}).items():
                # Reconstruct rating history
                rating_data["rating_history"] = [
                    (datetime.fromisoformat(ts), rating)
                    for ts, rating in rating_data.get("rating_history", [])
                ]

                rating = AgentRating(**rating_data)
                self.ratings[agent_id] = rating

            # Load teams
            for team_id, team_data in data.get("teams", {}).items():
                agents = [
                    self.get_agent(agent_id)
                    for agent_id in team_data["agent_ids"]
                ]
                agents = [a for a in agents if a is not None]  # Filter out missing agents

                if agents:
                    team = Team(
                        id=team_data["id"],
                        name=team_data["name"],
                        agents=agents,
                        strategy=team_data["strategy"],
                        created_at=datetime.fromisoformat(team_data["created_at"])
                    )
                    self.teams[team_id] = team

        except Exception as e:
            print(f"Warning: Could not load agent pool data: {e}")


# Singleton instance
_agent_pool_instance: Optional[AgentPool] = None


def get_agent_pool() -> AgentPool:
    """Get global agent pool instance"""
    global _agent_pool_instance
    if _agent_pool_instance is None:
        _agent_pool_instance = AgentPool()
    return _agent_pool_instance
