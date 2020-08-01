from utils import decorator
from configparser import ConfigParser
import config

@decorator.cancellacomandi
def init(update, context):
    s = ConfigParser();
    s.read('strings.ini')
    bot = context.bot
    bot.send_message(update.message.chat_id, text=s.get('source', config.language),
                                             parse_mode='HTML')
