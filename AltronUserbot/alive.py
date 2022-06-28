import asyncio
from AltronUserbot.helpers.command import commandpro
from pyrogram import Client
from pyrogram.types import Message


@Client.on_message(commandpro(["!alive", "/alive", "/start", "!altron"]))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/0957630b8248e79400247.jpg",
        caption=f"""**💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ ᴍᴜsɪᴄ+ᴠɪᴅᴇᴏ ᴀɴᴅ sᴘᴀᴍ ᴜsᴇʀʙᴏᴛ ᴍᴀᴅᴇ ʙʏ @Altron_X ... 
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴜᴘᴅᴀᴛᴇs : [ᴀʟᴛʀᴏɴ](https://t.me/Altron_X)
┣★ sᴜᴘᴘᴏʀᴛ : [ᴀʟᴛʀᴏɴ](https://t.me/TheAltron)
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴘʏᴛʜᴏɴ-x](https://t.me/dark_x_python)
┣★ ᴄʀᴇᴅɪᴛ   : [ʜᴇʀᴏ](https://t.me/Shailendra34)
┗━━━━━━━━━━━━━━━━━┛**""")


