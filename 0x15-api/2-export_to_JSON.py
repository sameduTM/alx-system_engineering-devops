#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def rest_api(emp_id):
    """Main function of module"""
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    response = requests.get(url)
    user = response.json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(emp_id)
    response = requests.get(url)
    todos = response.json()
    data = {emp_id: []}
    for todo in todos:
        task = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": user.get('username')
        }
        data[emp_id].append(task)
    with open('{}.json'.format(emp_id), 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    rest_api(sys.argv[1])
