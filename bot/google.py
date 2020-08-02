#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config, commands, dialogs
from telegram import ChatPermissions
from configparser import ConfigParser

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def error(update, context):
    logger.warning('Update "%s" genera errore: "%s"', update, context.error)


def main():
    updater = Updater(config.bot_token, use_context=True)
    dp = updater.dispatcher

    # commands and functions
    # '/start' trigger 'commands.start.init' function
    # ===============================================
    dp.add_handler(CommandHandler("start", commands.start.init))
    dp.add_handler(CommandHandler(["regole", "rules"], commands.regole.init))
    dp.add_handler(CommandHandler("ban", commands.ban.init))
    dp.add_handler(CommandHandler(["help", "aiuto"], commands.help.init))
    dp.add_handler(CommandHandler("source", commands.source.init))
    dp.add_handler(CommandHandler(["io", "me"], commands.me.init))
    dp.add_handler(CommandHandler(["muta", "mute"], commands.mute.init))
    dp.add_handler(CommandHandler(["smuta", "unmute"], commands.unmute.init))
    dp.add_handler(CommandHandler(["fissa", "pin"], commands.pin.init))
    dp.add_handler(CommandHandler("say", commands.say.init))
    dp.add_handler(CommandHandler("annuncio", commands.annuncio.init))
    dp.add_handler(CommandHandler("source", commands.source.init))
    # ===============================================
    
    
    # [1] Message replyes (ok google...)   [2] Welcome MessageHandler 
    # ===============================================
    dp.add_handler(MessageHandler(Filters.text, dialogs.handler.init))             # [1]
    dp.add_handler(MessageHandler(Filters.status_update, dialogs.welcome.init))    # [2]
    # ===============================================

    # Display errors and warnings 
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
