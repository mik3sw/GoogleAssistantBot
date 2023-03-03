# import modules
import commands
from telegram.ext import (
    CommandHandler as CMH,
    CallbackQueryHandler as CQH)


def user_commands(application):
    application.add_handler(CMH("start", commands.user.start.init))
    application.add_handler(CMH(["regole", "rules"], commands.user.rules.init))
    application.add_handler(CMH(["help", "aiuto"], commands.user.help.init))
    application.add_handler(CMH("source", commands.user.source.init))
    application.add_handler(CMH(["io", "me"], commands.user.me.init))


def admin_commands(application):
    application.add_handler(CMH("ban", commands.admin.ban.init))
    application.add_handler(CMH("unban", commands.admin.unban.init))
    application.add_handler(CMH("nuke", commands.admin.nuke.init))  # nuke command message
    application.add_handler(CQH(commands.admin.night.unsilence_button, pattern='unsilence_button'))
    application.add_handler(CQH(commands.admin.nuke.launch))  # nuke command button
    application.add_handler(CMH(["muta", "mute"], commands.admin.mute.init))
    application.add_handler(CMH(["smuta", "unmute"], commands.admin.unmute.init))
    application.add_handler(CMH(["fissa", "pin"], commands.admin.pin.init))
    application.add_handler(CMH("say", commands.admin.say.init))
    application.add_handler(CMH(["saypin", "annuncio"], commands.admin.annuncio.init))
    application.add_handler(CMH("check", commands.admin.check.init))
    application.add_handler(CMH("del", commands.admin.delete.init))
    application.add_handler(CMH(["notte", "night", "silenzio", "silence"], commands.admin.night.init))
    application.add_handler(CMH("kick", commands.admin.kick.init))
    application.add_handler(CMH("slow", commands.admin.slow.init))
    application.add_handler(CMH("autoban", commands.admin.autoban.init))
    application.add_handler(CMH("autokick", commands.admin.autokick.init))
    application.add_handler(CMH("leave", commands.admin.leave.init))
    application.add_handler(CMH("get", commands.admin.get.init))
