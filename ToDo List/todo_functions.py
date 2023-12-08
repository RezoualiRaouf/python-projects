class ToDoList:
    def __init__(self):
        # Initialize the to-do list as a class attribute
        self.to_do_list = {}

    def add_task(self):
        # Method to add a task to the to-do list
        task = input("Enter the task you want to add: ")
        key_task = input("Enter the shortcut for your task: ")
        self.to_do_list[key_task] = task
        print("Task added:", self.to_do_list)

    def remove_task(self):
        # Method to remove a task from the to-do list
        if self.to_do_list:
            print("Current tasks:", self.to_do_list)
            key_task = input("Enter the shortcut of the task to remove: ")

            while key_task not in self.to_do_list:
                key_task = input("Invalid key. Enter another shortcut: ")

            self.to_do_list.pop(key_task)
            print("Task removed. Updated tasks:", self.to_do_list)
        else:
            print("There are no tasks to remove yet!")

    def view_tasks(self):
        # Method to view all tasks in the to-do list
        if self.to_do_list:
            print("Current tasks:", self.to_do_list)
        else:
            print("There are no tasks to view yet!")

    def exit_application(self):
        # Method to exit the to-do list application
        print("Thanks for using our software.")