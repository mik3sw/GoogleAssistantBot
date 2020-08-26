from utils import decorator
@decorator.general_admin
@decorator.cancellacomandi
def init(update, context):
    context.bot.delete_message(update.message.chat_id, update.message.reply_to_message.message_id)