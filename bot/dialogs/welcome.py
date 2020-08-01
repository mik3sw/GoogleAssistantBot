import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from configparser import ConfigParser

def init(update, context):
	s = ConfigParser()
	s.read('strings.ini')

	for new in update.message.new_chat_members:
		keyboard = [[InlineKeyboardButton("Mercatino 📦", url='t.me/AOSPItaliashop')],
					[InlineKeyboardButton("Somme Regole 📜", url='https://telegra.ph/Google-Pixel-Italia-07-29')]]
		reply_markup = InlineKeyboardMarkup(keyboard)

		if str(new.username).lower() == config.bot_username:
			context.bot.send_message(update.message.chat_id, text=s.get('welcome_bot', config.language), parse_mode='HTML')

		else:
			update.message.reply_text(str(s.get('welcome', config.language)).format(
								  username="@" + new.username,
			                      chat_title=update.message.chat.title), reply_markup=reply_markup, parse_mode='HTML')
