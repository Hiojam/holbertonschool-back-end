#!/usr/bin/python3
"""
This script fetches returns information about a user TODO list
Usage: python script_name.py employee_id
"""

import json
import requests


def export_tasks(employee):
    # Fetching data from the API
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee["id"]}'
        )
    tasks = response.json()

    # Creating an array to store tasks for each user
    all_tasks = []
    for task in tasks:
        task_info = {
            "username": employee['username'],
            "task": task['title'],
            "completed": task['completed']
        }

        all_tasks.append(task_info)

    return all_tasks


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(f'{base_url}/users/').json()

    json_data = {}
    for employee in users:
        json_data[f"{employee['id']}"] = export_tasks(employee)

    # Exporting all tasks to a single JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_data, file, indent=2)
