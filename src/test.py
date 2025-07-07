from src.core.tool_client import a2a_client


a2a_client.add_remote_agent("http://localhost:10020")
a2a_client.add_remote_agent("http://localhost:10021")


def list_remote_agents():
    """List all registered remote agents."""
    print("Registered remote agents:")
    remote_agents = a2a_client.list_remote_agents()
    for k, v in remote_agents.items():
        print(f"Remote agent url: {k}")
        print(f"Remote agent name: {v['name']}")
        print(f"Remote agent skills: {v['skills']}")
        print(f"Remote agent version: {v['version']}")
        print("----\n")
    
    
def test_content_writer_agent(query: str):
    """Test the content writer agent by querying trending topics."""
    content_writer_res = a2a_client.create_task("http://localhost:10020", query)
    print(content_writer_res)


def test_content_summarizer_agent(query: str):
    """Test the content summarizer agent by analyzing trends."""
    content_summarizer_res = a2a_client.create_task("http://localhost:10021", query)
    print(content_summarizer_res)


def test_orchestrator_agent(query: str):
    """Test the orchestrator agent by performing a comprehensive trend analysis."""
    response = a2a_client.create_task("http://localhost:10022", query)
    print(response)


if __name__ == "__main__":
    list_remote_agents()
    query = input("query: ")
    test_orchestrator_agent(query)
    