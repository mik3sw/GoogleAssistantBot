from utils import decorator
from config import admin_group
@decorator.general_admin
#@decorator.cancellacomandi
def init(update, context):
    pass
    bot = context.bot
    try:
        bot.ban_chat_member(update.message.chat.id, update.message.reply_to_message.from_user.id, timeout=None, until_date=None)
        update.message.reply_text(text="<b>Ban process</b>\n\nUser_id: <code>{}</code>\nName: {}\nUsername: @{}\n\nSuccesfully banned".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username), parse_mode='HTML')
        context.bot.delete_message(update.message.chat_id, update.message.message_id)

        # resoconto gruppo admin
        text = context.args
        mess = ''
        for txt in text:
            mess = mess + ' ' + txt
        context.bot.send_message(chat_id=admin_group, text="<b>Ban process</b>\n\nUser_id: <code>{}</code>\nName: {}\nUsername: @{}\n\n<b>Performed by admin</b>: @{}\n\n<b>Ban reason</b>: {}".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username, update.message.from_user.username, mess), parse_mode='HTML')
    except:
        print("an error occurred [BAN] function")
        update.message.reply_text("Error during ban operation")
