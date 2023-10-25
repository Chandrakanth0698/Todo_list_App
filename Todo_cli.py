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
        validate_input(x)
    else:
        return x


def input_task_num():
    try:
        index_v = int(input("enter task number: "))
        if index_v == 0 or index_v > len(todo_list):
            print(f"enter values between 1 and {len(todo_list)}", end=" ")
            return input_task_num()
    except ValueError:
        return input_task_num()
    else:
        return index_v


# def validate_index(y):
#     try:
#         if 1 <= y <= len(todo_list):
#             return y
#         else:
#             print("enter valid task number: ", end=" ")
#             y = int(input())
#             return validate_index(y)
#     except ValueError:
#         return validate_index(y)


def read_todo_file():
    with open('todo.txt', 'r') as file:
        data = file.readlines()
    return data


def write_todo_file(data):
    with open('todo.txt', 'w') as file:
        file.writelines(data)


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
                num = input_task_num()
                # num = validate_index(num)
                edited_task = input("Enter task: ")
                edited_task = validate_input(edited_task)
                todo_list[num - 1] = edited_task+"\n"
                write_todo_file(todo_list)
        case 'remove':
            show()
            if len(todo_list) > 0:
                num = input_task_num()
                # num = validate_index(num)
                todo_list.pop(num - 1)
                write_todo_file(todo_list)
        case 'exit':
            print("Closing the Application.")
            break
        case _:
            print("Enter a valid input, eg: add <task> or edit or show or remove or exit")
