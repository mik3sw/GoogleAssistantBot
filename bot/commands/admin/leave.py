from utils import decorator

@decorator.ownerbot
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id, text="Leaving this group", parse_mode='HTML')
    bot.leaveChat(update.message.chat_id)