import os
import aiohttp
from Python_ARQ import ARQ
from dotenv import load_dotenv
from pyrogram import Client
from pytgcalls import PyTgCalls

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ARQ_API_KEY = "KYTPMA-MPFWHT-PREQWH-BYBVWG-ARQ"
SESSION = os.getenv("SESSION", "")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1323020756").split()))

aiohttpsession = aiohttp.ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)


bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="AltronUserbot"))
call_py = PyTgCalls(bot)
