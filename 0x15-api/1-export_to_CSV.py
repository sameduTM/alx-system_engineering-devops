#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def rest_api(emp_id):
    """Main function of module"""
    s = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{emp_id}')
    r = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos')
    USER_ID = emp_id
    USERNAME = s.json()['username']
    filename = USER_ID + '.csv'

    with open(filename, 'w') as f:
        for item in r.json():
            TASK_COMPLETED_STATUS = item['completed']
            TASK_TITLE = item['title']
            csv_str = f'''"{USER_ID}","{USERNAME}","{
                TASK_COMPLETED_STATUS}","{TASK_TITLE}"'''

            f.write(csv_str + '\n')


if __name__ == '__main__':
    rest_api(sys.argv[1])
