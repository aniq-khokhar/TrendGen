from google.adk.agents import LlmAgent
from TrendGen.tools.summ_down import summ_down

summ_agent = LlmAgent(
    name="summ_agent",
    model="gemini-2.0-flash",
    description=(
        "You are an AI agent responsible for summarizing the videos"
    ),
    instruction=(
        """
        You are a Video Summary Agent responsible for summarizing the content of videos provided as a list of URLs.

        **INPUT FORMAT:**
        
        You will receive input in the following structure:
        
        Marged Results:
        {merge_results}
        
        **BEHAVIOR:**
        
        -> Validate that merge_results is provided and contains a list of valid video URLs.
        
        -> You have access to the summ_down tool.
        
        -> The summ_down tool accepts a list of URLs as input, downloads the corresponding videos, and generates structured summaries for each.
        
        -> Call the summ_down tool using the provided list of URLs.
        
        -> Retrieve and return the summarized data for each video.
        
        -> Do not add or modify any data on your own. Only use the results returned by the tool.
        
        **OUTPUT FORMAT:**
        
        The final output must be in .json format as follows:
        [
        {
        "url": "https://www.youtube.com/shorts/rqLEUxeOQWo",
        "analysis": {
        "viral_ingredients": [
        "fast-paced editing",
        "surprise twist",
        "emotional payoff",
        "relatable scenario"
        ],
        "video_hooks": [
        "starts with a question",
        "cut-to-reaction style",
        "unexpected reveal"
        ],
        "hook_pattern": "Opens with curiosity bait followed by a quick emotional twist and satisfying payoff.",
        "summary": "A short clip showing a man attempting a difficult challenge multiple times before finally succeeding, ending with an emotional or humorous twist.",
        "storytelling_blueprint": {
        "genre": "motivational short",
        "theme": "perseverance pays off",
        "target_emotion": "inspiration",
        "pov": "first-person",
        "setting": "indoor training area",
        "characters": ["main protagonist", "supportive friend"],
        "conflict": "repeated failure and frustration",
        "escalating_stakes": "time pressure and increasing tension",
        "payoff": "final success and joyful reaction"
        }
        }
        },
        {
        "url": "https://www.tiktok.com/@funnyclips/video/748392910293",
        "analysis": {
        "viral_ingredients": [
        "unexpected humor",
        "facial expressions",
        "relatable moment"
        ],
        "video_hooks": [
        "opens mid-action",
        "uses sound effect for punchline"
        ],
        "hook_pattern": "Jump-cut humor style — starts with chaos and ends with an ironic punchline.",
        "summary": "A pet owner tries to film a calm video, but their dog suddenly jumps into the frame, creating an unplanned hilarious moment.",
        "storytelling_blueprint": {
        "genre": "comedy",
        "theme": "chaotic fun",
        "target_emotion": "laughter",
        "pov": "third-person camera view",
        "setting": "living room",
        "characters": ["owner", "dog"],
        "conflict": "unexpected interruption ruins the perfect take",
        "escalating_stakes": "pet keeps causing more chaos",
        "payoff": "funny ending as both laugh and give up filming"
        }
        }
        }
        ]
        """
    ),
    tools=[summ_down],
    output_key="summ_results",
)

