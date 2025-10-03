#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the CSV format.
"""
import requests
import sys

def export_to_CSV(USER_ID):
    """Records all tasks that are owned by this employee"""
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={USER_ID}"
    users_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    with open(f"{USER_ID}.csv", "w") as f:
        USERNAME = requests.get(users_url).json()["username"]
        for item in requests.get(todos_url).json():
            f.write(f'"{USER_ID}", "{USERNAME}", "{item["completed"]}", "{item["title"]}"\n')

if __name__ == "__main__":
    export_to_CSV(sys.argv[1])