from utils import decorator
import config
import functions

@decorator.general_admin
def init(update, context):
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
    txt = functions.general.txtReader('check')
    update.message.reply_text( text = str(txt).format(res_mem, del_mess, pin_mess), parse_mode='HTML')
    context.bot.delete_message(update.message.chat_id, update.message.message_id)