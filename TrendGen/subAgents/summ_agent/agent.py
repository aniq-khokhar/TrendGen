from google.adk.agents import LlmAgent

summ_agent = LlmAgent(
    name="summ_agent",
    model="gemini-2.0-flash",
    description=(
        "You are an AI agent responsible for summarizing the videos"
    ),
    instruction=(
        """
        
        """
    ),
    output_key="summ_results",
)

