import sqlite3
import pytest

DB_NAME = "network_telemetry.db"

def query_errors():
    """Helper function to fetch all ERROR level logs from SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT port_id, message FROM network_logs WHERE log_level = 'ERROR'")
    errors = cursor.fetchall()
    conn.close()
    return errors

def query_warnings():
    """Helper function to fetch all WARN level logs from SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT port_id, message FROM network_logs WHERE log_level = 'WARN'")
    warnings = cursor.fetchall()
    conn.close()
    return warnings

# --- AUTOMATED TEST SUITE ---

def test_no_critical_interface_failures():
    """
    Test Case 1: Ensures no network interface has gone completely DOWN.
    """
    errors = query_errors()
    # Assert that zero critical error logs were ingested
    assert len(errors) == 0, f"Critical failure detected! Found errors: {errors}"

def test_warning_count_threshold():
    """
    Test Case 2: Flags an alert if warning count exceeds threshold of 5.
    """
    warnings = query_warnings()
    assert len(warnings) < 5, f"High warning count detected: {len(warnings)} warnings logged."