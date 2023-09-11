from utils import decorator
from telegram import ChatPermissions
import datetime
from telegram.constants import ParseMode

@decorator.general_admin
#@decorator.cancellacomandi
async def init(update, context):
    bot = context.bot

    try:
        await bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,
                                     ChatPermissions(can_send_messages=False),
                                     until_date=datetime.datetime.now() + datetime.timedelta(days=1))

        await update.message.reply_text(text="<b>Mute process</b>\n\nUser_id: <code>{}</code>"
                                             "\nName: {}\nUsername: @{}"
                                             "\n\nSuccesfully muted".format(update.message.reply_to_message.from_user.id,
                                                                            update.message.reply_to_message.from_user.first_name,
                                                                            update.message.reply_to_message.from_user.username),
                                        parse_mode=ParseMode.HTML)
        await context.bot.delete_message(update.message.chat_id, update.message.message_id)

    except:
        print("an error occurred [MUTE] function")
        await update.message.reply_text("Error during unmute operation")
