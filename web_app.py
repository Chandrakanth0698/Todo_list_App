import streamlit as st
from Module import functions
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as file:
        pass


def add_todo():
    task = st.session_state["new_todo"]
    todo_list.append(task+"\n")
    functions.write_todo_file(todo_list)


todo_list = functions.read_todo_file()
st.title("My Todo App")
st.subheader("Add your daily tasks")

for index, todo in enumerate(todo_list):
    st.checkbox(todo,key=index)

st.text_input("", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
st.session_state

