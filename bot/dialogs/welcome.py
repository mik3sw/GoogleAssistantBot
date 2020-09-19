import config
import functions
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from configparser import ConfigParser

def init(update, context):

	r1 = ConfigParser()
	r1.read('settings.ini')

	keyboard = [[InlineKeyboardButton("Mercatino 📦", url='t.me/AOSPItaliashop')],
					[InlineKeyboardButton("Somme Regole 📜", url='https://telegra.ph/Google-Pixel-Italia-07-29')]]
	reply_markup = InlineKeyboardMarkup(keyboard)

	for new in update.message.new_chat_members:
		# ==========================
		# Quick check on new members
		# [1] chinese characters
		# [2] arabic characters
		# [3] (work in progress)
		# ==========================
		chinese = functions.chinese_characters.init(update, context, r1, new)
		arabic = functions.arabic_characters.init(update, context, r1, new)
		if chinese == True or arabic == True:
			print('ban triggered on new user')
		else:
			if str(new.username).lower() == config.bot_username:
				txt = functions.general.txtReader('welcome_bot')
				context.bot.send_message(update.message.chat_id, text=txt, parse_mode='HTML')
			else:
				txt = functions.general.txtReader('welcome')
				net = '<a href="t.me/aospitalianet">Network</a>'
				try:
					if new.username == None:
						name = new.first_name
					else:
						name = new.username
				except:
					name = "[ERROR]"
				update.message.reply_text(str(txt).format(name,update.message.chat.title, net), reply_markup=reply_markup, parse_mode='HTML')