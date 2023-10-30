import streamlit as st
from Module import functions
import os

if not os.path.exists('todo.txt'):
    with open('todo.txt', 'w') as file:
        pass

todo_list = functions.read_todo_file()
st.title("My Todo App")
st.subheader("Add your daily tasks")
st.checkbox("to add new todo")

task = st.text_input("", placeholder="Add new todo...")

