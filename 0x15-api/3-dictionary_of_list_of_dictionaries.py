#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys


def rest_api():
    """Main function of module"""
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()
    users_dict = {}
    for user in users:
        user_id = user.get('id')
        user_name = user.get('username')
        url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        todos = requests.get(url).json()
        todos_list = []
        for todo in todos:
            todos_list.append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": user_name
            })
        users_dict[user_id] = todos_list
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)


if __name__ == '__main__':
    rest_api()
