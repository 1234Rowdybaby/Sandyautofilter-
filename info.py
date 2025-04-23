import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '24222039'))
API_HASH = environ.get('API_HASH', '6dd2dc70434b2f577f76a2e993135662')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6046055058').split()]
USERNAME = environ.get('USERNAME', 'https://t.me/Sandymaiwait')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002433610423'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002694840394').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://koolscott5:U26geFv5dNH5HJ9u@movie.khl6kij.mongodb.net/?retryWrites=true&w=majority&appName=movie")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://koolscott5:U26geFv5dNH5HJ9u@movie.khl6kij.mongodb.net/?retryWrites=true&w=majority&appName=movie")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rahul")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Rahul')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002534471850'))
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/5635f6bd5f76da19ccc70-695af75bfa01aacbf2.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002686020221'))
URL = environ.get('URL', '')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002395784504'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/+URI0ggQ1mLAyM2Y1")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/+URI0ggQ1mLAyM2Y1")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/+URI0ggQ1mLAyM2Y1")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/e6c8c517ee3f42d5d772e-331533c6320d361b70.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "7e5614ab72f04b5f6df4e1e93c8fca3bd1910574")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shortifyurl.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "5b22551890e0d5f2fded51fd64218868131bef1a")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "shortner.in")
SHORTENER_API3 = environ.get("SHORTENER_API3", "7e609d0db7155014ae17d47582d1ffb073143a9e")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "seturl.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "300"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "10800"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002260068200')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002459015261'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 120))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', True)
