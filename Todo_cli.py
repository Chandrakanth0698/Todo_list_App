from Module import functions

user_prompt = "Enter a todo: add <task>, show, edit, remove or exit -> "

while True:
    todo_list = functions.read_todo_file()
    todo = input(user_prompt).strip()
    cmd, task = todo.split(" ")[0], " ".join(todo.split(" ")[1:]) + "\n"
    match cmd:
        case 'add':
            task = functions.validate_input(task)
            todo_list.append(task)
            functions.write_todo_file(todo_list)
        case 'show':
            functions.show(todo_list)
        case 'edit':
            functions.show(todo_list)
            if len(todo_list) > 0:
                num = functions.validate_index(todo_list)
                edited_task = input("Enter task: ")
                edited_task = functions.validate_input(edited_task)
                todo_list[num - 1] = edited_task+"\n"
                functions.write_todo_file(todo_list)
        case 'remove':
            functions.show(todo_list)
            if len(todo_list) > 0:
                num = functions.validate_index(todo_list)
                todo_list.pop(num - 1)
                functions.write_todo_file(todo_list)
        case 'exit':
            print("Closing the Application.")
            break
        case _:
            print("Enter a valid input, eg: add <task> or edit or show or remove or exit")
