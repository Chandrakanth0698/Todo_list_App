import streamlit as st
from Module import functions


def add_todo():
    task = st.session_state["new_todo"]
    todo_list.append(task+"\n")
    functions.write_todo_file(todo_list)
    st.session_state["new_todo"] = ""


todo_list = functions.read_todo_file()
st.title("My Todo App")
st.subheader("Type in to add your daily tasks or Checkbox the task to complete daily task")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if st.session_state[todo]:
        todo_list.pop(index)
        functions.write_todo_file(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

