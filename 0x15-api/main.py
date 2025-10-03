#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""
import json
import requests
import sys

dct =  { "USER_ID": [ {
    "username": "USERNAME", 
    "task": "TASK_TITLE", 
    "completed": "TASK_COMPLETED_STATUS"}]
    }

print(json.dumps(dct))