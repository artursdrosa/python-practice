def add_task(task, tasks):
    tasks.append(task)
    print(f'\nTask "{task}" added.')
    return
    
def list_tasks(tasks):
    if not tasks:
        print("\nNo tasks to display.")
        return
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        return

def remove_task(task_number, tasks):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'\nTask "{removed_task}" removed.')
        return
    else:
        print("\nInvalid task number.")
        return