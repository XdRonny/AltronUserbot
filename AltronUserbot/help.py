from pyrogram import filters, Client
from config import BOT_USERNAME, client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


@client.on_message(filters.command(["help"], ["/", "!", "."]))
async def start(Client, message: Message):
    HOME_TEXT = """
**ʜᴇʏᴀ..!! **
✘ __ɪ'ᴍ ɴᴏᴛ ᴊᴜsᴛ ᴀɴ ᴜsᴇʀʙᴏᴛ, ɪ ᴀᴍ ᴀʟsᴏ ᴀ sᴘᴀᴍʙᴏᴛ ʙᴏᴛ. ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴛʜʀᴏᴡ ᴜsᴇʀʙᴏᴛ. ɪ ᴄᴀɴ sᴘᴀᴍ ᴍsɢ ғʀᴏᴍ ʙᴏᴛ ᴀɴᴅ ᴜsᴇʀʙᴏᴛ ʙᴏᴛʜ. ɪ ʜᴀᴠᴇ ʟᴏᴛꜱ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ʏᴏᴜ ʟɪᴋᴇꜱ ᴛʜᴀᴛ__.
✘ __ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️__
"""
    buttons = [
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/TheAltron"),
                InlineKeyboardButton("✘ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/Altron_X"),
            ],
            [
                InlineKeyboardButton("☆ ʜᴇʟᴘ ᴍᴇɴᴜ ☆", url="https://t.me/{BOT_USERNAME}?start=true"),
            ]
            ]     
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"https://te.legra.ph/file/7abe179ff252aaabbf2a5.jpg", caption=HOME_TEXT, reply_markup=reply_markup)
    
    

