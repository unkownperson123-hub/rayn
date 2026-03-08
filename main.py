import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("SESSION_STRING")

# Bot client
bot = Client(
    "rayn-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Assistant client
assistant = Client(
    "rayn-assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

# Voice chat
pytgcalls = PyTgCalls(assistant)

async def start_bot():
    print("Starting Rayn Bot...")

    await bot.start()
    print("Bot Started")

    await assistant.start()
    print("Assistant Started")

    await pytgcalls.start()
    print("Voice Chat Engine Started")

    print("Rayn Music Bot Running 🚀")

    await asyncio.Event().wait()

if name == "main":
    asyncio.run(start_bot())
