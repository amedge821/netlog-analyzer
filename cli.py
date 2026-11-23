import sqlite3, argparse, os
from db_setup import DB_PATH

def query_logs(severity=None, port=None, limit=10):
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Database not found at {DB_PATH}. Run db_setup.py first.")
        return
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT timestamp, severity, port_id, message, packet_loss FROM network_logs WHERE 1=1"
    params = []
    if severity:
        query += " AND severity = ?"; params.append(severity.upper())
    if port:
        query += " AND port_id = ?"; params.append(port)
    query += " ORDER BY timestamp DESC LIMIT ?"; params.append(limit)
    rows = conn.execute(query, params).fetchall()
    conn.close()

    print(f"\n--- LOG QUERY RESULTS (Found: {len(rows)}) ---")
    for ts, sev, port_id, msg, loss in rows:
        loss_txt = f" | Packet Loss: {loss}%" if loss is not None else ""
        print(f"[{ts}] [{sev}] {port_id} | {msg}{loss_txt}")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Query Network Telemetry Logs")
    p.add_argument("--severity", choices=["INFO", "WARNING", "ERROR", "CRITICAL"])
    p.add_argument("--port", help="Filter by port (e.g., PORT_2)")
    p.add_argument("--limit", type=int, default=10)
    a = p.parse_args()
    query_logs(a.severity, a.port, a.limit)