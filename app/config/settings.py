from dotenv import load_dotenv
from typing import Final
import os

load_dotenv()

GROQ_API_KEY : Final[str] = os.getenv("GROQ_API_KEY")
HF_TOKEN: Final[str] = os.getenv("HF_TOKEN")