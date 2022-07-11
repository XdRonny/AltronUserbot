from pyrogram import filters, Client
from config import SUDO_USERS
from config import *
from pyrogram.types import Message


@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
@client2.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.me)
@client2.on_message(filters.command(["help"], ["/", "!", "."]) & filters.me)
async def start(Client, message: Message):
    await message.reply_text(
    "🤖 **ʜᴇʏᴀ..!! **\n\n[» ᴄʟɪᴄᴋ ᴍᴇ ғᴏʀ ᴠɪᴇᴡ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴇʟᴘ ᴍᴇɴᴜ ](https://t.me/{BOT_USERNAME}?start=true)"
    )
    
    
