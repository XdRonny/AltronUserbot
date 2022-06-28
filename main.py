import asyncio
from pytgcalls import idle
from config import arq, call_py


async def main():
    await call_py.start()
    print(
        """
    ------------------
   | Userbot Actived! |
    ------------------
"""
    )
    await idle()
    await arq.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
