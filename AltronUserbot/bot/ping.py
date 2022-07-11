from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import *
from helpers.data import *


@Client.on_message(filters.command(["ping"], ["/", "!", ".", "$"]) & filters.user(SUDO_USERS))
@Client.on_message(filters.command(["ping"], ["/", "!", ".", "$"]) & filters.me)
@Client.on_message(filters.command(["ping"], ["/", "!", ".", "$"]) & filters.user(OWNERS))
async def ping_pong(_, m: Message):
    start = time()
    reply = await m.reply_text("» __ᴀʟᴛʀᴏɴ__")
    ping = time() - start
    await reply.edit_text(
        f"🤖 ᴘɪɴɢ: `{ping * 1000:.3f} ᴍs`"
    )

