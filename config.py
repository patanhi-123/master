import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7675618993:AAElJv_YpBNB_tOBSrntImXs0f3Do9ppfHQ"
    # Telegram API ki ID
    API_ID = 20114039
    # Telegram API ki hash key
    API_HASH = "87297b8f3cc8fc9bbce591ad30da5896"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '8172163893'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://mcacourse01:nEDXm37rW8u1VKUe@cluster0.dt5hh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002647652455
    # Authentication log channel ki ID
    AUTH_LOG = -1002647652455
    # Hit log channel ki ID
    HIT_LOG = -1002647652455
    # DRM dump channel ki ID
    DRM_DUMP = -1002647652455
    # Main channel ki ID
    CHANNEL = -1002274225498
    # Channel ka link
    CH_URL = "https://t.me/BHUMIHAR_BOTSS"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/Thebhumihar"
    # Thumbnail image ka URL
    THUMB_URL = "https://telegra.ph/file/example-thumb-image.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

