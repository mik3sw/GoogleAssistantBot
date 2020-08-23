import random
from . import definisci
from . import chat_controls
from . import random_answer



def okgoogle(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower() == "ok google" or str(update.message.text).lower() == "hey google" or str(
                update.message.text).lower() == "google":
            update.message.reply_text("Ciao {}, come posso aiutarti?️ 💬".format(update.message.from_user.first_name), parse_mode='HTML')


def nexus5x(update, context):
    if update.message.text is not None:
        if 'nexus 5x' in str(update.message.text).lower():
            update.message.reply_text("Do you want some bootloop?",
                             reply_to_message_id=update.message.message_id)


def buonasera(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower().startswith("buonasera"):
            update.message.reply_text(
                             "Buonasera {username} 🌅".format(username=update.message.from_user.first_name),
                             reply_to_message_id=update.message.message_id)


# Buongiorno
def buongiorno(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower().startswith("buongiorno"):
            update.message.reply_text(
                             "Buongiorno {username} ☀️".format(username=update.message.from_user.first_name),
                             reply_to_message_id=update.message.message_id)


# Buonanotte
def buonanotte(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower().startswith("buonanotte"):
            update.message.reply_text(
                             "Buonanotte {username}".format(username=update.message.from_user.first_name),
                             reply_to_message_id=update.message.message_id)


# come stai
def comestai(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower().startswith("come stai google"):
            update.message.reply_text("Sto bene {username}, grazie per avermelo chiesto 💙❤️💛💙💚❤️".format(
                username=update.message.from_user.first_name), reply_to_message_id=update.message.message_id)


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


def init(update, context):
    chat_controls.arabic_characters(update, context)
    chat_controls.chinese_characters(update, context)
    okgoogle(update, context)
    nexus5x(update, context)
    buongiorno(update, context)
    buonanotte(update, context)
    comestai(update, context)
    buonasera(update, context)
    cosafai(update, context)
    cosapensi(update, context)
    curiosita(update, context)
    definisci.init(update, context)
    
    
