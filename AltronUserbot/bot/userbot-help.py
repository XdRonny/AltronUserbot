from pyrogram import filters, Client
from config import client, SUDO_USERS
from pyrogram.types import Message
from config import *

@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.me)
async def start(Client, message: Message):
    await message.reply_text(
    f"🤖 **ʜᴇʏᴀ..!! **\n\n» __ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ ɢᴏ ᴛᴏ ʏᴏᴜʀ ᴄʀᴇᴀᴛᴇᴅ ʙᴏᴛ's ᴅᴍ__ » @{BOT_USERNAME}\n\n__sᴏᴏɴ ᴀᴅᴅɪɴɢ ɪɴʟɪɴᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙᴜᴛᴛᴏɴs ɪɴ ᴜsᴇʀʙᴏᴛ__ ᴊᴏɪɴ » @Altron_X"
    )
    
    

