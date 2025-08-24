from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from lib.langchain import LangChain

langchain = LangChain()

prompt = '''
    messages: Segundo a NASA quais seriam os beneficios cientificos de ir para Marte?
'''

response = langchain.llm.invoke(prompt)

url = 'https://raw.githubusercontent.com/allanspadini/curso-flash-rag/main/m2m_strategy_and_objectives_development.pdf'
loader = PyPDFLoader(url)

pages = list()

for page in loader.lazy_load():
    pages.append(page)

# Infos about document
# print(f"{pages[0].metadata}\n")

# Content

embed_model = HuggingFaceEmbeddings(model_name="mixedbread-ai/mxbai-embed-large-v1")

vector_store = InMemoryVectorStore.from_documents(pages, embed_model)

docs = vector_store.similarity_search("Objectives Development Process", k=2)

for doc in docs:
    print(f" Page {doc.metadata['page']}: {doc.page_content[:300]}\n")