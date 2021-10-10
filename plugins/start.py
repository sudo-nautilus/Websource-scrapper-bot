import os
import asyncio
import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters, errors
from pyrogram.types import *

@Client.on_message(filters.command('start') & filters.private)
async def start(bot, cmd):
    await cmd.reply_text(f"👋 **Hello** [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id} !\n I am baka web scrapper bot I can give you source code of any websites !(almost 🧐) )",
                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Developer",
                                                                                  url="https://t.me/diablo_13N"),
                                                             InlineKeyboardButton("Support Group",
                                                                                  url="https://t.me/anim_chatx")], [
                                                                InlineKeyboardButton("my Channel",
                                                                                     url="https://t.me/baka_no_onii")],
                                                            [InlineKeyboardButton("Delete this message", callback_data="delmess")]]))
