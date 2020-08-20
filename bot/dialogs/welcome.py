import config
import utils
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from configparser import ConfigParser
import re

def init(update, context):
	s = ConfigParser()
	s.read('strings.ini')

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
		chinese = utils.chinese_characters.init(update, context, s, r1, new)
		arabic = utils.arabic_characters.init(update, context, s, r1, new)
		if chinese == True or arabic == True:
			print('ban triggered on new user')
		else:
			if str(new.username).lower() == config.bot_username:
				context.bot.send_message(update.message.chat_id, text=s.get('welcome_bot', config.language), parse_mode='HTML')
			else:
				net = '<a href="t.me/aospitalianet">Network</a>'
				update.message.reply_text(str(s.get('welcome', config.language)).format(new.username,update.message.chat.title, net), reply_markup=reply_markup, parse_mode='HTML')