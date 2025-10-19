from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# Finding items in the table
data = supabase.table("todos").select("*").execute()
data = supabase.table("todos").select("id,name").execute() # Fetch specific item
data = supabase.table("todos").select("id,name").eq("name", "item 2").execute() # Fetch in item equal to the stated


# Inserting items in the table
data = supabase.table("todos").insert({"name": "item 2"}).execute()


# Update items
data = supabase.table("todos").update({"name": "Code"}).eq("name", "item 1").execute() # update using name
data = supabase.table("todos").update({"name": "Work out"}).eq("id", 2).execute() # update using id


# Deleting items 
data = supabase.table("todos").delete().eq("name", "Work out").execute()
print(data)