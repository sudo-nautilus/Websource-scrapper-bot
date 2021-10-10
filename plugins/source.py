import os
import asyncio
import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters, errors
from pyrogram.types import *

@Client.on_message(filters.command('source') & filters.private)
async def start(bot, cmd):
    txt = cmd.text
    if len(txt) > 8:
        RURL = txt.split(" ")[1]
        page = = requests.get(RURL)
        soup = BeautifulSoup(page.content, "html.parser")
        with open("web-source-scrapper.txt", "w+") as file:
            file.write(soup)


        remove("ultroid_updates.txt")

    else:
        await cmd.reply_sticker("CAACAgIAAxkBAAJtdWEJ8kFVLOTcJZkoO4AgLEQiqhjVAAIpKwAC4KOCBxOA6A0D4-_jIAQ", quote=True)
        await cmd.reply_text("No query please give streamtape vaild link",
