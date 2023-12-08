# This is a to-do list Python script

# Use a dictionary to store tasks with shortcuts for easy removal
to_do_list = {}

print("----------How to use our to-do list----------\nCommands:")
print("add -> adds a task \nremove -> removes a task \nview -> view all tasks \nexit -> exit software")

while True:
    # Get user input for the desired command
    user_input = input("Enter the command you want: ").lower()

    if user_input == "add":
        # Add a task to the to-do list
        task = input("Enter the task you want to add: ")
        key_task = input("Enter the shortcut for your task: ")
        to_do_list[key_task] = task
        print("Task added:", to_do_list)

    elif user_input == "remove":
        # Remove a task from the to-do list
        if to_do_list:
            print("Current tasks:", to_do_list)
            key_task = input("Enter the shortcut of the task to remove: ")

            while key_task not in to_do_list:
                key_task = input("Invalid key. Enter another shortcut: ")

            to_do_list.pop(key_task)
            print("Task removed. Updated tasks:", to_do_list)
        else:
            print("There are no tasks to remove yet!")

    elif user_input == "view":
        # View all tasks in the to-do list
        if to_do_list:
            print("Current tasks:", to_do_list)
        else:
            print("There are no tasks to view yet!")

    elif user_input == "exit":
        # Exit the to-do list application
        print("Thanks for using our software.")
        break

    else:
        # Handle invalid commands
        print("Invalid command. Please try again.")