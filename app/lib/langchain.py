from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.tools import tool
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY


class LangChain(object):

    def __init__(self, prompt: str):
        self.prompt = prompt
        self.llm = ChatGroq(model='llama-3.3-70b-versatile', api_key=GROQ_API_KEY)
        self.embeding_model = HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")
        self.vector_store = InMemoryVectorStore()
        self.pages = list()

    def load_pdf(self) -> InMemoryVectorStore:
        # Url DataSet
        url = 'https://raw.githubusercontent.com/allanspadini/curso-flash-rag/main/m2m_strategy_and_objectives_development.pdf'
        loader = PyPDFLoader(url)

        for page in loader.load():
            self.pages.append(page)

        self.vector_store.from_documents(self.pages, self.embeding_model)

        return self.vector_store

    @tool
    def get_context(self, query: str) -> str:
        """Get the context based in reseach"""
        retriever = self.vector_store.as_retriever()
        result = retriever.invoke(query)
        return result
    
    def find_similarity(self):
        docs = self.vector_store.similarity_search("Objectives Development Process", k=2)