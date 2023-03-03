#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import modules
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.ext import MessageHandler, filters
import config
import dialogs
import errors
import plugins
from commands import index


def main():
    # initialize bot
    application = ApplicationBuilder().token(config.bot_token).build()

    # Plugins
    # Weather daily report [BETA]
    application.add_handler(CommandHandler("weather", plugins.weather.init))

    # Admin commands
    index.admin_commands(application)

    # User commands
    index.user_commands(application)

    # Message Handlers
    application.add_handler(MessageHandler(filters.PHOTO, dialogs.images.init))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, dialogs.welcome.init))    # Welcome
    application.add_handler(MessageHandler(filters.UpdateType.MESSAGE, dialogs.main.init))   # Dialogs and chat controls

    # Display errors and warnings
    application.add_error_handler(errors.log.init)              # console log
    application.add_error_handler(errors.callback_error.init)   # channel log

    # start the BOT
    application.run_polling()


# run the bot
# -----------
if __name__ == '__main__':
    main()