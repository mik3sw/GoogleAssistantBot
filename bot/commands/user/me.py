# import modules
from telegram.constants import ParseMode
# from utils import decorator


#@decorator.cancellacomandi
async def init(update, context):
    await update.message.reply_text(text="Name: {nomeutente}\n"
                                         "Username: {username}\n"
                                         "ID: {id}\n"
                                         "Chat_id: {chat_id}".format(nomeutente=update.message.from_user.first_name,
                                                                     username="@"+update.message.from_user.username,
                                                                     id=update.message.from_user.id,
                                                                     chat_id=update.message.chat_id),
                                    parse_mode=ParseMode.HTML)
    await context.bot.delete_message(update.message.chat_id, update.message.message_id)