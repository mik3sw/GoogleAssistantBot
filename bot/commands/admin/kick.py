from utils import decorator
from config import log_channel
from errors.log import log

@decorator.general_admin
#@decorator.cancellacomandi
def init(update, context):
    pass
    bot = context.bot
    try:
        bot.ban_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id, timeout=None, until_date=None)
        bot.unban_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id)
        update.message.reply_text(text="<b>Kick process</b>\n\nUser_id: <code>{}</code>\nName: {}\nUsername: @{}\n\nSuccesfully kicked".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username), parse_mode='HTML')
        context.bot.delete_message(update.message.chat_id, update.message.message_id)

        # resoconto gruppo admin
        text = context.args
        mess = ''
        for txt in text:
            mess = mess + ' ' + txt
        if mess == '':
            mess = 'not provided'
        
        context.bot.send_message(chat_id=log_channel , text="🔴 <b>Kick process</b> #kick\n\nChat: {}\nChat_id: {}\nUser_id: <code>{}</code>\nName: {}\nUsername: @{}\n\n<b>Performed by admin</b>: @{}\n\n<b>Kick reason</b>: {}".format(update.message.chat.title, update.message.chat_id, update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username, update.message.from_user.username, mess), parse_mode='HTML')
    except:
        log("An error occurred [KICK] function")
        update.message.reply_text("Error during kick operation")