import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


# Sign up a user
def sign_up(email, password):
    try:
        user = supabase.auth.sign_up(
    {
        "email": email,
        "password": password,
    }
)
        return user
    except Exception as e:
        st.error(f"Registration failed: {e}") 

# Sign in a user
def sign_in(email, password):
    try:
        user = supabase.auth.sign_in_with_password(
    {
        "email": email,
        "password": password,
    }
)
        return user
    except Exception as e:
        st.error(f"Login failed failed: {e}") 

# Sign out
def sign_out():
    try:
        supabase.auth.sign_up()
        st.session_state.user_email = None
        st.rerun()
    except Exception as e:
        st.error(f"Logout failed: {e}")

def main_app(user_email):
    st.title("Welcome page")
    st.success(f"Welcome, {user_email}")
    if st.button("Logout"):
        sign_out()


def auth_screen():
    st.title("Streamlit abd Supabase Auth  App")
    option = st.selectbox("Choose an action:", ["Login", "Sign up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if option == "Sign up" and st.button("Register"):
        user = sign_up(email, password)
        if user and user.user:
            st.success("Registration successful! Please log in.")

    if option == "Login" and st.button("Login"):
        user = sign_in(email, password)
        if user and user.user:
            st.session_state.user_email = user.user.email
        st.success(f"Welcome back, {email}!")
        st.error("Login failed. Please check your credentials.")
        st.rerun()

if "user_email" not in st.session_state:
    st.session_state.user_email = None

if st.session_state.user_email:
    main_app(st.session_state.user_email)

else:
    auth_screen()
    