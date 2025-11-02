"""
Core infrastructure for Competitive AI Frameworks v2.0

This module provides the foundational systems for the expanded framework:
- Agent pool management and roster system
- Team composition and recommendations
- Tournament orchestration
- ELO rating system
- League and season management
"""

from .agent_pool import (
    Agent,
    AgentRating,
    Team,
    AgentPool,
    ExperienceLevel,
    Specialization,
    get_agent_pool
)

__all__ = [
    "Agent",
    "AgentRating",
    "Team",
    "AgentPool",
    "ExperienceLevel",
    "Specialization",
    "get_agent_pool"
]
