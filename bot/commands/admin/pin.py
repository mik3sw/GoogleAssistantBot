# import modules
from utils import decorator


@decorator.general_admin
#@decorator.cancellacomandi
async def init(update, context):
    bot = context.bot
    await bot.pin_chat_message(update.message.chat_id, update.message.reply_to_message.message_id)
    await bot.delete_message(update.message.chat_id, update.message.message_id)