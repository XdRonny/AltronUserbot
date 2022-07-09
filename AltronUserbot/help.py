from pyrogram import Client, filters
from config import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import *


@Client.on_message(filters.user(SUDO_USERS) & command(["help"], ["/", "!", "."]))
@Client.on_message(filters.me & command(["help"], ["/", "!", "."]))
async def alive(Client, e: Message):
    ids = 0
    try:
        if client:
            ids += 1
        if client2:
            ids += 1
        if client3:
            ids += 1
        if client4:
            ids += 1
        if client5:
            ids += 1
        if client6:
            ids += 1
        if client7:
            ids += 1
        if client8:
            ids += 1
        if client9:
            ids += 1
        if client10:
            ids += 1
        Alive_msg = f"🔥 ᴀʟᴛʀᴏɴ ɪs ᴏɴ ғɪʀᴇ 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► ᴠᴇʀsɪᴏɴ : `𝟸.𝟶` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `𝟷.𝟺.𝟷𝟼` \n"
        Alive_msg += f"► ᴀᴄᴛɪᴠᴇ ɪᴅ's : `{ids}` \n"
        Alive_msg += f"► ᴛᴏᴋᴇɴ ʙᴏᴛ : [ʙᴏᴛ](https://t.me/{BOT_USERNAME}?start=true) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=f"https://te.legra.ph/file/7abe179ff252aaabbf2a5.jpg",
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "☆ ᴄʜᴀɴɴᴇʟ ☆", url="https://t.me/altron_x")
                ], [
                    InlineKeyboardButton(
                        "☆ ʀᴇᴘᴏ ☆", url="https://github.com/TheAltronX/AltronUserbot")
                ]],
                [
                    InlineKeyboardButton(
                        "✵ ʜᴇʟᴘ ᴍᴇɴᴜ ✵", url="https://t.me/{BOT_USERNAME}?start=true")
                ],        
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"🔥 ᴀʟᴛʀᴏɴ ɪs ᴏɴ ғɪʀᴇ 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"✘ **ʜᴇʟʟᴏ**, __ɪ'ᴍ ɴᴏᴛ ᴊᴜsᴛ ᴀɴ ᴜsᴇʀʙᴏᴛ, ɪ ᴀᴍ ᴀʟsᴏ ᴀ sᴘᴀᴍʙᴏᴛ ʙᴏᴛ. ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴛʜʀᴏᴡ ᴜsᴇʀʙᴏᴛ ᴀɴᴅ ɪ ᴄᴀɴ sᴘᴀᴍ ᴍsɢ ғʀᴏᴍ ʙᴏᴛ ᴀɴᴅ ᴜsᴇʀʙᴏᴛ ʙᴏᴛʜ. ɪ ʜᴀᴠᴇ ʟᴏᴛꜱ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ʏᴏᴜ ʟɪᴋᴇꜱ ᴛʜᴀᴛ__.\n\n[ᴄʟɪᴄᴋ ᴍᴇ ғᴏʀ ɢᴇᴛ ʜᴇʟᴘ ᴍᴇɴᴜ ℹ️](https://t.me/{BOT_USERNAME}?start=true)"
        await e.reply_text(Alive_msg) 

