from pyrogram import Client, filters 
from pyrogram.types import Message
from config import SUDO_USERS
import asyncio
from helpers.data import *


@Client.on_message(filters.command(["inviteall", "kidnapall"], [".", "/", "!"]) & filters.user(SUDO_USERS))
@Client.on_message(filters.command(["inviteall", "kidnapall"], [".", "/", "!"]) & filters.user(OWNERS))
@Client.on_message(filters.command(["inviteall", "kidnapall"], [".", "/", "!"]) & filters.me)
async def inviteall(client: Client, message: Message):
    hero = await message.reply_text("__ɢɪᴠᴇ ᴍᴇ ᴀ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ғᴏʀ sᴄʀᴀᴘ ᴍᴇᴍʙᴇʀs...__")
    text = message.text.split(" ", 1)
    query = text[1]
    chat = await client.get_chat(query)
    tgchat = message.chat
    await hero.edit_text(f"__ɪɴᴠɪᴛɪɴɢ ᴜsᴇʀs ғʀᴏᴍ__ {chat.username}")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        zxb= ["online" , "recently"]
        if user.status in zxb:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()
