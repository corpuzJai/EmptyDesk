import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

root = tk.Tk()
root.geometry("600x500") # Set window size
root.title("Empty Desk") # Set window title

# ----- Class Dropdown -----
classes = [
    "CSCI 199.2",
    "CSCI 60",
    "CSCI 70",
    "CSCI 41",
    "CSCI 50i",
    "DLQ 10",
    "ISCS 30.XX"
]
selected_class = tk.StringVar()
selected_class.set(classes[0])

class_dropdown = ttk.OptionMenu(root, selected_class, *classes)
class_dropdown.grid(row=0, column=0)

# ----- Calendar -----
cal = Calendar(root, selectmode='day', year=2025, month=8)
cal.grid(row=0, column=1)

# ----- Absent Counter -----
absents = {} # { "<Class>" : [Dates], etc. }

# ----- Label Status -----
class_status = tk.Label(root, text="", fg="white")
class_status.grid(row=1, column=0)

# ----- Functions -----
def add_absent():
    class_name = selected_class.get()
    date = cal.get_date()
    absents.setdefault(class_name, [])

    if date not in absents[class_name]:
        absents[class_name].append(date)
        class_status.config(text=f"Absent on {date} to {class_name}")
    else:
        class_status.config(text=f"{date} already marked as Absent in {class_name}", fg="orange")

def show_absents():
    class_name = selected_class.get()
    empty_desk = absents.get(class_name, [])
    class_status.config(text=f"{class_name} has {len(empty_desk)} cut(s): {', '.join(empty_desk)}", fg="light blue")

# ----- Buttons -----
add_absent_button = tk.Button(root, text="Add Absent", command=add_absent, pady=10)
add_absent_button.grid(row=2, column=1)

show_absents_button = tk.Button(root, text="Show Empty Desks", command=show_absents, pady=10)
show_absents_button.grid(row=3, column=1)




root.focus_force()
root.lift()
root.mainloop()