import re
from configparser import ConfigParser

def arabic(update, context, r1):
    if r1.get('chat', 'arabic_characters') == 'True':
        #china = re.findall(r'[\u4e00-\u9fff]+', new.first_name)
        arabic = bool(re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+',update.message.from_user.first_name))
        arabic1 = bool(re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+',update.message.text))
        if arabic or arabic1:
            update.message.reply_text("User [{}][{}][@{}] Banned\n<b>Reason:</b> non_latin_filter triggered [arabic characters]".format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.username), parse_mode = 'HTML')
            return True
        else:
            return False
    else:
        return False


def chinese(update, context, r1):
    if r1.get('chat', 'chinese_characters') == 'True':
        china = bool(re.findall(r'[\u4e00-\u9fff]+', update.message.from_user.first_name))
        china1 = bool(re.findall(r'[\u4e00-\u9fff]+', update.message.text))
        if china or china1:
            update.message.reply_text("User [{}][{}][@{}] Banned\n<b>Reason:</b> non_latin_filter triggered [chinese characters]".format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.username), parse_mode = 'HTML')
            return True
        else:
            return False
    else:
        return False

def russian(update, context, r1):
    if r1.get('new_user', 'russian_characters') == 'True':
        russia = bool(re.search('[а-яА-Я]', update.message.from_user.first_name))
        russia1 = bool(re.search('[а-яА-Я]', update.message.text))
        if russia or russia1:
            update.message.reply_text("User [{}][{}][@{}] Banned\n<b>Reason:</b> non_latin_filter triggered [russian characters]".format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.username), parse_mode = 'HTML')
            return True
        else:
            return False
    else:
        return False


def init(update, context):
    if update.message is not None:
        r1 = ConfigParser()
        r1.read('settings.ini')
        
        if chinese(update, context, r1) or arabic(update, context, r1) or russian(update, context, r1):
            print("latin filter triggered")
            context.bot.delete_message(update.message.chat_id, update.message.message_id)
            context.bot.kick_chat_member(update.message.chat.id, update.message.from_user.id, timeout=None, until_date=None) 
    
