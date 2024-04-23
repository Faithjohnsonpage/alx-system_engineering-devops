#!/usr/bin/python3
"""This script uses a REST API  for a given employee ID,
exports employee's data in JSON format."""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    response1 = requests.get('https://jsonplaceholder.typicode.com/users/')
    response2 = requests.get('https://jsonplaceholder.typicode.com/todos/')
    response1 = response1.json()
    response2 = response2.json()

    employee_id = int(sys.argv[1])
    file_name = f"{employee_id}.json"

    username = ''
    for user in response1:
        if user.get('id') == employee_id:
            username = user.get('username')
            break

    task_dict = {}
    tasks_list = []

    # Collect all tasks for this user
    for task in response2:
        if task.get('userId') == employee_id:
            task_dict = {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            }
            tasks_list.append(task_dict)

    # Dictionary to write in JSON file
    final_dict = {employee_id: tasks_list}

    # Write JSON data to the file
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(final_dict, f)
