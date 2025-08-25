from app.config.settings import SYSTEM_PROMPT
from app.lib.langchain import LangChain
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition, create_react_agent
from IPython.display import Image

class Graph(object):
    def __init__(self):
        self.langchain = LangChain()
        self.graph = StateGraph(MessagesState)
        self.tools = [self.langchain.get_context]
        self.agent_pdf = create_react_agent(model=self.langchain.llm, tools=self.tools, prompt=SYSTEM_PROMPT)

    def generate_nodes(self):
        self.graph.add_node("assistent", self.agent_pdf)
        self.graph.add_node("tools", ToolNode(self.tools))

        self.graph.add_edge(START, "assistent")
        self.graph.add_conditional_edges("assistent", tools_condition)

        self.graph.add_edge("tools", "assistent")
        self.graph.add_edge("assistent", END)

        memory = MemorySaver()
        app = self.graph.compile(checkpointer=memory)

        return Image(app.get_graph().draw_mermaid_png())
