# (c) @diablo_13N
# main ul bot
import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "1234"))
	API_HASH = os.environ.get("API_HASH", "1234")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
