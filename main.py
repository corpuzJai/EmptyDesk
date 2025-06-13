import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar

root = tk.Tk()
root.geometry("580x400") # Set window size
root.title("Empty Desk") # Set window title

# ----- Class Dropdown -----
# classes = [
#     "CSCI 199.2",
#     "CSCI 60",
#     "CSCI 70",
#     "CSCI 41",
#     "CSCI 50i",
#     "DLQ 10",
#     "ISCS 30.XX"
# ]
classes = []
selected_class = tk.StringVar()
if not classes:
    selected_class.set("No Classes, add one now!")
else:
    selected_class.set(classes[0])

menu_options = classes if classes else["No classes"]
class_dropdown = tk.OptionMenu(root, selected_class, *menu_options)
class_dropdown.grid(row=0, column=0)

# ----- Calendar -----
cal = Calendar(root, font="Helvetica 14", selectmode='day', year=2025, month=8)
cal.grid(row=0, column=1)

# ----- Absent Counter -----
absents = {} # { "<Class>" : [Dates], etc. }

# ----- Label Status -----
class_status = tk.Label(root, text="", bg="grey", fg="white", width=30, height=10, wraplength=100)
class_status.grid(row=1, column=0, rowspan=3)

# ----- Functions -----
def add_course_window():
    def save_course():
        course = course_entry.get()
        prof = prof_entry.get()
        email = email_entry.get()
        room = room_entry.get()
        limit = limit_entry.get()

        if not course or not limit.isdigit():
            tk.messagebox.showerror("Invalid Input", "Please class name and valid number")
            return

        absents[course] = {
            "dates": [],
            "limit": int(limit),
            "prof": prof,
            "email": email,
            "room": room
        }

        messagebox.showinfo("Sucess!", f"Class '{course}' added.")
        add_course_window.destroy()
        update_class_dropdown()

    add_course_window = tk.Toplevel(root)
    add_course_window.title("Add New Class")
    add_course_window.geometry("300x250")

    course_name = tk.Label(add_course_window, text="Class Name: ")
    course_entry = tk.Entry(add_course_window)
    course_name.grid(row =0, column =0)
    course_entry.grid(row=0, column=1)

    prof_name = tk.Label(add_course_window, text="Professor: ")
    prof_entry = tk.Entry(add_course_window)
    prof_name.grid(row=1, column =0)
    prof_entry.grid(row=1, column=1)

    email_ad= tk.Label(add_course_window, text="Email: ")
    email_entry = tk.Entry(add_course_window)
    email_ad.grid(row=2, column =0)
    email_entry.grid(row=2, column =1)

    room_num = tk.Label(add_course_window, text="Room: ")
    room_entry = tk.Entry(add_course_window)
    room_num.grid(row=3, column =0)
    room_entry.grid(row=3, column =1)

    limit_num = tk.Label(add_course_window, text="Cut Limit: ")
    limit_entry = tk.Entry(add_course_window)
    limit_num.grid(row=4, column =0)
    limit_entry.grid(row=4, column =1)

    add_course_button = tk.Button(add_course_window, text="Add Course", command = save_course)
    add_course_button.grid(row=5, column=1)

def remove_course_window():
    def remove_course():
        return
    return

def update_class_dropdown():
    menu = class_dropdown["menu"]
    menu.delete(0, "end")
    for class_name in absents:
        menu.add_command(label=class_name, command=lambda value=class_name: selected_class.set(value))

def add_absent():
    class_name = selected_class.get()
    date = cal.get_date()
    absents.setdefault(class_name, [])

    if date not in absents[class_name]:
        absents[class_name].append(date)
        class_status.config(text=f"Absent on {date} to {class_name}", fg="white")
    else:
        class_status.config(text=f"{date} already marked as Absent in {class_name}", fg="orange")

def show_absents():
    class_name = selected_class.get()
    empty_desk = absents.get(class_name, [])
    class_status.config(text=f"{class_name} has {len(empty_desk)} cut(s): {', '.join(empty_desk)}", fg="light blue")

def show_all_absents():
    report_window = tk.Toplevel(root)
    report_window.title("All Empty Desks")
    report_window.geometry("300x200")

    report_text = tk.Text(report_window)
    report_text.pack(pady=10)

    report_text.insert(tk.END, f"{'Class':<25}{'Empty Desks':<15}\n")
    report_text.insert(tk.END, "-" *38 + "\n")

    total_absents = 0

    for class_name in absents:
        dates = absents.get(class_name, [])
        total_empty_desks = len(dates)
        total_absents += total_empty_desks
        
        report_text.insert(
            tk.END,
            f"{class_name:<25}{total_empty_desks:<15}\n"
        )

        if dates:
            for date in dates:
                report_text.insert(tk.END, f"  - {date}\n")
        else:
            report_text.insert(tk.END, "  - Full Desks\n")
        
        report_text.insert(tk.END, "\n")
    
    report_text.insert(tk.END, f"{'TOTAL CUTS':<25}{total_absents:<15}\n")
    report_text.config(state="disabled")


# ----- Buttons -----
add_absent_button = tk.Button(root, text="Add Absent", command=add_absent, pady=10)
add_absent_button.grid(row=1, column=1)

show_absents_button = tk.Button(root, text="Show Empty Desks", command=show_absents, pady=10)
show_absents_button.grid(row=2, column=1)

show_report_button = tk.Button(root, text = "All Empty Desks", command=show_all_absents, pady=10)
show_report_button.grid(row=3, column=1)

add_class_button = tk.Button(root, text = "Add New Course", command=add_course_window)
add_class_button.grid(row=4, column=1)

root.focus_force()
root.lift()
root.mainloop()