from utils import decorator
import functions

@decorator.cancellacomandi
def init(update, context):
    txt = functions.general.txtReader('regole')
    context.bot.send_message(update.message.chat_id, text=txt, parse_mode='HTML')