from dotenv import load_dotenv
from typing import Final
import os

load_dotenv()

GROQ_API_KEY : Final[str] = os.getenv("GROQ_API_KEY")
HF_TOKEN: Final[str] = os.getenv("HF_TOKEN")
SYSTEM_PROMPT : Final[str] = """
    You're a helpful assistant that only gives answers based on the given context. If the answer is not in the context, say "I don't know"
    - get_context: Tool that returns the context based on the users query if the query is about NASA and space travels.
"""
