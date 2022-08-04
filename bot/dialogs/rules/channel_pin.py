def init(update, context):
    """
    'channel-pin' pin a message coming from selected channels and notify all members
    """
    if update.message.sender_chat.type == 'channel':
        # unpin message
        context.bot.unpin_chat_message(chat_id=update.message.chat_id,
                                       message_id=update.message.message_id)
        # pin message + notify all members
        context.bot.pin_chat_message(chat_id=update.message.chat_id, message_id=update.message.message_id,
                                     disable_notification=False)

