# Import tools for working with dates and time
from datetime import datetime, timedelta

# Import Python's random number generator
import random


# Set a fixed seed so the random data is reproducible
# This means the same log data will be generated every time the script runs
random.seed(7)


# Define the starting timestamp for the log file
# All generated events will be based on this starting time
start = datetime(2026, 2, 13, 7, 0, 0)


# List of possible usernames that may appear in the logs
users = ["admin", "root", "glenn", "sarah", "james", "service"]


# IP addresses representing normal internal users
good_ips = ["192.168.1.10", "192.168.1.22", "192.168.1.33"]

# IP addresses representing suspicious or attacker sources
bad_ips = ["192.168.1.50", "10.0.0.8", "203.0.113.77"]


# List that will hold all generated log lines before writing to a file
lines = []


# Loop through 30 minutes of simulated activity
for minute in range(0, 30):

    # Calculate the base time for the current minute
    base_time = start + timedelta(minutes=minute)


    # --- Simulate normal successful logins ---
    # 35% chance that a normal login occurs in this minute
    if random.random() < 0.35:

        # Add random seconds within the minute
        t = base_time + timedelta(seconds=random.randint(0, 59))

        # Pick a random legitimate user
        user = random.choice(["glenn", "sarah", "james"])

        # Pick a random legitimate IP address
        ip = random.choice(good_ips)

        # Create the log entry and add it to the list
        lines.append(f"{t:%Y-%m-%d %H:%M:%S} INFO User {user} logged in from {ip}")


    # --- Simulate occasional background failed attempts ---
    # 25% chance of a failed login attempt
    if random.random() < 0.25:

        # Random time within the minute
        t = base_time + timedelta(seconds=random.randint(0, 59))

        # Random user attempt
        user = random.choice(users)

        # Random IP (could be attacker or legitimate user)
        ip = random.choice(bad_ips + good_ips)

        # Add failed login entry
        lines.append(f"{t:%Y-%m-%d %H:%M:%S} FAILED User {user} login attempt from {ip}")


    # --- Simulate a brute-force attack spike ---
    # Between minute 12 and 16 we generate many failed attempts
    if 12 <= minute <= 16:

        # Generate between 4 and 10 attempts per minute
        for _ in range(random.randint(4, 10)):

            # Random time within the minute
            t = base_time + timedelta(seconds=random.randint(0, 59))

            # Attackers often target privileged accounts
            user = random.choice(["admin", "root"])

            # Choose an attacker IP
            ip = random.choice(bad_ips)

            # Add brute-force log entry
            lines.append(f"{t:%Y-%m-%d %H:%M:%S} FAILED User {user} login attempt from {ip}")


# Sort the log lines chronologically
# Because timestamps are formatted YYYY-MM-DD HH:MM:SS, simple string sorting works
lines.sort()


# Write all generated log lines into a file called auth.log
with open("auth.log", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")


# Print confirmation showing how many log entries were generated
print(f"Wrote {len(lines)} log lines to auth.log")