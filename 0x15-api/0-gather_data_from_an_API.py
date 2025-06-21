#!/usr/bin/python3
"""
This module retrieves and displays the TODO list progress for a given employee ID
by querying a REST API (https://jsonplaceholder.typicode.com/).

The script fetches the employee's name and their list of tasks, then displays the
number of completed tasks out of the total, along with the titles of the completed tasks.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>
"""
import sys
import urllib3


def gather_data_from_an_API(empId):
    """
    Fetches and displays TODO list progress for a given employee.

    Args:
        empId (str): The employee's ID.

    Retrieves the employee's name and list of tasks via API requests,
    then prints the number of completed tasks out of the total,
    followed by the titles of the completed tasks.
    """
    if empId is not int:
        print("Error: employee ID must be an integer")
        return
    url = f"https://jsonplaceholder.typicode.com/todos?userId={empId}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{empId}"
    response = urllib3.request("GET", url)
    user_resp = urllib3.request("GET", user_url)
    tasks = response.json()
    
    # all tasks
    y = len(response.json())
    
    # completed tasks
    x = len([
        item for item in response.json() if item["completed"] == True])

    print(
        f"Employee {user_resp.json()["name"]}is done with tasks({x}/{y}):")
    for item in tasks:
        if item["completed"] == True:
            print(f"\t{item["title"]}")


if __name__ == "__main__":
    empId = sys.argv[1]
    gather_data_from_an_API(empId)
