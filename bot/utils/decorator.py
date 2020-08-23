#DEFINIZIONE COMANDI ADMIN
from functools import wraps
import config

#only people from config.LIST_OF_ADMINS can perform that command
def restricted(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id not in config.LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context)
    return wrapped

#delete command message (ex: /ban)
def cancellacomandi(func):
    @wraps(func)
    def wrapped(update, context):
        bot = context.bot
        if update.message.text is not None:
          if update.message.text.startswith("/"):
            bot.delete_message(update.message.chat_id, update.message.message_id)
        return func(update, context)
    return wrapped

# Owner of the bot
#only people from config.OWNER_LIST can perform that command
def ownerbot(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id not in config.OWNER_LIST:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context)
    return wrapped


# see admins/creator automatically in a group
# only group's admin can perform that command/press that InlineButton
def general_admin(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user
        try:
            stat = context.bot.get_chat_member(update.message.chat_id, update.effective_user['id'])['status']
        except:
            stat = context.bot.get_chat_member(update.callback_query.message.chat_id, update.callback_query.from_user['id'])['status']
        print(stat)
        if stat not in config.TITLES:
            print("Unauthorized access denied for {}.".format(user_id['id']))
            return
        return func(update, context)
    return wrapped
