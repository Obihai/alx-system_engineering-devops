#!/usr/bin/python3
"""
This script accesses a REST API to retrieve the to-do list progress of an employee given their ID
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    # Set up the base URL and the full URL for the employee with the given ID
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = "{}/{}".format(base_url, employee_id)

    # Get the employee's name
    response = requests.get(url)
    employee_name = response.json().get('name')

    # Get the to-do list for the employee
    todo_url = "{}/todos".format(url)
    response = requests.get(todo_url)
    tasks = response.json()

    # Calculate the number of completed tasks and the list of completed task titles
    done = 0
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    # Print the employee's to-do list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, done, len(tasks)))
    for task in done_tasks:
        print("\t{}".format(task.get('title')))


if __name__ == '__main__':
    # Get the employee ID from the command line argument and call the function to retrieve the progress
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
