from utils import decorator
from telegram import ChatPermissions


#FUNZIONE SMUTA
@decorator.general_admin
#@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    pass
    try:
      bot.restrict_chat_member(update.message.chat_id,update.message.reply_to_message.from_user.id,
      ChatPermissions(
						can_send_messages=True, 
						can_send_media_messages=True, 
						can_send_polls=True,
						can_send_other_messages=True, 
						can_add_web_page_previews=True,
						can_invite_users=True
					)
      )
      bot.send_message(update.message.chat_id, text="User: [{}][{}][@{}]\nSuccesfully unmuted".format(update.message.reply_to_message.from_user.id, update.message.reply_to_message.from_user.first_name, update.message.reply_to_message.from_user.username))

    except:
      print("an error occurred [UNMUTE] function")
      update.message.reply_text("Error during unmute operation")
