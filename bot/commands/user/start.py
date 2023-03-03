# import modules
import functions
from telegram.constants import ParseMode


async def init(update, context):
    txt = functions.general.txtReader('start')
    await update.message.reply_text(text=txt, parse_mode=ParseMode.HTML)
