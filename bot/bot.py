#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler)
import config, dialogs, errors, plugins, functions
from telegram import MessageEntity
from dialogs import misc, rules
from threading import Thread
from utils import decorator
from commands import index
import os
import sys



def main():
    updater = Updater(config.bot_token, use_context=True)
    dp = updater.dispatcher
    function = dp.add_handler

    # restart function
    # ===============================================
    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    #only the owner of the bot can use restart command
    @decorator.ownerbot
    def restart(update, context):
        update.message.reply_text('<b>[SYSTEM]</b>\n\nThe bot is now restarting...', parse_mode='HTML')
        Thread(target=stop_and_restart).start()
    # ===============================================

    # Owner commands
    function(CommandHandler(["restart", "r"], restart))

    # Plugins
    # Weather daily report [BETA]
    function(CommandHandler("weather", plugins.weather.init,pass_args=True,pass_job_queue=True,pass_chat_data=True))

    # Admin commands
    index.admin_commands(dp)

    #User commands
    index.user_commands(dp)

    # Message Handlers
    function(MessageHandler(Filters.status_update.new_chat_members, dialogs.welcome.init))    # Welcome
    function(MessageHandler(Filters.update.message, dialogs.main.init))                       # Dialogs and chat controls

    # Display errors and warnings
    dp.add_error_handler(errors.log.init)              #console log
    dp.add_error_handler(errors.callback_error.init)   #channel log
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()