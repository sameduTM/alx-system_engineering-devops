#!/usr/bin/python3
"""Gather data from an API"""
import sys
import urllib3


def gather_data_from_an_API(empId):
    """Main function of our aoi function"""
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
