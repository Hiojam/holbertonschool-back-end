#!/usr/bin/python3
"""
This script fetches information about an employee's TODO list progress.
Usage: python script_name.py employee_id
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    url = 'https://jsonplaceholder.typicode.com'
    base_url = f'{url}/users/{employee_id}'
    todos_url = f'{url}/todos?userId={employee_id}'

    try:
        employee_info = requests.get(base_url).json()
        todos = requests.get(todos_url).json()

        # Filter completed tasks
        completed_tasks = [
            task['title'] for task in todos if task['completed']
            ]
        total_tasks = len(todos)

        # Display progress
        output = [
            f"Employee {employee_info['name']} is done with tasks"
            f"({len(completed_tasks)}/{total_tasks}):"
        ]

        for task in completed_tasks:
            output.append(f"\t {task}")

        return "\n".join(output)

    except requests.RequestException as e:
        return f"Error: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    print(get_employee_todo_progress(employee_id))
