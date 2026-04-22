
# 📚 Research Paper Q&A Assistant

### 🚀 Agentic AI Capstone Project (2026)

## 👤 Author

**Name:** Ankita Prusty
**Course:** Agentic AI Course 2026
**Instructor:** Dr. Kanthi Kiran Sirra

---

# 📌 Project Overview

The **Research Paper Q&A Assistant** is an intelligent AI system that allows users to ask questions and get answers directly from a structured knowledge base of research papers.

It is built using a **lightweight Agentic AI architecture**, simulating real-world systems using:

* Memory
* Routing logic
* Retrieval system
* Tool usage
* Evaluation layer

---

# 🎯 Key Features

✔ Natural language question answering
✔ Multi-turn conversation memory
✔ Rule-based Agent routing system
✔ Document-based retrieval system
✔ Tool integration (time/date)
✔ Self-evaluation scoring (faithfulness)
✔ Streamlit chat UI

---

# 🧠 System Architecture

```text id="arch1"
User Query
   ↓
Memory Node
   ↓
Router Node
   ↓
Retrieve / Tool / Skip
   ↓
Answer Generation Node
   ↓
Evaluation Node
   ↓
Save Node
   ↓
Final Response
```

---

# 🧰 Tech Stack

| Technology        | Purpose             |
| ----------------- | ------------------- |
| Python            | Core development    |
| Streamlit         | UI framework        |
| Rule-based Agent  | Workflow logic      |
| In-memory storage | Conversation memory |

---

# 📚 Knowledge Base

The system is trained on key AI/ML topics:

* Transformers
* BERT
* GPT Models
* Attention Mechanism
* Tokenization
* Embeddings
* Retrieval-Augmented Generation (RAG)
* Evaluation Methods

---

# ⚙️ How It Works

1. User enters a question
2. Router decides action:

   * Retrieve knowledge
   * Use tool
   * Skip retrieval
3. Relevant context is fetched
4. Answer is generated
5. Evaluation checks correctness
6. Response is stored in memory

---

# 🚀 How to Run

## 1️⃣ Install dependencies

```bash id="run1"
pip install streamlit
```

---

## 2️⃣ Start application

```bash id="run2"
streamlit run app.py
```

---

# 💬 Example Queries

* What is Transformer architecture?
* Explain BERT model
* What is GPT?
* What is attention mechanism?
* What is current time?

---

# 📊 Evaluation System

* Faithfulness score range: 0 → 1
* Threshold: 0.7
* If score < threshold → retry response generation

---

# 📁 Project Structure

```text id="struct1"
research-ai/
│
├── app.py              # Streamlit UI
├── agent.py            # Core logic
├── nodes.py            # Agent pipeline functions
├── docs/               # Knowledge base
└── README.md
```

---

# 🔮 Future Improvements

* 🔥 Integrate real LLM (Groq / OpenAI)
* 📄 Add PDF upload support
* 🧠 Replace rule-based system with LangGraph
* 📊 Add RAGAS evaluation
* 🌐 Deploy on cloud (Streamlit / Azure)

---

# 🧪 Project Highlights

✔ Agentic AI design (multi-node system)
✔ Retrieval-based Q&A system
✔ Memory-based conversations
✔ Tool integration
✔ Evaluation feedback loop

---

# 👨‍💻 Author

**Abhik Don**
Agentic AI Course 2026

---

# ⭐ Final Note

This project demonstrates a **mini Agentic AI system** combining retrieval, reasoning, memory, and evaluation into a single interactive assistant.

---
