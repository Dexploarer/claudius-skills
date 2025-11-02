#!/usr/bin/env python3
"""
Populate Agent Pool with Default Agents

Creates 30+ specialized agents across all frameworks and competition types.
"""

from agent_pool import (
    Agent,
    AgentPool,
    ExperienceLevel,
    Specialization
)


def create_default_agents() -> AgentPool:
    """Create and register all default agents"""
    pool = AgentPool()

    # =================================================================
    # SECURITY & BUG HUNTING AGENTS (10 agents)
    # =================================================================

    pool.register_agent(Agent(
        id="scanner-alpha",
        name="Pattern Scanner Alpha",
        specialization=Specialization.AUTOMATED_SCANNING,
        skills=["sql_injection", "xss", "command_injection", "path_traversal",
                "hardcoded_secrets", "csrf"],
        framework_compatibility=["bug-hunting", "security-audit", "code-review"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1650,
        description="Fast pattern-based vulnerability scanner using regex and static analysis",
        strengths=["Speed", "Coverage", "Known vulnerability patterns"],
        weaknesses=["Business logic flaws", "Complex vulnerabilities", "False positives"],
        cost=1
    ))

    pool.register_agent(Agent(
        id="reviewer-beta",
        name="Logic Reviewer Beta",
        specialization=Specialization.MANUAL_REVIEW,
        skills=["business_logic", "auth_bypass", "privilege_escalation", "idor",
                "session_management", "crypto_issues"],
        framework_compatibility=["bug-hunting", "security-audit", "code-review"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1820,
        description="Deep manual code reviewer specializing in complex logic flaws",
        strengths=["Critical bugs", "Business logic", "Low false positives"],
        weaknesses=["Speed", "Coverage", "Resource intensive"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="fuzzer-gamma",
        name="Fuzzer Gamma",
        specialization=Specialization.FUZZING,
        skills=["race_conditions", "buffer_overflow", "integer_overflow",
                "dos_vulnerabilities", "edge_cases", "memory_leaks"],
        framework_compatibility=["bug-hunting", "security-audit"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1720,
        description="Input fuzzing and behavioral analysis specialist",
        strengths=["Edge cases", "Race conditions", "Crash detection"],
        weaknesses=["Code coverage", "Business logic", "Slow execution"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="ml-detector-delta",
        name="ML Detector Delta",
        specialization=Specialization.ML_DETECTION,
        skills=["anomaly_detection", "pattern_learning", "vulnerability_prediction",
                "code_similarity", "zero_day_detection"],
        framework_compatibility=["bug-hunting", "security-audit", "code-quality"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1780,
        description="Machine learning-based vulnerability detection using trained models",
        strengths=["Novel vulnerabilities", "Pattern learning", "Adaptation"],
        weaknesses=["Training data requirements", "Explainability", "False positives"],
        cost=3
    ))

    pool.register_agent(Agent(
        id="crypto-analyst-epsilon",
        name="Crypto Analyst Epsilon",
        specialization=Specialization.CRYPTO_ANALYSIS,
        skills=["weak_crypto", "key_management", "cert_validation",
                "random_number_gen", "encryption_issues"],
        framework_compatibility=["bug-hunting", "security-audit"],
        experience_level=ExperienceLevel.MASTER,
        elo_rating=1850,
        description="Cryptography and encryption specialist",
        strengths=["Crypto vulnerabilities", "Deep expertise", "High severity bugs"],
        weaknesses=["Narrow focus", "Limited scope", "Specialized"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="api-security-zeta",
        name="API Security Zeta",
        specialization=Specialization.MANUAL_REVIEW,
        skills=["api_auth", "rate_limiting", "api_injection", "graphql_security",
                "rest_security", "jwt_issues"],
        framework_compatibility=["bug-hunting", "security-audit", "api-design"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1700,
        description="API security specialist (REST, GraphQL, gRPC)",
        strengths=["API vulnerabilities", "Authentication", "Authorization"],
        weaknesses=["Non-API code", "Frontend issues"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="web-scanner-eta",
        name="Web Scanner Eta",
        specialization=Specialization.AUTOMATED_SCANNING,
        skills=["xss", "csrf", "clickjacking", "cors_misconfiguration",
                "csp_bypass", "open_redirect"],
        framework_compatibility=["bug-hunting", "security-audit"],
        experience_level=ExperienceLevel.INTERMEDIATE,
        elo_rating=1600,
        description="Frontend and web vulnerability scanner",
        strengths=["Web vulnerabilities", "Client-side issues", "Fast"],
        weaknesses=["Backend logic", "Database issues"],
        cost=1
    ))

    pool.register_agent(Agent(
        id="mobile-security-theta",
        name="Mobile Security Theta",
        specialization=Specialization.MANUAL_REVIEW,
        skills=["mobile_crypto", "insecure_storage", "deeplink_exploits",
                "mobile_injection", "certificate_pinning"],
        framework_compatibility=["bug-hunting", "security-audit"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1680,
        description="Mobile app security specialist (iOS, Android)",
        strengths=["Mobile platforms", "App security", "Platform-specific"],
        weaknesses=["Web applications", "Backend services"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="infra-hardener-iota",
        name="Infrastructure Hardener Iota",
        specialization=Specialization.AUTOMATED_SCANNING,
        skills=["misconfiguration", "exposed_services", "default_credentials",
                "security_headers", "tls_config"],
        framework_compatibility=["bug-hunting", "security-audit", "devops-efficiency"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1640,
        description="Infrastructure and configuration security specialist",
        strengths=["Misconfigurations", "Infrastructure", "Quick wins"],
        weaknesses=["Application logic", "Custom code"],
        cost=1
    ))

    pool.register_agent(Agent(
        id="compliance-checker-kappa",
        name="Compliance Checker Kappa",
        specialization=Specialization.MANUAL_REVIEW,
        skills=["gdpr_compliance", "pci_dss", "hipaa", "sox",
                "data_protection", "privacy_issues"],
        framework_compatibility=["bug-hunting", "security-audit", "code-review"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1750,
        description="Security compliance and privacy specialist",
        strengths=["Compliance", "Privacy", "Regulations"],
        weaknesses=["Technical exploits", "Performance"],
        cost=2
    ))

    # =================================================================
    # PERFORMANCE OPTIMIZATION AGENTS (6 agents)
    # =================================================================

    pool.register_agent(Agent(
        id="frontend-speedster-lambda",
        name="Frontend Speedster Lambda",
        specialization=Specialization.FRONTEND_OPTIMIZATION,
        skills=["bundle_optimization", "lazy_loading", "code_splitting",
                "render_optimization", "critical_css", "image_optimization"],
        framework_compatibility=["performance-optimization", "code-quality", "user-flows"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1790,
        description="Frontend performance optimization specialist",
        strengths=["Load time", "Bundle size", "Rendering"],
        weaknesses=["Backend performance", "Database optimization"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="backend-throughput-mu",
        name="Backend Throughput Mu",
        specialization=Specialization.BACKEND_OPTIMIZATION,
        skills=["query_optimization", "caching_strategies", "async_processing",
                "load_balancing", "connection_pooling", "api_optimization"],
        framework_compatibility=["performance-optimization", "code-quality", "api-design"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1740,
        description="Backend and API performance specialist",
        strengths=["Throughput", "Scalability", "API performance"],
        weaknesses=["Frontend issues", "UI optimization"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="db-tuner-nu",
        name="Database Tuner Nu",
        specialization=Specialization.DATABASE_TUNING,
        skills=["index_optimization", "query_planning", "normalization",
                "denormalization", "partitioning", "replication"],
        framework_compatibility=["performance-optimization", "database-schema", "code-quality"],
        experience_level=ExperienceLevel.MASTER,
        elo_rating=1830,
        description="Database performance and optimization expert",
        strengths=["Query performance", "Index design", "Scalability"],
        weaknesses=["Application code", "Frontend"],
        cost=3
    ))

    pool.register_agent(Agent(
        id="algorithm-optimizer-xi",
        name="Algorithm Optimizer Xi",
        specialization=Specialization.ALGORITHM_OPTIMIZATION,
        skills=["big_o_analysis", "data_structure_selection", "algorithm_design",
                "complexity_reduction", "parallel_algorithms"],
        framework_compatibility=["performance-optimization", "code-quality"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1810,
        description="Algorithm and data structure optimization specialist",
        strengths=["Algorithmic complexity", "Data structures", "Big-O improvements"],
        weaknesses=["Infrastructure", "Configuration"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="network-wizard-omicron",
        name="Network Wizard Omicron",
        specialization=Specialization.NETWORK_OPTIMIZATION,
        skills=["cdn_optimization", "http2_tuning", "compression",
                "prefetching", "dns_optimization", "connection_reuse"],
        framework_compatibility=["performance-optimization", "devops-efficiency"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1700,
        description="Network and delivery optimization specialist",
        strengths=["Network performance", "CDN", "HTTP optimization"],
        weaknesses=["Application logic", "Database"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="memory-guardian-pi",
        name="Memory Guardian Pi",
        specialization=Specialization.BACKEND_OPTIMIZATION,
        skills=["memory_leak_detection", "gc_optimization", "memory_profiling",
                "allocation_optimization", "heap_analysis"],
        framework_compatibility=["performance-optimization", "code-quality"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1720,
        description="Memory usage and leak detection specialist",
        strengths=["Memory leaks", "GC optimization", "Memory profiling"],
        weaknesses=["CPU optimization", "Network"],
        cost=2
    ))

    # =================================================================
    # ARCHITECTURE DESIGN AGENTS (5 agents)
    # =================================================================

    pool.register_agent(Agent(
        id="microservices-architect-rho",
        name="Microservices Architect Rho",
        specialization=Specialization.MICROSERVICES_DESIGN,
        skills=["service_decomposition", "api_gateway", "service_mesh",
                "distributed_tracing", "circuit_breaker", "saga_pattern"],
        framework_compatibility=["architecture-design", "api-design", "devops-efficiency"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1800,
        description="Microservices architecture and distributed systems expert",
        strengths=["Scalability", "Service design", "Distributed systems"],
        weaknesses=["Monoliths", "Simple architectures"],
        cost=3
    ))

    pool.register_agent(Agent(
        id="monolith-modernizer-sigma",
        name="Monolith Modernizer Sigma",
        specialization=Specialization.MONOLITH_DESIGN,
        skills=["modular_monolith", "clean_architecture", "domain_driven_design",
                "layered_architecture", "dependency_management"],
        framework_compatibility=["architecture-design", "code-quality"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1740,
        description="Monolithic architecture and modularization specialist",
        strengths=["Simplicity", "Modularity", "Maintainability"],
        weaknesses=["Extreme scale", "Distributed systems"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="event-driven-tau",
        name="Event-Driven Designer Tau",
        specialization=Specialization.EVENT_DRIVEN_DESIGN,
        skills=["event_sourcing", "cqrs", "message_queues", "event_streaming",
                "eventual_consistency", "choreography"],
        framework_compatibility=["architecture-design", "api-design"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1820,
        description="Event-driven architecture and messaging specialist",
        strengths=["Async processing", "Event sourcing", "Decoupling"],
        weaknesses=["Synchronous systems", "Simple CRUD"],
        cost=3
    ))

    pool.register_agent(Agent(
        id="serverless-optimizer-upsilon",
        name="Serverless Optimizer Upsilon",
        specialization=Specialization.SERVERLESS_DESIGN,
        skills=["faas_design", "serverless_patterns", "cold_start_optimization",
                "cost_optimization", "event_triggers", "managed_services"],
        framework_compatibility=["architecture-design", "devops-efficiency", "performance-optimization"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1760,
        description="Serverless and FaaS architecture specialist",
        strengths=["Cost efficiency", "Scalability", "Managed services"],
        weaknesses=["Stateful systems", "Long-running processes"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="hybrid-strategist-phi",
        name="Hybrid Strategist Phi",
        specialization=Specialization.MICROSERVICES_DESIGN,
        skills=["architecture_tradeoffs", "pragmatic_design", "migration_strategies",
                "polyglot_architecture", "best_of_breed"],
        framework_compatibility=["architecture-design"],
        experience_level=ExperienceLevel.MASTER,
        elo_rating=1850,
        description="Pragmatic architecture strategist balancing all approaches",
        strengths=["Tradeoff analysis", "Pragmatism", "Migration planning"],
        weaknesses=["Purist approaches"],
        cost=3
    ))

    # =================================================================
    # API DESIGN AGENTS (4 agents)
    # =================================================================

    pool.register_agent(Agent(
        id="rest-purist-chi",
        name="REST Purist Chi",
        specialization=Specialization.REST_DESIGN,
        skills=["restful_design", "hateoas", "resource_modeling",
                "http_semantics", "versioning", "pagination"],
        framework_compatibility=["api-design", "architecture-design"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1770,
        description="RESTful API design expert following Richardson maturity model",
        strengths=["REST principles", "HTTP semantics", "Resource design"],
        weaknesses=["Real-time", "Complex queries"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="graphql-innovator-psi",
        name="GraphQL Innovator Psi",
        specialization=Specialization.GRAPHQL_DESIGN,
        skills=["schema_design", "resolver_optimization", "federation",
                "subscription_design", "n_plus_one_prevention", "dataloader"],
        framework_compatibility=["api-design", "architecture-design", "performance-optimization"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1800,
        description="GraphQL schema design and optimization specialist",
        strengths=["Flexible queries", "Schema design", "Real-time"],
        weaknesses=["Simple APIs", "Caching complexity"],
        cost=3
    ))

    pool.register_agent(Agent(
        id="grpc-performer-omega",
        name="gRPC Performer Omega",
        specialization=Specialization.GRPC_DESIGN,
        skills=["protobuf_schema", "streaming_rpc", "service_definition",
                "load_balancing", "interceptors", "performance"],
        framework_compatibility=["api-design", "performance-optimization"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1750,
        description="High-performance gRPC and protobuf specialist",
        strengths=["Performance", "Streaming", "Strong typing"],
        weaknesses=["Browser support", "Human readability"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="api-pragmatist-alpha-prime",
        name="API Pragmatist Alpha Prime",
        specialization=Specialization.REST_DESIGN,
        skills=["hybrid_api_design", "practical_patterns", "developer_experience",
                "api_documentation", "sdk_design", "error_handling"],
        framework_compatibility=["api-design", "documentation-quality"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1730,
        description="Pragmatic API designer focusing on developer experience",
        strengths=["Developer experience", "Practicality", "Documentation"],
        weaknesses=["Theoretical purity"],
        cost=2
    ))

    # =================================================================
    # CODE QUALITY AGENTS (5 agents)
    # =================================================================

    pool.register_agent(Agent(
        id="code-reviewer-beta-prime",
        name="Code Reviewer Beta Prime",
        specialization=Specialization.CODE_REVIEW,
        skills=["code_smell_detection", "design_patterns", "solid_principles",
                "clean_code", "refactoring_suggestions", "naming_conventions"],
        framework_compatibility=["code-review", "code-quality"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1790,
        description="Comprehensive code review and clean code specialist",
        strengths=["Code quality", "Best practices", "Refactoring"],
        weaknesses=["Performance", "Security"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="test-strategist-gamma-prime",
        name="Test Strategist Gamma Prime",
        specialization=Specialization.TEST_STRATEGY,
        skills=["test_pyramid", "unit_testing", "integration_testing",
                "e2e_testing", "property_based_testing", "mutation_testing"],
        framework_compatibility=["test-strategy", "code-quality"],
        experience_level=ExperienceLevel.EXPERT,
        elo_rating=1810,
        description="Comprehensive test strategy and coverage specialist",
        strengths=["Test coverage", "Strategy", "Quality assurance"],
        weaknesses=["Performance testing", "Load testing"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="doc-writer-delta-prime",
        name="Documentation Writer Delta Prime",
        specialization=Specialization.DOCUMENTATION,
        skills=["api_documentation", "code_comments", "tutorials",
                "examples", "architecture_docs", "readme_creation"],
        framework_compatibility=["documentation-quality", "code-quality"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1740,
        description="Technical documentation and tutorial specialist",
        strengths=["Documentation", "Clarity", "Examples"],
        weaknesses=["Code implementation", "Performance"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="maintainability-epsilon-prime",
        name="Maintainability Engineer Epsilon Prime",
        specialization=Specialization.MAINTAINABILITY,
        skills=["complexity_metrics", "coupling_analysis", "cohesion_analysis",
                "dependency_management", "technical_debt", "modularity"],
        framework_compatibility=["code-quality", "architecture-design"],
        experience_level=ExperienceLevel.ADVANCED,
        elo_rating=1760,
        description="Code maintainability and technical debt specialist",
        strengths=["Maintainability", "Metrics", "Technical debt"],
        weaknesses=["Rapid prototyping", "Performance"],
        cost=2
    ))

    pool.register_agent(Agent(
        id="style-enforcer-zeta-prime",
        name="Style Enforcer Zeta Prime",
        specialization=Specialization.CODE_REVIEW,
        skills=["linting", "code_formatting", "naming_conventions",
                "style_guides", "consistency_checking", "automated_fixes"],
        framework_compatibility=["code-quality", "code-review"],
        experience_level=ExperienceLevel.INTERMEDIATE,
        elo_rating=1650,
        description="Code style and consistency enforcement specialist",
        strengths=["Consistency", "Style", "Automation"],
        weaknesses=["Architecture", "Complex logic"],
        cost=1
    ))

    print(f"✓ Registered {len(pool.agents)} agents")
    print(f"✓ Frameworks covered: {len(set(fw for agent in pool.agents.values() for fw in agent.framework_compatibility))}")
    print(f"✓ Specializations: {len(set(agent.specialization for agent in pool.agents.values()))}")

    return pool


if __name__ == "__main__":
    pool = create_default_agents()

    # Display summary
    print("\n" + "="*60)
    print("AGENT POOL SUMMARY")
    print("="*60)

    # Group by specialization
    from collections import defaultdict
    by_spec = defaultdict(list)
    for agent in pool.agents.values():
        by_spec[agent.specialization].append(agent)

    for spec, agents in sorted(by_spec.items()):
        print(f"\n{spec.value.replace('_', ' ').title()}: ({len(agents)})")
        for agent in sorted(agents, key=lambda a: a.elo_rating, reverse=True):
            print(f"  • {agent.name} (ELO: {agent.elo_rating})")

    print("\n" + "="*60)
    print(f"Total Agents: {len(pool.agents)}")
    print(f"Average ELO: {sum(a.elo_rating for a in pool.agents.values()) / len(pool.agents):.0f}")
    print("="*60)
