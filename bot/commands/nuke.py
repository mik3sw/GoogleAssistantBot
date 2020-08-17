from utils import decorator
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time
@decorator.general_admin
#@decorator.cancellacomandi
def init(update, context):
    pass
    bot = context.bot
    keyboard = [[InlineKeyboardButton('☢️ AUTORIZZA LANCIO ☢️', callback_data = 'nuke')]]
    try:
        bot.send_video(update.message.chat_id, 
        video='https://media1.giphy.com/media/3ov9k9Ss9N3wO6FQ7C/giphy.gif', 
        caption='<b>MISSILE PRONTO AL LANCIO</b>\n\nAutorizzazione richiesta per confermare il lancio\n<i>Raccomandiamo di indossare occhiali da sole per assistere all\'esplosione</i>',reply_markup = InlineKeyboardMarkup(keyboard), parse_mode='HTML')
        #bot.kick_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id, timeout=None, until_date=None)
        #update.message.reply_text("Utente [{}][{}][{}] Bannato con successo".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username))
    except:
        print("an error occurred [NUKE] function")
        update.message.reply_text("Errore durante la procedura di nuclearizzazione")

@decorator.general_admin
def launch(update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'nuke':
        try:
            n = 5
            while n>0:
                query.edit_message_caption(caption="<b>LANCIO AUTORIZZATO</b>\n\nDetonazione in <b>{}</b>".format(n), parse_mode='HTML')
                time.sleep(1)
                n = n-1
            context.bot.delete_message(query.chat_id, query.message_id)
            print("done")

