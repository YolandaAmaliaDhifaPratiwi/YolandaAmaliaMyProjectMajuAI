# backend/retriever.py
import os


class Retriever:
    def __init__(self, vector_path='./faiss_index/'):
        self.vector_path = vector_path
# This is a minimal stub. Implement embedding + FAISS indexing as needed.


def query(self, query_text, top_k=3):
# Return list of dicts: {"id":..., "content":...}
# For demo, return empty list or a mocked doc.
    return [{'id':'doc1','content':'Contoh ringkasan materi: regresi linear adalah ...'}]
