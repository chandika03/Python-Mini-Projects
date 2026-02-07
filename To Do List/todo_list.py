tasks = []
def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done ")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter the task: ")
    tasks.append({"title":title, "done": False})

def view_task():
    if not tasks:
        print("There is no task yet")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. {task['title']} [{status}]")
def mark_done():
    view_task()
    index = int(input("Task number to mark done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
def delete_task():
    view_task()
    index = int(input("Task number you want to delete: ")) - 1
    if 0<=index<len(tasks):
        tasks.pop(index)

while True:
    show_menu()
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_done()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        print("Bye Bye 😭😭")
        break
    else:
        print("Invalid choice")
