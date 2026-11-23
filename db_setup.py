import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
DB_PATH = os.path.join(DATA_DIR, "network_logs.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS network_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            port_id TEXT,
            severity TEXT,
            message TEXT,
            packet_loss REAL
        )
    """)
    conn.commit()
    conn.close()
    print(f"[DB SETUP] Initialized 'network_logs' table at {DB_PATH}")

if __name__ == "__main__":
    init_db()