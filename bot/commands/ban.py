from utils import decorator
@decorator.general_admin
#@decorator.cancellacomandi
def init(update, context):
    pass
    bot = context.bot
    try:
        bot.send_video(update.message.chat_id, 
        video='http://4.bp.blogspot.com/-HUn5hfk8OzQ/UM_Pi-bGphI/AAAAAAAAEVY/JO-DljB1L2I/s1600/explosi%25C3%25B3n+gif.gif', 
        caption='<b>QUESTA NON E\' UN\'ESERCITAZIONE</b>\n\nRecarsi immediatamente al bunker antiatomico, ripeto <b>NON E\' UN\'ESERCITAZIONE</b>', parse_mode='HTML')
        bot.kick_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id, timeout=None, until_date=None)
        update.message.reply_text("Utente [{}][{}][{}] Bannato con successo".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username))
    except:
        print("an error occurred [BAN] function")
        update.message.reply_text("Errore durante la procedura")
