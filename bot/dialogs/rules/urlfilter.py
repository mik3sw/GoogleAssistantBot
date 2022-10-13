import config
from telegram import MessageEntity


def init(update, context):
    if update.message is None:
        return
    if not(update.message.from_user.id in config.LIST_OF_ADMINS):
        for x in config.url_denylist:
            if x in update.message.text:
                spam = True
                for link in config.url_whitelist:
                    if link in update.message.text.lower():
                        spam = False
            else:
                spam = False

        if spam:
            context.bot.send_message(config.admin_group, text="(DEBUG MESSAGE)\nIl seguente messaggio e' stato bloccato:\n\n{}".format(update.message.text))
                    
            context.bot.delete_message(update.message.chat_id, update.message.message_id)
            context.bot.send_message(update.message.chat_id, text="This link has been blocked by an administrator")
