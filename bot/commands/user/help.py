# import modules
import functions
from telegram.constants import ParseMode


async def init(update, context):
    txt = functions.general.txtReader('help')
    await update.message.reply_text(text=txt, parse_mode=ParseMode.HTML)
    await context.bot.delete_message(update.message.chat_id, update.message.message_id)
