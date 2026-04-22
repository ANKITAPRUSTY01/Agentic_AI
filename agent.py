from graph import build_graph

app = build_graph()

def ask(q, thread_id="user1"):
    res = app.invoke(
        {
            "question": q,
            "eval_retries": 0
        },
        config={"configurable": {"thread_id": thread_id}}
    )

    return res.get("answer", "No answer")