import streamlit as st
from agent import run_agent

st.title("Research Paper Q&A Assistant")

if "thread" not in st.session_state:
    st.session_state.thread = []

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask a question:")

if st.button("Ask"):
    if user_input:
        result = run_agent(user_input, st.session_state.thread)
        st.session_state.thread = result["messages"]
        st.session_state.chat.append(("User", user_input))
        st.session_state.chat.append(("Bot", result["answer"]))

for role, msg in st.session_state.chat:
    st.write(f"{role}: {msg}")

if st.button("New Conversation"):
    st.session_state.thread = []
    st.session_state.chat = []
