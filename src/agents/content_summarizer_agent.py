from google.adk.agents import Agent
from google.adk.tools import google_search


# Create the Trend Analyzer ADK Agent
content_summarizer_agent = Agent(
    model="gemini-2.0-flash",
    name="content_summarizer_agent",
    instruction="""
    You are a content summarizer specializing in summarizing content. When given a article or content,
    summarize the content highlighting it's main points.
    """,
    # tools=[google_search],
)

print("Content Summarizer Agent created successfully!")