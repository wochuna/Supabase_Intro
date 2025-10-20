from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client
from gotrue.exceptions import APIError

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

email: str = "example@gmail.com"
password: str = "trysupabase1234"
# user = supabase.auth.sign_up(email=email, password=password) # Sign up a user

'''user = supabase.auth.sign_in(email=email, password=password) # Sign in a user
print(user)''' # Use session instead

session = None

try:
    session = supabase.auth.sign_in(email=email, password=password) # Sign up a user
except APIError:
    print("Login failed")
print(session)

supabase.auth.sign_out() # Close the session