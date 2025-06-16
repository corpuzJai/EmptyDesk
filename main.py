import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import Calendar

root = tk.Tk()
root.geometry("580x400") # Set window size
root.title("Empty Desk") # Set window title

# ----- Class Dropdown -----
classes = []
classes = []
selected_class = tk.StringVar()
menu_options = classes if classes else["No classes,raahh"]
class_dropdown = tk.OptionMenu(root, selected_class, *menu_options)
class_dropdown.grid(row=0, column=0, padx=5)

# Disables dropdown if there are no classes available
if not classes:
    selected_class.set("No Classes, add one now!")
    class_dropdown.config(state="disabled")
else:
    class_dropdown.config(state="normal")
    selected_class.set(classes[0])

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

        classes.append(course)
        absents[course] = {
            "dates": [],
            "limit": int(limit),
            "prof": prof,
            "email": email,
            "room": room
        }

        messagebox.showinfo("Sucess!", f"Class '{course}' added.")
        update_class_dropdown()
        add_course_window.destroy()

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

    if not classes:
        selected_class.set("No Classes")
        class_dropdown.config(state="disabled")
    else:
        for class_name in classes:
            menu.add_command(label=class_name, command=tk._setit(selected_class, class_name))
        selected_class.set(classes[0])
        class_dropdown.config(state="normal")

def add_absent():
    class_name = selected_class.get()
    date = cal.get_date()
    #absents.setdefault(class_name, [])

    # Make sure the class exists
    if class_name not in absents:
        class_status.config(text="No valid class selected.", fg="red")
        return

    class_data = absents[class_name]
    if date not in class_data["dates"]:
        class_data['dates'].append(date)
        total_cuts=len(class_data["dates"])
        limit = class_data["limit"]

        # Shows near limit warning
        warning_threshold = limit - 1 if limit <=3 else limit - 2

        if total_cuts == warning_threshold:
            messagebox.showwarning(
                "Warning",
                f"You are nearing the cut limit for {class_name}! ({total_cuts}/{limit} cuts)"
            )
        elif total_cuts >= limit:
            messagebox.showerror(
                "Withdrawn",
                f"You have exceeded the cut limit for {class_name}.\n This class will now be removed."
            )
            absents.pop(class_name, None)
            if class_name in classes:
                classes.remove(class_name)
            update_class_dropdown()
            class_status.config(text=f"{class_name} removed due to excessive cuts.", fg="red")
            return

        class_status.config(text=f"Absent on {date} to {class_name}", fg="white")
    else:
        class_status.config(text=f"{date} already marked as Absent in {class_name}", fg="orange")

def show_absents():
    class_name = selected_class.get()
    class_data = absents.get(class_name, [])
    dates = class_data.get("dates", [])
    class_status.config(text=f"{class_name} has {len(dates)} cut(s): {', '.join(dates)}", fg="light blue")

# def show_all_absents():
#     report_window = tk.Toplevel(root)
#     report_window.title("All Empty Desks")
#     report_window.geometry("300x200")

#     report_text = tk.Text(report_window)
#     report_text.pack(pady=10)

#     report_text.insert(tk.END, f"{'Class':<25}{'Empty Desks':<15}\n")
#     report_text.insert(tk.END, "-" *38 + "\n")

#     total_absents = 0

#     for class_name, data in absents.items():
#         dates = data.get("dates", [])
#         count_empty_desks = len(dates)
#         total_absents += count_empty_desks
        
#         report_text.insert(
#             tk.END,
#             f"{class_name:<25}{count_empty_desks:<15}\n"
#         )

#         if dates:
#             for date in dates:
#                 report_text.insert(tk.END, f"  - {date}\n")
#         else:
#             report_text.insert(tk.END, "  - Full Desks\n")
        
#         report_text.insert(tk.END, "\n")
    
#     report_text.insert(tk.END, f"{'TOTAL CUTS':<25}{total_absents:<15}\n")
#     report_text.config(state="disabled")

def show_class_details():
    class_report_window = tk.Toplevel(root)
    class_report_window.title("Class Details")
    class_report_window.geometry("500x400")

    class_report_text = tk.Text(class_report_window, wrap="word", padx=10, pady=10)
    class_report_text.pack(fill="both", expand=True)

    if not absents:
        class_report_text.insert(tk.END, "No classes available.\n")
    else:
        for class_name, info in absents.items():
            prof = info.get("prof", "N/A")
            email = info.get("email", "N/A")
            room = info.get("room", "N/A")
            limit = info.get("limit", "N/A")
            dates = info.get("dates", [])
            num_cuts = len(dates)

            class_report_text.insert(tk.END, f"Course Code: {class_name}\n")
            class_report_text.insert(tk.END, f"Professor: {prof}\n")
            class_report_text.insert(tk.END, f"Email: {email}\n")
            class_report_text.insert(tk.END, f"Room: {room}\n")
            class_report_text.insert(tk.END, f"Cut Limit: {limit}\n")
            class_report_text.insert(tk.END, f"Empty Desks: {num_cuts}\n")

            if dates:
                class_report_text.insert(tk.END, "Empty Desks:\n")
                for date in dates:
                    class_report_text.insert(tk.END, f"  - {date}\n")
            else:
                class_report_text.insert(tk.END, "  - Full Desks\n")

            class_report_text.insert(tk.END, "\n" + "-" * 40 + "\n\n")

    class_report_text.config(state="disabled")

    return


# ----- Buttons -----
add_absent_button = tk.Button(root, text="Add Absent", command=add_absent, pady=10)
add_absent_button.grid(row=1, column=1)

show_absents_button = tk.Button(root, text="Show Empty Desks", command=show_absents, pady=10)
show_absents_button.grid(row=2, column=1)

# show_report_button = tk.Button(root, text = "All Empty Desks", command=show_all_absents, pady=10)
# show_report_button.grid(row=3, column=1)
show_class_button = tk.Button(root, text = "Class Details", command=show_class_details, pady=10)
show_class_button.grid(row=3, column=1)

add_class_button = tk.Button(root, text = "Add New Course", command=add_course_window)
add_class_button.grid(row=4, column=1)

root.focus_force()
root.lift()
root.mainloop()