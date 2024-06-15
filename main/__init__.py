#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# variables
API_ID = "24310324"#config("API_ID", default=None, cast=int)
API_HASH = "c464afc9e1b8b2793a43fe8ece443bf5"#config("API_HASH", default=None)
BOT_TOKEN = "7307527131:AAHQ4lqjf2m--TddjQRSWP_UrJ7WuO5et0g"#config("BOT_TOKEN", default=None)
SESSION = "AQGqa00AQl_eHp1I_II8gEOSPHFBBz6ipjRGNL3sBdbuaiZwmFnWhGw4GFL0Yq1ryMWuGGZD-WePYdLMg4-nOxvOeJwjOTCpWnzzhs-1dYSaawq7nZuWy0YS43tTrU7jV9liA4T4_5pg6xtvSYj6qOFWG0La0hsozrei6ERBnHU5Yh3rz-ONWw6XL4Fhgz7vK9w8u-wKROYTB21mZoUES7bkeV7poOVOhjP8eYi_ejk8VtywLtZJPrLVleVFg-f2C-zSVETJsAeQkk_tjHlNKnzhHe4d-WUB53WaageHN0yboXvDees-z1S6oaUdLjmiSkO06RlwHwJT4xGMzlLxh9hywEYhgAAAAAFNVAIIAA" #config("SESSION", default=None)
FORCESUB = "nachmeribulbul"#config("FORCESUB", default=None)
AUTH = "5592318472"#config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    # print(e)
    # logger.info(e)
    sys.exit(1)
