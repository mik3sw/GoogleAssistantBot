# import modules
from telegram.constants import ParseMode
import functions


async def init(update, context):
    txt = functions.general.txtReader('source')
    await update.message.reply_text(text=txt, parse_mode=ParseMode.HTML)
