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

def btnAdd():
    firstNum = e.get()
    global fNum 
    global math
    math = "add"
    fNum = int(firstNum)
    e.delete(0, tk.END)

def btnEqual():
    secondNum = e.get()
    e.delete(0, tk.END)

    if math == "add":
        e.insert(0, fNum + int(secondNum))
    elif math == "subtract":
        e.insert(0, fNum - int(secondNum))
    elif math == "multiply":
        e.insert(0, fNum * int(secondNum))
    elif math == "divide":
        e.insert(0, fNum / int(secondNum))

def btnSubtract():
    firstNum = e.get()
    global fNum 
    global math
    math = "subtract"
    fNum = int(firstNum)
    e.delete(0, tk.END)

def btnMultiply():
    firstNum = e.get()
    global fNum 
    global math
    math = "multiply"
    fNum = int(firstNum)
    e.delete(0, tk.END)

def btnDivide():
    firstNum = e.get()
    global fNum 
    global math
    math = "divide"
    fNum = int(firstNum)
    e.delete(0, tk.END)


# Define buttons
button_1=tk.Button(root, text="1", padx =40, pady=20, command=lambda: btnClick(1))
button_2=tk.Button(root, text="2", padx =40, pady=20, command=lambda: btnClick(2))
button_3=tk.Button(root, text="3", padx =40, pady=20, command=lambda: btnClick(3))
button_4=tk.Button(root, text="4", padx =40, pady=20, command=lambda: btnClick(4))
button_5=tk.Button(root, text="5", padx =40, pady=20, command=lambda: btnClick(5))
button_6=tk.Button(root, text="6", padx =40, pady=20, command=lambda: btnClick(6))
button_7=tk.Button(root, text="7", padx =40, pady=20, command=lambda: btnClick(7))
button_8=tk.Button(root, text="8", padx =40, pady=20, command=lambda: btnClick(8))
button_9=tk.Button(root, text="9", padx =40, pady=20, command=lambda: btnClick(9))
button_0=tk.Button(root, text="0", padx =40, pady=20, command=lambda: btnClick(0))

button_add=tk.Button(root, text="+", padx=40, pady="20", command=btnAdd)
button_subtract=tk.Button(root, text="-", padx=40, pady="20", command=btnSubtract)
button_multiply=tk.Button(root, text="*", padx=40, pady="20", command=btnMultiply)
button_divide=tk.Button(root, text="/", padx=40, pady="20", command=btnDivide)
button_equal=tk.Button(root, text="=", padx=40, pady="20", command=btnEqual)
button_clear=tk.Button(root, text="CLR", padx=30, pady="20", command=btnClear)

# Put buttons on window
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)

button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=0)

root.mainloop()