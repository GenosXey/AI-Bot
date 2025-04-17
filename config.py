import os

API_ID = os.getenv("API_ID", "24817837")
API_HASH = os.getenv("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8086801925:AAFC1H9aum3e3_Ny0J_oYAOBHuqBfYWL1_o")
ADMIN = int(os.getenv("ADMIN", "7428552084"))

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002376378205"))

DB_URI = os.getenv("DB_URI", "Gemini")
DB_NAME = os.getenv("DB_NAME", "mongodb+srv://Ethan:Ethan123@telegrambots.lva9j.mongodb.net/?retryWrites=true&w=majority&appName=TELEGRAMBOTS")

IS_FSUB = bool(os.environ.get("FSUB", True)) # Set "True" For Force Subscribe Enable
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "-1002647818964") # Add Multiple Channels iD By Space
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")] # DONT TOUCH

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyCqmDwlmYKVKtYi9H1KWmz53Yvcqfvr0MQ")
