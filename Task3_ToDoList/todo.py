# tasks = []

# tasks.append("Create and schedule social media content")
# tasks.append("Design one creative post/poster for the week")
# tasks.append("Research current industry trends")
# tasks.append("Engage with Audience on social media platforms")
# tasks.append("Track performance and insights")

# print("Before Delete:", tasks)

# tasks.remove("Design one creative post/poster for the week")

# print("After Delete:", tasks)

# for task in tasks:
#     print(task)
tasks = []

while True:
    print("\n----- TO DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added!")

    elif choice == "2":
        print(tasks)

    elif choice == "3":
        task = input("Enter task to delete: ")
        tasks.remove(task)
        print("Task Deleted!")

    elif choice == "4":
        print("Goodbye!")
        break