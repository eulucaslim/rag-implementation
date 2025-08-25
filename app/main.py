from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from lib.langchain import LangChain
from langchain_core.messages import HumanMessage


langchain = LangChain()
# for doc in docs:
#     print(f" Page {doc.metadata['page']}: {doc.page_content[:300]}\n")

# retriever = vector_store.as_retriever()

template = """
    You're a helpful assistant that only gives anwers bases on the given context. If the answer is not in the context, say "I don't know".

    Context: {context}

    Question: {question}

    Answer:

"""

# prompt = ChatPromptTemplate.from_template(template)

# chain = (
#     {"context": retriever, "question": RunnablePassthrough()}
#     | prompt
#     | langchain.llm
#     | StrOutputParser()
# )

# response = chain.invoke("What are the Objectives Development Process")
# md = Markdown(response)

# console.print(md)

@tool
def get_context_agriculture(query: str) -> str:
    """Get the context based in reseach"""
    retriever = vector_store_agriculture.as_retriever()
    result = retriever.invoke(query)
    return result

@tool
def get_context_dengue(query: str) -> str:
    """Get the context based in reseach"""
    retriever = vector_store_dengue.as_retriever()
    result = retriever.invoke(query)
    return result



# print(get_context_dengue.invoke("Cases of dengue we had since the beginning of 2025?"))

system_prompt = """You're a helpful assistant that only gives answers based on the given context. If the answer is not in the context, say "I don't know"
- pega_contexto: Tool that returns the context based on the users query if the query is about NASA and space travels.
- pega_contexto_agriculture: Tool that returns the context based on the users query if the query is about agriculture.
- pega_contexto_dengue: Tool that returns the context based on the users query if the query is about dengue.
"""

agent_pdf = create_react_agent(model=langchain.llm, tools=tools, prompt=system_prompt)
result = agent_pdf.invoke({
    "messages": [
        ("user", "What causes dengue?")
    ]
})

# Use a Graph to create a ChatBot! 

def chat_with_memory(message_user: str, thread_id="1", verbose=False):
    config = {"configurable": {"thread_id": thread_id}}
    messages = app.invoke({"messages": [HumanMessage(content=message_user)]}, config)

    if verbose:
        for message in messages['messages']:
            message.pretty_print()
    else:
        messages['messages'][-1].pretty_print()

chat_with_memory(message_user="Why is agriculture crucial for India's economy, and what's its current need?", thread_id="2", verbose=False)