from utils import decorator
import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time

nuked = 0

@decorator.general_admin
#@decorator.cancellacomandi
def init(update, context):
    pass
    bot = context.bot
    keyboard = [[InlineKeyboardButton('☢️ AUTORIZZA LANCIO ☢️', callback_data = 'nuke')]]
    try:
        stronzo = update.message.reply_to_message.from_user.id
        set_nuke(stronzo)
        bot.send_video(update.message.chat_id, 
        video='https://media1.giphy.com/media/3ov9k9Ss9N3wO6FQ7C/giphy.gif', 
        caption='[{}]\n<b>MISSILE PRONTO AL LANCIO</b>\n\nAutorizzazione richiesta per confermare il lancio\n<i>Raccomandiamo di indossare occhiali da sole per assistere all\'esplosione</i>'.format(stronzo),reply_markup = InlineKeyboardMarkup(keyboard), parse_mode='HTML')
        #bot.kick_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id, timeout=None, until_date=None)
        #update.message.reply_text("Utente [{}][{}][{}] Bannato con successo".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username))
    except:
        print("an error occurred [NUKE] function")
        update.message.reply_text("Errore durante la procedura di nuclearizzazione")

@decorator.general_admin
def launch(update, context):
    pass
    #print("\n\n\nRICONOSCO L'ADMIN\n\n\n")
    query = update.callback_query
    query.answer()
    if query.data == 'nuke':
        try:
            n = 5
            while n>0:
                query.edit_message_caption(caption="<b>LANCIO AUTORIZZATO</b>\n\nDetonazione in <b>{}</b>".format(n), parse_mode='HTML')
                time.sleep(1)
                n = n-1
            context.bot.delete_message(update.callback_query.message.chat_id, update.callback_query.message.message_id)
            print("done")
            #https://i.pinimg.com/originals/6c/48/5e/6c485efad8b910e5289fc7968ea1d22f.gif
            context.bot.send_video(update.callback_query.message.chat_id, 
                video='https://i.pinimg.com/originals/6c/48/5e/6c485efad8b910e5289fc7968ea1d22f.gif', 
                caption='<b>UTENTE NUCLEARIZZATO CON SUCCESSO</b>', parse_mode='HTML')
            global nuked
            print(nuked)
            #context.bot.kick_chat_member(update.message.chat.id, nuked, timeout=None, until_date=None)
            #print(stronzo)

        except:
            print('Error')
            

def set_nuke(stronzo):
    global nuked 
    nuked = stronzo
    print(nuked)

