#!/usr/bin/python3
"""
This script fetches exports information to Json
Usage: python script_name.py employee_id
"""

import json
import requests
import sys


def export_to_json(employee_id):
    url = 'https://jsonplaceholder.typicode.com'
    base_url = f'{url}/users/{employee_id}'
    todos_url = f'{url}/todos?userId={employee_id}'

    try:
        employee_info = requests.get(base_url).json()
        todos = requests.get(todos_url).json()

        tasks = []
        for task in todos:
            task_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_info['username']
            }
            tasks.append(task_data)

        output_data = {str(employee_id): tasks}

        file_name = f"{employee_id}.json"
        with open(file_name, 'w') as file:
            json.dump(output_data, file, indent=2)

        print(f"Data exported to {file_name}")

    except requests.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
