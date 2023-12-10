from todo_functions import ToDoList

def main():
    # Create an instance of the ToDoList class
    todo_list_instance = ToDoList()

    # Main loop
    while True:
        user_input = input("Enter the command you want: ").lower()

        if user_input == "add":
            todo_list_instance.add_task()

        elif user_input == "remove":
            todo_list_instance.remove_task()

        elif user_input == "view":
            todo_list_instance.view_tasks()

        elif user_input == "exit":
            todo_list_instance.exit_application()
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()