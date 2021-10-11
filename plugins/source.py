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
        
        with open(f"web-baka-scrapper-{cmd.from_user.id}.txt", "w+") as file:
            file.write(soup)
        try:
        await cmd.reply_document("web-baka-scrapper-{cmd.from_user.id}.txt")

        remove(f"web-baka-scrapper-{cmd.from_user.id}.txt")
    else:
        await cmd.reply_sticker("CAACAgIAAxkBAAJtdWEJ8kFVLOTcJZkoO4AgLEQiqhjVAAIpKwAC4KOCBxOA6A0D4-_jIAQ", quote=True)
        await cmd.reply_text("No query please give streamtape vaild link",
