# import modules
from utils import decorator
from telegram.constants import ParseMode


@decorator.ownerbot
#@decorator.cancellacomandi
async def init(update, context):

    try:
        groups = context.args
        print(groups)
        for g in groups:
            try:
                bot = context.bot
                await bot.leaveChat(g)
                print(f"Leaving chat_id: {g} - success")
                await update.message.reply_text(text=f"Leaving chat_id: {g} - success", parse_mode=ParseMode.HTML)
            except:
                print(f"Leaving chat_id: {g} - failed")
                await update.message.reply_text(text=f"Leaving chat_id: {g} - failed", parse_mode=ParseMode.HTML)
        
    except:
        bot = context.bot
        await update.message.reply_text(text="Leaving this group", parse_mode=ParseMode.HTML)
        await bot.leaveChat(update.message.chat_id)
