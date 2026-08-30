#GUI Window
import tkinter as tk 

window = tk.Tk()

window.title ("To Do List")
window.geometry("500x600")

def add_task():
    task = task_entry.get()
    print(task)

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

#Button : Add Task 

add_button = tk.Button(
    window,
    text = "Add Task",
    command = add_task
)
add_button.pack()

window.mainloop() 

