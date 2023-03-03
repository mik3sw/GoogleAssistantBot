# import modules
from utils import decorator
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from telegram.constants import ParseMode


nuked = 0
@decorator.general_admin
# @decorator.cancellacomandi
async def init(update, context):
    global original_msg
    original_msg = update.message.message_id
    bot = context.bot
    keyboard = [[InlineKeyboardButton('☢️ AUTORIZZA LANCIO ☢️', callback_data = 'nuke')]]
    try:
        stronzo = update.message.reply_to_message.from_user.id
        set_nuke(stronzo)
        print(stronzo)
        await bot.send_video(update.message.chat_id,
                             reply_to_message_id=update.message.message_id,
                             video='https://media1.giphy.com/media/3ov9k9Ss9N3wO6FQ7C/giphy.gif',
                             caption='[{}]\n<b>MISSILE PRONTO AL LANCIO</b>\n\n'
                                     'Autorizzazione richiesta per confermare il lancio\n'
                                     '<i>Raccomandiamo di indossare occhiali da sole per assistere all\'esplosione</i>'.format(stronzo),
                             reply_markup = InlineKeyboardMarkup(keyboard),
                             parse_mode='HTML')
        #bot.kick_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id, timeout=None, until_date=None)
        #update.message.reply_text("Utente [{}][{}][{}] Bannato con successo".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username))
    except:
        print("an error occurred [NUKE] function")
        await update.message.reply_text("Errore durante la procedura di nuclearizzazione")


original_msg = 0


@decorator.general_admin
async def launch(update, context):
    global original_msg
    query = update.callback_query
    await query.answer()
    if query.data == 'nuke':
        try:
            n = 5
            while n>0:
                await query.edit_message_caption(caption="<b>LANCIO AUTORIZZATO</b>\n\n"
                                                         "Detonazione in <b>{}</b>".format(n), parse_mode=ParseMode.HTML)
                await asyncio.sleep(1)
                n = n-1
            await context.bot.delete_message(update.callback_query.message.chat_id, update.callback_query.message.message_id)
            print("done")
            #https://i.pinimg.com/originals/6c/48/5e/6c485efad8b910e5289fc7968ea1d22f.gif
            await context.bot.send_video(update.callback_query.message.chat_id,
                reply_to_message_id=original_msg,
                video='https://i.pinimg.com/originals/6c/48/5e/6c485efad8b910e5289fc7968ea1d22f.gif',
                caption='<b>NUCLEARIZZAZIONE COMPLETATA</b>\n'
                        '<b>Stato obiettivo</b>: eliminato\n'
                        '<b>Resoconto</b>: il lancio ha avuto successo', parse_mode=ParseMode.HTML)
            global nuked

            await context.bot.ban_chat_member(update.callback_query.message.chat_id, nuked)


        except:
            print('Error')


def set_nuke(stronzo):
    global nuked
    nuked = stronzo
