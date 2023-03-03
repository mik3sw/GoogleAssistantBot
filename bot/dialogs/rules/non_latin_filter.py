import re
from configparser import ConfigParser
from telegram.constants import ParseMode


async def arabic(update, context, r1):
    if r1.get('chat', 'arabic_characters') == 'True':
        #china = re.findall(r'[\u4e00-\u9fff]+', new.first_name)
        #arabic = bool(re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+',update.message.from_user.first_name))
        try:
            arabic = bool(re.findall(r'[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+',update.message.text))
        except TypeError:
            arabic = False
        if arabic:
            await update.message.reply_text("User [{}][{}][@{}] Banned\n<b>"
                                            "Reason:</b> non_latin_filter triggered [arabic characters]".format(update.message.from_user.id,
                                                                                                                update.message.from_user.first_name,
                                                                                                                update.message.from_user.username),
                                            parse_mode=ParseMode.HTML)
            return True
        else:
            return False
    else:
        return False


async def chinese(update, context, r1):
    if r1.get('chat', 'chinese_characters') == 'True':
        #china = bool(re.findall(r'[\u4e00-\u9fff]+', update.message.from_user.first_name))
        try:
            china = bool(re.findall(r'[\u4e00-\u9fff]+', update.message.text))
        except TypeError:
            china = False
        if china:
            await update.message.reply_text("User [{}][{}][@{}] Banned\n"
                                      "<b>Reason:</b> non_latin_filter triggered [chinese characters]".format(update.message.from_user.id,
                                                                                                              update.message.from_user.first_name,
                                                                                                              update.message.from_user.username),
                                      parse_mode=ParseMode.HTML)
            return True
        else:
            return False
    else:
        return False


async def russian(update, context, r1):
    if r1.get('chat', 'russian_characters') == 'True':
        #russia = bool(re.search('[а-яА-Я]', update.message.from_user.first_name))
        try:
            russia = bool(re.search('[а-яА-Я]', update.message.text))
        except TypeError:
            russia = False
        if russia:
            await update.message.reply_text("User [{}][{}][@{}] Banned\n"
                                            "<b>Reason:</b> non_latin_filter triggered [russian characters]".format(update.message.from_user.id,
                                                                                                                    update.message.from_user.first_name,
                                                                                                                    update.message.from_user.username),
                                            parse_mode=ParseMode.HTML)
            return True
        else:
            return False
    else:
        return False


async def init(update, context):
    if update.message is not None:
        r1 = ConfigParser()
        r1.read('settings.ini')

        flag1 = await chinese(update, context, r1)
        flag2 = await arabic(update, context, r1)
        flag3 = await russian(update, context, r1)
        if flag1 or flag2 or flag3:
            print("latin filter triggered")
            await context.bot.delete_message(update.message.chat_id, update.message.message_id)
            await context.bot.ban_chat_member(update.message.chat.id, update.message.from_user.id)
    
