from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY")) #

def summarize_news(text):
    if not text or not text.strip():
        return "No content available to analyze."

    # Upgraded prompt for Truth Auditing and Bias Detection
    prompt = f"""
    Act as a Neutral News Auditor. Analyze this text:
    1. Provide a 3-line objective summary.
    2. Identify 'Loaded Words' or emotional bias.
    3. Highlight any conflicting facts or missing data.

    News Text:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", #
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
