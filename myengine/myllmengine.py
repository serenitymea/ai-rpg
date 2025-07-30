"""
работа с ИИ
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

class LLMEngine:
    def get_response(self, prompt: str) -> str:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
        )
        return response.choices[0].message.content.strip()
