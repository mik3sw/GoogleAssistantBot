import re

def init(update, context, r1 ,new):
    if r1.get('new_user', 'chinese_characters') == 'True':
        china = re.findall(r'[\u4e00-\u9fff]+', new.first_name)
        #arabic = re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+',new.first_name)
        if china != [] and new.username == None:
            context.bot.kick_chat_member(update.message.chat.id, new.id, timeout=None, until_date=None)
            update.message.reply_text("User [{}][{}][@{}] Banned\n<b>Reason:</b> non_latin_filter triggered [chinese characters]".format(new.id, new.first_name, new.username), parse_mode = 'HTML')
            return True
        else:
            return False
    else:
        return False