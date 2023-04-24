import requests
import sys

employee_id = sys.argv[1]

response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

if response.status_code == 200:
    tasks = response.json()
    num_tasks = len(tasks)
    num_completed_tasks = sum(task['completed'] for task in tasks)
    employee_name = tasks[0]['username']
    
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{num_tasks}):")
    
    for task in tasks:
        if task['completed']:
            print(f"\t {task['title']}")
else:
    print("Error occurred while fetching TODO list for employee")
