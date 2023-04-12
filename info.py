import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 2867802
API_HASH = '2b554cd6cd6ba30879edb053639e0170'
BOT_TOKEN = '5385354574:AAHd-OhFNr1IFcDDGy734V8VM90idD-eyQk'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False
PICS = ('https://upload.wikimedia.org/wikipedia/en/f/fc/VeerappanImg.jpg https://imgnew.outlookindia.com/public/uploads/articles/2017/2/4/veerappan_021223.jpg https://cdn.dnaindia.com/sites/default/files/styles/full/public/2016/05/18/461686-veerappan.jpg').split()

# Admins, Channels & Users
ADMINS = [5216689081]
CHANNELS = ['okfiles']
AUTH_USERS = [5216689081]
AUTH_CHANNEL = None
AUTH_GROUPS = ['movewilla1']
auth_grp = AUTH_GROUPS
auth_channel = AUTH_CHANNEL

# MongoDB information
DATABASE_URI = "mongodb+srv://veerappan:veerappan@cluster0.rtmxppr.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

LOG_CHANNEL = -1001662023089
SUPPORT_CHAT = 'MWILLA_MAIN2'
P_TTI_SHOW_OFF = True
SINGLE_BUTTON = True
IMDB = True
CUSTOM_FILE_CAPTION = "<b>🍿{file_name}\n💿Size:</b> {file_size}\n\n<b>🔥Join Our Main Channel🔥</b>\nhttps://t.me/+zoNJaYoQi6E5MGZl"
BATCH_FILE_CAPTION = "<b>🍿{file_name}\n💿Size:</b> {file_size}\n\n<b>🔥Join Our Main Channel🔥</b>\nhttps://t.me/+zoNJaYoQi6E5MGZl"
IMDB_TEMPLATE = "📺𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> | {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10 \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres}"
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = True
MAX_LIST_ELM = None
INDEX_REQ_CHANNEL = LOG_CHANNEL
FILE_STORE_CHANNEL = [-1001725304892,-1001299127702]
MELCOW_NEW_USERS = False
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = False

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
