from utils import decorator

@decorator.general_admin
def init(update, context):
	bot = context.bot
	mess = ''
	try:
		text = context.args
		for txt in text:
			mess = mess + ' ' + txt
	except:
		print('error during [annuncio/saypin]')
	
	bot.send_message(update.message.chat_id, text=mess, parse_mode = 'HTML')
	bot.pin_chat_message(update.message.chat_id, update.message.message_id+1)
	bot.delete_message(update.message.chat_id, update.message.message_id)