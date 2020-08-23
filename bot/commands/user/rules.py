from utils import decorator
from configparser import ConfigParser
import config
import functions

@decorator.cancellacomandi
def init(update, context):
    txt = functions.general.txtReader('regole')
    update.message.reply_text(txt, parse_mode='HTML')
    
