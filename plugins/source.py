# Basic bs4 and requests extraction...
import os
import asyncio
import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters, errors
from pyrogram.types import *

@Client.on_message(filters.command('source') & filters.private)
async def start(bot, cmd):
    txt = cmd.text
    me = await bot.get_me()
    if len(txt) > 8:
        RURL = txt.split(" ")[1]
        a = await cmd.reply_text(f"Wait **Baka** I am scrapping the webpage `{RURL}` ...")
        try:
            page = requests.get(RURL)
            soup = BeautifulSoup(page.content, "html.parser")
            pre = soup.prettify()
            strsoup = str(pre)
            name = f"Web-baka-scrapper-{cmd.from_user.id}.txt"
            with open(name, 'w') as f:
                f.write(strsoup)
            cap = f"Source: [->]({RURL})\nFrom {me.mention} baka !"
            await cmd.reply_document(document=name, caption=cap, quote=True)
            await a.edit("Completed !!")
            await a.delete()
        except:
            await a.edit("Something is wrong with your link 😑\nMake sure that's a webpage link...")
        remove(name)
    else:
        await cmd.reply_sticker("CAACAgUAAxkBAAEMHjphY-XBDkah-iAgca0nflKX3arZqAACIgQAAthVoVXewVW3WmMkcSEE", quote=True)
        await cmd.reply_text("Just paste your link in /source `[webpage link]`")
