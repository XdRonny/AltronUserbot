from pyrogram import filters
from config import SUDO_USERS
from config import *
from pyrogram.types import Message


@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.me)
async def start(client, message: Message):
    await message.reply_text(
    "**🤖 ʜᴇʏᴀ..!!**\n\n»__ ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ ɢᴏ ᴛᴏ ʏᴏᴜʀ ᴄʀᴇᴀᴛᴇᴅ ʙᴏᴛ's ᴅᴍ » @{BOT_USERNAME} \n\nsᴏᴏɴ ᴀᴅᴅɪɴɢ ɪɴʟɪɴᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙᴜᴛᴛᴏɴs ɪɴ ᴜsᴇʀʙᴏᴛ\nᴊᴏɪɴ » @Altron_X__"
    )
    
    