import os

TOKEN = os.environ.get("BOT_TOKEN")
API_HASH = os.environ.get("API_HASH")
API_ID = int(os.environ.get("API_ID"))
START_MESSAGE = os.environ.get("START_MESSAGE", "<b>Hi ! I am a simple torrent searcher using Torrent Searcher api.\n\n\nMade with 🐍 by @Ironman_cloud)
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", "<b>Made with ❤️ by @Ironman_cloud</b>")
TORRENTS = {}
