from a2a.types import AgentSkill   

from src.core.server_wrapper import create_agent_a2a_server
from src.agents.orchestrator_agent import orchestrator_agent


def create_orchestrator_agent_server(host="localhost", port=10022):
    """Create A2A server for Host Agent using the unified wrapper."""
    return create_agent_a2a_server(
        agent=orchestrator_agent,
        name="Orchestrator Agent",
        description="Orchestrates content creation using specialized agents",
        skills=[
            AgentSkill(
                id="comprehensive_trend_analysis",
                name="Comprehensive Trend Analysis",
                description="Finds trending topics and provides deep analysis of the most relevant one",
                tags=["trends", "analysis", "orchestration", "insights"],
                examples=[
                    "Analyze current trends",
                    "What's trending and why is it important?",
                    "Give me a comprehensive trend report",
                ],
            )
        ],
        host=host,
        port=port,
        status_message="Orchestrating content generation...",
        artifact_name="topic_content"
)
