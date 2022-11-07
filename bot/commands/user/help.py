import functions

def init(update, context):
    txt = functions.general.txtReader('help')
    update.message.reply_text(text=txt, parse_mode='HTML')
    context.bot.delete_message(update.message.chat_id, update.message.message_id)