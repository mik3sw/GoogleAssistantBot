# import modules
import re
from config import admin_group
from telegram.constants import ParseMode


def custom_spam(capt):
    spam_list = ['errori di prezzo', 'offerta imperdibile']
    res = [ele for ele in spam_list if(ele in capt)]
    return bool(res)


async def init(update, context):
    if update.message.photo is not None:
        capt = update.message.caption
        try:
            china = bool(re.findall(r'[\u4e00-\u9fff]+', capt))
            arabic = bool(re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+',capt))
            russia = bool(re.search('[а-яА-Я]', capt))
        except TypeError:
            china, arabic, russia = False, False, False

        spam = custom_spam(str(capt).lower())
        
        if china or arabic or russia or spam:
            # caption with banned characters
            await context.bot.delete_message(update.message.chat_id, update.message.message_id)
            await context.bot.ban_chat_member(update.message.chat_id,update.message.from_user.id)
            await context.bot.send_message(admin_group,text ="Banned image detected!\n"
                                                             "[{}][{}][@{}] Banned and message deleted!".format(update.message.from_user.id,
                                                                                                                update.message.from_user.first_name,
                                                                                                                update.message.from_user.username),
                                           parse_mode=ParseMode.HTML)
