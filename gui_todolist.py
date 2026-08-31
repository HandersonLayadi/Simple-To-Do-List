#GUI Window
import tkinter as tk 
import todolist

window = tk.Tk()

window.title ("To Do List")
window.geometry("500x600")

def add_task():
    task = task_entry.get()
    
    todolist.tasks.append(task)
    todolist.save_tasks()
    
    task_list.insert(tk.END, task)
    
def load_tasks():
    for task in todolist.tasks:
        task_list.insert(tk.END, task)
    

#GUI Title
title = tk.Label (
    window, 
    text = "To Do List",
    font = ("Arial", 20)
)

title.pack ()

#GUI Entry 
task_entry = tk.Entry(window)
task_entry.pack()

# Task List
task_list = tk.Listbox(
    window,
    width=60,
    height=20
)

task_list.pack()

load_tasks()

#Button : Add Task 
add_button = tk.Button(
    window,
    text = "Add Task",
    command = add_task
)
add_button.pack()

window.mainloop() 

