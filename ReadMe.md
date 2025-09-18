# Python Automation Scripts

## Project Overview
This project contains a set of **Python automation scripts** designed to reduce human error and improve efficiency in daily system operations.  
Key features include:
- **Automated Backup**: Compress files/folders with timestamped filenames.  
- **Scheduled Tasks (Cron job)**: Run automated backups or cleanup jobs on a schedule.  
- **Log Rotation**: Rotate and compress old logs to prevent disk usage issues.  

---

## Project Structure
```bash
python-automation/
├── scripts/
│   ├── zip_backup.py       # Automated backup
│   ├── log_rotation.py     # Log rotation
│   └── cleanup.py          # System cleanup
├── data/
│   └── my_data.txt         # Sample data
├── backups/                # Backup outputs
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── .github/
    └── workflows/
        └── python-ci.yml   # GitHub Actions CI/CD
```

## Installation & Usage
1. Setup Environment
```bash
git clone https://github.com/CatherineChen-CyberSecurity/python-automation.git
cd python-automation
pip install -r requirements.txt
```
2. Run Backup Script
```bash
python scripts/zip_backup.py data/
```
3. Schedule with Cron (Linux example)
```bash
0 2 * * * /usr/bin/python /home/user/python-automation/scripts/zip_backup.py /home/user/data
```

## CI/CD (GitHub Actions)

Automated Testing: Run pytest on push or PR events.

Automated Deployment: Ensure scripts can be packaged and executed successfully.

Workflow file: .github/workflows/python-ci.yml

## Tech Stack

Python 3.x

GitHub Actions (CI/CD)

Cron (Linux scheduling)