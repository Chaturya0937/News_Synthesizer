from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_news(text):
    if not text or not text.strip():
        return "No content available to summarize."

    prompt = f"""
    Summarize the following news article in 4–5 simple lines.
    Use clear, non-technical language.

    News:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=200
    )

    return response.choices[0].message.content.strip()
