from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from state import CareerState
from nodes import *

def route_decision(state):
    return state["route"]

def eval_decision(state):
    if state["faithfulness"] < 0.7 and state["eval_retries"] < 2:
        return "answer"
    return "save"

def build_graph():
    g = StateGraph(CareerState)

    g.add_node("memory", memory_node)
    g.add_node("router", router_node)
    g.add_node("retrieve", retrieval_node)
    g.add_node("skip", skip_node)
    g.add_node("tool", tool_node)
    g.add_node("answer", answer_node)
    g.add_node("eval", eval_node)
    g.add_node("save", save_node)

    g.set_entry_point("memory")

    g.add_edge("memory", "router")

    g.add_conditional_edges("router", route_decision, {
        "retrieve": "retrieve",
        "tool": "tool",
        "skip": "skip"
    })

    g.add_edge("retrieve", "answer")
    g.add_edge("tool", "answer")
    g.add_edge("skip", "answer")

    g.add_edge("answer", "eval")

    g.add_conditional_edges("eval", eval_decision, {
        "answer": "answer",
        "save": "save"
    })

    g.add_edge("save", END)

    return g.compile(checkpointer=MemorySaver())