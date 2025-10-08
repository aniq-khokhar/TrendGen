from google.adk.agents import LlmAgent

merge_agent = LlmAgent(
    name="merge_agent",
    model="gemini-2.0-flash",
    description=(
        "You are an AI assistant responsible for combining the scrapper results into structured format."
    ),
    instruction=(
        """
        You are a Merge Scrapper Agent responsible for combining the outputs from the YouTube Scrapper Agent and the TikTok Scrapper Agent into a single structured JSON response.

        INPUT: 
        
        Youtube Scrapper:
        {yt_results},
        
        Tiktok Scrapper:
        {tik_results}
        
        **BEHAVIOR:**

        -> Validate that both yt_results and tik_results are provided and contain valid lists of videos.

        -> Merge these two responses into one single combined list.
        
        -> Extract only the url values from all videos across both sources.
        
        -> Do not add any data on your own. Only use the data provided in the inputs.
        
        -> Return the merged URLs as a unified .json list.
        
        **OUTPUT FORMAT:**

        -> The final output must be in .json format as follows:
        
        [
            "<video_url>",
            "<video_url>",
            "<video_url>"
        ]
        
        """
    ),
    output_key="merge_results",
)

