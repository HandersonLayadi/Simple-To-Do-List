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
    font = ("Arial", 20)
)

title.pack ()

#GUI Entry 
task_entry = tk.Entry(
    window, 
    width = 50
)
task_entry.pack(pady = 10)

# Task List
task_list = tk.Listbox(
    window,
    width=60,
    height=20
)

task_list.pack()

load_tasks()

button_frame = tk.Frame(window)
button_frame.pack()

#Button : Add Task 
add_button = tk.Button(
    button_frame,
    text = "Add Task",
    command = add_task
)
add_button.pack()

#Button : Remove Task 
remove_button = tk.Button(
    button_frame,
    text = "Remove Task",
    command = remove_task
)
remove_button.pack ()

#Button : Edit Task 
edit_button = tk.Button(
    button_frame,
    text = "Edit Task",
    command = edit_task
)
edit_button.pack()

#Button : Exit App 
exit_button = tk.Button(
    window, 
    text = "Exit",
    command = exit_app
)

exit_button.pack()
add_button.pack(side=tk.LEFT, padx = 5)
remove_button.pack(side=tk.LEFT, padx = 5)
edit_button.pack(side=tk.LEFT, padx = 5)
task_entry.pack(pady = 10)
task_list.pack(pady = 10)
exit_button.pack(pady = 10)
window.mainloop() 

