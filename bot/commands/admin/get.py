from utils import decorator

@decorator.general_admin
#@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    msg = update.message.reply_to_message
    text = f"""<b>Resoconto messaggio</b>

<b>Utente [ID]</b>: <code>{msg.from_user.id}</code>
<b>Utente [Nome]</b>: <code>{msg.from_user.first_name}</code>
<b>Utente [Username]</b>: @{msg.from_user.username}
    
<b>Messaggio [ID]</b>: <code>{msg.message_id}</code>
<b>Messaggio [text]</b>: <code>{msg.text}</code>"""
    update.message.reply_text(text, parse_mode='HTML')
    bot.delete_message(update.message.chat_id, update.message.message_id)