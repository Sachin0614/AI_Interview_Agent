import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class GroqInterviewEngine:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Add it inside .env file.")

        self.client = Groq(api_key=api_key)
        self.model = "llama-3.1-8b-instant"

    def generate_response(self, system_instruction, user_input, history=None):
        if history is None:
            history = []

        messages = [{"role": "system", "content": system_instruction}]

        for chat in history[-8:]:
            messages.append({"role": "user", "content": chat["user"]})
            messages.append({"role": "assistant", "content": chat["assistant"]})

        messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.6,
            max_tokens=350
        )

        return response.choices[0].message.content.strip()