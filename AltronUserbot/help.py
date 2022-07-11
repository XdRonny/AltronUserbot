from pyrogram import filters, Client
from config import BOT_USERNAME, client, SUDO_USERS
from pyrogram.types import Message


@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.me)
async def start(Client, message: Message):
    HOME_TEXT = """
**ʜᴇʏᴀ..!! 💖**
✘ __ɪ'ᴍ ɴᴏᴛ ᴊᴜsᴛ ᴀɴ ᴜsᴇʀʙᴏᴛ, ɪ ᴀᴍ ᴀʟsᴏ ᴀ sᴘᴀᴍʙᴏᴛ ʙᴏᴛ. ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴛʜʀᴏᴡ ᴜsᴇʀʙᴏᴛ. ɪ ᴄᴀɴ sᴘᴀᴍ ᴍsɢ ғʀᴏᴍ ʙᴏᴛ ᴀɴᴅ ᴜsᴇʀʙᴏᴛ ʙᴏᴛʜ. ɪ ʜᴀᴠᴇ ʟᴏᴛꜱ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ʏᴏᴜ ʟɪᴋᴇꜱ ᴛʜᴀᴛ__.

✘ [ᴄʟɪᴄᴋ ᴏɴ ʜᴇʀᴇ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️](https://t.me/{BOT_USERNAME})
"""
  
    await message.reply_text(HOME_TEXT)
    
    

