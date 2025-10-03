#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the CSV format.
"""
import json
import sys
import urllib.request


def export_to_CSV(USER_ID):
    """Records all tasks that are owned by this employee"""
    uri_todos = f'https://jsonplaceholder.typicode.com/todos?userId={USER_ID}'
    user_uri = 'https://jsonplaceholder.typicode.com/users'

    with urllib.request.urlopen(user_uri) as f:
        data = f.read().decode('utf-8')

        users = json.loads(data)

        user = [x for x in users if x.get('id') == USER_ID]

        USERN = json.dumps(user[0].get('username'))

    with urllib.request.urlopen(uri_todos) as f:
        user_todos = f.read().decode('utf-8')
        user_todos = json.loads(user_todos)

    todo_list = []
    for todo in user_todos:
        TASK_COMPLETED_STATUS = todo.get('completed')
        TASK_TITLE = todo.get('title')
        fmt = f'"{USER_ID}",{USERN},"{TASK_COMPLETED_STATUS}","{TASK_TITLE}"'
        todo_list.append(fmt)

    todo_list = "\n".join(todo_list)

    with open(f'{(USER_ID)}.csv', 'a') as f:
        f.writelines(todo_list)


if __name__ == "__main__":
    export_to_CSV(int(sys.argv[1]))
