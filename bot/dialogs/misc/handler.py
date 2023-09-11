import random
from . import definisci
from . import random_answer
from . import answers
from configparser import ConfigParser
from telegram import ChatPermissions
from telegram.constants import ParseMode
import config


async def general(update, context):
    if update.message.text is not None:
        for x in answers.cases:
            if x in str(update.message.text).lower():
                await update.message.reply_text(str(answers.cases[x]).format(name = update.message.from_user.first_name))


async def cosapensi(update, context):
    if update.message.text is not None:
        if 'cosa pensi google' in str(update.message.text).lower() or 'google cosa pensi' in str(update.message.text).lower():
            google_is_thinking = random_answer.google_is_thinking
            var_numero = random.randint(1, len(google_is_thinking))
            await update.message.reply_text(google_is_thinking[var_numero],
                             reply_to_message_id=update.message.message_id, parse_mode=ParseMode.HTML)


async def cosafai(update, context):
    if update.message.text is not None:
        if 'che fai google' in str(update.message.text).lower() or 'che stai facendo google' in str(update.message.text).lower() or 'cosa stai facendo google' in str(update.message.text).lower():
            google_is_doing = random_answer.google_is_doing
            var_numero = random.randint(1, len(google_is_doing))
            await update.message.reply_text(google_is_doing[var_numero],
                             reply_to_message_id=update.message.message_id, parse_mode=ParseMode.HTML)


async def curiosita(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower() == 'google curiosità':
            google_curiosita = random_answer.google_curiosita
            var_numero = random.randint(1, len(google_curiosita))
            await update.message.reply_text(google_curiosita[var_numero],
                             reply_to_message_id=update.message.message_id, parse_mode=ParseMode.HTML)


async def mercatino(update, context):
    if update.message.text is not None:
        words = ["-vendo-", "-vende-", "-vendi-", "-vendere-"]
        for w in words:
            text_message = "-" + str(update.message.text).lower().replace("\n", " ").replace(" ", "-").replace("?", "") + "-"
            if w in text_message:
                await update.message.reply_text(text='Ciao <a href="tg://user?id={}\">{}</a>!\n'
                                                     '<b>Sembra che tu stia cercando o vendendo qualcosa</b> all\'interno del gruppo.\n'
                                                     'Per questo abbiamo un topic dedicato '
                                                     "all'interno del gruppo @googlepixelit .\n\n"
                                                     'Per postare un annucio abbiamo un bot dedicato: @aospitaliashopbot\n\n'
                                                     'N.B. e comunque eventuali trattative vanno gestite in privato!'.format(update.message.from_user.id, update.message.from_user.first_name),
                                                reply_to_message_id=update.message.message_id, parse_mode=ParseMode.HTML,
                                                disable_web_page_preview=True)


async def slowmode_check(update, context):
    # check if config is already in bot_data
    if 'slowmode_cnf' in context.bot_data:
        slowmode_cnf = context.bot_data['slowmode_cnf']
    else:  # otherwise read config from file
        slowmode_cnf = ConfigParser()
        slowmode_cnf.read('slowmode.ini')

    # check if this chat has available config, otherwise set defaults (to inactive)
    if str(update.message.chat_id) not in slowmode_cnf:
        slowmode_cnf[str(update.message.chat_id)] = {'active': '0', 'msg_num': '3', 'seconds': '30'}

    # update slowmode.ini
    with open('slowmode.ini', 'w') as file:
        slowmode_cnf.write(file)

    # update bot_data
    context.bot_data['slowmode_cnf'] = slowmode_cnf

    # get list of admin
    if 'admins' not in context.chat_data:
        all_admins = await context.bot.get_chat_administrators(update.effective_chat.id)
        admins = [ele.user.id for ele in all_admins if (ele.user.is_bot is False)]
        context.chat_data['admins'] = admins

    # read slowmode parameters
    active = bool(int(slowmode_cnf[str(update.message.chat_id)]['active']))
    msg_num = int(slowmode_cnf[str(update.message.chat_id)]['msg_num'])
    seconds = int(slowmode_cnf[str(update.message.chat_id)]['seconds'])

    # check if slow mode is active
    if active and (update.message.from_user.id not in context.chat_data['admins']):
        # check if the user has already an active counter for consecutive messages
        if 'slow_counter' in context.user_data:
            # check continuity
            delta = update.message.message_id - context.user_data['last_msg_id']
            if delta == 1:  # if new message is consecutive
                if context.user_data['slow_counter'] == msg_num:   # if new message exceeds msg_num
                    # notify the user
                    if update.message.from_user.username is None:
                        msg = f"{update.message.from_user.name} hai superato il limite di "
                    else:
                        msg = f"@{update.message.from_user.username} hai superato il limite di "
                    msg += f"{msg_num} messaggi consecutivi\n"
                    msg += f"non potrai scrivere per {seconds} secondi\n"
                    sent_message = await context.bot.send_message(chat_id=update.message.chat_id, text=msg,
                                                                  message_thread_id=update.message.message_thread_id)

                    # mute the user
                    await context.bot.restrictChatMember(chat_id=update.message.chat_id,
                                                   user_id=update.message.from_user.id,
                                                   permissions=ChatPermissions(can_send_messages=False))

                    # unmute function (delayed by 'seconds')
                    async def delayed_unmute(context, update=update, sent_message=sent_message.message_id):
                        # standard permissions
                        std_permission = ChatPermissions(can_send_messages=True,
                                                       can_send_other_messages=True,
                                                       can_add_web_page_previews=True)

                        # unmute user
                        await context.bot.restrictChatMember(chat_id=update.message.chat_id,
                                                       user_id=update.message.from_user.id,
                                                      permissions=std_permission)
                        # clean chat
                        await context.bot.delete_message(chat_id=update.message.chat_id,
                                                   message_id=sent_message)
                    # schedule unmute task
                    context.job_queue.run_once(delayed_unmute, int(slowmode_cnf[str(update.message.chat_id)]['seconds']))

                    # clean counters for this user
                    del context.user_data['slow_counter']
                    del context.user_data['last_msg_id']

                else:  # increase counter and update last_msg_id
                    context.user_data['slow_counter'] += 1
                    context.user_data['last_msg_id'] = update.message.message_id

            else:  # message is not consecutive, reset counters
                context.user_data['slow_counter'] = 1
                context.user_data['last_msg_id'] = update.message.message_id

        else:  # first message by the user, initialize counters
            context.user_data['slow_counter'] = 1
            context.user_data['last_msg_id'] = update.message.message_id


async def init(update, context):
    await general(update, context)
    await cosafai(update, context)
    await cosapensi(update, context)
    await curiosita(update, context)
    await mercatino(update, context)
    await slowmode_check(update, context)
    await definisci.init(update, context)

    