import config
import functions
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from configparser import ConfigParser

def init(update, context):

	r1 = ConfigParser()
	r1.read('settings.ini')


	for new in update.message.new_chat_members:
		# ==========================
		# Quick check on new members
		# [1] chinese characters
		# [2] arabic characters
		# [3] russian characters
		# ==========================
		chinese = functions.chinese_characters.init(update, context, r1, new)
		arabic = functions.arabic_characters.init(update, context, r1, new)
		russian = functions.russian_characters.init(update, context, r1, new)
		spammer = functions.custom_spam.init(update, context, r1, new)

		if chinese or arabic or russian or spammer:
			print('ban triggered on new user')
		else:
			if str(new.username).lower() == config.bot_username:
				txt = functions.general.txtReader('welcome_bot')
				context.bot.send_message(update.message.chat_id, text=txt, parse_mode='HTML')
			else:
				net = '<a href="t.me/aospitalianet">Network</a>'
				try:
					if new.username == None:
						name = "<a href=\"tg://user?id={}\">{}</a>".format(new.id, new.first_name)
					else:
						name = "@"+new.username
				except:
					name = "[ERROR]"

				if update.message.chat_id == config.mercatino: #mercatino
					txt = functions.general.txtReader('welcome_market')
					keyboard = [[InlineKeyboardButton("📦 Come postare un annuncio 📦", url = 'https://telegra.ph/Come-pubblicare-un-annuncio-linee-guida-10-14')]]
					reply_markup = InlineKeyboardMarkup(keyboard)
					update.message.reply_text(str(txt).format(name,update.message.chat.title), reply_markup=reply_markup, parse_mode='HTML')
				else:
					txt = functions.general.txtReader('welcome')
					keyboard = [[InlineKeyboardButton("Mercatino 📦", url='t.me/AOSPItaliashop')],
								[InlineKeyboardButton("Somme Regole 📜", url='https://telegra.ph/Google-Pixel-Italia-07-29')]]
					reply_markup = InlineKeyboardMarkup(keyboard)
					update.message.reply_text(str(txt).format(name,update.message.chat.title, net), reply_markup=reply_markup, parse_mode='HTML')