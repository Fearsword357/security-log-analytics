Python Log Analyzer – Brute Force Detection
Overview

This project is a simple cybersecurity log analysis tool written in Python.
It simulates authentication logs and analyzes them to detect potential brute-force login attacks.

The tool demonstrates how security analysts investigate authentication logs to identify suspicious activity such as:

repeated failed login attempts

brute-force password attacks

suspicious source IP addresses

abnormal spikes in authentication failures

The project was built as a learning exercise to demonstrate basic SOC (Security Operations Center) style log analysis using Python.

Features

Generates realistic authentication log data

Detects repeated failed login attempts

Identifies suspicious IP addresses

Detects potential brute-force attacks

Visualizes login failure spikes using graphs

Project Structure
Security-Log-Analytics
│
├ src/
│   ├ generate_logs.py
│   └ analyze_logs.py
│
├ data/
│   └ auth.log
│
├ examples/
│   └ attack_simulation_example.py
│
├ README.md
├ requirements.txt
└ .gitignore
How It Works
1. Log Generation

generate_logs.py creates a simulated authentication log file containing:

normal login activity

occasional failed login attempts

a simulated brute-force attack window

Example log entry:

2026-02-13 07:12:36 FAILED User root login attempt from 203.0.113.77
2. Log Analysis

analyze_logs.py reads the log file and performs several analyses:

counts failed login attempts per IP address

counts failed login attempts per minute

detects IP addresses with excessive failed login attempts

visualizes attack spikes using matplotlib

Example output:

Failed Login Attempts by IP:
192.168.1.50 -> 12
203.0.113.77 -> 14

Possible Brute Force Alerts:
ALERT: 192.168.1.50 has 12 failed login attempts
ALERT: 203.0.113.77 has 14 failed login attempts
Installation

Install required Python libraries:

pip install -r requirements.txt
Usage

Generate log data:

python generate_logs.py

Analyze logs:

python analyze_logs.py

The analysis script will display:

suspicious IP addresses

failed login statistics

a graph of login failures over time

Example Detection

The analyzer can detect bursts of failed login attempts typical of brute-force attacks.

Example timeline:

07:12 -> 5 failures
07:13 -> 6 failures
07:14 -> 7 failures
07:15 -> 6 failures

This spike indicates an automated login attack.

Technologies Used

Python

Matplotlib

Basic log parsing techniques

Learning Goals

This project demonstrates:

basic log analysis

security event detection

simple threat detection logic

data visualization for cybersecurity analysis

Future Improvements

Possible upgrades:

automatic attack window detection

export results to CSV

real-time log monitoring

integration with SIEM-style alert rules

Author

Personal cybersecurity portfolio project.

Why this README is good

It clearly shows:

cybersecurity knowledge

Python skills

understanding of SOC workflows

ability to document projects

That’s exactly what portfolio projects should show.