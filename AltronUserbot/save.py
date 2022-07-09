import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.command import commandpro


@Client.on_message(commandpro(["!save", "op"]) & filters.private & ~filters.me)
async def downloader(_, message: Message):
    targetcontent = message.reply_to_message
    downloadtargetcontent = await Client.download_media(targetcontent)
    send = await Client.send_document("me", downloadtargetcontent)
    os.remove(downloadtargetcontent)


"""sᴀᴠᴇ ᴀɴʏ sᴇʟғ ᴅᴇsᴛʀᴜᴄᴛɪᴠᴇ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴛᴏ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇ"""