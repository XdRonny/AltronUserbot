import os
import aiohttp
from Python_ARQ import ARQ
from dotenv import load_dotenv
from pyrogram import Client
from pytgcalls import PyTgCalls

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(os.getenv("API_ID", "10454970"))
API_HASH = os.getenv("API_HASH", "54a1bf2bcdf0b5a89a3e9d248f298d32")
ARQ_API_KEY = "KYTPMA-MPFWHT-PREQWH-BYBVWG-ARQ"
SESSION = os.getenv("SESSION", "BQCqnnMjEKoVZhJtpH-vZQvcIbFIHJV3OaUXhX9LOLxI8rwH1L7GY5CEOZo5uGNPj7UX1sDK7v1kQdXYT6tgD1SnwPmLgvBLxkMC9TKaYW6fiWltJoQiSy2um3jBAtlttXNfsJvdOd4NAxKlNmfVLFShangxiqNmWn_9dRh3ZawdBB2WGf2m_nHrC_zJDf8_1ujsTXohATZsQIEbN1ijtpByFno61Aw8OnIa04tQ5miIm9S2ki-q610L9c4UE26f3bX-45DdqfsVusK7m4CKmNO6dZK9eYpZXiDVnVSXg4OoVXEaexPdZw9cUKsSOT57InHpC7yiRJm0x6Rsb3Y2M74LAAAAATTHWc4A")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1323020756").split()))

aiohttpsession = aiohttp.ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)


bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="HeroUserbot"))
call_py = PyTgCalls(bot)
