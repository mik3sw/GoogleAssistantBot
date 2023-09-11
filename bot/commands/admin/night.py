# import modules
from utils import decorator
from telegram import ChatPermissions
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode

permission = ChatPermissions(
    can_send_messages=False)
    # can_send_polls=False,
    # can_send_other_messages=False,
    # can_add_web_page_previews=False,
    # can_change_info=False,
    # can_invite_users=False,
    # can_pin_messages=False,
    # can_send_audios=False,
    # can_send_documents=False,
    # can_send_photos=False,
    # can_send_videos=False,
    # can_send_video_notes=False,
    # can_send_voice_notes=False,
    # can_manage_topics=False)
    # can_send_media_messages=False,


@decorator.general_admin
#@decorator.cancellacomandi
async def init(update, context):
    bot = context.bot
    keyboard = [[InlineKeyboardButton("Deactivate", callback_data='unsilence_button')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await bot.set_chat_permissions(update.message.chat_id,permission)
    # video = 'https://i.pinimg.com/originals/a5/33/11/a5331134ee11f537982c7d816778544b.gif'
    # bot.send_video(update.message.chat_id, video=video, caption="Activating night mode...🌙\nSarete tutti mutati fino alla disattivazione (non potrete inviare messaggi, immagini, stickers, ecc...)", reply_markup=reply_markup,parse_mode='HTML')
    await update.message.reply_text(text="Activating night mode...🌙\n"
                                         "Sarete tutti mutati fino alla disattivazione "
                                         "(non potrete inviare messaggi, immagini, stickers, ecc...)",
                                    reply_markup=reply_markup,parse_mode=ParseMode.HTML)
    await context.bot.delete_message(update.message.chat_id, update.message.message_id)


@decorator.general_admin
async def unsilence_button(update,context):
    bot = context.bot
    query = update.callback_query
    await query.answer()
    if query.data == 'unsilence_button':
        perm_true = ChatPermissions(
            can_send_messages=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_send_videos=False,
            can_send_audios=False)
        
        message = "Night mode disabled ☀️"
        query = update.callback_query
        await bot.set_chat_permissions(update.effective_chat.id, perm_true)
        # query.edit_message_caption(caption=message, parse_mode='HTML')
        await query.edit_message_text(text=message, parse_mode=ParseMode.HTML)
