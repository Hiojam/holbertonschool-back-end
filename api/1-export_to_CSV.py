#!/usr/bin/python3
"""
This script fetches exports information to CSV
Usage: python script_name.py employee_id
"""

import csv
import requests
import sys


def export_to_csv(employee_id):
    url = 'https://jsonplaceholder.typicode.com'
    base_url = f'{url}/users/{employee_id}'
    todos_url = f'{url}/todos?userId={employee_id}'

    try:
        employee_info = requests.get(base_url).json()
        todos = requests.get(todos_url).json()

        output_rows = []
        for task in todos:
            completed_status = "True" if task['completed'] else "False"
            output_rows.append([
                employee_info['id'],
                employee_info['name'],
                completed_status,
                task['title']
            ])

        file_name = f"{employee_info['id']}.csv"
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(output_rows)

        print(f"Data exported to {file_name}")

    except requests.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
