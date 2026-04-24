from management import add_task, list_tasks, remove_task

tasks = []
while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("\nEnter the task: ")
        add_task(task, tasks)
    elif choice == '2':
        list_tasks(tasks)
    elif choice == '3':
        try:
            task_number = int(input("\nEnter the task number to remove: "))
            remove_task(task_number, tasks)
        except ValueError:
            print("\nPlease enter a valid number.")
    elif choice == '4':
        print("\nExiting Task Manager.")
        break
    else:
        print("\nInvalid option. Please try again.")



