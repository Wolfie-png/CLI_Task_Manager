class Task:
    
    def __init__(self, name):
        self.name = name
        self.status = False
    

def get_task_id(Tasks):
    try:
        id = int(input("Task ID: "))
    except ValueError:
        print("invalid task ID")
        return 
    if id <= 0 or id > len(Tasks):
        print("Invalid task ID")
        return  
    return id
        
        
def addTask():
    name = input("Task title: ")
    if (name.strip() == ""):
        print("Empty name not allowed")
        return
    task = Task(name)
    Tasks.append(task)
    print("\n Task added successfully")
    
    
def viewTask():
    for index, task in enumerate(Tasks):
        status = 'x' if task.status == True else " "
        print(f"[{index + 1}] [{status}] {task.name}")
def completeTask():
    id = get_task_id(Tasks) 
    
    if (isinstance(id , int)):
    
        Tasks[id - 1].status = True
    
def deleteTask():
    id = get_task_id(Tasks) 
    
    if(isinstance(id , int)):
        Tasks.remove(Tasks[id - 1])
    

Tasks = []
def main():
    
    
    
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
                addTask()
            case 2:
                viewTask()
            case 3:
                completeTask()
            case 4:
                deleteTask()
            case 5:
                return 0
        
    
    
    
    
if __name__ == '__main__':
    main()