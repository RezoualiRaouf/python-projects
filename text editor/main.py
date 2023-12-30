import tkinter as tk

from editor import TextEditor

def main():
    app_title = "Raouf's Text Editor"
    window = tk.Tk()
    window.title(app_title)

    window.rowconfigure(0, minsize=600)
    window.columnconfigure(1, minsize=800)

    text_editor = TextEditor(window)

    window.mainloop()

if __name__ == "__main__":
    main()

