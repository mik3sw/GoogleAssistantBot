from utils import decorator
import functions

def init(update, context):
    txt = functions.general.txtReader('source')
    update.message.reply_text(text=txt, parse_mode='HTML')