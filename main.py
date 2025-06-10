import tkinter as tk
from tkcalendar import Calendar, DateEntry

root = tk.Tk()
root.geometry("600x500") # Set window size
root.title("Empty Desk") # Set window title

# Functions
def addClass():
    newClass = tk.Label(root, text=entry.get())
    newClass.pack()


# Input Fields 
entry = tk.Entry(root)
# Creating Label Widget
myLabel = tk.Label(root,
                text="Hello World!",
                font=('Arial', 18)
                )

myLabel2 = tk.Label(root,
                text="This tracks class attendance"
                )

myButton = tk.Button(root,
                text="Add Class",
                padx=15,
                command=addClass
                )

# Adding Lable in screen
myLabel.pack()
myLabel2.pack()
myButton.pack()
entry.pack()

root.mainloop()