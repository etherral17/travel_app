import streamlit as st

def login():
    st.header("🔐 Member Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        users = st.secrets["users"]
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")
