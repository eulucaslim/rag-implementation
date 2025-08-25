from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import MessagesState
from langgraph.graph import START, StateGraph, END
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from IPython.display import Image, display

class Graph(object):
    def __init__(self):
        self.graph = StateGraph(MessagesState)

    def generate_nodes(self):
        self.graph.add_node("assistent", agent_pdf)
        self.graph.add_node("tools", ToolNode(tools))

        self.graph.add_edge(START, "assistent")
        self.graph.add_conditional_edges("assistent", tools_condition)

        self.graph.add_edge("tools", "assistent")
        self.graph.add_edge("assistent", END)

        memory = MemorySaver()
        app = self.graph.compile(checkpointer=memory)

        return Image(app.get_graph().draw_mermaid_png())
