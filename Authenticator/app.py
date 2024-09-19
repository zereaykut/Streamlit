import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title="Streamlit Authenticator",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Setup
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# Hasher.hash_passwords(config["credentials"])

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["pre-authorized"]
)

page = st.sidebar.selectbox("Page", 
                            [
                                "Creating a login widget",
                                "Authenticating users",
                                "Creating a reset password widget",
                                "Creating a new user registration widget",
                                "Creating a forgot password widget",
                                "Creating a forgot username widget",
                                "Creating an update user details widget"
                                ], 
                            index=0)

# Creating a login widget
if page == "Creating a login widget":
    authenticator.login()


# Authenticating users
if page == "Authenticating users":
    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f"Welcome *{st.session_state["name"]}*")
        st.title("Some content")
    elif st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Please enter your username and password")


# Creating a reset password widget
if page == "Creating a reset password widget":
    if st.session_state["authentication_status"]:
        try:
            if authenticator.reset_password(st.session_state["username"]):
                st.success("Password modified successfully")
        except Exception as e:
            st.error(e)
    else:
        st.warning("Please authenticate a user")


# Creating a new user registration widget
if page == "Creating a new user registration widget":
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
        if email_of_registered_user:
            st.success("User registered successfully")
    except Exception as e:
        st.error(e)


# Creating a forgot password widget
if page == "Creating a forgot password widget":
    try:
        username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
        if username_of_forgotten_password:
            st.success("New password to be sent securely")
            # The developer should securely transfer the new password to the user.
        elif username_of_forgotten_password == False:
            st.error("Username not found")
    except Exception as e:
        st.error(e)


# Creating a forgot username widget
if page == "Creating a forgot username widget":
    try:
        username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
        if username_of_forgotten_username:
            st.success("Username to be sent securely")
            # The developer should securely transfer the username to the user.
        elif username_of_forgotten_username == False:
            st.error("Email not found")
    except Exception as e:
        st.error(e)


# Creating an update user details widget
if page == "Creating an update user details widget":
    if st.session_state["authentication_status"]:
        try:
            if authenticator.update_user_details(st.session_state["username"]):
                st.success("Entries updated successfully")
        except Exception as e:
            st.error(e)
    else:
        st.warning("Please authenticate a user")


# Updating the configuration file
# with open("config.yaml", "w") as file:
#     yaml.dump(config, file, default_flow_style=False)