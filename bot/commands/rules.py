from utils import decorator
from configparser import ConfigParser
import config

@decorator.cancellacomandi
def init(update, context):
    s = ConfigParser();
    s.read('strings.ini')
    update.message.reply_text(s.get('regole', config.language), parse_mode='HTML')
    
