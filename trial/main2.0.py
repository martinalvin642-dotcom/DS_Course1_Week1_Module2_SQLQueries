# Import functions from task_manager.task_utils package
from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
from validation import validate_task_title, validate_task_description, validate_due_date

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            title = input("Enter task title: ")
            if not validate_task_title(title):
                print("Invalid title. Title cannot be empty.")
            else:
                description = input("Enter task description: ")
                if not validate_task_description(description):
                    print("Invalid description. Description cannot be empty.")
                else:
                    due_date = input("Enter due date (YYYY-MM-DD): ")
                    if not validate_due_date(due_date):
                        print("Invalid date. Please use YYYY-MM-DD format.")
                    else:
                        add_task(title, description, due_date)
        elif choice == "2":
            view_pending_tasks()
            index = input("Enter task number to mark as complete: ")
            if len(index) == 0:
                print("Invalid input.")
            else:
                mark_task_as_complete(int(index) - 1)
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            progress = calculate_progress()
            print("Progress:", round(progress, 2), "%")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
