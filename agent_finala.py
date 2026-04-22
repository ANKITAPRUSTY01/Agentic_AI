from typing import TypedDict, List
from datetime import datetime

def llm_call(prompt):
    return "Answer based on context: " + prompt[:200]

class CapstoneState(TypedDict):
    question: str
    messages: List[str]
    route: str
    retrieved: str
    sources: List[str]
    tool_result: str
    answer: str
    faithfulness: float
    eval_retries: int

docs = [
    {"id": "doc1", "topic": "Transformers", "text": "Transformers use self-attention mechanisms to process sequences in parallel."},
    {"id": "doc2", "topic": "BERT", "text": "BERT is a bidirectional encoder trained using masked language modeling."},
    {"id": "doc3", "topic": "GPT", "text": "GPT models are autoregressive transformers used for text generation."},
    {"id": "doc4", "topic": "Attention", "text": "Attention allows models to focus on relevant parts of input sequences."},
    {"id": "doc5", "topic": "Fine-tuning", "text": "Fine-tuning adapts pretrained models to downstream tasks."},
    {"id": "doc6", "topic": "Tokenization", "text": "Tokenization splits text into tokens for processing."},
    {"id": "doc7", "topic": "Embeddings", "text": "Embeddings convert text into dense vector representations."},
    {"id": "doc8", "topic": "RAG", "text": "Retrieval-Augmented Generation combines retrieval with generation."},
    {"id": "doc9", "topic": "Evaluation", "text": "Faithfulness ensures answers are grounded in retrieved context."},
    {"id": "doc10", "topic": "LLMs", "text": "Large Language Models are trained on massive datasets."}
]

def memory_node(state):
    state["messages"].append(state["question"])
    state["messages"] = state["messages"][-6:]
    return state

def router_node(state):
    q = state["question"].lower()
    if "time" in q:
        state["route"] = "tool"
    elif "hello" in q or "hi" in q:
        state["route"] = "skip"
    else:
        state["route"] = "retrieve"
    return state

def retrieval_node(state):
    q = state["question"].lower()
    results = []
    for d in docs:
        if any(word in d["text"].lower() for word in q.split()):
            results.append(d)
    results = results[:3]
    context = "\n".join([f"[{r['topic']}] {r['text']}" for r in results])
    state["retrieved"] = context
    state["sources"] = [r["topic"] for r in results]
    return state

def tool_node(state):
    state["tool_result"] = str(datetime.now())
    return state

def answer_node(state):
    prompt = f"Question: {state['question']}\nContext: {state.get('retrieved','')}\nTool: {state.get('tool_result','')}"
    state["answer"] = llm_call(prompt)
    return state

def eval_node(state):
    state["faithfulness"] = 0.8 if state.get("retrieved") else 1.0
    return state

def save_node(state):
    state["messages"].append(state["answer"])
    return state

def run_agent(question, thread):
    state = {
        "question": question,
        "messages": thread,
        "route": "",
        "retrieved": "",
        "sources": [],
        "tool_result": "",
        "answer": "",
        "faithfulness": 0.0,
        "eval_retries": 0
    }

    state = memory_node(state)
    state = router_node(state)

    if state["route"] == "retrieve":
        state = retrieval_node(state)
    elif state["route"] == "tool":
        state = tool_node(state)

    state = answer_node(state)
    state = eval_node(state)
    state = save_node(state)

    return state
