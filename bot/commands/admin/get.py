from utils import decorator
from errors.log import log


@decorator.general_admin
#@decorator.cancellacomandi
def init(update, context):
    try:
        bot = context.bot
        msg = update.message.reply_to_message
        text = f"""<b>Resoconto messaggio</b>
<b>Chat [ID]</b>: <code>{update.message.chat_id}</code>
<b>Chat [Title]</b>: <code>{update.message.chat.title}</code>

<b>User [ID]</b>: <code>{msg.from_user.id}</code>
<b>User [Nome]</b>: <code>{msg.from_user.first_name}</code>
<b>User [Username]</b>: @{msg.from_user.username}
        
<b>Message [ID]</b>: <code>{msg.message_id}</code>
<b>Message [text]</b>: <code>{msg.text}</code>"""
        update.message.reply_text(text, parse_mode='HTML')
        
    except:
        bot.delete_message(update.message.chat_id, update.message.message_id)
        log("Error during [GET] command")