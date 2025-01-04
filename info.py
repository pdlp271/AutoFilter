import re
import os
from os import environ
from Script import script
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
API_ID = int(environ.get('API_ID', '20421609'))
API_HASH = environ.get('API_HASH', '17187c5466fb7044793bfa8bcaa9ec68')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

PICS = (environ.get('PICS', 'https://telegra.ph/file/e70b244bb8fe9725e66f1.jpg https://telegra.ph/file/34e7e5bea04a88d534414.jpg https://telegra.ph/file/57a9ae4c1858927eda696.jpg https://telegra.ph/file/ee8aeccd8085907695d5a.jpg https://telegra.ph/file/a15da92b0761b4e8b7e50.jpg')).split() #SAMPLE PIC
START_IMG = environ.get('START_IMG', 'https://graph.org/file/208ae1ffacc082167dbc4.jpg')
QR_CODE = environ.get('QR_CODE', '')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1511468725').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/master_hp_raj")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001965914571'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/+hf0frQmRGu41Yzll')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001840476165').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Hanuman:hanuman@cluster0.l5toshc.mongodb.net/?retryWrites=true&w=majority")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @codflix_bots</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

#chatgptAI
AI = is_enabled((environ.get("AI","True")), True)
OPENAI_API = environ.get("OPENAI_API", " ")
DEEP_API = environ.get("DEEP_API", "3ac9b077-654f-45c6-a1f0-a04a5ef6b69e")
GOOGLE_API_KEY = environ.get("GOOGLE_API_KEY", "AIzaSyD214hhYJ-xf8rfaWX044_g1VEBQ0ua55Q")
AI_LOGS = int(environ.get("AI_LOGS", "-1002241178189")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of Bot ]

DATABASE_NAME = environ.get('DATABASE_NAME', "Hanuman")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'HPfiles')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002241178189'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1002241178189'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1002241178189'))
URL = environ.get('URL', 'mytestbot-jvdfhbj.com') # your deployment url
STICKERS_IDS = ('CAACAgUAAxkBAAEC5s1mfmbnUx4f7jYODXqmoDo_QltzLQACmw4AAl3VAVYieASlHlskATUE').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002241178189'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/+nxvxKoPvhCQ1YTU1")
SHORTENER_API = environ.get("SHORTENER_API", "7e335f593c8245c04914bc963bf25651b04c58f2")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'publicearn.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "8eb15032be0a2c1a4617bd3ccb5ab7ec6f7728ca")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'yamlinks.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "dcab14efdb8e3231f789590031cc348b36c69dff")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'Rglinks.com')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '-1002241178189')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001599336908'))
request_channel = environ.get('REQUEST_CHANNEL', '-1001928522177')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1002241178189'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1001928522177'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
    }
DEFAULT_POST_MODE = {
    'singel_post_mode' : False,
    'all_files_post_mode' : False
}
