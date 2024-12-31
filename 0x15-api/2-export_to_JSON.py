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
    filename = emp_id + '.json'
    json_dict = {}
    USER_ID = emp_id
    USERNAME = s.json()['username']
    dict_val = {}
    item_list = []
    with open(filename, 'w') as f:
        for item in r.json():
            dict_val["task"] = item['title']
            dict_val["completed"] = item['completed']
            dict_val["username"] = USERNAME
            item_list.append(dict_val)
        json_dict[USER_ID] = item_list
        json.dump(json_dict, f)


if __name__ == '__main__':
    rest_api(sys.argv[1])
