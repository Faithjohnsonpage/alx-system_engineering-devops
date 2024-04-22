#!/usr/bin/python3
"""This script uses a REST API  for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys


if __name__ == '__main__':
    response1 = requests.get('https://jsonplaceholder.typicode.com/users/')
    response2 = requests.get('https://jsonplaceholder.typicode.com/todos/')
    response1 = response1.json()
    response2 = response2.json()

    employee_id = int(sys.argv[1])

    total_tasks = 0
    task_completed = 0

    for task in response2:
        if task.get('userId') == employee_id:
            total_tasks += 1
            if task.get('completed') is True:
                task_completed += 1

    for user in response1:
        if user.get('id') == employee_id:
            user_info = "Employee {} is done with tasks({}/{}):".\
                format(user.get('name'), task_completed, total_tasks)

    print(user_info)
    for task in response2:
        if task.get('userId') == employee_id:
            if task.get('completed') is True:
                print("\t {}".format(task.get('title')))
