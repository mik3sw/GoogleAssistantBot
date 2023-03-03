# import modules
from utils import decorator
from configparser import ConfigParser


@decorator.general_admin
#@decorator.cancellacomandi
async def init(update, context):
    """
    This command is executed sending to the bot:
        /slow [options]

    Options:
        * flag: 0 or 1 used to activate/deactivate the slow mode (0 deactivate, 1 activate)
        * msg_num: integer representing the maximum consecutive allowed messages (default is 3)
        * seconds: integer representing the seconds that a user must wait to write again is msg_num is exceeded

    examples:
        /slow 1 5 60   # activate slow mode,  msg_num=5, seconds=60
        /slow 1 5      # equivalent to /slow 1 5 30
        /slow 0        # equivalent to /slow 0 3 30 (here 3 and 30 are meaningless, whatever value is ok for both)
        /slow          # equivalent to /slow 1 3 30
        /slow -ls      # shows settings applied
    """

    

    # decode command
    msg = context.args

    # assign values to activate, msg_num and seconds
    if len(msg) == 0:   # case: /slow
        active = '1'
        msg_num = '3'
        seconds = '30'
    elif len(msg) == 1:   # case: /slow flag
        if msg[0] == '-ls':
            text = read_file('slowmode.ini', update.message.chat_id, update.message.chat.title)
            await update.message.reply_text(text=text, parse_mode = 'HTML')
            await context.bot.delete_message(update.message.chat_id, update.message.message_id)
            return
        else:
            active = msg[0]
            msg_num = '3'
            seconds = '30'
    elif len(msg) == 2:   # case: /slow flag msg_num
        active = msg[0]
        msg_num = msg[1]
        seconds = '30'
    else:   # case: /slow flag msg_num seconds
        active = msg[0]
        msg_num = msg[1]
        seconds = msg[2]

    # read 'slowmode.ini'
    slowmode_cnf = ConfigParser()
    slowmode_cnf.read('slowmode.ini')

    # update 'slowmode.ini'
    if str(update.message.chat_id) in slowmode_cnf:   # the group already has an entry for slowmode
        slowmode_cnf[str(update.message.chat_id)]['active'] = active
        slowmode_cnf[str(update.message.chat_id)]['msg_num'] = msg_num
        slowmode_cnf[str(update.message.chat_id)]['seconds'] = seconds
    else:
        slowmode_cnf[str(update.message.chat_id)] = {'active': active, 'msg_num': msg_num, 'seconds': seconds}

    # save updated config
    with open('slowmode.ini', 'w') as file:
        slowmode_cnf.write(file)

    # delete previous config
    if 'slowmode_cnf' in context.bot_data:
        del context.bot_data['slowmode_cnf']
    
    await context.bot.delete_message(update.message.chat_id, update.message.message_id)


def read_file(file, chat, title):
    s = ConfigParser()
    s.read(file)
    lst=['active','msg_num','seconds']
    message = f'<b>Slow mode settings</b>\n\n{title}\n{chat}\n\n'
    for x in lst:
        txt = s.get(f'{chat}', f'{x}')
        message += f'{x}: {txt}\n'
    return message
