/**
 * Agent Pool Management System
 *
 * Manages all available agents across frameworks, enabling flexible team composition,
 * recommendations, and roster management.
 */

import * as fs from 'fs';
import * as path from 'path';

export enum ExperienceLevel {
  NOVICE = 1,
  BEGINNER = 2,
  INTERMEDIATE = 3,
  ADVANCED = 4,
  EXPERT = 5,
  MASTER = 6,
  GRANDMASTER = 7,
  LEGEND = 8,
  MYTHIC = 9,
  GODLIKE = 10,
}

export enum Specialization {
  // Security
  AUTOMATED_SCANNING = 'automated_scanning',
  MANUAL_REVIEW = 'manual_review',
  FUZZING = 'fuzzing',
  ML_DETECTION = 'ml_detection',

  // Performance
  FRONTEND_OPTIMIZATION = 'frontend_optimization',
  BACKEND_OPTIMIZATION = 'backend_optimization',
  DATABASE_TUNING = 'database_tuning',

  // Architecture
  MICROSERVICES_DESIGN = 'microservices_design',
  EVENT_DRIVEN_DESIGN = 'event_driven_design',

  // Quality
  CODE_REVIEW = 'code_review',
  TEST_STRATEGY = 'test_strategy',
  DOCUMENTATION = 'documentation',
}

export interface Agent {
  id: string;
  name: string;
  specialization: Specialization;
  skills: string[];
  framework_compatibility: string[];
  experience_level: ExperienceLevel;
  win_rate: number;
  elo_rating: number;
  games_played: number;
  description: string;
  strengths: string[];
  weaknesses: string[];
  cost: number;
}

export interface Team {
  id: string;
  name: string;
  agents: Agent[];
  strategy: string;
  created_at: Date;
}

export class AgentPool {
  private agents: Map<string, Agent> = new Map();
  private teams: Map<string, Team> = new Map();
  private persistence_path: string;

  constructor(persistence_path: string = './persistence/agent_pool.json') {
    this.persistence_path = persistence_path;
    this._load_data();
  }

  public register_agent(agent: Agent): void {
    this.agents.set(agent.id, agent);
    this._save_data();
  }

  public get_agent(agent_id: string): Agent | null {
    return this.agents.get(agent_id) || null;
  }

  public list_agents(
    framework?: string,
    specialization?: Specialization,
    min_experience?: ExperienceLevel
  ): Agent[] {
    let agents = Array.from(this.agents.values());

    if (framework) {
      agents = agents.filter(a => a.framework_compatibility.includes(framework));
    }

    if (specialization) {
      agents = agents.filter(a => a.specialization === specialization);
    }

    if (min_experience) {
      agents = agents.filter(a => a.experience_level >= min_experience);
    }

    return agents.sort((a, b) => b.elo_rating - a.elo_rating);
  }

  public create_team(name: string, agent_ids: string[], strategy: string = 'custom'): Team {
    const agents: Agent[] = [];
    for (const agent_id of agent_ids) {
      const agent = this.get_agent(agent_id);
      if (!agent) {
        throw new Error(`Agent '${agent_id}' not found`);
      }
      agents.push(agent);
    }

    const team: Team = {
      id: `team_${new Date().toISOString().replace(/[:.]/g, '-').slice(0, -5)}`,
      name,
      agents,
      strategy,
      created_at: new Date(),
    };

    this.teams.set(team.id, team);
    this._save_data();

    return team;
  }

  public get_leaderboard(framework?: string, limit: number = 20): Array<[number, Agent]> {
    const agents = this.list_agents(framework);
    return agents.slice(0, limit).map((agent, index) => [index + 1, agent]);
  }

  private _save_data(): void {
    try {
      const dir = path.dirname(this.persistence_path);
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }

      const data = {
        agents: Object.fromEntries(this.agents),
        teams: Object.fromEntries(
          Array.from(this.teams.entries()).map(([id, team]) => [
            id,
            {
              ...team,
              agent_ids: team.agents.map(a => a.id),
              created_at: team.created_at.toISOString(),
            },
          ])
        ),
      };

      fs.writeFileSync(this.persistence_path, JSON.stringify(data, null, 2));
    } catch (error) {
      console.warn('Could not save agent pool data:', error);
    }
  }

  private _load_data(): void {
    if (!fs.existsSync(this.persistence_path)) {
      return;
    }

    try {
      const data = JSON.parse(fs.readFileSync(this.persistence_path, 'utf-8'));

      // Load agents
      if (data.agents) {
        for (const [agent_id, agent_data] of Object.entries(data.agents)) {
          this.agents.set(agent_id, agent_data as Agent);
        }
      }

      // Load teams
      if (data.teams) {
        for (const [team_id, team_data] of Object.entries(data.teams as any)) {
          const agents = team_data.agent_ids
            .map((id: string) => this.get_agent(id))
            .filter((a: Agent | null): a is Agent => a !== null);

          if (agents.length > 0) {
            this.teams.set(team_id, {
              id: team_data.id,
              name: team_data.name,
              agents,
              strategy: team_data.strategy,
              created_at: new Date(team_data.created_at),
            });
          }
        }
      }
    } catch (error) {
      console.warn('Could not load agent pool data:', error);
    }
  }
}

// Singleton instance
let _agent_pool_instance: AgentPool | null = null;

export function get_agent_pool(): AgentPool {
  if (_agent_pool_instance === null) {
    _agent_pool_instance = new AgentPool();
  }
  return _agent_pool_instance;
}
