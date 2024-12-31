#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_todo_list_progress(employee_id):
    """
    Fetches and prints the TODO list progress for a given employee from a REST API.

    Parameters:
    - employee_id (int): The unique identifier for the employee.

    The function prints:
    - The employee's name and their task completion status.
    - The titles of the completed tasks.
    """
    # Base URL for the API (replace with the actual URL if different)
    api_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information
    user_response = requests.get(f"{api_url}/users/{employee_id}")
    user_data = user_response.json()

    # Fetch todos information
    todos_response = requests.get(
        f"{api_url}/todos", params={"userId": employee_id})
    todos_data = todos_response.json()

    # Filter tasks based on completion status
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]

    # Output employee progress
    employee_name = user_data.get('name', 'Unknown')
    print(f"""Employee {employee_name} is done with tasks({
          len(completed_tasks)}/{total_tasks}):""")

    # Output titles of completed tasks
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    """
    Entry point of the script when run from the command line.
    Expects an employee ID as a command-line argument.
    """
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            get_todo_list_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID.")
    else:
        print("Usage: python script_name.py <employee_id>")
