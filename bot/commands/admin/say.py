from utils import decorator
@decorator.general_admin
#@decorator.cancellacomandi
def init(update, context):
	text = context.args
	print(text)
	mess = ''
	for txt in text:
		mess = mess + ' ' + txt
	print(mess)
	
	update.message.reply_text(text='{}'.format(mess), parse_mode='HTML')
	context.bot.delete_message(update.message.chat_id, update.message.message_id)