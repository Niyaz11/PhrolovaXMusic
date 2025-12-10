import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ── Core bot config ────────────────────────────────────────────────────────────
API_ID = ("29245477")
API_HASH = ("0abc83883262245c90ca337b7a0375c4")
BOT_TOKEN = ("8462016049:AAFc616pDsbIHi_9oznM5Of8skNyBLhu1VI")

OWNER_ID = ("7654385403")
OWNER_USERNAME = ("EternalsHelplineBot")
BOT_USERNAME = ("PhrolovaXRobot")
BOT_NAME = ("Phrolova Music Bot")
ASSUSERNAME = ("Phrolova Assistant")

# ── Database & logging ─────────────────────────────────────────────────────────
MONGO_DB_URI = ("BQG-QCUADnnVXVuveX6LuoqnxCBIwhra6bW8KLvSTOwc2-eKJ9YrIhMVaJs9Pb4s2kDOmHC0Eqn18Hh23ThKA5CPS7vOguAFGMZvwnqrmutfh6r8vx6-8QJH3LL_oyIRDzURtds2DOTEsbcyLnu-nJti4h7wN4HyNCeB78ZYy213LLhD_iC3f8O6SYgtGhhWGxb6yIwnZXTxeK2wBWpvyFVRWBFvxXz33BX411WgFlgQ1dDwKHCBqXGN7vqlcQ9nXXAFz13z7HFyKhguBb6P48NDAa9YIVu7P-R1iJUv4nnMZ8AAwiDdFUdP7L7jELIdJNnVcQ9nynY3ngCisAunj7Zuse8djgAAAAHjIGUMAA")
LOGGER_ID = (-1002456565415)

# ── Limits (durations in min/sec; sizes in bytes) ──────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "157286400"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1288490189"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))

# ── External APIs ──────────────────────────────────────────────────────────────
COOKIE_URL = "https://batbin.me/bractea"  # required (paste link)

API_URL = getenv("")        # optional

API_KEY = getenv("1a853d_YG-HBNXmKh7S3aZOC3Czqa3CuGI7Jh2n") 

DEEP_API = "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"     # optional

# ── Hosting / deployment ───────────────────────────────────────────────────────
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ── Git / updates ──────────────────────────────────────────────────────────────
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Niyaz11/PhrolovaXMusic/tree/Master")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("")  # needed if repo is private

# ── Support links ──────────────────────────────────────────────────────────────
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EternalsHelplineBot")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EternalsHelplineBot")

# ── Assistant auto-leave ───────────────────────────────────────────────────────
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ── Debug ──────────────────────────────────────────────────────────────────────
DEBUG_IGNORE_LOG = True

# ── Spotify (optional) ─────────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ── Session strings (optional) ─────────────────────────────────────────────────
STRING1 = "mongodb+srv://musicxrobot:8Up92WwJbgUS39FV@cluster0.ys1jirt.mongodb.net/"
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ── Media assets ───────────────────────────────────────────────────────────────
START_VIDS = [
    "https://files.catbox.moe/mfflt7.mp4"
]

STICKERS = [
    "CAACAgUAAx0CbtMXSgABAW6caMkVZHh-SOgPD2le3Jj11X3RKHIAAlQcAAJtkUhWuAQct1VGfYkeBA",
]

HELP_IMG_URL = "https://files.catbox.moe/zzad1n.mp4"
PING_VID_URL = "https://files.catbox.moe/pwdo2t.mp4"

PLAYLIST_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
STATS_VID_URL = "https://files.catbox.moe/xyeute.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/wrj24v.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/a8jnkm.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/a8jnkm.jpg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ───── Utility & Functional ───── #
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── Bot Introduction Messages ───── #
AYU = ["💞", "🦋", "🔍", "🧪", "⚡️", "🔥", "🎩", "🌈", "🍷", "🥂", "🥃", "🕊️", "🪄", "💌", "🧨"]
AYUV = [
    "<b>Hᴇʏ Tʜᴇʀᴇ •{0} I'ᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ + ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ Mᴀɴʏ Fᴇᴀᴛᴜʀᴇs\nDɪᴛᴄʜ ᴛʜᴇ ᴛʜʀᴇᴀᴅs, ʟᴇᴛ's ᴠɪʙᴇ ᴛᴏ ᴛʜᴇ ʀʜʏᴛʜᴍ Jᴏɪɴ ᴍᴇ ᴏɴ Tᴇʟᴇɢʀᴀᴍ's ᴄᴜᴛᴇsᴛ ᴍᴜsɪᴄ ʙᴏᴛ.🎶\n\nʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ 24×7 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ 🎵\n\nsᴜᴘᴘᴏʀᴛ @EternalsHelplineBot</b>",
]

# ── Runtime structures ─────────────────────────────────────────────────────────
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ── Minimal validation ─────────────────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")

if not COOKIE_URL:
    raise SystemExit("[ERROR] - COOKIE_URL is required.")

# Only allow these cookie link formats
if not re.match(r"^https://(batbin\.me|pastebin\.com)/[A-Za-z0-9]+$", COOKIE_URL):
    raise SystemExit("[ERROR] - Invalid COOKIE_URL. Use https://batbin.me/<id> or https://pastebin.com/<id>")
