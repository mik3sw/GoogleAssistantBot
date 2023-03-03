# import modules
from utils import decorator
from errors.log import log
from telegram.constants import ParseMode


@decorator.general_admin
async def init(update, context):
	bot = context.bot
	mess = ''
	try:
		text = context.args
		for txt in text:
			mess = mess + ' ' + txt
	except:
		log('error during [annuncio/saypin]')

	if update.message.is_topic_message:
		await bot.send_message(update.message.chat_id, text=mess, parse_mode=ParseMode.HTML, message_thread_id=update.message.message_thread_id)
	else:
		await bot.send_message(update.message.chat_id, text=mess, parse_mode=ParseMode.HTML)

	await bot.pin_chat_message(update.message.chat_id, update.message.message_id+1)
	await bot.delete_message(update.message.chat_id, update.message.message_id)
