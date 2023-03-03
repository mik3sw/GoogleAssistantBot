# import modules
from configparser import ConfigParser
import config
import time
from telegram.constants import ParseMode


# Build a button menu (inline and keyboard)
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


# Read message text from 'strings.ini'
def txtReader(setting):
    s = ConfigParser()
    s.read('strings.ini')
    return s.get(setting, config.language)


async def ban_user(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    user = update.message.from_user.id
    kick = await bot.ban_chat_member(chat, user)
    return kick


async def kick_user(update,context):
    bot = context.bot
    chat = update.effective_chat.id
    kick_temp = await bot.ban_chat_member(chat, update.message.from_user.id, until_date=int(time.time()+30))
    return kick_temp


async def delete_message(update, context):
    bot = context.bot
    chat = update.effective_chat.id
    id_message = update.message.message_id
    delete = await bot.delete_message(chat,id_message)
    return delete


async def message(update,context,text = ""):
    bot = context.bot
    chat = update.effective_chat.id
    msg = await bot.send_message(chat,text,parse_mode=ParseMode.HTML)
    return msg


async def reply_message(update,context,text = ""):
    msg = await update.message.reply_text(text,parse_mode=ParseMode.HTML)
    return msg


##############################
## Object entity definition ##
##############################
def bot_object(update,context):
    bot = context.bot
    return bot


def chat_object(update):
    chat = update.effective_chat
    return chat


def user_object(update):
    user = update.effective_message.from_user
    return user


def user_reply_object(update):
    user = update.message.reply_to_message.from_user
    return user


def new_user_object(update):
    for member in update.message.new_chat_members:
        new_user = member
        return new_user
