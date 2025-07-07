# Generic function to create an A2A server for any ADK agent
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard
)

from src.core.agent_executor import ADKAgentExecutor


def create_agent_a2a_server(
    agent,
    name,
    description,
    skills,
    host="localhost",
    port=10020,
    status_message="Processing request...",
    artifact_name="response"
):
    """Create an A2A server for any ADK agent.

    Args:
        agent: The ADK agent instance
        name: Display name for the agent
        description: Agent description
        skills: List of AgentSkill objects
        host: Server host
        port: Server port
        status_message: Message shown while processing
        artifact_name: Name for response artifacts

    Returns:
        A2AStarletteApplication instance
    """
    # Agent capabilities
    capabilities = AgentCapabilities(streaming=True)

    # Agent card (metadata)
    agent_card = AgentCard(
        name=name,
        description=description,
        url=f"http://{host}:{port}/",
        version="1.0.0",
        defaultInputModes=["text", "text/plain"],
        defaultOutputModes=["text", "text/plain"],
        capabilities=capabilities,
        skills=skills,
    )

    # Create executor with custom parameters
    executor = ADKAgentExecutor(
        agent=agent,
        status_message=status_message,
        artifact_name=artifact_name
    )

    request_handler = DefaultRequestHandler(
        agent_executor=executor,
        task_store=InMemoryTaskStore(),
    )

    # Create A2A application
    return A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler
    )