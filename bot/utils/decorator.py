#DEFINIZIONE COMANDI ADMIN
from functools import wraps
import config


def restricted(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id not in config.LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context)
    return wrapped

#DELETE COMMANDS
def cancellacomandi(func):
    @wraps(func)
    def wrapped(update, context):
        bot = context.bot
        if update.message.text is not None:
          if update.message.text.startswith("/"):
            bot.delete_message(update.message.chat_id, update.message.message_id)
        return func(update, context)
    return wrapped

#OWNERBOT
def ownerbot(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id not in config.OWNER_LIST:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context)
    return wrapped

#COLLABORATORI
def collaborators(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user
        if user_id not in config.COLLABORATORS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context)
    return wrapped

#see admins/creator automatically in a group
def general_admin(func):
    @wraps(func)
    def wrapped(update, context):
        user_id = update.effective_user
        stat = context.bot.get_chat_member(update.message.chat_id, update.effective_user['id'])['status']
        print(stat)
        if stat not in config.TITLES:
            print("Unauthorized access denied for {}.".format(user_id['id']))
            return
        return func(update, context)
    return wrapped
