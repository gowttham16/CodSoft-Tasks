tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4) : ")

    # Add Task

    if choice == "1":
        task = input("Enter the task : ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    # Remove Task

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

            try:
                task_number = int(input("Enter task number to remove : "))
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully!")
            except:
                print("Invalid task number.")

    # Exit Program
    
    elif choice == "4":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")