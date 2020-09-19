import config

def init(update, context):
    if update.message.text is not None:
        for x in config.bad_words:
            if x in str(update.message.text).lower():
                update.message.reply_text("[WARNING] - Bad word detected")
                context.bot.delete_message(update.message.chat_id, update.message.message_id)