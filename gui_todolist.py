#GUI Window
import tkinter as tk 
import todolist

window = tk.Tk()

window.title ("To Do List")
window.geometry("500x600")

#Add Task 
def add_task():
    task = task_entry.get()
    
    todolist.tasks.append(task)
    todolist.save_tasks()
    
    task_list.insert(tk.END, task)
    
    task_entry.delete(0, tk.END)
    
#Load Task
def load_tasks():
    for task in todolist.tasks:
        task_list.insert(tk.END, task)
    
#Remove Task 
def remove_task():
    
    selected = task_list.curselection()
            
    if selected :
                index = selected[0]
                todolist.tasks.pop (index)
                todolist.save_tasks()
                
                task_list.delete(index)

def edit_task() : 
    selected = task_list.curselection()
    
    if selected : 
        index = selected[0]
        
        new_task = task_entry.get()
        
        if new_task : 
            todolist.tasks[index] = new_task
            todolist.save_tasks()
            
            task_list.delete(index)
            task_list.insert(index, new_task)
            
            task_entry.delete(0, tk.END)

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

#Button : Remove Task 
remove_button = tk.Button(
    window,
    text = "Remove Task",
    command = remove_task
)
remove_button.pack ()

#Button : Edit Task 
edit_button = tk.Button(
    window,
    text = "Edit Task",
    command = edit_task
)
edit_button.pack()

window.mainloop() 

