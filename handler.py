from twilio.rest import Client
import streamlit as st

def send_message_to_handler(name, email, package, message):
    account_sid = st.secrets["twilio"]["account_sid"]
    auth_token = st.secrets["twilio"]["auth_token"]
    handler_phone = st.secrets["twilio"]["handler_phone"]
    sender_phone = st.secrets["twilio"]["from_phone"]

    client = Client(account_sid, auth_token)

    msg_body = (
        f"New Tour Request:\n"
        f"Name: {name}\nEmail: {email}\nPackage: {package}\nMessage: {message}"
    )

    message = client.messages.create(
        body=msg_body,
        from_=sender_phone,
        to=handler_phone
    )

    print(f"Message sent: {message.sid}")
