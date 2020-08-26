#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import config, dialogs, commands, errors
import os
import sys
from threading import Thread
from utils import decorator


def main():
    updater = Updater(config.bot_token, use_context=True)
    dp = updater.dispatcher

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


    # Commands and Functions
    # '/start' trigger 'commands.user.start.init' function
    # ===============================================
    
    # Owner commands
    # ===============================================
    dp.add_handler(CommandHandler(["restart", "r"], restart))

    # Admin commands
    # ===============================================
    dp.add_handler(CommandHandler("ban", commands.admin.ban.init))
    dp.add_handler(CommandHandler("unban", commands.admin.unban.init))
    dp.add_handler(CommandHandler("nuke", commands.admin.nuke.init)) # nuke command message
    dp.add_handler(CallbackQueryHandler(commands.admin.nuke.launch)) # nuke command button
    dp.add_handler(CommandHandler(["muta", "mute"], commands.admin.mute.init))
    dp.add_handler(CommandHandler(["smuta", "unmute"], commands.admin.unmute.init))
    dp.add_handler(CommandHandler(["fissa", "pin"], commands.admin.pin.init))
    dp.add_handler(CommandHandler("say", commands.admin.say.init))
    dp.add_handler(CommandHandler("annuncio", commands.admin.annuncio.init))
    dp.add_handler(CommandHandler("check", commands.admin.check.init))
    dp.add_handler(CommandHandler("del", commands.admin.delete.init))

    #User commands
    # ===============================================
    dp.add_handler(CommandHandler("start", commands.user.start.init))
    dp.add_handler(CommandHandler(["regole", "rules"], commands.user.rules.init))
    dp.add_handler(CommandHandler(["help", "aiuto"], commands.user.help.init))
    dp.add_handler(CommandHandler("source", commands.user.source.init))
    dp.add_handler(CommandHandler(["io", "me"], commands.user.me.init))

    
    # [1] Message replyes (ok google...)   [2] Welcome MessageHandler 
    # ===============================================
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, dialogs.welcome.init))    # [2]
    dp.add_handler(MessageHandler(Filters.update.message, dialogs.handler.init))                    # [1]
    # ===============================================

    # Display errors and warnings 
    dp.add_error_handler(errors.log.init)
    dp.add_error_handler(errors.callback_error.init)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
