# StudyBuddy — LLM Chatbot for Data Science


**Project:** LLM-Based Tools and Gemini API Integration for Data Scientists


## Deskripsi singkat
StudyBuddy adalah chatbot edukasi untuk pelajar dan pemula data science. Chatbot membantu menjelaskan konsep, memberi contoh kode Python, dan merekomendasikan materi pembelajaran. Ia menggunakan LLM (Gemini) dengan opsi RAG, memory singkat, dan pengaturan gaya bahasa.


## Fitur
- Chat UI (Streamlit) dengan `st.session_state` untuk menyimpan percakapan.
- Integrasi LLM (Gemini API) — wrapper sederhana.
- Retrieval (FAISS) untuk dokumen kursus (opsional).
- Memory session sederhana (SQLite/JSON).
- Parameter kreatif: `temperature`, `style`, `use_rag`, `use_memory`.


## Struktur project
studybuddy/
├─ README.md
├─ requirements.txt
├─ .env.example
├─ app.py                 # Streamlit app (UI + session_state)
├─ backend/
│  ├─ llm_client.py       # Wrapper Gemini API
│  ├─ retriever.py        # embeddings + vectorstore wrapper
│  ├─ agent_tools.py      # fungsi yang dapat dipanggil model
│  └─ memory_store.py     # simpan/retrieve percakapan
├─ assets/
│  └─ screenshots/        # simpan screenshot UI untuk submission
└─ notebooks/             # optional demo notebooks


## Setup & Run (local)
1. Install Python 3.9+.
2. Buat virtualenv & aktifkan.
```bash
python -m venv venv
source venv/bin/activate # macOS/Linux
venv\Scripts\activate # Windows
pip install -r requirements.txt
Copy .env.example ke .env dan isi GEMINI_API_KEY (atau set Google Cloud credentials sesuai kebutuhan).
Jalankan: streamlit run app.py
Buka http://localhost:8501.
Catatan :
SDK/shape response Gemini berbeda-beda. Jika menggunakan Vertex AI, ikuti cara autentikasi Google Cloud.
Untuk submission, sertakan 3 screenshot di assets/screenshots/.
Deliverables :
URL GitHub repo (atau Google Drive link jika belum punya GitHub)
Screenshot UI (3 images)
