from google.adk.agents import LlmAgent
from TrendGen.tools.summ_down import summ_down

one_sum_agent = LlmAgent(
    name="one_sum_agent",
    model="gemini-2.0-flash",
    description=(
        ""
    ),
    instruction=(
        """
        
        """
    ),
    tools=[],
    output_key="one_sum_results",
)

