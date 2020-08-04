import re
from configparser import ConfigParser

def init(update, context):
    r1 = ConfigParser()
    r1.read('settings.ini')
    
    if update.message.text is not None:
        # ============================
		# IF NON_LATIN_FILTER IS TRUE
		# ============================
        if r1.get('settings', 'non_latin_filter')=='True':
            china = re.findall(r'[\u4e00-\u9fff]+', update.message.text)
            if china != []:
                print(china)
                context.bot.delete_message(update.message.chat_id, update.message.message_id)
                context.bot.send_message(update.message.chat_id, text = "Chinese characters not allowed")
