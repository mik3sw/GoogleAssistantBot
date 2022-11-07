import functions
from utils import decorator


def init(update, context):
    txt = functions.general.txtReader('start')
    update.message.reply_text(text=txt, parse_mode='HTML')
