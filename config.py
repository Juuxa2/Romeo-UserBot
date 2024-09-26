from os import getenv

API_ID = int(getenv("API_ID", "23949116"))
API_HASH = getenv("API_HASH", "4ec783a0bb5d1705872019a5582052b2")
BOT_TOKEN = getenv("BOT_TOKEN", "7724150021:AAGNxF-8uGgFGVjzUVYe4iOhD7egcp7X4bA")
OWNER_ID = int(getenv("OWNER_ID", "5419679301"))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5392070730").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/RRomeo-RJ/Romeo-UserBot")
BRANCH = getenv("BRANCH", "main")
