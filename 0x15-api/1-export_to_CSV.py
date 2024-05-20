#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress and exports data in CSV format"""

import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        userId = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    if user.status_code != 200:
        print(f"Failed to retrieve employee data for ID {userId}")
        sys.exit(1)

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(userId))
    if todos.status_code != 200:
        print(f"Failed to retrieve TODO list for employee ID {userId}")
        sys.exit(1)

    totalTasks = 0
    completed = 0
    completed_tasks_titles = []

    tasks = todos.json()
    for task in tasks:
        totalTasks += 1
        if task.get('completed'):
            completed += 1
            completed_tasks_titles.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    for title in completed_tasks_titles:
        print("\t {}".format(title))

    # Export to CSV
    csv_filename = "{}.csv".format(userId)
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': userId,
                'USERNAME': name,
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })

    print(f"Data exported to {csv_filename}")

