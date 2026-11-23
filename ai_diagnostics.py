import sqlite3
import os
from db_setup import DB_PATH


# Rule-based diagnostic map simulating AI workflow logic
TROUBLESHOOTING_RULES = {
    "PORT_2_DOWN": {
        "root_cause": "Physical link degradation or SFP optical transceiver failure.",
        "steps": [
            "1. Run command 'show interface PORT_2 status' to verify physical link state.",
            "2. Inspect SFP optical power levels to check for signal loss.",
            "3. Replace fiber patch cable or failover to secondary redundant trunk."
        ]
    },
    "HIGH_PACKET_LOSS": {
        "root_cause": "Network congestion, misconfigured buffer queues, or frame drops.",
        "steps": [
            "1. Check interface bandwidth usage using 'show interface throughput'.",
            "2. Verify QoS queue configuration and drop counters.",
            "3. Perform path trace to isolate the bottleneck node."
        ]
    }
}

def fetch_flagged_logs():
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Database file not found at {DB_PATH}.")
        return []
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT timestamp, port_id, severity, message, packet_loss FROM network_logs "
        "WHERE severity IN ('ERROR','CRITICAL') OR packet_loss > 5.0 "
        "OR LOWER(message) LIKE '%down%'"
    ).fetchall()
    conn.close()
    return rows

def generate_ai_remediation(log_entry):
    """Simulate AI Diagnostic Engine processing a contextualized error payload."""
    ts, port_id, severity, message, packet_loss = log_entry

    print("\n" + "="*70)
    print(f"[ALERT DETECTED] [{ts}] Device: {port_id} | Sev: {severity}")
    print(f"Message: {message} | Packet Loss: {packet_loss}%")
    print("-" * 70)
    print("[AI DIAGNOSTIC WORKFLOW EXECUTING...]")

    # Pattern match error key
    matched_rule = None
    if "PORT_2" in message or "DOWN" in message:
        matched_rule = TROUBLESHOOTING_RULES["PORT_2_DOWN"]
    elif packet_loss > 5.0:
        matched_rule = TROUBLESHOOTING_RULES["HIGH_PACKET_LOSS"]
    else:
        matched_rule = None

    if matched_rule:
        print(f"Root Cause Hypothesis : {matched_rule['root_cause']}")
        print("Actionable Remediation Steps:")
        for step in matched_rule["steps"]:
            print(f"  {step}")
    else:
        print("Root Cause Hypothesis : Uncategorized telemetry anomaly.")
        print("Actionable Remediation Steps:")
        print("  1. Collect detailed system debug logs.")
        print("  2. Escalated to Tier 2 Network Engineering team.")
        
    print("="*70)

def main():
    flagged_events = fetch_flagged_logs()
    if not flagged_events:
        print("No critical logs found in database. System status: HEALTHY.")
        return

    print(f"Found {len(flagged_events)} event(s) requiring AI analysis.")
    for event in flagged_events:
        generate_ai_remediation(event)

if __name__ == "__main__":
    main()