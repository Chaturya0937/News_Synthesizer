import asyncio
import os
from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv

load_dotenv()

async def run_scout(topic):
    # Using gemini-2.0-flash for 2026 stable browser-use support
    llm = ChatGoogle(model='gemini-2.0-flash') 

    instruction = (
        f"Go to eenadu.net and sakshi.com. Search for news about '{topic}'. "
        "Extract the main headline and the lead paragraph from both. "
        "If a PIB.gov.in link is found for this topic, extract its content for verification."
    )

    agent = Agent(task=instruction, llm=llm)
    
    print(f"🚀 Scout Agent starting for: {topic}...")
    result = await agent.run()
    return result

if __name__ == "__main__":
    asyncio.run(run_scout("Andhra Pradesh Budget"))
    
