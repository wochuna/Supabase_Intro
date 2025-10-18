from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

data = supabase.table("todos").select("*").execute()
data = supabase.table("todos").select("id,name").execute() # Fetch specific item
data = supabase.table("todos").select("id,name").eq("name", "item 2").execute() # Fetch in item equal to the stated
print(data)