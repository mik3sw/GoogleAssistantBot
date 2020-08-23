from utils import decorator
from telegram import ChatPermissions
import datetime

@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    pass
    try:
      bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,
      ChatPermissions(
						can_send_messages=False, 
						can_send_media_messages=False, 
						can_send_polls=False,
						can_send_other_messages=False, 
						can_add_web_page_previews=False,
						can_invite_users=False
					),
					until_date=datetime.datetime.now() + datetime.timedelta(days=1))
      bot.send_message(update.message.chat_id, text="User: [{}][{}][@{}]\nSuccesfully muted".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username))
    except:
      print("an error occurred [MUTE] function")
      update.message.reply_text("Error during unmute operation")
