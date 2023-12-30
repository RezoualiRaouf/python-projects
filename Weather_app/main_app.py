import tkinter as Tk
from Weather_info import Weather

if __name__ == "__main__":
    
    Window = Tk.Tk()
    app = Weather(Window)
    Window.mainloop()
