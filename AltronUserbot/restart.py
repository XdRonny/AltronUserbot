import os
import sys
from pyrogram.types import Message
from helpers.command import commandpro
from pyrogram import Client
from os import system, execle, environ
from helpers.decorators import errors, sudo_users_only


@Client.on_message(commandpro(["R", "!restart", "Restart", "/restart"]))
@errors
@sudo_users_only
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("» __ᴜsᴇʀʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ__\n» __ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴜsᴇʀʙᴏᴛ ᴀғᴛᴇʀ 𝟹𝟶s__ ")
    execle(sys.executable, *args, environ)
    return
