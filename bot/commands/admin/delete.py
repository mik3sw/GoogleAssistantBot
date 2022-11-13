from utils import decorator
from errors.log import log

@decorator.general_admin
@decorator.cancellacomandi
def init(update, context):
    try:
        context.bot.delete_message(update.message.chat_id, update.message.reply_to_message.message_id)
    except:
        log("Error during [DELETE] command")