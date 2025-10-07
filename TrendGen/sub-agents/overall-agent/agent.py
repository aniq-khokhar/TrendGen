from google.adk.agents import SequentialAgent


root_agent = SequentialAgent(
    name="overall-agent",
    sub_agents=[],
    description="Executes a sequence of code writing, reviewing, and refactoring.",
    # The agents will run in the order provided: Writer -> Reviewer -> Refactorer
)