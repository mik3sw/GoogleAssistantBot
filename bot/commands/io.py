from utils import decorator
@decorator.cancellacomandi
def init(update, context):
    bot = context.bot
    bot.send_message(update.message.from_user.id, text="NOME UTENTE: {nomeutente}\nUSERNAME: {username}\nID: {id}"
        .format(nomeutente=update.message.from_user.first_name, username="@"+update.message.from_user.username, id=update.message.from_user.id), 
        parse_mode='HTML')