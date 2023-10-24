user_prompt = "Enter a todo: add <task>, show, edit, remove or exit -> "
todo_list = []


def show():
    if len(todo_list) == 0:
        print("Empty to do list!!!")
    else:
        for index, item in enumerate(todo_list):
            print(f'{index + 1}. {item}')


def validate_input(x):
    if x == "":
        print("no input, Enter task only:", end=" ")
        x = input()
        return validate_input(x)
    else:
        return x


def validate_index(y):
    if 1 <= y <= len(todo_list):
        return y
    else:
        print("enter valid task number: ", end=" ")
        y = int(input())
        return validate_index(y)


while True:
    todo = input(user_prompt).strip()
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
            task = validate_input(task)
            todo_list.append(task)
        case 'show':
            show()
        case 'edit':
            show()
            if len(todo_list)>0:
                num = int(input("enter task number to edit: "))
                num = validate_index(num)
                edited_task = input("Enter task: ")
                edited_task = validate_input(edited_task)
                todo_list[num - 1] = edited_task
        case 'remove':
            show()
            num = int(input("enter task number to remove: "))
            num = validate_index(num)
            todo_list.pop(num - 1)
        case 'exit':
            print("Closing the Application.")
            break
        case _:
            print("Enter a valid input, eg: add <task> or edit or show or remove or exit")
