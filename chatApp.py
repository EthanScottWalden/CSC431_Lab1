import os
from datetime import datetime

# Define team details
team_name = "PhishersOfMen"
team_members = ["Elijah Salgado", "Brendon Mwamba", "Ethan Walden", "Savannah Punak"]

# Define the file path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, f"{team_name}.txt")

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to file
with open(file_path, "w") as file:
    file.write(f"Team Members:\n{', '.join(team_members)}\n")
    file.write(f"Timestamp: {timestamp}\n")

print(f"File written to {file_path}")


"""
In order to download our new ChatApp, You must follow the list of instructions
    1. Make sure you have python installed on your local machine.
        (If not this link will take you to the website to download python https://www.python.org/downloads/windows/)
    2. Open your terminal or command line
    3. Go to the directory where you installed the chatApp.py file
    4. Run this code (exclude the "") "python chatApp.py
    5. The application should be installed onto your desktop
    6. Open the application and start chatting away with classmates!
"""