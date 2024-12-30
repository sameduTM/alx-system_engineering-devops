#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def rest_api():
    """Main function of module"""
    s = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}')
    r = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{sys.argv[1]}/todos')
    EMPLOYEE_NAME = s.json()['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(r.json())
    for item in r.json():
        if item['completed'] is True:
            NUMBER_OF_DONE_TASKS += 1

    print(f'''Employee {EMPLOYEE_NAME} is done with tasks ({
        NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})''')

    for item in r.json():
        if item['completed'] is True:
            print('    ', item['title'])


if __name__ == '__main__':
    rest_api()
