from utils import decorator
import functions

#@decorator.cancellacomandi
def init(update, context):
    txt = functions.general.txtReader('regole')
    update.message.reply_text(text=txt, parse_mode='HTML')
    context.bot.delete_message(update.message.chat_id, update.message.message_id)