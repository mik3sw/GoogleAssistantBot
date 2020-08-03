from utils import decorator
from configparser import ConfigParser
import config

@decorator.general_admin
def init(update, context):
    s = ConfigParser();
    s.read('strings.ini')
    p=context.bot.get_chat_member(update.message.chat_id, config.bot_id)
    res_mem = '❌'
    del_mess = '❌'
    pin_mess = '❌'
    if p.can_restrict_members:
        res_mem = '✅'
    if p.can_delete_messages:
        del_mess = '✅'
    if p.can_pin_messages:
        pin_mess = '✅'
    update.message.reply_text(str(s.get('check', config.language)).format(res_mem, del_mess, pin_mess), parse_mode='HTML')
