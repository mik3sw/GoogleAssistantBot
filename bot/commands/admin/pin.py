from utils import decorator
 

@decorator.general_admin
def init(update, context):
    bot = context.bot
    bot.pin_chat_message(update.message.chat_id, update.message.reply_to_message.message_id)
    bot.delete_message(update.message.chat_id, update.message.message_id)
