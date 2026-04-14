from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    print("Task added successfully!")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index >= 0 and index < len(tasks):
        tasks[index]["completed"] = True
    print("Task marked as complete!")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = []
    for task in tasks:
        if task["completed"] == False:
            pending.append(task)
    if len(pending) == 0:
        print("No pending tasks.")
    else:
        for i in range(len(pending)):
            print(i + 1, ". ", pending[i]["title"], " - Due: ", pending[i]["due_date"], sep="")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progres = 0
    else:
        completed = 0
        for task in tasks:
            if task["completed"] == True:
                completed += 1
        progres = (completed / len(tasks)) * 100
    return progres
