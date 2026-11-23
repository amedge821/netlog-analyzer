import os
import re
import sqlite3
from db_setup import DB_PATH, init_db

LOSS_RE = re.compile(r"(\d+(?:\.\d+)?)\s*%")

def parse_line(line):
    """TIMESTAMP | LOG_LEVEL | PORT_ID | MESSAGE"""
    parts = [p.strip() for p in line.strip().split("|")]
    if len(parts) != 4:
        return None
    timestamp, severity, port_id, message = parts
    severity = {"WARN": "WARNING"}.get(severity.upper(), severity.upper())
    loss = None
    if "loss" in message.lower():
        m = LOSS_RE.search(message)
        loss = float(m.group(1)) if m else None
    return timestamp, severity, port_id, message, loss

def ingest_logs(log_filepath="syslog.txt"):
    if not os.path.exists(log_filepath):
        print(f"File {log_filepath} not found.")
        return

    init_db()  # guarantees the table exists
    conn = sqlite3.connect(DB_PATH)
    inserted = 0
    with open(log_filepath, "r") as f:
        for line in f:
            rec = parse_line(line)
            if rec:
                conn.execute(
                    "INSERT INTO network_logs (timestamp, severity, port_id, message, packet_loss) "
                    "VALUES (?, ?, ?, ?, ?)", rec)
                inserted += 1
    conn.commit()
    conn.close()
    print(f"Ingested {inserted} log records into {DB_PATH}.")

if __name__ == "__main__":
    ingest_logs()