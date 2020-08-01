from utils import decorator
@decorator.restricted
@decorator.cancellacomandi
def init(update, context):
	bot = context.bot
	pass
	if update.message.text is not None:
		if update.message.text.startswith("/say"):
			var_messaggio = update.message.text
			var_messaggio = var_messaggio.replace("/say", "")
			bot.send_message(update.message.chat_id, text='{}'.format(var_messaggio), parse_mode='HTML')