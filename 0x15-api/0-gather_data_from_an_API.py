#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def gather_data_from_api(empId):
    """Main function of module"""
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={empId}"
    users_url = f"https://jsonplaceholder.typicode.com/users/{empId}"

    EMPLOYEE_NAME = requests.get(users_url).json()["name"]
    TOTAL_NUMBER_OF_TASKS = len(requests.get(todos_url).json())
    NUMBER_OF_DONE_TASKS = len([i for i in requests.get(todos_url).json()
                                 if i["completed"] == True])
    
    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks"
        f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    )
    for item in requests.get(todos_url).json():
        if item["completed"] == True:
            TASK_TITLE = item["title"]
            print(f"\t {TASK_TITLE}")
    

if __name__ == "__main__":
    gather_data_from_api(sys.argv[1])