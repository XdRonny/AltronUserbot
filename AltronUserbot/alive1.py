from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client
 

 
@Client.on_message(filters.command(["omp", "awake"], [".", "!"]) & filters.me)
async def alive(client: Client, e: Message):
        Alive_msg = f" 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo="https://te.legra.ph/file/0957630b8248e79400247.jpg",
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/Superior_Bots")
                ], [
                    InlineKeyboardButton(
                        "• 𝐑𝐞𝐩𝐨 •", url="https://github.com/ITZ-ZAID/ZAID-USERBOT")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo="https://te.legra.ph/file/0957630b8248e79400247.jpg",
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/Superior_Bots"),
                ],
                [
                    InlineKeyboardButton("• 𝐑𝐞𝐩𝐨 •", url="https://github.com/Itz-Zaid/Zaid-Userbot"),
                ],
            ],
        ),
    ) 


