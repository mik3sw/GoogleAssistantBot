# import modules
from telegram.error import (TelegramError, Forbidden, BadRequest, TimedOut, ChatMigrated, NetworkError)
import config
import logging
from rich.logging import RichHandler
from telegram.constants import ParseMode

# level=logging.INFO
# FORMAT = "%(message)s"
FORMAT='%(asctime)s - %(name)s - %(message)s'
logging.basicConfig(
    format=FORMAT, 
    level=logging.INFO,
    datefmt="[%X]", 
    handlers=[RichHandler()]
)
# logger = logging.getLogger(__name__)
logger = logging.getLogger("rich")


async def init(update, context):
    txt = update.message.text
    err = '[error]'
    try:
        raise context.error
    except Forbidden:
        err = '<i>[ERROR] Forbidden</i>\n'
        # error_message(update, context, err)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        err = '<i>[ERROR] BadRequest - malformed requests</i>\n'
        # error_message(update, context, err)
        # handle malformed requests - read more below!
    except TimedOut:
        err = '<i>[ERROR] TimedOut - slow connection problems</i>\n'
        # error_message(update, context, err)
        # handle slow connection problems
    except NetworkError:
        err = '<i>[ERROR] NetworkError - other connection problems</i>\n'
        # error_message(update, context, err)
        # handle other connection problems
    except ChatMigrated:
        err = '<i>[ERROR] ChatMigrated - chat_id not found (maybe group/channel migrated?)</i>\n'
        # error_message(update, context, err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        err = '<i>[ERROR] TelegramError\nThis is a generic error not handled by other handlers, check the console logs for info</i>\n'
        # error_message(update, context, err)
        # handle all other telegram related errors
    except AttributeError:
        err = '<i>[ERROR] AttributeError -  bad code</i>'
    except TypeError:
        # err = '[ERROR] TypeError - Unknown'
        # need to fix this... 
        # err = "TypeError"
        err = None
    
    if err != None:
        nomeutente=update.message.from_user.first_name
        username="@"+update.message.from_user.username
        id=update.message.from_user.id
        chat_id = update.message.chat_id
        chat_name = update.message.chat.title
        await error_message(update, context, err, txt, nomeutente, username, id, chat_id, chat_name)
        

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def error_message(update, context, err, txt, name, username, id, chatid, chat_name):
    log = '\n<i>[LOG] errore: {}</i>'.format(context.error)
    await context.bot.send_message(chat_id=config.log_channel, text = "🟡 <b>Resoconto errore</b>\n"
                                                                      "<b>Chat</b>: [{}][{}]\n"
                                                                      "<b>Utente</b>: [{}][{}][{}]\n"
                                                                      "<b>Comando/messaggio</b>:{}\n\n"
                                                                      "<b>Errori rilevati</b>:\n{}{}".format(chat_name,
                                                                                                             chatid,
                                                                                                             id,
                                                                                                             name,
                                                                                                             username,
                                                                                                             txt,
                                                                                                             err,
                                                                                                             log),
                                   parse_mode=ParseMode.HTML)
