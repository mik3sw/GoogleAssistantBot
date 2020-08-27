from utils import decorator
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.chat_id, text="Name: {nomeutente}\nUsername: {username}\nID: {id}\nChat_id: {chat_id}"
        .format(nomeutente=update.message.from_user.first_name, username="@"+update.message.from_user.username, id=update.message.from_user.id, chat_id = update.message.chat_id), 
        parse_mode='HTML')
