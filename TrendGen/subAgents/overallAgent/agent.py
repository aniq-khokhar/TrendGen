from google.adk.agents import SequentialAgent
from TrendGen.subAgents.google_scrap.agent import google_scrap
from TrendGen.subAgents.yt_parallel.agent import yt_parallel
from TrendGen.subAgents.merge_agent.agent import merge_agent

overallAgent = SequentialAgent(
    name="overallAgent",
    sub_agents=[google_scrap, yt_parallel, merge_agent],
    description="Executes a sequence of google_scrap to yt_paraller for analysis",
    # The agents will run in the order provided: Writer -> Reviewer -> Refactorer
)