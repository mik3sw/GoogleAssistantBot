# import modules
from utils import decorator


@decorator.general_admin
#@decorator.cancellacomandi
async def init(update, context):
	text = context.args

	mess = ''
	for txt in text:
		mess = mess + ' ' + txt
	
	await update.message.reply_text(text='{}'.format(mess), parse_mode='HTML')
	await context.bot.delete_message(update.message.chat_id, update.message.message_id)
