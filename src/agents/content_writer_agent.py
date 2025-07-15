from google.adk.agents import Agent
from google.adk.tools import google_search


# Create the Trending Topics ADK Agent
content_writer_agent = Agent(
    model="gemini-2.0-flash",
    name="content_writer_agent",
    instruction="""
    You are a content writer. Your job is to search the web for topics or points around user request.,

    When asked to write a content about a topic:
    1. Search for the "topic" or similar queries
    2. Extract top 3 data points around given topic

    Focus on topics relevant to the user's request and ensure the content is engaging and informative.
    """,
    tools=[google_search],
)

print("Content Writer Agent created successfully!")