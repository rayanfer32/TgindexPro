import os
try:
  import telethon
except:
  os.system("pip3 install -U -r requirements.txt")



from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = os.environ['API_ID']#int(input("Enter your API_ID: "))
api_hash = os.environ['API_HASH']#input("Enter your API_HASH: ")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
