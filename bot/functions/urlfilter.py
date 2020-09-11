import config
from telegram import MessageEntity


def checkURL(update, context, url):
    if url in config.url_denylist:
        update.message.reply_text(
            "This link has been blocked by an administrator")
        context.bot.delete_message(
            update.message.chat_id, update.message.message_id)


def init(update, context):
    if update.message is None:
        return

    me = update.message.parse_entities()
    for key, url in me.items():
        if key.type == MessageEntity.URL or key.type == MessageEntity.TEXT_LINK:
            checkURL(update, context, url)
