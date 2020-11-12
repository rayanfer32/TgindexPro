from telethon import TelegramClient, events
from .config import  api_id, api_hash, debug ,bot_token

bot = TelegramClient('bot',api_id,api_hash).start(bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    await event.reply('Howdy, how are you doing?')

@bot.on(events.NewMessage)
async def echo_all(event):
    await event.reply(event.text)

def serve():
  with bot:
    bot.run_until_disconnected()