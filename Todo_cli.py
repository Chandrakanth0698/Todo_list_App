user_prompt = "Enter a todo: add, show, remove -> "
todo_list = []

while True:
    todo = input(user_prompt)
    cmd, task = todo.split(" ")[0], " ".join(todo.split(" ")[1:])
    # if cmd == "add":
    #     todo_list.append(task)
    # elif cmd == "show":
    #     for i in range(len(todo_list)):
    #         print(i+1, " ", todo_list[i])
    # elif cmd == "remove":
    #     num = int(input("enter task number: "))
    #     if num > len(todo_list):
    #         print("enter valid number")
    #         continue
    #     else:
    #         todo_list.pop(num-1)
    # else:
    #     print("enter a valid Input: eg: add <task> or show or remove ")
    match cmd:
        case 'add':
            todo_list.append(task)
        case 'show':
            for i in range(len(todo_list)):
                print(i+1, " ", todo_list[i])
        case 'remove':
            num = int(input("enter task number to remove: "))
            if num > len(todo_list):
                print("Enter a Valid number: ")
                continue
            else:
                todo_list.pop(num-1)
        case _:
            print("Enter a valid input, eg: add <task> or show or remove")

