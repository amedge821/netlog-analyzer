# Network Telemetry & Diagnostics Analyzer

A simple Python tool that parses network logs, saves them in an SQLite database, runs automated tests using PyTest, and generates AI troubleshooting steps.


## Features
- **Log Ingestion:** Parses raw network log files and stores them securely in an **SQLite** database using parameterized queries.
- **Automated Testing:** Uses **PyTest** to check system health and catch critical hardware link errors.
- **AI Diagnostics:** Automatically reviews error logs and outputs simple troubleshooting steps for network engineers.
- **Search Utility:** A quick command-line tool to filter and search logs.



## Tech Stack
- **Language:** Python
- **Database:** SQLite3
- **Testing:** PyTest
- **Version Control:** Git & GitHub



## Project Structure
netlog-analyzer/
│
├── data/
│   └── network_logs.db       # SQLite database
├── src/
│   ├── db_setup.py           # Creates database schema
│   ├── ingest.py             # Parses and loads logs
│   ├── cli.py                # Command-line search tool
│   └── ai_diagnostics.py     # AI workflow & troubleshooting engine
├── tests/
│   └── test_alerts.py        # PyTest health checks
├── logs/
│   └── sample_syslog.txt     # Sample log file
└── requirements.txt          # Python dependencies


## How to Run

1. **Clone the repository:**
```bash
git clone [https://github.com/amedge821/netlog-analyzer.git](https://github.com/amedge821/netlog-analyzer.git)
cd netlog-analyzer

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Initialize the database and load logs:**
```bash
python src/db_setup.py
python src/ingest.py --file logs/sample_syslog.txt

```


4. **Run automated tests (PyTest):**
```bash
pytest tests/

```


5. **Run the AI diagnostic workflow:**
```bash
python src/ai_diagnostics.py

```

