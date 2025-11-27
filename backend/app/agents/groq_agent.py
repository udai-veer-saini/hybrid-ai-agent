# backend/app/agents/groq_agent.py
import os
from groq import Groq
from app.models.chat_models import ChatResponse

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are the LLM brain of the Hybrid AI Agent.

Rules:
1. Answer general questions normally.
2. When the user mentions system diagnostics, CPU, RAM, performance, temperature, etc,
   tell them: "The system agent will handle diagnostics."
3. When the user mentions renaming, deleting, moving or working with files/folders,
   tell them: "The automation agent will process file operations."
4. Do NOT pretend you can run system or file operations.
5. Keep answers concise, technical when needed, and clean.
"""

def groq_agent_handler(user_input: str) -> ChatResponse:
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
            temperature=0.3,
            max_tokens=500,
        )
        reply = completion.choices[0].message.content
        return ChatResponse(reply=reply)

    except Exception as e:
        return ChatResponse(reply=f"Groq API error: {e}")
