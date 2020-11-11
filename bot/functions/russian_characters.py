import re

def init(update, context, r1 ,new):
    if r1.get('new_user', 'russian_characters') == 'True':
        russian = bool(re.search('[а-яА-Я]', new.first_name))
        if russian and new.username == None:
            context.bot.kick_chat_member(update.message.chat.id, new.id, timeout=None, until_date=None)
            update.message.reply_text("User [{}][{}][@{}] Banned\n<b>Reason:</b> non_latin_filter triggered [Cyrillic characters]".format(new.id, new.first_name, new.username), parse_mode = 'HTML')
            return True
        else:
            return False
    else:
        return False