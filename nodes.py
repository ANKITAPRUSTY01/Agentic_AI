import re
from langchain_groq import ChatGroq
from chroma import collection, embedder

llm = ChatGroq(model="llama-3.3-70b-versatile")

# 🧠 MEMORY NODE
def memory_node(state):
    msgs = state.get("messages", [])
    msgs.append(state["question"])

    name = state.get("user_name", "")
    skills = state.get("user_skills", [])

    q = state["question"].lower()

    # extract name
    if "my name is" in q:
        name = q.split("my name is")[-1].strip().title()

    # extract skills
    skill_list = ["python", "sql", "ml", "machine learning", "ai"]
    for s in skill_list:
        if s in q:
            skills.append(s.title())

    return {
        "messages": msgs[-6:],
        "user_name": name,
        "user_skills": list(set(skills))
    }

# 🚦 ROUTER NODE
def router_node(state):
    q = state["question"].lower()

    if "roadmap" in q or "how" in q:
        return {"route": "retrieve"}
    elif "skill" in q or "missing" in q:
        return {"route": "tool"}
    else:
        return {"route": "skip"}

# 📚 RETRIEVAL NODE (REAL RAG)
def retrieval_node(state):
    query_emb = embedder.encode([state["question"]]).tolist()

    results = collection.query(
        query_embeddings=query_emb,
        n_results=3
    )

    docs = results["documents"][0]
    context = "\n".join(docs)

    return {
        "retrieved": context,
        "sources": results["metadatas"][0]
    }

# ⏭ SKIP NODE
def skip_node(state):
    return {"retrieved": "", "sources": []}

# 🛠 TOOL NODE (DYNAMIC)
def tool_node(state):
    required = ["Python", "Machine Learning", "Deep Learning"]
    user_skills = state.get("user_skills", [])

    missing = list(set(required) - set(user_skills))

    return {
        "tool_result": f"User has: {user_skills}\nMissing: {missing}"
    }

# 🤖 ANSWER NODE
def answer_node(state):
    prompt = f"""
    You are a Career AI Mentor.

    User Name: {state.get("user_name", "User")}
    User Skills: {state.get("user_skills", [])}

    Question: {state["question"]}

    Context (Knowledge Base):
    {state.get("retrieved", "")}

    Tool Output (Skill Analysis):
    {state.get("tool_result", "")}

    Instructions:
    - If context is present → use ONLY context
    - If tool output exists → explain missing skills clearly
    - Personalize answer using user name
    - Keep answer structured (points)
    - Do NOT hallucinate

    Answer:
    """

    res = llm.invoke(prompt)

    return {"answer": res.content}
# ✅ EVAL NODE
def eval_node(state):
    answer = state.get("answer", "")
    context = state.get("retrieved", "")

    # simple faithfulness check
    if context and answer:
        score = 1.0 if any(word in answer for word in context.split()[:20]) else 0.5
    else:
        score = 0.8

    return {
        "faithfulness": score,
        "eval_retries": state.get("eval_retries", 0) + 1
    }

# 💾 SAVE NODE
def save_node(state):
    msgs = state.get("messages", [])
    msgs.append(state.get("answer", ""))
    return {"messages": msgs}