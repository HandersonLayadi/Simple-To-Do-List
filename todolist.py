# Task data (JSON)

import json
import os

file_path = os.path.join(os.path.dirname(__file__), "tasks.json")


# Load tasks
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        tasks = json.load(file)
else:
    tasks = []


# Save tasks
def save_tasks():
    with open(file_path, "w") as file:
        json.dump(tasks, file)
