# import modules
from telegram.constants import ParseMode


async def init(update, context, r1 ,new):
    if r1.get('new_user', 'custom') == 'True':
        spammer = False
        spammer_name = ['Téléаgrаm', 'GrouР', 'Рrivаte Рromotioㄨㄨ']
        for ext in spammer_name:
            if ext in update.message.from_user.first_name:
                spammer = True
        if spammer:
            await context.bot.ban_chat_member(update.message.chat.id, new.id, timeout=None, until_date=None)
            await update.message.reply_text("User [{}][{}][@{}] Banned\n\n"
                                            "<b>Reason:</b> Spammer".format(new.id,
                                                                            new.first_name,
                                                                            new.username),
                                            parse_mode=ParseMode.HTML)
            return True
        else:
            return False
    else:
        return False
    