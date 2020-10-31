import re

def custom_spam(capt):
    spam_list = ['errori di prezzo', 'offerta imperdibile']
    res = [ele for ele in spam_list if(ele in capt)]
    return bool(res)


def init(update, context):
    if update.message.photo is not None:
        capt = update.message.caption
        china = bool(re.findall(r'[\u4e00-\u9fff]+', capt))
        arabic = bool(re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+',capt))
        russia = bool(re.search('[а-яА-Я]', capt))
        spam = custom_spam(str(capt).lower())
        
        if china or arabic or russia or spam:
            #caption with banned characters
            context.bot.delete_message(update.message.chat_id, update.message.message_id)
            context.bot.kick_chat_member(update.message.chat_id,update.message.from_user.id)
            context.bot.send_message(update.message.chat_id,text ="Banned image detected!\n[{}][{}][@{}] Banned and message deleted!".format(update.message.from_user.id, update.message.from_user.first_name, update.message.from_user.username),parse_mode='HTML')


