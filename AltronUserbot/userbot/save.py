import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.command import commandpro
from helpers.decorators import sudo_users_only, errors


@Client.on_message(commandpro(["!save", "op"]) & filters.private & ~filters.edited)
@sudo_users_only
@errors
async def downloader(_, message: Message):
    targetcontent = message.reply_to_message
    downloadtargetcontent = await Client.download_media(targetcontent)
    send = await Client.send_document("me", downloadtargetcontent)
    os.remove(downloadtargetcontent)


"""Save Any Self Destructive Photo Or Video To Your Saved Message"""