import tkinter as tk
from tkinter import filedialog
import os
import git

class TextEditor:
    def __init__(self, window):
        """
        Initialize the TextEditor instance.

        Parameters:
        - window (tk.Tk): The main Tkinter window.
        """
        self.window = window
        self.filepath = None
        self.text_stack = []
        self.current_filename = "Main Text Area"
        self.repo_path = git.Repo(search_parent_directories=True).working_tree_dir
        
        # Configure the window
        self.window.rowconfigure(0, minsize=600)
        self.window.columnconfigure(1, minsize=800)

        # Create the text editing area
        self.txt_edit = tk.Text(self.window, height=10, width=50)
        self.txt_edit.grid(column=1, row=0, sticky="news")

        # Create the frame for buttons
        self.frame_btn = tk.Frame(self.window, bd=2, width=200, height=200)
        self.frame_btn.grid(column=0, row=0, sticky="nw")

        # Define buttons
        self.btn_newfile = tk.Button(self.frame_btn, text="New file", fg="#FF8E00", background="white", width=10,
                                command=self.new_file)
        self.btn_open = tk.Button(self.frame_btn, text="Open file", fg="blue", background="Lightblue", width=10,
                                command=self.open_file)
        self.btn_reset = tk.Button(self.frame_btn, text="Reset text", fg="Black", background="tomato", width=10,
                                command=self.reset_text)
        self.btn_save = tk.Button(self.frame_btn, text="Save file", fg="Black", background="lemon chiffon", width=10,
                                command=self.save_file)
        self.btn_undo = tk.Button(self.frame_btn, text="Undo", fg="Black", background="cyan", width=10,
                                command=self.undo)
        self.btn_add_commit = tk.Button(self.frame_btn, text="Add&Commit", fg="Black", width=10, 
                                command=self.Add_commit)
        self.btn_push = tk.Button(self.frame_btn, text="Push file", fg="Black", width=10, 
                                command= self.push_to_remote)

        # Grid layout for buttons
        self.btn_newfile.grid(column=0, row=0, sticky="n", pady=6)
        self.btn_open.grid(column=0, row=1, sticky="n", pady=6)
        self.btn_reset.grid(column=0, row=2, sticky="n", pady=6)
        self.btn_save.grid(column=0, row=3, sticky="n", pady=6)
        self.btn_undo.grid(column=0, row=4, sticky="n", pady=6)
        self.btn_add_commit.grid(column=0, row=5, sticky="n", pady=6)
        self.btn_push.grid(column=0, row=8, sticky="n", pady=6)

        # Bind key release event to track_changes method
        self.window.bind("<KeyRelease>", self.track_changes)

        # Create label to display the current file name
        self.lbl_filename = tk.Label(self.window, text=f"Current File: {self.current_filename}", font=("Arial", 12),
                                     background="lightblue")
        self.lbl_filename.grid()

        # Create entry to enter the commit message
        self.entry_commit_msg = tk.Entry(self.frame_btn, width=24)
        self.entry_commit_msg.grid(column=0, row=7, padx=10, pady=8)

        # Create a lable to display that the entry text is only for commit msg
        self.lbl_commit_msg = tk.Label(self.frame_btn,text= "enter your commit msg here:", font=("Arial", 12))
        self.lbl_commit_msg.grid(column=0, row= 6, padx=10, pady=8)

    def update_filename(self):
        """
        Update the label displaying the current file name.
        """
        self.lbl_filename.config(text=f"Current File: {os.path.basename(self.current_filename)}")

    def track_changes(self, event):
        """
        Track changes in the text content and update the filename label.
        """
        current_content = str(self.txt_edit.get("1.0", tk.END))
        self.text_stack.append(current_content)
        self.update_filename()

    def open_file(self):
        """
        Open a file and update the text area.
        """
        self.filepath = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("Text file", ".txt"),
                                                               ("html file", ".html"),
                                                               ("Readme file", ".md"),
                                                               ("Python file", ".py"),
                                                               ("c file", ".c"),
                                                               ("All files", "*.*")
                                                                ]
                                                    )
        if self.filepath:
            with open(self.filepath, "r") as file:
                self.txt_edit.delete("1.0", tk.END)
                self.txt_edit.insert(tk.END, file.read())
                self.text_stack.clear()
            self.current_filename = self.filepath
            self.update_filename()

    def new_file(self):
        """
        Create a new file and update the text area.
        """
        self.filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                                      filetypes=[("Text file", ".txt"),
                                                                 ("html file", ".html"),
                                                                 ("Readme file", ".md"),
                                                                 ("Python file", ".py"),
                                                                 ("c file", ".c"),
                                                                 ("All files", "*.*")
                                                                ]
                                                    )
        if self.filepath:
            with open(self.filepath, "w") as file:
                self.txt_edit.delete("1.0", tk.END)
                self.text_stack.clear()
            self.current_filename = self.filepath
            
            self.update_filename()

    def save_file(self):
        """
        Save the content to the current file.
        """
        if self.filepath:
            file_content = str(self.txt_edit.get("1.0", tk.END))
            with open(self.filepath, "w") as file:
                file.write(file_content)
            self.update_filename()
        else:
        # If the user cancels the file dialog, set self.filepath to an empty string
            self.filepath = ""

    def reset_text(self):
        """
        Reset the text area.
        """
        self.txt_edit.delete("1.0", tk.END)
        self.text_stack.clear()
        self.current_filename = "Main Text Area"
        self.update_filename()

    def undo(self):
        """
        Undo the last change in the text area.
        """
        if self.text_stack:
            undo_data = self.text_stack.pop()
            self.txt_edit.delete("1.0", tk.END)
            self.txt_edit.insert(tk.END, undo_data)
        self.update_filename()

    def Add_commit(self):
        entered_text = self.entry_commit_msg.get()

        if entered_text:
            if self.filepath:  # Ensure self.filepath is not None or an empty string
                repo_path = git.Repo(search_parent_directories=True).working_tree_dir
                repo = git.Repo(repo_path)

                file_path_to_add = os.path.relpath(self.filepath, repo_path)
                
                try:
                    # Commit changes
                    repo.index.add(file_path_to_add)
                    repo.index.commit(entered_text)
                    tk.messagebox.showinfo("Commit Successful", "Commit operation completed successfully.")

                    # Push to remote
                    self.push_to_remote(repo)
                except git.exc.GitCommandError as commit_error:
                    tk.messagebox.showerror("Commit Failed", f"Commit operation failed: {commit_error}")
            else:
                tk.messagebox.showerror("Error", "File path not set. Save the file before committing.")

    def push_to_remote(self, repo):
        branch_name = 'main'
        remote_name = 'origin'
        origin = repo.remotes[remote_name]

        try:
            origin.push(branch_name)
            tk.messagebox.showinfo("Push Successful", "Push operation completed successfully.")
        except git.exc.GitCommandError as push_error:
            tk.messagebox.showerror("Push Failed", f"Push operation failed: {push_error}")

