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
        
        
def addTask(Tasks):
    name = input("Task title: ")
    if (name.strip() == ""):
        print("Empty name not allowed")
        return
    task = Task(name)
    Tasks.append(task)
    print("\n Task added successfully")
    
    
def viewTask(tasks):
    if not tasks:
        print("No tasks found")
        return
    
    for index, task in enumerate(tasks):
        status = 'x' if task.status == True else " "
        print(f"[{index + 1}] [{status}] {task.name}")
def completeTask(tasks):
    id = get_task_id(tasks) 
    
    if (isinstance(id , int)):
    
        tasks[id - 1].status = True
    
def deleteTask(tasks):
    id = get_task_id(tasks) 
    
    if(isinstance(id , int)):
        tasks.remove(tasks[id - 1])
    


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
                addTask(Tasks)
            case 2:
                viewTask(Tasks)
            case 3:
                completeTask(Tasks)
            case 4:
                deleteTask(Tasks)
            case 5:
                return 0
        
    
    
    
    
if __name__ == '__main__':
    main()