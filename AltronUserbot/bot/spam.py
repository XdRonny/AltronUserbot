from pyrogram.types import Message
import asyncio
import time
from pyrogram import filters, Client
from config import SUDO_USERS as SUDO_USER, bot


@bot.on_message(filters.user(SUDO_USER) & filters.command(["delspam", "deletespam"], ["$", "/"]))
async def delspam(client: Client, message: Message):
    hero = await message.reply_text("⚡ ᴜsᴀɢᴇ:\n /delspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for i in range(quantity):
        await hero.delete()
        msg = await bot.send_message(message.chat.id, spam_text)
        await asyncio.sleep(1)
        await msg.delete()
        await asyncio.sleep(1)


@bot.on_message(filters.user(SUDO_USER) & filters.command(["spam"], ["$", "/"]))
async def suspam(client: Client, message: Message):
    hero = await message.reply_text("⚡ ᴜsᴀɢᴇ:\n /spam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await bot.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.2)
        return

    for _ in range(quantity):
        await hero.delete()
        await bot.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.2)


@bot.on_message(filters.user(SUDO_USER) & filters.command(["fastspam", "fspam"], ["$", "/"]))
async def spspam(client: Client, message: Message):
    hero = await message.reply_text("⚡ ᴜsᴀɢᴇ:\n /fspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await bot.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.001)
        return
    
    for _ in range(quantity):
        await hero.delete()
        await bot.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.001)


@bot.on_message(filters.user(SUDO_USER) & filters.command(["slowspam", "dspam", "delayspam"], ["$", "/"]))
async def sperm(client: Client, message: Message):
    hero = await message.reply_text("⚡ ᴜsᴀɢᴇ:\n /slowspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await bot.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(3)
        return

    for _ in range(quantity):
        await hero.delete()
        msg = await bot.send_message(message.chat.id, spam_text)
        await asyncio.sleep(3)


@bot.on_message(filters.user(SUDO_USER) & filters.command(["sspam", "stickerspam"], ["$", "/"]))
async def pussy(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("» __ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴡɪᴛʜ ᴀᴍᴏᴜɴᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴘᴀᴍ__")
        return
    if not message.reply_to_message.sticker:
        await message.edit_text(text="» __ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴡɪᴛʜ ᴀᴍᴏᴜɴᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴘᴀᴍ__")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await bot.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if umm.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await bot.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)


