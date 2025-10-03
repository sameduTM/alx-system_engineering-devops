#!/usr/bin/python3
import json
import sys
import urllib.request
"""Python script that returns information about a users todo
   list using REST API
"""

employee_id = int(sys.argv[1])
uri_todos = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
user_uri = 'https://jsonplaceholder.typicode.com/users'

with urllib.request.urlopen(user_uri) as f:
    data = f.read().decode('utf-8')

    users = json.loads(data)

    user = [x for x in users if x['id'] == employee_id]

    EMPLOYEE_NAME = user[0]['name']

with urllib.request.urlopen(uri_todos) as f:
    user_todos = f.read().decode('utf-8')

    user_todos = json.loads(user_todos)

    completed_tasks = [ct['title'] for ct in
                       user_todos if ct['completed'] is True]

    NUMBER_OF_DONE_TASKS = len(completed_tasks)

    TOTAL_NUMBER_OF_TASKS = len(user_todos)

tasks_progress = f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})"

print(f"Employee {EMPLOYEE_NAME} is done with tasks {tasks_progress}:")

for TASK_TITLE in completed_tasks:
    print(f"\t {TASK_TITLE}")
