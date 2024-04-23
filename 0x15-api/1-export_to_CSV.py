#!/usr/bin/python3
"""This script uses a REST API  for a given employee ID,
exports employee's data in CSV format."""
import csv
import requests
import sys


if __name__ == '__main__':
    response1 = requests.get('https://jsonplaceholder.typicode.com/users/')
    response2 = requests.get('https://jsonplaceholder.typicode.com/todos/')
    response1 = response1.json()
    response2 = response2.json()

    employee_id = int(sys.argv[1])
    file_name = f"{employee_id}.csv"

    dict_task = {}

    for index, task in enumerate(response2):
        if task.get('userId') == employee_id:
            # Create a dictionary at each index with the task details
            dict_task[index] = {
                'completed': task.get('completed'),
                'title': task.get('title')
            }

    username = ''
    for user in response1:
        if user.get('id') == employee_id:
            username = user.get('username')
            break

    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer_obj = csv.writer(f, quoting=csv.QUOTE_ALL)
        for value in dict_task.values():
            writer_obj.writerow([employee_id, username,
                                value['completed'], value['title']])
