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
        "email": "wochunayvonne@gmail.com",
        "password": "trysupabase1234",
    }
)
        return user
    except Exception as e:
        st.error(f"Registration failed: {e}") 

# Sign in a user
def sign_in_with_password(email, password):
    try:
        user = supabase.auth.sign_up(
    {
        "email": "wochunayvonne@gmail.com",
        "password": "trysupabase1234",
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


