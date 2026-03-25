# Import the datetime module for working with timestamps
from datetime import datetime

# Import matplotlib so we can create graphs of the attack activity
import matplotlib.pyplot as plt


# Dictionary to store number of failed login attempts per IP address
# Example format:
# { "203.0.113.77": 12, "10.0.0.8": 6 }
ip_failures = {}

# Dictionary to store number of failed attempts per minute
# Example format:
# { "07:12": 8, "07:13": 10 }
minute_failures = {}


# Open the log file in read mode
with open("auth.log", "r") as file:

    # Loop through each line in the log file
    for line in file:

        # We only care about failed login attempts
        if "FAILED" in line:

            # Split the line into parts using spaces
            parts = line.split()

            # Extract the timestamp (date + time)
            date = parts[0]
            time = parts[1]

            # Extract the IP address (last element in the line)
            ip = parts[-1]

            # Convert the timestamp into a datetime object
            timestamp = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")

            # Extract the minute (HH:MM) to track activity per minute
            minute = timestamp.strftime("%H:%M")


            # -----------------------------
            # Count failed attempts per IP
            # -----------------------------
            if ip in ip_failures:
                ip_failures[ip] += 1
            else:
                ip_failures[ip] = 1


            # ---------------------------------
            # Count failed attempts per minute
            # ---------------------------------
            if minute in minute_failures:
                minute_failures[minute] += 1
            else:
                minute_failures[minute] = 1


# -----------------------------
# Print attack summary
# -----------------------------

print("Failed Login Attempts by IP:")

# Loop through IP dictionary and display results
for ip, count in ip_failures.items():
    print(ip, "->", count)

# -----------------------------
# Detect possible brute force attacks
# -----------------------------

print("\nPossible Brute Force Alerts:")

# Loop through each IP and check how many failed attempts it has
for ip, count in ip_failures.items():

    # If an IP has more than 10 failed attempts, flag it
    if count > 10:

        print("ALERT:", ip, "has", count, "failed login attempts")

print("\nFailed Attempts Per Minute:")

# Loop through minute dictionary
for minute, count in minute_failures.items():
    print(minute, "->", count)


# -----------------------------
# Create graph of attack spike
# -----------------------------

# Convert dictionary keys and values into lists for plotting
minutes = list(minute_failures.keys())
counts = list(minute_failures.values())


# Create a line graph showing failed attempts over time
plt.figure(figsize=(10,5))

plt.plot(minutes, counts, marker='o')

# Graph labels
plt.title("Failed Login Attempts Per Minute")
plt.xlabel("Time (Minute)")
plt.ylabel("Number of Failed Logins")

# Rotate x-axis labels so they are readable
plt.xticks(rotation=45)

# Adjust layout to prevent label overlap
plt.tight_layout()

# Display the graph
plt.show()