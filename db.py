# db.py
import sqlite3

def init_db():
    conn = sqlite3.connect("tags.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tags (
            tag_id TEXT PRIMARY KEY,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_description(tag_id):
    conn = sqlite3.connect("tags.db")
    c = conn.cursor()
    c.execute("SELECT description FROM tags WHERE tag_id = ?", (tag_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def add_tag(tag_id, description):
    conn = sqlite3.connect("tags.db")
    c = conn.cursor()
    c.execute("REPLACE INTO tags (tag_id, description) VALUES (?, ?)", (tag_id, description))
    conn.commit()
    conn.close()

def remove_tag(tag_id):
    conn = sqlite3.connect("tags.db")
    c = conn.cursor()
    c.execute("DELETE FROM tags WHERE tag_id = ?", (tag_id,))
    conn.commit()
    conn.close()
