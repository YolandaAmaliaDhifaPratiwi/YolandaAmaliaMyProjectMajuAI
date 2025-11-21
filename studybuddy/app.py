import os
import streamlit as st
from backend.llm_client import GeminiClient
from backend.retriever import Retriever
from backend.memory_store import MemoryStore

# Load env
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="StudyBuddy - Data Science", layout="centered")

if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {"role": "user/assistant", "text": "..."}
if "style" not in st.session_state:
    st.session_state.style = "santai"

client = GeminiClient(api_key=os.getenv("GEMINI_API_KEY"))
retriever = Retriever()         # wrapper for embeddings + FAISS
memory = MemoryStore("memory.db")  # simple local store

st.title("StudyBuddy — Chatbot Data Science")
col1, col2 = st.columns([3,1])
with col2:
    st.selectbox("Gaya bahasa", ["santai","netral","formal"], key="style")
    st.checkbox("Gunakan RAG (dokumen)", value=True, key="use_rag")
    st.slider("Temperature", 0.0, 1.0, 0.2, key="temperature")

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['text']}")
    else:
        st.markdown(f"**StudyBuddy:** {msg['text']}")

prompt = st.text_input("Tanyakan sesuatu tentang Data Science atau minta contoh kode:")
if st.button("Kirim"):
    user_text = prompt
    st.session_state.messages.append({"role":"user","text":user_text})

    # optionally retrieve context
    context_docs = []
    if st.session_state.use_rag:
        context_docs = retriever.query(user_text, top_k=3)

    # build system prompt with style
    system_prompt = f"You are StudyBuddy, jawab singkat, gaya {st.session_state.style}."

    resp = client.generate(
        user_text,
        system_prompt=system_prompt,
        context_docs=context_docs,
        temperature=float(st.session_state.temperature),
        max_output_tokens=512,
    )

    # handle function call result if any (client may return function_call field)
    if resp.get("function_call"):
        # client returned a predicted function call; execute safely via agent_tools
        func_name = resp["function_call"]["name"]
        args = resp["function_call"].get("arguments", {})
        result = client.execute_function(func_name, args)  # implement safety checks inside
        # then feed result back to model for final answer (optional)
        followup = client.generate_followup_with_function_result(resp, result)
        st.session_state.messages.append({"role":"assistant","text":followup})
    else:
        st.session_state.messages.append({"role":"assistant","text":resp["text"]})

    st.experimental_rerun()
