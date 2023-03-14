from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1000"))

OWNER_ID = int(getenv("OWNER_ID", ""))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/a696147ea37e2a68f6a7e.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/a696147ea37e2a68f6a7e.jpg")

SESSION = getenv("SESSION", "")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Punjabi_study_hall")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AboutPunjabi")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5017218199").split()))


FAILED = "https://telegra.ph/file/a696147ea37e2a68f6a7e.jpg"
