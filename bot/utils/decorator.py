# DEFINIZIONE COMANDI ADMIN
from functools import wraps
import config
from rich.console import Console

# initialize console
console = Console()


# only people from config.LIST_OF_ADMINS can perform that command
def restricted(func):
    @wraps(func)
    async def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id not in config.LIST_OF_ADMINS:
            console.log("Unauthorized access denied for {}.".format(user_id))
            return
        return await func(update, context)
    return wrapped


# delete command message (ex: /ban)
def cancellacomandi(func):
    @wraps(func)
    async def wrapped(update, context):
        if update.message.text is not None:
            if update.message.text.startswith("/"):
                await context.bot.delete_message(update.message.chat_id, update.message.message_id)
        return await func(update, context)
    return wrapped


# Owner of the bot
# only people from config.OWNER_LIST can perform that command
def ownerbot(func):
    @wraps(func)
    async def wrapped(update, context):
        user_id = update.effective_user.id
        if user_id not in config.OWNER_LIST:
            console.log("Unauthorized access denied for {}.".format(user_id))
            return
        return await func(update, context)
    return wrapped


# see admins/creator automatically in a group
# only group's admin can perform that command/press that InlineButton
def general_admin(func):
    @wraps(func)
    async def wrapped(update, context):
        user_id = update.effective_user
        try:
            stat = await context.bot.get_chat_member(update.message.chat_id, update.effective_user['id'])
            stat = stat['status']
        except:
            stat = await context.bot.get_chat_member(update.callback_query.message.chat_id, update.callback_query.from_user['id'])
            stat = stat['status']

        if stat in config.TITLES:
            console.log("Action performed by: {}".format(stat))
        else:
            console.log("Unauthorized access denied for {}.".format(user_id['id']))
            return
        return await func(update, context)
    return wrapped
