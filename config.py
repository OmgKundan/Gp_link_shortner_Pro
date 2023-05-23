# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23501167"))
API_HASH = os.environ.get("API_HASH", "72f7270a1b4bd3ee93629a396ebb5004")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6093098314:AAFLevnUGEg0boQ3hrkVUSA1M9FdWK3dCM8")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5143024716")] if os.environ.get("ADMINS") else []
ADMIN = ADMIN
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TelegramBots")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://TelegramBot:kundanv1006x@telegrambot.phzuxsj.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5143024716")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel User name Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
