import commands
from telegram.ext import (
    CommandHandler as CMH,
    MessageHandler as MH,
    CallbackQueryHandler as CQH,
    ConversationHandler as CH)

def user_commands(dp):
    function = dp.add_handler
    function(CMH("start", commands.user.start.init))
    function(CMH(["regole", "rules"], commands.user.rules.init))
    function(CMH(["help", "aiuto"], commands.user.help.init))
    function(CMH("source", commands.user.source.init))
    function(CMH(["io", "me"], commands.user.me.init))

def admin_commands(dp):
    function = dp.add_handler
    function(CMH("ban", commands.admin.ban.init))
    function(CMH("unban", commands.admin.unban.init))
    function(CMH("nuke", commands.admin.nuke.init)) # nuke command message
    function(CQH(commands.admin.night.unsilence_button, pattern='unsilence_button'))
    function(CQH(commands.admin.nuke.launch)) # nuke command button
    function(CMH(["muta", "mute"], commands.admin.mute.init))
    function(CMH(["smuta", "unmute"], commands.admin.unmute.init))
    function(CMH(["fissa", "pin"], commands.admin.pin.init))
    function(CMH("say", commands.admin.say.init))
    function(CMH(["saypin","annuncio"], commands.admin.annuncio.init ,pass_args=True))
    function(CMH("check", commands.admin.check.init))
    function(CMH("del", commands.admin.delete.init))
    function(CMH(["notte", "night", "silenzio", "silence"], commands.admin.night.init))
    function(CMH("kick", commands.admin.kick.init))
    
    