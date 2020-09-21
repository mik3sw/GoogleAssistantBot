from utils import decorator
from telegram import ChatPermissions
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_polls=False, can_send_other_messages=False,
    can_add_web_page_previews=False, can_change_info=False,
    can_invite_users=False, can_pin_messages=False)

@decorator.general_admin
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    keyboard = [[InlineKeyboardButton("Deactivate", callback_data='unsilence_button')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.set_chat_permissions(update.message.chat_id,permission)
    video = 'https://i.pinimg.com/originals/a5/33/11/a5331134ee11f537982c7d816778544b.gif' 
    bot.send_video(update.message.chat_id, video=video, caption="Activating night mode...🌙", reply_markup=reply_markup,parse_mode='HTML')

@decorator.general_admin
def unsilence_button(update,context):
    print("controllo unsilence")
    bot = context.bot
    query = update.callback_query
    query.answer()
    if query.data == 'unsilence_button':
        perm_true = ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=False,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False)
        message = "Night mode disabled ☀️"
        query = update.callback_query
        bot.set_chat_permissions(update.effective_chat.id, perm_true)
        query.edit_message_caption(caption=message, parse_mode='HTML')