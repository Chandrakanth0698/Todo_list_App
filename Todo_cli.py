user_prompt = "Enter a todo: add <task>, show, edit, remove or exit -> "


def show():
    if len(todo_list) == 0:
        print("Empty to do list!!!")
    else:
        for index, item in enumerate(todo_list):
            print(f'{index + 1}. {item}'.strip("\n"))


def validate_input(x):
    if x == "" or x == "\n":
        print("no input, Enter task only:", end=" ")
        x = input() + "\n"
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


def read_todo_file():
    file = open('todo.txt', 'r')
    data = file.readlines()
    file.close()
    return data


def write_todo_file(data):
    file = open('todo.txt', 'w')
    file.writelines(data)
    file.close()


while True:
    todo_list = read_todo_file()
    todo = input(user_prompt).strip()
    cmd, task = todo.split(" ")[0], " ".join(todo.split(" ")[1:]) + "\n"
    match cmd:
        case 'add':
            task = validate_input(task)
            todo_list.append(task)
            write_todo_file(todo_list)
        case 'show':
            show()
        case 'edit':
            show()
            if len(todo_list) > 0:
                num = int(input("enter task number to edit: "))
                num = validate_index(num)
                edited_task = input("Enter task: ")
                edited_task = validate_input(edited_task)
                todo_list[num - 1] = edited_task+"\n"
                write_todo_file(todo_list)
        case 'remove':
            show()
            if len(todo_list) > 0:
                num = int(input("enter task number to remove: "))
                num = validate_index(num)
                todo_list.pop(num - 1)
                write_todo_file(todo_list)
        case 'exit':
            print("Closing the Application.")
            break
        case _:
            print("Enter a valid input, eg: add <task> or edit or show or remove or exit")
