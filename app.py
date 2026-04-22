import streamlit as st
from agent import ask
import uuid

st.set_page_config(page_title="Career AI Mentor", layout="wide")

# =========================
# SESSION STATE INIT
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("🎓 Career AI Mentor")

    st.markdown("""
    ### 📌 About
    This AI assistant helps you:
    - Get career guidance
    - Identify missing skills
    - Learn AI/ML roadmap

    ### ⚙️ Features
    - Memory (remembers you)
    - Skill analysis
    - AI roadmap generation
    - Knowledge-based answers

    ### 🧠 Tech Stack
    - LangGraph
    - ChromaDB (RAG)
    - Groq LLM
    """)

    if st.button("🔄 New Conversation"):
        st.session_state.messages = []
        st.session_state.thread_id = str(uuid.uuid4())
        st.success("New session started!")

# =========================
# MAIN TITLE
# =========================
st.title("💬 Career AI Chat Assistant")

# =========================
# DISPLAY CHAT HISTORY
# =========================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# USER INPUT
# =========================
user_input = st.chat_input("Ask your career question...")

if user_input:
    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # get AI response
    response = ask(user_input, thread_id=st.session_state.thread_id)

    # show AI message
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)