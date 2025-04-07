import streamlit as st
from db import init_db, insert_consumer
from handler import send_message_to_handler
import json
from auth import login

# Custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load package data
with open("packages.json") as f:
    packages = json.load(f)

# Sidebar with thumbnails
st.sidebar.title("Available Packages")
selected_package = st.sidebar.selectbox("Choose a package", list(packages.keys()))
st.sidebar.image(f"assets/thumbnails/{packages[selected_package]['image']}", use_column_width=True)
st.sidebar.markdown(f"**{selected_package}** - {packages[selected_package]['description']}")

# Tabs
tab = st.selectbox("Navigate", ["News", "Packages", "Video Tours", "Know Us", "Login"])

if tab == "News":
    st.header("📰 Latest Travel News")
    st.info("Stay tuned for new destinations launching this summer!")

elif tab == "Packages":
    st.header("📦 Tour Packages")
    st.subheader(selected_package)
    st.write(packages[selected_package]["details"])

    st.markdown("### Book this package")
    with st.form("booking_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        message = st.text_area("Message for the handler")
        submit = st.form_submit_button("Submit")

        if submit:
            insert_consumer(name, email, selected_package)
            send_message_to_handler(name, email, selected_package, message)
            st.success("Your request has been sent to our handler!")

elif tab == "Video Tours":
    st.header("🎥 Virtual Tours")
    st.video("https://www.youtube.com/watch?v=2OEL4P1Rz04")

elif tab == "Know Us":
    st.header("👋 About Us")
    st.write("We are your go-to travel companion, offering curated experiences across the globe.")

elif tab == "Login":
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login()
    else:
        st.success("You're already logged in!")
