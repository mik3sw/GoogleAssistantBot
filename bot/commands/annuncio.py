from utils import decorator
@decorator.restricted

def init(update, context):
	pass
	bot = context.bot
	if update.message.text is not None:
		if update.message.text.startswith("/annuncio"):
			mess = update.message.text
			mess = mess.replace("/annuncio ", "")
			bot.send_message(update.message.chat_id, text=mess, parse_mode = 'HTML')
			bot.pin_chat_message(update.message.chat_id, update.message.message_id+1)
			bot.delete_message(update.message.chat_id, update.message.message_id)
		else:
			print("annuncio non valido")