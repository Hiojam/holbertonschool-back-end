import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        employee_info = requests.get(base_url).json()
        todos = requests.get(todos_url).json()

        # Filter completed tasks
        completed_tasks = [task['title'] for task in todos if task['completed']]
        total_tasks = len(completed_tasks) + len(todos) - len(completed_tasks)

        # Display progress
        print(f"Employee {employee_info['name']} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task}")

    except requests.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
