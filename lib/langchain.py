from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY

class LangChain(object):

    def __init__(self):
        self.llm = ChatGroq(
            model='llama-3.3-70b-versatile', 
            api_key=GROQ_API_KEY
        )