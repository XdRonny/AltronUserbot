import os
os.system("pip install telethon")

os.system("pip3 install -U pyrogram")

from telethon.sync import TelegramClient
from telethon.sessions import StringSession 
from pyrogram import Client
from telethon.tl.functions.channels import JoinChannelRequest


okbro = input("Enter y or yes to continue: ")

if okbro == "y" or "yes":
  print("Choose String Type \n1.Telethon\n2.Pyrogram")
  library = input("\nYour Choice:" )
  if library == "1":
    print("Welcome To Telethon String Generator")
    APP_ID = int(input("Enter APP ID - "))
    API_HASH = input("Enter API HASH - ")
    try:
      with TelegramClient(StringSession(), APP_ID, API_HASH) as bot:
        string_session = bot.session.save()
        bot(JoinChannelRequest("@Altron_X"))
        print("You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions.")
        bot.send_message("me", f"`{string_session}`\n\n• __Dont Share String Session With Anyone__\n•Dont Invite Anyone To Heroku")
    except Exception as e:
      print(e)
  elif library == "2":
    APP_ID = int(input("\nEnter Ur APP ID ~: "))
    API_HASH = input("\nEnter Ur API_HASH ~: ")
    try:
      with Client(':memory:', APP_ID, API_HASH) as boy:
        lol = boy.export_session_string()
        text = "`{}`\n\n Pyrogram String Session".format(lol)
        boy.send_message("me", text)
    except Exception as e:
      print(e)
    print("Successfully Pyrogram String Session Has Been Generated \nCheck Ur Saved Message \nIf U Terminate Sessions Then U Have To Generate Gain\nDont Try To Share STRING SESSION with Anyone")
  else:
    print("\nclick On Green Button And Start Again  \nChoose 1 For Userbot \nChoose 2 For Pyrogram \n Pahle Run karo fir se Tab 1 ya 2 Koi Ek Select Karna")