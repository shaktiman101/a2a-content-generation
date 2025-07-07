from a2a.types import AgentSkill    
    
from src.agents.content_summarizer_agent import content_summarizer_agent
from src.core.server_wrapper import create_agent_a2a_server


def create_content_summarizer_agent_server(host="localhost", port=10021):
    """Create A2A server for Analyzer Agent using the unified wrapper."""
    return create_agent_a2a_server(
        agent=content_summarizer_agent,
        name="Content Summarizer Agent",
        description="Performs deep analysis of trends with quantitative data",
        skills=[
            AgentSkill(
                id="summarize_content",
                name="Summarize Content",
                description="Provides a detailed summary of the content",
                tags=["analysis", "data", "metrics", "statistics"],
                examples=[
                    "Analyze the #ClimateChange trend",
                    "Get metrics for the Taylor Swift trend",
                    "Provide data analysis for AI adoption trend",
                ],
            )
        ],
        host=host,
        port=port,
        status_message="Generating summary of the data...",
        artifact_name="content_summary"
    )