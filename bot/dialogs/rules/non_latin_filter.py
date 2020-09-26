import re
from configparser import ConfigParser

def arabic(update, context, r1):
    if r1.get('chat', 'arabic_characters') == 'True':
        #china = re.findall(r'[\u4e00-\u9fff]+', new.first_name)
        arabic = re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+',update.message.from_user.first_name)
        if arabic != []:
            context.bot.kick_chat_member(update.message.chat.id, update.message.from_user.id, timeout=None, until_date=None)
            update.message.reply_text("User [{}][{}][@{}] Banned\n<b>Reason:</b> non_latin_filter triggered [arabic characters]".format(update.message.from_user.id, new.first_name, new.username), parse_mode = 'HTML')
            return True
        else:
            return False
    else:
        return False


def chinese(update, context, r1):
    if r1.get('chat', 'chinese_characters') == 'True':
        china = re.findall(r'[\u4e00-\u9fff]+', update.message.from_user.first_name)
        #arabic = re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+',new.first_name)
        if china != []:
            context.bot.kick_chat_member(update.message.chat.id, update.message.from_user.id, timeout=None, until_date=None)
            update.message.reply_text("User [{}][{}][@{}] Banned\n<b>Reason:</b> non_latin_filter triggered [chinese characters]".format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.username), parse_mode = 'HTML')
            return True
        else:
            return False
    else:
        return False


def init(update, context):
    if update.message is not None:
        r1 = ConfigParser()
        r1.read('settings.ini')
        if chinese(update, context, r1) or arabic(update, context, r1):
            print("latin filter triggered") 
    
