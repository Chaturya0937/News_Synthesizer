import asyncio
from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv

load_dotenv()

async def run_scout(topic):
    # Using the 2.0-flash model for 2026 stability
    llm = ChatGoogle(model='gemini-2.0-flash') 

    instruction = (
        f"Go to eenadu.net and sakshi.com. Search for news about '{topic}'. "
        "Extract the main headline and the lead paragraph from both sources."
    )

    agent = Agent(task=instruction, llm=llm)
    
    print(f"🚀 Scout Agent is starting for: {topic}...")
    result = await agent.run()
    return result

if __name__ == "__main__":
    asyncio.run(run_scout("Andhra Pradesh Budget"))
