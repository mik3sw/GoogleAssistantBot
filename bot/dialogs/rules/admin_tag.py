from config import group


async def init(update, context):
    """
    This rule, allow to notify the admins in their private group
    """

    if update.message.text is not None:
        if "@admin" in update.message.text.lower():
            # message for user
            msg = "Grazie della segnalazione, ho avvisato gli admin del gruppo."
            await update.message.reply_text(text=msg)

            # message for admins
            msg = "Qualcuna/o ha richiesto la vostra attenzione qui:\n\n"
            msg += f"Gruppo: {update.message.chat.title}\n"
            msg += f"link: {update.message.link}"

            notification_message = await context.bot.send_message(chat_id=group['admin']['id'], text=msg)
            await context.bot.pin_chat_message(chat_id=group['admin']['id'],
                                         message_id=notification_message.message_id,
                                         disable_notification=False)
        