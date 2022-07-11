from pyrogram import filters, Client
from config import BOT_USERNAME, client, SUDO_USERS
from pyrogram.types import Message


@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.me)
async def start(Client, message: Message):
    await message.reply_text(
    "**ʜᴇʏᴀ..!! **\n\n[✘ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʀᴇ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️](https://t.me/{BOT_USERNAME}?start=true)"
    )
    
    

