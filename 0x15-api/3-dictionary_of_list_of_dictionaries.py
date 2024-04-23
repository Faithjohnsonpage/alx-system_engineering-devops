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
    users = response1.json()
    todos = response2.json()

    file_name = "todo_all_employees.json"

    final_dict = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        task_list = []  # Create a new list for each user

        for task in todos:
            if task['userId'] == user_id:
                task_dict = {
                    'username': username,
                    'task': task.get('title'),
                    'completed': task.get('completed')
                }
                task_list.append(task_dict)

        final_dict[user_id] = task_list

    # Write JSON data to the file
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(final_dict, f)
