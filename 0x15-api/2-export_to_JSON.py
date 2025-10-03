#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import urllib.request
import sys


def export_to_JSON(USER_ID):
    """Records all tasks that are owned by this employee"""
    uri_todos = f'https://jsonplaceholder.typicode.com/todos?userId={USER_ID}'
    user_uri = 'https://jsonplaceholder.typicode.com/users'

    with urllib.request.urlopen(user_uri) as f:
        data = f.read().decode('utf-8')

        users = json.loads(data)

        user = [x for x in users if x.get('id') == USER_ID]

        USERNAME = user[0].get('username')

    with urllib.request.urlopen(uri_todos) as f:
        user_todos = f.read().decode('utf-8')
        user_todos = json.loads(user_todos)

    user_todo_list = []
    for todo in user_todos:
        fmt = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": todo.get('username')
        }
        user_todo_list.append(fmt)

    with open(f'{USER_ID}', 'a') as jsonfile:
        json.dump({f'{USER_ID}': user_todo_list}, jsonfile)


if __name__ == "__main__":
    export_to_JSON(int(sys.argv[1]))
