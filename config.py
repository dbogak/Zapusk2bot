import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
URL = os.getenv("URL")
ADMIN_ID = os.getenv("ADMIN_ID")