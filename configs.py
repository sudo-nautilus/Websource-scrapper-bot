# (c) @diablo_13N
# main ul bot
import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "2176353"))
	API_HASH = os.environ.get("API_HASH", "9265189e6b3c63d54bf637256fe78523")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
