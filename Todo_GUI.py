from Module import functions
import time
import PySimpleGUI as sg
label = sg.Text("Type in a todo ")
input_box = sg.InputText("Enter a todo")
now = sg.Text(time.strftime("Time: %b %d, %y %H:%M:%S"))
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
window = sg.Window('My todo GUI', layout=[[now], [label, input_box, add_button], [edit_button, complete_button]])
window.read()
window.close()
