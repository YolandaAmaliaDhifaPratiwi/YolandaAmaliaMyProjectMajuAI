# backend/memory_store.py
import sqlite3
import json


class MemoryStore:
    def __init__(self, db_path='memory.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._setup()


def _setup(self):
    cur = self.conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY, session_id TEXT, role TEXT, text TEXT)''')
    self.conn.commit()


def save(self, session_id, role, text):
    cur = self.conn.cursor()
    cur.execute('INSERT INTO memory (session_id, role, text) VALUES (?,?,?)', (session_id, role, text))
    self.conn.commit()


def get_session(self, session_id):
    cur = self.conn.cursor()
    cur.execute('SELECT role, text FROM memory WHERE session_id=? ORDER BY id', (session_id,))
    return [{'role':r,'text':t} for r,t in cur.fetchall()]
