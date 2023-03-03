# import modules
import functions
# from utils import decorator


# @decorator.cancellacomandi
async def init(update, context):
    txt = functions.general.txtReader('regole')
    await update.message.reply_text(text=txt, parse_mode='HTML')
    await context.bot.delete_message(update.message.chat_id, update.message.message_id)
