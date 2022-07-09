import asyncio
import datetime
import os
import re
import sys
from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio
from helpers.queues import QUEUE, add_to_queue, get_queue, clear_queue

from config import bot, client, call_py, call_py2, call_py3, call_py4, call_py5, SUDO_USERS


aud_list = [
    "./helpers/AUDIO1.mp3",
    "./helpers/AUDIO2.mp3",
]



@bot.on_message(filters.user(SUDO_USERS) & filters.command(["vcraid"], ["/", ".", "!"]))
@bot.on_message(filters.me & filters.command(["vcraid"], ["/", ".", "!"]))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    inp = e.text.split(None, 2)[1]
    chat = await client.get_chat(inp)
    chat_id = chat.id
    aud = choice(aud_list) 

    if inp:
        bot = await e.reply_text("**Starting Raid **")
        link = f"https://github.com/TheAltron{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"__😈 Raiding in:__ {chat.title} \n\n__🔊 Audio:__ {songname} \n\n__#⃣ Position:__ #{pos}")
        else:
            if call_py:
                await call_py.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py2:
                await call_py2.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py3:
                await call_py3.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py4:
                await call_py4.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            if call_py5:
                await call_py5.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await bot.delete()
            await e.reply_text(f"**> Raiding in:** {chat.title} \n\n**> Audio:** {songname} \n**> Position:** Ongoing Raid")



@bot.on_message(filters.user(SUDO_USERS) & filters.command(["raidend"], ["/", ".", "!"]))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await client.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.leave_group_call(chat_id)
            if call_py2:
                await call_py2.leave_group_call(chat_id)
            if call_py3:
                await call_py3.leave_group_call(chat_id)
            if call_py4:
                await call_py4.leave_group_call(chat_id)
            if call_py5:
                await call_py5.leave_group_call(chat_id)
            await e.reply_text("**VC Raid Ended!**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**No ongoing raid!**")


@bot.on_message(filters.user(SUDO_USERS) & filters.command(["raidpause"], ["/", ".", "!"]))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await client.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.pause_stream(chat_id)
            if call_py2:
                await call_py2.pause_stream(chat_id)
            if call_py3:
                await call_py3.pause_stream(chat_id)
            if call_py4:
                await call_py4.pause_stream(chat_id)
            if call_py5:
                await call_py5.pause_stream(chat_id)
            await e.reply_text(f"**VC Raid Paued In:** {chat_.title}")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No ongoing raid!**")


@bot.on_message(filters.user(SUDO_USERS) & filters.command(["raidresume"], ["/", ".", "!"]))
async def ping(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text.split(None, 2)[1]
        chat_ = await client.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    if chat_id in QUEUE:
        try:
            if call_py:
                await call_py.resume_stream(chat_id)
            if call_py2:
                await call_py2.resume_stream(chat_id)
            if call_py3:
                await call_py3.resume_stream(chat_id)
            if call_py4:
                await call_py4.resume_stream(chat_id)
            if call_py5:
                await call_py5.resume_stream(chat_id)
            await e.reply_text(f"**VC Raid Resumed In {chat_.title}**")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**No raid is currently paused!**")
