from utils import decorator
@decorator.general_admin
@decorator.cancellacomandi
def init(update, context):
    pass
    bot = context.bot
    try:
        bot.kick_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id, timeout=None, until_date=None)
        bot.send_message(update.message.chat_id, text="User: [{}][{}][{}]\nSuccesfully banned".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username))
    except:
        print("an error occurred [BAN] function")
        update.message.reply_text("Error during ban operation")
