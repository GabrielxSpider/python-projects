# List to store tasks
tasks = []

# Main program loop
while True:
    print("\n1 - Add task")
    print("2 - List tasks")
    print("3 - Remove task")
    print("4 - Exit")

    option = input("Choose an option: ")

    # Add a new task to the list
    if option == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")

    # Display all stored tasks
    elif option == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i, t in enumerate(tasks):
                print(f"{i} - {t}")

    # Remove a task based on its index
    elif option == "3":
        for i, t in enumerate(tasks):
            print(f"{i} - {t}")

        try:
            index = int(input("Enter the task index: "))
            tasks.pop(index)
            print("Task removed!")
        except:
            print("Invalid index.")

    # Exit the program
    elif option == "4":
        print("Exiting...")
        break

    # Handle invalid options
    else:
        print("Invalid option.")