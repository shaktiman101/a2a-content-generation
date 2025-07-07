from a2a.types import AgentSkill   

from src.agents.content_writer_agent import content_writer_agent
from src.core.server_wrapper import create_agent_a2a_server

def create_content_writer_agent_server(host="localhost", port=10020):
    """Create A2A server for Trending Agent using the unified wrapper."""
    return create_agent_a2a_server(
        agent=content_writer_agent,
        name="Trending Topics Agent",
        description="Searches the web for current trending topics from social media",
        skills=[
            AgentSkill(
                id="find_trends",
                name="Find Trending Topics",
                description="Searches for current trending topics on social media",
                tags=["trends", "social media", "twitter", "current events"],
                examples=[
                    "What's trending today?",
                    "Show me current Twitter trends",
                    "What are people talking about on social media?",
                ],
            )
        ],
        host=host,
        port=port,
        status_message="Generating content for user query...",
        artifact_name="content_generation"
    )