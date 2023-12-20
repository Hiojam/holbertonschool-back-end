#!/usr/bin/python3
"""
This script fetches exports information to Json
Usage: python script_name.py employee_id
"""

import requests
import json


def export_tasks():
    # Fetching data from the API
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = response.json()

    # Creating a dictionary to store tasks for each user
    all_tasks = {}
    for task in tasks:
        user_id = task['userId']
        task_info = {
            "username": task['title'],
            "task": task['title'],
            "completed": task['completed']
        }
        # Checking if the user_id key exists in the dictionary
        # If it exists, append the task_info to the existing list
        if user_id in all_tasks:
            all_tasks[user_id].append(task_info)
        else:
            all_tasks[user_id] = [task_info]

    # Exporting tasks to JSON files for each user
    for user_id, user_tasks in all_tasks.items():
        filename = f"{user_id}.json"
        with open(filename, 'w') as file:
            json.dump(user_tasks, file, indent=2)

    # Exporting all tasks to a single JSON file
    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    export_tasks()
