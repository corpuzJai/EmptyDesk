import tkinter as tk
from tkcalendar import Calendar, DateEntry

root = tk.Tk()
root.title("Empty Desk") # Set window title

e = tk.Entry(root, width=40, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

def btnClick(number):
    e.insert(tk.END, number)

def btnClear():
    e.delete(0, tk.END)    

def btnEqual():
    try:
        result = eval(e.get())
        e.delete(0, tk.END)
        e.insert(0, str(result))
    except Exception:
        e.delete(0, tk.END)
        e.insert(0, "Error")

# Button Layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create Button
for (text, row, col) in buttons:
    if text == '=':
        action = btnEqual
    elif text == 'C':
        action = btnClear
    else:
        action = lambda val=text: btnClick(val)
    tk.Button(root, text=text, width=5, height=2, command=action).grid(row=row, column=col, padx=5)


root.mainloop()