#Task data 

tasks = []

#Menu 

while True :
    print ("\n--- TO DO LIST ---")
    print ("1. Add Task")
    print ("2. View Task")
    print ("3. Remove Task")
    print ("4. Exit")
    
    choice = input ("Choose an option : ")
    
    #Add a task
    if choice == "1" : 
        task = input("Enter a task : ")
        tasks.append (task)
        print("Task Has Been Added!")
        
    #View a task    
    elif choice == "2" :
        for index, task in enumerate(tasks) : 
            print (index + 1, ".", task)
            
    #Remove a task 
    elif choice =="3" : 
        if not tasks : 
            print("Your task list is empty")
        else : 
            for index, task in enumerate(tasks) : 
                print (f"{index + 1}. {task}")   
            
            task_num = int(input("Enter a teask to be removed : "))
            
            if 1 <= task_num <= len(tasks) : 
                removed = tasks.pop(task_num - 1)
                print ("Removed : ", removed)
            else : 
                print ("Invalid Task Number")
                
    #Exit 
    elif choice =="4" : 
        print('Goodbye Master')
        break