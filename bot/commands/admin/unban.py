# import modules
from utils import decorator
from config import log_channel
from errors.log import log
import asyncio
from telegram.constants import ParseMode


@decorator.general_admin
async def init(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    reply = update.message.reply_to_message
    try:
        await bot.unban_chat_member(chat, reply.from_user.id)
        await asyncio.sleep(1)
        await update.message.reply_text(text = "🔵 <b>Unban process</b> #unban\n\n "
                                               "User_id: <code>{}</code>\n"
                                               "Name:{}\n"
                                               "Username @{}\n\n"
                                               "<b>Succesfully unbanned</b>".format(update.message.reply_to_message.from_user.id,
                                                                                    update.message.reply_to_message.from_user.first_name,
                                                                                    update.message.reply_to_message.from_user.username),
                                        parse_mode=ParseMode.HTML)
        await context.bot.delete_message(update.message.chat_id, update.message.message_id)
        await context.bot.send_message(chat_id=log_channel, text="<b>Unban process</b>\n\nUser_id: <code>{}</code>\n"
                                                                 "Name: {}\n"
                                                                 "Username: @{}\n\n"
                                                                 "<b>Unbanned by admin</b>: @{}".format(update.message.reply_to_message.from_user.id,
                                                                                                        update.message.reply_to_message.from_user.first_name,
                                                                                                        update.message.reply_to_message.from_user.username,
                                                                                                        update.message.from_user.username),
                                       parse_mode=ParseMode.HTML)
    except:
        log("an error occurred [UNBAN] function")
        await update.message.reply_text("Error during unban operation")
        