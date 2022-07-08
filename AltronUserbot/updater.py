import os
import zipfile
import wget
import shutil
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS


async def restart(message: Message, restart_type):
    if restart_type == "update":
        text = "1"
    else:
        text = "2"
    try:
        await os.execvp(
            "python3",
            [
                "python3",
                "./main.py",
                f"{message.chat.id}",
                f"{message.from_user.id}",
                f"{text}",
            ],
        )
    except:
        await os.execvp(
            "python",
            [
                "python",
                "./main.py",
                f"{message.chat.id}",
                f"{message.from_user.id}",
                f"{text}",
            ],
        )
        

# --------------------------Update---------------------

@Client.on_message(filters.command(["update"], [".", "/", "!"]) & filters.me)
async def update(client: Client, message: Message):
    try:
        await message.edit('**Updating...**')
        link = "https://github.com/TheAltronX/AltronUserbot/archive/refs/heads/main.zip"
        wget.download(link, 'temp/archive.zip')

        with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
            zip_ref.extractall("temp/")
        os.remove("temp/archive.zip")

        shutil.make_archive("temp/archive", "zip", "temp/AltronUserbot-main/")

        with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
            zip_ref.extractall(".")
        os.remove("temp/archive.zip")

        await message.edit('**ᴜsᴇʀʙᴏᴛ sᴜᴄᴄᴇsғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ \nʀᴇsᴛᴀʀᴛɪɴɢ...**')
        await restart(message, restart_type="update")
    except:
        await message.edit(f"**ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ...**")



