from configparser import ConfigParser
import config

def init(update, context):
    s = ConfigParser();
    s.read('strings.ini')
    update.message.reply_text(s.get('start', config.language), parse_mode='HTML')