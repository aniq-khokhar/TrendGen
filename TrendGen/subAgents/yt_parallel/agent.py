from google.adk.agents import ParallelAgent
from TrendGen.subAgents.yt_scrapper.agent import yt_scrapper
from TrendGen.subAgents.tiktok_scrapper.agent import tiktok_scrapper

yt_parallel = ParallelAgent(
     name="yt_parallel",
     sub_agents=[yt_scrapper, tiktok_scrapper],
     description="Runs two scrapper agents in parallel to gather information."
 )


