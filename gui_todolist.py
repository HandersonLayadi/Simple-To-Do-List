#GUI Window
import tkinter as tk 
import todolist

window = tk.Tk()

window.title ("To Do List")
window.geometry("500x600")
window.configure(bg="#C4C2C2")

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
            for index in reversed(selected) : 
                todolist.tasks.pop(index)
                task_list.delete(index)
                
            todolist.save_tasks()
#Edit Task 
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

#Exit Window 
def exit_app () : 
    window.destroy()

#GUI Title
title = tk.Label (
    window, 
    text = "To Do List",
    font = ("Arial", 24, "bold")
)

title.pack ( pady = 10)

#GUI Entry 
task_entry = tk.Entry(
    window, 
    width = 35,
    font = ("Arial", 14)
)
task_entry.pack(pady = 10)

list_frame = tk.Frame(window)
list_frame.pack(pady = 10)

# Task List
task_list = tk.Listbox(
    list_frame,
    width=60,
    height=15,
    bg = "#F5F7FA",
    selectmode=tk.MULTIPLE
)

task_list.pack(side=tk.LEFT)

#Scrollbar
scrollbar = tk.Scrollbar(list_frame)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#Connecting Task List to Scrollbar
task_list.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=task_list.yview)

load_tasks()

button_frame = tk.Frame(
    window,
    )
button_frame.pack()

#Button : Add Task 
add_button = tk.Button(
    button_frame,
    text = "Add Task",
    command = add_task,
    width = 10,
    bg = "#4F994B"
)
add_button.pack(side=tk.LEFT, padx = 5)

#Button : Remove Task 
remove_button = tk.Button(
    button_frame,
    text = "Remove Task",
    command = remove_task,
    width = 10,
    bg = "#EF4444"
)
remove_button.pack (side=tk.LEFT, padx = 5)

#Button : Edit Task 
edit_button = tk.Button(
    button_frame,
    text = "Edit Task",
    command = edit_task,
    width = 10,
    bg = "#2ABCD1"
)
edit_button.pack(side=tk.LEFT, padx = 5)

#Button : Exit App 
exit_button = tk.Button(
    window, 
    text = "Exit",
    command = exit_app,
    width = 10,
    bg = "#9C9C9C"
)

exit_button.pack(padx = 10, pady = 10)

window.mainloop() 

