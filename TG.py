import time

import telegram

def signal_myTG(text):
    try:
        TOKEN = '814536928:AAEcl6sWMvDjaKr2r_kJDV9vzDifUv4Rn-U'
        chat_IDs = ['509403225']
        bot = telegram.Bot(token=TOKEN)
        bot.send_message(chat_id=chat_IDs[0], text=text)
        time.sleep(1)
    except:
        time.sleep(5)

def signal_myTG_silent(text):
    try:
        TOKEN = '814536928:AAEcl6sWMvDjaKr2r_kJDV9vzDifUv4Rn-U'
        chat_IDs = ['509403225']
        bot = telegram.Bot(token=TOKEN)
        bot.send_message(chat_id=chat_IDs[0], text=text, disable_notification=True)
        time.sleep(1)
    except:
        time.sleep(5)