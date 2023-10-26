def show(todo_list):
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


def validate_index(todo_list):
    try:
        index = int(input("enter task number: "))
        if index == 0 or index > len(todo_list):
            print(f"enter values between 1 and {len(todo_list)}", end=" ")
            return validate_index(todo_list)
    except ValueError:
        return validate_index(todo_list)
    else:
        return index


def read_todo_file():
    with open('todo.txt', 'r') as file:
        data = file.readlines()
    return data


def write_todo_file(data):
    with open('todo.txt', 'w') as file:
        file.writelines(data)
