import config

async def init(update, context):
    if update.message.text is not None:
        for x in config.bad_words:
            if x in str(update.message.text).lower():
                await update.message.reply_text("[WARNING] - Bad word detected")
                await context.bot.delete_message(update.message.chat_id, update.message.message_id)
