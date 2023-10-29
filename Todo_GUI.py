from Module import functions
import time
import PySimpleGUI as sg
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as file:
        pass

label = sg.Text("Type in a todo ")
input_box = sg.InputText(tooltip="Enter a todo", key='todo')
list_box = sg.Listbox(values=functions.read_todo_file(), key="todo_list", enable_events=True, size=(45, 10))
now = sg.Text(key='clock')
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My todo GUI', layout=[[now],
                                          [label, input_box, add_button],
                                          [list_box, edit_button, complete_button],
                                          [exit_button]])

while True:
    todo_list = functions.read_todo_file()
    event, values = window.read(timeout=900)
    window['clock'].update(value=time.strftime("Time: %b %d, %y %H:%M:%S"))
    match event:
        case 'Add':
            if values['todo'] == "":
                pass
            else:
                task = values['todo']+"\n"
                todo_list.append(task)
                functions.write_todo_file(todo_list)
                window['todo_list'].update(values=todo_list)
                window['todo'].update(value=[])
        case 'Edit':
            try:
                if values['todo'] == "":
                    pass
                else:
                    edited_task = values['todo'] + "\n"
                    num = todo_list.index(values['todo_list'][0])
                    todo_list[num] = edited_task
                    functions.write_todo_file(todo_list)
                    window['todo_list'].update(values=todo_list)
                    window['todo'].update(value=[])
            except IndexError:
                sg.popup("Try to edit only the items in the list!!!")

        case 'Complete':
            try:
                if values['todo'] == "":
                    pass
                else:
                    completed_task = values['todo_list'][0]
                    num = todo_list.index(completed_task)
                    todo_list.pop(num)
                    functions.write_todo_file(todo_list)
                    window['todo_list'].update(values=todo_list)
                    window['todo'].update(value=[])
            except IndexError:
                sg.popup("Try to mark complete only the items in the list!!!")
        case 'todo_list':
            window['todo'].update(value=values['todo_list'][0][:-1])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
window.close()
