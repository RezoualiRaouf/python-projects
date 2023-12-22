import tkinter as tk
from editor import TextEditor

def main():
    window = tk.Tk()
    window.title("Raouf's Text Editor")

    window.rowconfigure(0, minsize=600)
    window.columnconfigure(1, minsize=800)

    text_editor = TextEditor(window)

    window.mainloop()

if __name__ == "__main__":
    main()
