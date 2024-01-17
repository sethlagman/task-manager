"""A simple to-do list app using tkinter"""

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

task_count = 0

def add_task():
    """Adds the user's task to the listbox"""

    if entry.get():
        global task_count
        task_count += 1

        if priority.get() == "Low Priority":
            task_list.insert(END, entry.get())

        elif priority.get() == "Medium Priority":
            medium_task_list.insert(END, entry.get())

        elif priority.get() == "High Priority":
            high_task_list.insert(END, entry.get())

        else:
            task_list.insert(END, entry.get())

def delete_task():
    """Deletes a task"""

    global task_count
    selected_low_task = task_list.curselection()

    if selected_low_task:
        confirm = messagebox.askyesno("To-do App","Are you sure you want to delete this task?")

        if confirm:
            task_count -= 1

            task_list.delete(selected_low_task)

    selected_medium_task = medium_task_list.curselection()

    if selected_medium_task:
        confirm = messagebox.askyesno("To-do App","Are you sure you want to delete this task?")

        if confirm:
            task_count -= 1

            medium_task_list.delete(selected_medium_task)

    selected_high_task = task_list.curselection()

    if selected_high_task:
        confirm = messagebox.askyesno("To-do App","Are you sure you want to delete this task?")

        if confirm:
            task_count -= 1

            high_task_list.delete(selected_high_task)

def complete_task():
    """Marks a task as complete"""

    global task_count
    selected_low_task = task_list.curselection()

    if selected_low_task:
        task_count -= 1

        task_list.delete(selected_low_task)

    selected_medium_task = medium_task_list.curselection()

    if selected_medium_task:
        task_count -= 1

        medium_task_list.delete(selected_medium_task)

    selected_high_task = high_task_list.curselection()

    if selected_high_task:
        task_count -= 1

        high_task_list.delete(selected_high_task)

def clear_button():
    """Clears the user's input"""

    entry.delete(0, END)

def count_task():
    """Counts the task present in the list"""

    count_label.config(text=task_count)

def exit_app():
    """Confirms the application's exit"""

    confirm = messagebox.askyesno("To-do App", "Are you sure you want to close the application?")

    if confirm:
        root.quit()

    
root = Tk()
root.title("To-do App")

title = Label(root, text="To-do list", font="Georgia 50")
title.grid(row=0, columnspan=3)

prompt = Label(root, text="Enter the task:", font="Georgia 15")
prompt.grid(row=1, column=0, sticky='we')

entry = Entry(root, text="")
entry.grid(row=1, column=1, sticky='we')

string_var = StringVar()
priority = Combobox(root, values=("Low Priority", "Medium Priority", "High Priority"), state="readonly", textvariable=string_var)
priority.grid(row=1, column=2)
string_var.set("Choose a priority")

clear = Button(root, text="Clear", command=clear_button)
clear.grid(row=2, columnspan=3, sticky='we')

delete = Button(root, text="Delete Task", command=delete_task)
delete.grid(row=4, columnspan=3, sticky='we')

count = Button(root, text="Count", command=count_task)
count.grid(row=6, columnspan=2, sticky='we')

count_label = Label(root, text="?")
count_label.grid(row=6, column=2)

add = Button(root, text="Add Task", command=add_task)
add.grid(row=3, columnspan=3, sticky='we')

complete = Button(root, text="Complete Task", command=complete_task)
complete.grid(row=5, columnspan=3, sticky='we')

low_priority = Label(root, text="Low Priority")
low_priority.grid(row=7)

task_list = Listbox(root)
task_list.grid(row=8, sticky='we')

medium_priority = Label(root, text="Medium Priority")
medium_priority.grid(row=7, column=1)

medium_task_list = Listbox(root)
medium_task_list.grid(row=8, column=1, sticky='we')

high_priority = Label(root, text="High Priority")
high_priority.grid(row=7, column=2)

high_task_list = Listbox(root)
high_task_list.grid(row=8, column=2, sticky='we')

root.protocol("WM_DELETE_WINDOW", exit_app)
root.mainloop()
