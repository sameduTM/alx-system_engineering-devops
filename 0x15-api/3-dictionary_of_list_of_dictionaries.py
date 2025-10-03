#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys


def todo_all_employees():
    """Dictionary of list of dictionaries"""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    all_tasks_dict = {}
    for user in requests.get(users_url).json():
        USER_ID = user["id"]
        USERNAME = user["username"]
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={USER_ID}"
        tasks = []
        for item in requests.get(todos_url).json():
            TASK_TITLE = item["title"]
            TASK_COMPLETED_STATUS = item["completed"]
            tasks += [{"username": USERNAME, "task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS}]
        all_tasks_dict[USER_ID] = tasks

    with open("todo_all_employees.json", "w") as f:
        f.write(json.dumps(all_tasks_dict))

    

if __name__ == "__main__":
    todo_all_employees()