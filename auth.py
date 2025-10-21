from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


# Sign up a user

'''response = supabase.auth.sign_up(
    {
        "email": "wochunayvonne@gmail.com",
        "password": "trysupabase1234",
    }
)'''

# Sign in a user
try:
    response = supabase.auth.sign_in_with_password(
        "email" ="lynne@gmail.com",
        "password" ="lynne1",
        )
    print("Login successful:", response)
except Exception as e:
    print("Login failed:", str(e))



# Sign out
# response = supabase.auth.sign_out()

