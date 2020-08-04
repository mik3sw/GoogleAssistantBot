import config
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
		# ============================
		# IF NON_LATIN_FILTER IS TRUE
		# ============================
		if r1.get('settings', 'non_latin_filter') == 'True':
			china = re.findall(r'[\u4e00-\u9fff]+', new.first_name)
			if china == []:
				if str(new.username).lower() == config.bot_username:
					context.bot.send_message(update.message.chat_id, text=s.get('welcome_bot', config.language), parse_mode='HTML')
				else:
					net = '<a href="t.me/aospitalianet">Network</a>'
					update.message.reply_text(str(s.get('welcome', config.language)).format(new.username,update.message.chat.title, net), reply_markup=reply_markup, parse_mode='HTML')

			else:
				context.bot.kick_chat_member(update.message.chat.id, new.id, timeout=None, until_date=None)
				update.message.reply_text("Utente [{}][{}][{}] Bannato con successo\nnon_latin_filter triggered".format(new.id, new.first_name, new.username))
		# ============================
		# IF NON_LATIN_FILTER IS FALSE
		# ============================
		else:
			if str(new.username).lower() == config.bot_username:
				context.bot.send_message(update.message.chat_id, text=s.get('welcome_bot', config.language), parse_mode='HTML')
			else:
				net = '<a href="t.me/aospitalianet">Network</a>'
				update.message.reply_text(str(s.get('welcome', config.language)).format(new.username,update.message.chat.title, net), reply_markup=reply_markup, parse_mode='HTML')
		# ============================