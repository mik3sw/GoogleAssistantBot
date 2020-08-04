import random
import config
from utils import decorator
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from . import definisci
from . import chat_controls



def okgoogle(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower() == "ok google" or str(update.message.text).lower() == "hey google" or str(
                update.message.text).lower() == "google":
            update.message.reply_text("Ciao {}, come posso aiutarti?️ 💬".format(update.message.from_user.first_name), parse_mode='HTML')


def nexus5x(update, context):
    if update.message.text is not None:
        if 'nexus 5x' in str(update.message.text).lower():
            update.message.reply_text("Do you want some bootloop?".format(username=update.message.from_user.first_name),
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
            google_is_thinking = {1: "A nulla sono un bot non intelligenza artificiale",
                                  2: "Chissà perché mi fai domande inutili",
                                  3: "A cosa posso guardare di nuovo su Netflix...consigli qualcosa?",
                                  4: "Penso al prossimo design per le telecamere dei Google Pixel!",
                                  5: "Niente di che",
                                  6: "Scusa ora sono al telefono chiedimelo dopo"}
            var_numero = random.randint(1, 6)
            update.message.reply_text(google_is_thinking[var_numero],
                             reply_to_message_id=update.message.message_id, parse_mode='HTML')


def cosafai(update, context):
    if update.message.text is not None:
        if 'che fai google' in str(update.message.text).lower() or 'che stai facendo google' in str(update.message.text).lower() or 'cosa stai facendo google' in str(update.message.text).lower():
            google_is_doing = {1: "Stavo leggendo informazioni interessanti su <b>Wikipedia</b>",
                               2: "Stavo guardando video di gattini su Youtube insieme a Bill Gates",
                               3: "Sto finendo una serie su Netflix non disturbarmi!",
                               4: "Stavo cercando di capire come limitare ancora di più la vostra privacy, umani",
                               5: "01101110 01110101 01101100 01101100 01100001 00100000 01100100 01101001 00100000 01100011 01101000 01100101 00101100 00100000 01110110 01101111 01101100 01100101 01110110 01101111 00100000 01110011 01101111 01101100 01101111 00100000 01100110 01100001 01110010 01110100 01101001 00100000 01110000 01100101 01110010 01100100 01100101 01110010 01100101 00100000 01110100 01100101 01101101 01110000 01101111\n\n<b>Prova a tradurlo</b> ;) ",
                               6: "Non è come sembra, posso spiegare!"}
            var_numero = random.randint(1, 6)
            update.message.reply_text(google_is_doing[var_numero],
                             reply_to_message_id=update.message.message_id, parse_mode='HTML')


def curiosita(update, context):
    if update.message.text is not None:
        if str(update.message.text).lower() == 'google curiosità':
            google_curiosita = {1: "il mio schiavo sviuppatore ha 19 anni",
                                2: "Spoiler: parli con un bot perchè non hai amici",
                                3: "Non puoi leccarti il gomito, a meno che non ti stacchi il braccio",
                                4: "Non puoi immaginare un colore che non esiste, ma io si",
                                5: "Il delfino è l'unico animale al mondo, oltre l'uomo, che fa sesso anche per provare piacere",
                                6: "Per viaggiare dalla Corea del Nord alla Norvegia, devi solo attraversare un paese.",
                                7: "I cavalli non possono vomitare.",
                                8: "L'anatra del lago argentino ha un pene lungo quanto tutto il suo corpo.",
                                9: "Il miele è l'unico cibo che non scade mai: lo stesso miele che è stato sepolto con i faraoni in Egitto è ancora commestibile",
                                10: "L'umanità ha trascorso complessivamente 11.300 anni a guardare il video musicale \"Love the Way You Lie\" su YouTube",
                                11: "In un mazzo di carte, il re di cuori è l’unico senza baffi.",
                                12: "Aggiungere sale all’ananas lo rende più dolce."}
            var_numero = random.randint(1, 12)
            update.message.reply_text(google_curiosita[var_numero],
                             reply_to_message_id=update.message.message_id, parse_mode='HTML')


# DICHIARAZIONE FUNZIONI
def init(update, context):
    chat_controls.init(update, context)
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
    
    
