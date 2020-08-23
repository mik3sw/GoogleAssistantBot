def init(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    reply = update.message.reply_to_message
    try:
        bot.unban_chat_member(chat, reply.from_user.id)
        update.message.reply_text("User: [{}][{}][{}]\nSuccesfully unbanned".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username))
    except:
        print("an error occurred [UNBAN] function")
        update.message.reply_text("Error during unban operation")
    