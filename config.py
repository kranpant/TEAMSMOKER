import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 23281569
API_HASH = "a4b1ede83dfbdfefdbc474035df634f4"
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN","8559204606:AAHHBApP0ajAL6Jh6ZDAuEizNXQDKR1BFQ0" default=None)
BOT_TOKEN2 = getenv("BOT_TOKEN2","8548826639:AAG_MhlkhVV0jO70a-kTFALzI1AvP_xr4OM" default=None)
BOT_TOKEN3 = getenv("BOT_TOKEN3","8424188372:AAEUOrFVf6ltODHGFlQn9oAnkTG8vEKcsds" default=None)
BOT_TOKEN4 = getenv("BOT_TOKEN4","8486490317:AAHhfOmRjOznt0o9oHvqOhE38kd1atat2mc" default=None)
BOT_TOKEN5 = getenv("BOT_TOKEN5","8279419686:AAENjTMk7qi7eBY0bNI0WzuzLk2DTjcDFQs" default=None)
BOT_TOKEN6 = getenv("BOT_TOKEN6","8550945087:AAGC_hVAqAKw4m82sUDv44ABrgmMaOA9KhU" default=None)
BOT_TOKEN7 = getenv("BOT_TOKEN7","8122341984:AAGnTNzoVWtW2eki3yKGVhDw1P0RHiKarjA" default=None)
BOT_TOKEN8 = getenv("BOT_TOKEN8","8381481152:AAEAzSz7oTjKRr5GKf8CzSEj5d4w9VtCXh0" default=None)
BOT_TOKEN9 = getenv("BOT_TOKEN9","8562948465:AAFuDw--7H_QsmzBNduhXWoEasTidAteEC4" default=None)
BOT_TOKEN10 = getenv("BOT_TOKEN10","8585725407:AAHan_3ersHHs5skszNZk7TcuY8wVfjq4jg" default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5518687442").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="5533647702"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)


