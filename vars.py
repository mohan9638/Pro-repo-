#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25693368"))
API_HASH = environ.get("API_HASH", "2dcf91b0f99c0b9d4875e87020e6bd07")
BOT_TOKEN = environ.get("BOT_TOKEN", "8406524910:AAEG_tGC6oJ4hQif58OQ_9Q7eos-jqSj_TY")

OWNER = int(environ.get("OWNER", "5927517339"))
CREDIT = environ.get("CREDIT", "Astronaut bro")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5927517339').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5927517339').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
