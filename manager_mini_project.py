# Manager task for python using class and object 
import random
class task_manager():
  total_task=[] 
  personal_details={}
  task_id={}

  def __init__(self):
    self.name=input("Enter the your name:")
    self.age=input("Enter your age:")
    self.phone=input("Enter your Phone number:")
    self.email=input("Enter your email:")
    self.number=random.randint(1000,9999)
    self.task_id["TaskID"]=self.number
    self.personal_details['name']=self.name
    self.personal_details['age']=self.age
    self.personal_details['phone']=self.phone
    self.personal_details['email']=self.email

    print("Personal Details added sucessfully")


  def main(self):
    print("----------------------")
    print("Welcome To Task Manager")

    while True:

      try:
         print("1) Task ID")
         print("2) Show Your Details")
         print("3) Add The Task")
         print("4) View The task")
         print("5) Edit The Task")
         print("6) Delete The Task")
         print("7) Filter The Task")
         print("8) Task status")
         print("9) Exit \n")

         choice =int(input("Enter Your choice (1,2,3,4,5,6,7,8,9):"))
         if choice ==1:
            self.taskid()
         if choice == 2:
            self.your_details()
         elif choice == 3:
            self.add_task()
         elif choice == 4:
            self.view_task()
         elif choice == 5:
            self.edit_task()
         elif choice == 6:
            self.delete_task()
         elif choice== 7:
            self.filter_task()
         elif choice == 8:
            self.status()
         elif choice == 9:
            self.exit()
            break
         else:
          print("Invalid option")

      except ValueError as e:
         print("value error",e)

  @classmethod
  def taskid(cls):
    print("---------------")
    print("Task Id")
    print(f"Your Task id is: {task_manager.task_id}")
    print("--------------------------")

  def your_details(cls):
    print("-----------------")
    print("Your Details")
    for key,value in task_manager.personal_details.items():
      print(f"{key}:{value}")
    print("----------------------------------")
  def add_task(cls):
    print("-----------------")
    print("Add The Task")
    task=input("Enter your task:")
    task_manager.total_task.append(task)
    print(f"Your Task is: {task_manager.total_task}")
    print("Tasks Added succesfully")
    print("------------------------------")

  def view_task(self):
    print("-------------------")
    print("View The Task")
    for task in task_manager.total_task:
      print(f"Your Task :{task}\n")
      print("-----------------------------")

  def edit_task(self):
    print("-------------------")
    print("Edit the Task")
    task=input("Enter the task to be edited:").lower()
    if task in task_manager.total_task:
      index = task_manager.total_task.index(task)
      new_task=input("Enter the new task:")
      task_manager.total_task[index]=new_task
      print("Task Edited a succesfully")
    else:
      print("Task not found")

  def delete_task(self):
    print("----------------------------------")
    print("Delete The task")
    task=input("Enter the task to be deleted:")
    if task in task_manager.total_task:           
      task_manager.total_task.remove(task)             
      print("task deleted succesfully")                      
      print("--------------------------------")
    else:
      print("Task not found")

  def filter_task(self):
    print("--------------------------------")
    print("Filter the task")
    task=input("Enter the task to be filtered:")
    if task in task_manager.total_task:
      index=task_manager.total_task.index(task)
      print(task_manager.total_task[index])
      print("----------------------------------")
    else:
      print("Task not found")

  def status(self):
    print("----------------------------")
    print("Task status")
    user_task_id=int(input("Enter the task id:"))  
    for value in task_manager.task_id.values():
      if value == user_task_id:
       if len(task_manager.total_task)== 0:
         print(f"Heyy! {task_manager.personal_details['name']} no Task is pending")
       else:
         print(f"Heyy! {task_manager.personal_details['name']} Your Task is pending")
      else:
         print("Task Id is invalid")

  def exit(self):
    print("Thank you for using application")

p1=task_manager()
p1.main()
