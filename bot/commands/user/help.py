from utils import decorator
from configparser import ConfigParser
import config
import functions

def init(update, context):
    txt = functions.general.txtReader('help')
    update.message.reply_text(txt, parse_mode='HTML')
