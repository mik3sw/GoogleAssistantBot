import re
from configparser import ConfigParser

def chinese_characters(update, context):
    r1 = ConfigParser()
    r1.read('settings.ini')
    
    if update.message.text is not None:
        if r1.get('chat', 'chinese_characters')=='True':
            china = re.findall(r'[\u4e00-\u9fff]+', update.message.text)
            if china != []:
                context.bot.delete_message(update.message.chat_id, update.message.message_id)
                context.bot.send_message(update.message.chat_id, text = "Chinese characters not allowed!")

def arabic_characters(update, context):
    r1 = ConfigParser()
    r1.read('settings.ini')
    
    if update.message.text is not None:
        if r1.get('chat', 'arabic_characters')=='True':
            arabic = re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+', update.message.text)
            if arabic != []:
                context.bot.delete_message(update.message.chat_id, update.message.message_id)
                context.bot.send_message(update.message.chat_id, text = "Arabic characters not allowed!")
