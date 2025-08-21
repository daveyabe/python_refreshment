todo_list = []

while True:

  if todo_list == []:
    print("Your Todo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1

  print("Options:")
  print("1) Add Task:")
  print("2) Remove Task")
  print("3) Quit")
  
  choice = input("enter option 1,2,or 3: ")
  if choice == "1":
    print("Adding task")
    new_task = input("Enter the new task you'd like to add: ")
    todo_list.append(new_task)
    print(f"Your new task {new_task} has been added to the todo list")
  elif choice == "2":
    if todo_list == []:
      print("Your Todo list is empty")
    else:
      removed_value = todo_list.pop()
      print(f"{removed_value} has been removed from your ToDo list!")
  elif choice == "3":
    print("Quitting! Cya Later")
    break
