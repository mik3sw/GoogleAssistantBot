# import modules
import config
import functions
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from configparser import ConfigParser
from errors.log import log
from telegram.constants import ParseMode


async def init(update, context):
    r1 = ConfigParser()
    r1.read('settings.ini')

    for new in update.message.new_chat_members:
        log("🟢 New user in chat: {}".format(update.message.chat.title))
        # ==========================
        # Quick check on new members
        # [1] chinese characters
        # [2] arabic characters
        # [3] russian characters
        # ==========================
        chinese = await functions.chinese_characters.init(update, context, r1, new)
        arabic = await functions.arabic_characters.init(update, context, r1, new)
        russian = await functions.russian_characters.init(update, context, r1, new)
        spammer = await functions.custom_spam.init(update, context, r1, new)

        if chinese or arabic or russian or spammer:
            print('ban triggered on new user')
        else:
            if str(new.username).lower() == config.bot_username:
                txt = functions.general.txtReader('welcome_bot')
                await context.bot.send_message(update.message.chat_id, text=txt, parse_mode=ParseMode.HTML)
            else:
                try:
                    name = "@" + new.username \
                        if new.username is not None \
                        else new.name
                except:
                    name = "[ERROR]"

                if update.message.chat_id == config.group['pixel']['id']:
                    txt = functions.general.txtReader('welcome')
                    keyboard = [
                        [InlineKeyboardButton("Somme Regole 📜", url='https://telegra.ph/Google-Pixel-Italia-07-29')],
                        [InlineKeyboardButton("macOS Italia", url='https://t.me/macOSItalia')],
                        [InlineKeyboardButton("FOSS Italia", url='https://t.me/fossitaly')]]
                    reply_markup = InlineKeyboardMarkup(keyboard)

                    try:
                        await context.bot.send_message(chat_id=config.group['pixel']['id'],
                                                       text=str(txt).format(name, update.message.chat.title),
                                                       message_thread_id=config.group['pixel']['main_topic'],
                                                       reply_markup=reply_markup, parse_mode=ParseMode.HTML)
                    except:
                        pass

                    if config.send_log_to_channel:
                        msg = "🟢 <b>New user</b> #new\n\nChat: {}\nChat_id: {}\nUser_id: <code>{}</code>\nName: {}\nUsername: @{}".format(
                            update.message.chat.title,
                            update.message.chat_id,
                            new.id,
                            new.first_name,
                            new.username)
                        await context.bot.send_message(chat_id=config.log_channel, text=msg, parse_mode='HTML')
                    else:
                        pass

                elif update.message.chat_id == config.group['macos']['id']:
                    txt = functions.general.txtReader('welcome')
                    keyboard = [
                        [InlineKeyboardButton("Somme Regole 📜", url='https://telegra.ph/Google-Pixel-Italia-07-29')],
                        [InlineKeyboardButton("Google Pixel Italia", url='https://t.me/googlepixelit')],
                        [InlineKeyboardButton("FOSS Italia", url='https://t.me/fossitaly')]]
                    reply_markup = InlineKeyboardMarkup(keyboard)

                    try:
                        await context.bot.send_message(chat_id=config.group['macos']['id'],
                                                       text=str(txt).format(name, update.message.chat.title),
                                                       reply_markup=reply_markup, parse_mode=ParseMode.HTML)
                    except:
                        pass

                    if config.send_log_to_channel:
                        msg = "🟢 <b>New user</b> #new\n\nChat: {}\nChat_id: {}\nUser_id: <code>{}</code>\nName: {}\nUsername: @{}".format(
                            update.message.chat.title,
                            update.message.chat_id,
                            new.id,
                            new.first_name,
                            new.username)
                        await context.bot.send_message(chat_id=config.log_channel, text=msg, parse_mode='HTML')
                    else:
                        pass

                elif update.message.chat_id == config.group['foss']['id']:
                        txt = functions.general.txtReader('welcome')
                        keyboard = [
                            [InlineKeyboardButton("Somme Regole 📜",
                                                  url='https://telegra.ph/Google-Pixel-Italia-07-29')],
                            [InlineKeyboardButton("Google Pixel Italia", url='https://t.me/googlepixelit')],
                            [InlineKeyboardButton("macOS Italia", url='https://t.me/macOSItalia')]]
                        reply_markup = InlineKeyboardMarkup(keyboard)

                        try:
                            await context.bot.send_message(chat_id=config.group['foss']['id'],
                                                           text=str(txt).format(name, update.message.chat.title),
                                                           reply_markup=reply_markup, parse_mode=ParseMode.HTML)
                        except:
                            pass

                        if config.send_log_to_channel:
                            msg = "🟢 <b>New user</b> #new\n\nChat: {}\nChat_id: {}\nUser_id: <code>{}</code>\nName: {}\nUsername: @{}".format(
                                update.message.chat.title,
                                update.message.chat_id,
                                new.id,
                                new.first_name,
                                new.username)
                            await context.bot.send_message(chat_id=config.log_channel, text=msg, parse_mode='HTML')
                        else:
                            pass

                elif update.message.chat_id == config.group['admin']['id']:
                    pass

                else:
                    txt = functions.general.txtReader('welcome_other')
                    keyboard = [
                        [InlineKeyboardButton("Google Pixel Italia", url='https://t.me/googlepixelit')],
                        [InlineKeyboardButton("macOS Italia", url='https://t.me/macOSItalia')],
                        [InlineKeyboardButton("FOSS Italia", url='https://t.me/fossitaly')]]
                    reply_markup = InlineKeyboardMarkup(keyboard)

                    await update.message.reply_text(str(txt).format(name),
                                                    reply_markup=reply_markup, parse_mode='HTML')

