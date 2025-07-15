import asyncio
import threading
import time

from dotenv import load_dotenv
import uvicorn

from src.servers.content_writer_server import create_content_writer_agent_server
from src.servers.content_summarizer_server import create_content_summarizer_agent_server
from src.servers.orchestrator_server import create_orchestrator_agent_server


load_dotenv()
# Global servers to keep references
servers = []


async def run_server_notebook(create_agent_function, port):
    """Run server with proper error handling."""
    try:
        print(f"🚀 Starting agent on port {port}...")
        app = create_agent_function()
        config = uvicorn.Config(
            app.build(),
            host="127.0.0.1",
            port=port,
            log_level="error",
            loop="asyncio"
        )
        server = uvicorn.Server(config)
        servers.append(server)
        await server.serve()
    except Exception as e:
        print(f"Agent error: {e}")


def run_agent_in_background(create_agent_function, port, name):
    """Run an agent server in a background thread."""
    def run() -> None:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            # Create the coroutine inside the new event loop
            loop.run_until_complete(run_server_notebook(create_agent_function, port))
        except Exception as e:
            print(f"{name} error: {e}")

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    return thread


# Start agent servers with corrected function calls
print("Starting agent servers...\n")

trending_thread = run_agent_in_background(create_content_writer_agent_server, 10020, "Content Writer Agent")
analyzer_thread = run_agent_in_background(create_content_summarizer_agent_server, 10021, "Content Summarizer Agent")
host_thread = run_agent_in_background(create_orchestrator_agent_server, 10022, "Orchestrator Agent")

# Wait for servers to start
time.sleep(3)

# Check if threads are alive
if trending_thread.is_alive() and analyzer_thread.is_alive():
    print("\n✅ Agent servers are running!")
    print("   - Trending Agent: http://127.0.0.1:10020")
    print("   - Analyzer Agent: http://127.0.0.1:10021")
    print("   - Host Agent: http://127.0.0.1:10022")
else:
    print("\n❌ Agent servers failed to start. Check the error messages above.")