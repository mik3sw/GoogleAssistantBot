# import modules
from utils import decorator
from telegram import ChatPermissions
from telegram.constants import ParseMode


@decorator.general_admin
#@decorator.cancellacomandi
async def init(update, context):
    bot = context.bot
    pass
    try:
        await bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,
                                       ChatPermissions(can_send_messages=True,
                                                       can_send_other_messages=True,
                                                       can_add_web_page_previews=True))
        
        await update.message.reply_text(text="<b>Unmute process</b>\n\n"
                                             "User_id: <code>{}</code>\n"
                                             "Name: {}\n"
                                             "Username: @{}\n\n"
                                             "Succesfully unmuted".format(update.message.reply_to_message.from_user.id,
                                                                          update.message.reply_to_message.from_user.first_name,
                                                                          update.message.reply_to_message.from_user.username),
                                        parse_mode=ParseMode.HTML)
        await context.bot.delete_message(update.message.chat_id, update.message.message_id)

    except:
        print("an error occurred [UNMUTE] function")
        await update.message.reply_text("Error during unmute operation")
