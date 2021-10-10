
import os
import aiohttp
from configs import Config
from bs4 import BeautifulSoup
from pyrogram import Client
from pyrogram.types import *
cloudscraper

Bot = Client("Bakascrapper", bot_token=Config.BOT_TOKEN, api_id=Config.API_ID, api_hash=Config.API_HASH, plugins={"root": "plugins"})

Bot.run()
