import config
# from telegram import MessageEntity


async def init(update, context):
    if update.message is None:
        return
    if not(update.message.from_user.id in config.LIST_OF_ADMINS):
        for x in config.url_denylist:
            if update.message.text is not None:
                if x in update.message.text:
                    spam = True
                    for link in config.url_whitelist:
                        if link in update.message.text.lower():
                            spam = False
                else:
                    spam = False
            else:
                spam = False

        if spam:
            try:
                username = "@" + update.message.from_user.username
            except TypeError:
                username = update.message.from_user.name
            await context.bot.send_message(update.message.chat_id,
                                           text=f"{username}\nLink bloccato, per prevenire lo spam eliminiamo i link t.me, "
                                                f"usa la funzione di telegram per creare hyperlink.",
                                           message_thread_id=update.message.message_thread_id)

            await context.bot.send_message(config.admin_group, text="(DEBUG MESSAGE)\nIl seguente messaggio e' stato bloccato:\n\n{}".format(update.message.text))
            await context.bot.delete_message(update.message.chat_id, update.message.message_id)
