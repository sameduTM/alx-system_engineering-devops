#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys

def export_to_JSON(USER_ID):
    """Records all tasks that are owned by this employee"""
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={USER_ID}"
    users_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"

    USERNAME = requests.get(users_url).json()["username"]
    tasks = []
    for item in requests.get(todos_url).json():
        TASK_TITLE = item["title"]
        TASK_COMPLETED_STATUS = item["completed"]
        tasks += [{"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS, "username": USERNAME}]
    tasks_dict = {USER_ID: tasks}
    
    with open(f"{USER_ID}.json", "w") as f:
        json.dump(tasks_dict, f)



if __name__ == "__main__":
    export_to_JSON(sys.argv[1])