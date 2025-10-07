from google.adk.agents import SequentialAgent
from TrendGen.subAgents.google_scrap.agent import google_scrap


overallAgent = SequentialAgent(
    name="overallAgent",
    sub_agents=[google_scrap],
    description="Executes a sequence of code writing, reviewing, and refactoring.",
    # The agents will run in the order provided: Writer -> Reviewer -> Refactorer
)