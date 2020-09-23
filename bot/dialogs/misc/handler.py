import random
from . import definisci
from . import random_answer
from . import answers



def general(update, context):
    if update.message.text is not None:
        for x in answers.cases:
            if x in str(update.message.text).lower():
                update.message.reply_text(str(answers.cases[x]).format(name = update.message.from_user.first_name))

def cosapensi(update, context):
    if update.message.text is not None:
        if 'cosa pensi google' in str(update.message.text).lower() or 'google cosa pensi' in str(update.message.text).lower():
            google_is_thinking = random_answer.google_is_thinking
            var_numero = random.randint(1, len(google_is_thinking))
            update.message.reply_text(google_is_thinking[var_numero],
                             reply_to_message_id=update.message.message_id, parse_mode='HTML')


def cosafai(update, context):
    if update.message.text is not None:
        if 'che fai google' in str(update.message.text).lower() or 'che stai facendo google' in str(update.message.text).lower() or 'cosa stai facendo google' in str(update.message.text).lower():
            google_is_doing = random_answer.google_is_doing
            var_numero = random.randint(1, len(google_is_doing))
            update.message.reply_text(google_is_doing[var_numero],
                             reply_to_message_id=update.message.message_id, parse_mode='HTML')


def curiosita(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower() == 'google curiosità':
            google_curiosita = random_answer.google_curiosita
            var_numero = random.randint(1, len(google_curiosita))
            update.message.reply_text(google_curiosita[var_numero],
                             reply_to_message_id=update.message.message_id, parse_mode='HTML')

def mercatino(update, context):
    if (update.message.text is not None) and (update.message.chat_id != -1001160935294):
        words = ["vendo", "qualcuno vende"]
        for x in words:
            if x in str(update.message.text).lower():
                context.bot.delete_message(update.message.chat_id, update.message.message_id)
                context.bot.send_message(update.message.chat_id, text='Ciao <a href="tg://user?id={}\">{}</a>!\nHo cancellato il tuo messaggio perchè <b>sembra che tu stia cercando o vendendo qualcosa</b> all\'interno del gruppo.\nPer questo abbiamo un gruppo dedicato!\n\nEccolo qua: t.me/aospitaliashop\n'.format(update.message.from_user.id, update.message.from_user.first_name), parse_mode = 'HTML')



def init(update, context):
    general(update, context)
    cosafai(update, context)
    cosapensi(update, context)
    curiosita(update, context)
    mercatino(update, context)
    definisci.init(update, context)
    