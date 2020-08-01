import wikipedia as wiki
from datetime import datetime
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup)



def init(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower().startswith("google definisci") or str(update.message.text).lower().startswith("google cerca"):
            bot = context.bot
            if str(update.message.text).lower().startswith("google definisci"):
                arg = update.message.text[17:]
            else:
                arg = update.message.text[13:]

            wiki.set_lang('it')
            try:
                pg = wiki.page(wiki.search(arg)[0])
                title = pg.title
                pg_url = pg.url
                definizione = pg.summary
                button_list = [[InlineKeyboardButton("Guarda su Wikipedia", url=pg_url)]]

                text = "<b>{}:</b>\n\n{}".format(title, definizione)

                update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(button_list), parse_mode='HTML')
            except:
                bot.send_message(update.message.chat_id, text="Mi spiace {user} non ho trovato quello che cercavi"
                                 .format(user=update.message.from_user.first_name))
