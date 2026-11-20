class Task:
    
    def __init__(self, name):
        self.name = name
        self.status = False
    

def get_task_id(Tasks, raw_id):
    try:
        id = int(raw_id)
    except ValueError:
        
        return None
    if id <= 0 or id > len(Tasks):
        
        return  None
    return id
        
        
def addTask(Tasks, name):
    
    if (name.strip() == ""):
        return False
    task = Task(name)
    Tasks.append(task)
    return True
    
    
def viewTask(tasks):
    if not tasks:
        return "No tasks found"
    
    task_names = ""
    for index, task in enumerate(tasks):
        status = 'x' if task.status == True else " "
        to_join = f"[{index + 1}] [{status}] {task.name} \n"
        task_names += to_join
        
    return task_names
        
def completeTask(tasks, id):
    
    
    if (type(id) is int):
        
        if( id >0 and id <= len(tasks)):
    
            tasks[id - 1].status = True
            return True
    return False
    
def deleteTask(tasks, id):
     
    
    if(type(id) is int):
        if( id >0 and id <= len(tasks)):
            tasks.remove(tasks[id - 1])
            return True
    return False
    


def main():
    
    Tasks = []
    
    
    
    while(1):
        print("""====TaskFlow====
                  1. Add Task
                  2. view Task
                  3. Complete Task
                  4. Delete Task
                  5. Exit""")
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Please enter a number")
            continue
        if(choice < 1 or choice > 5):
            print("Invalid choice")
            continue
   
        match choice:
            case 1:
                name = input("Task title: ")
                print("Task added successfully" if addTask(Tasks, name) else "Empty name not allowed")
            case 2:
                print(viewTask(Tasks))
            case 3:
                raw_id = input("Enter task id: ")
                id = get_task_id(Tasks, raw_id) 
                
                if completeTask(Tasks, id):
                    print('Task Completed successfully')
                else:
                    print('Invalid ID')
            case 4:
                raw_id = input("Enter task id: ")
                id = get_task_id(Tasks, raw_id)
                if deleteTask(Tasks, id):
                    print("Task deleted successfully")
                else:
                    print("Invalid ID")
            case 5:
                return 0
        
    
    
    
    
if __name__ == '__main__':
    main()