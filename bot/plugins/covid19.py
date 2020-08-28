from covid19_script import Covid
import time
import datetime
import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from utils import decorator

# Covid-19 data from 
# https://github.com/ahmednafies/covid


def message_builder():
    c = Covid()

    country = 'Italia'
    confirmed = c.totale_positivi
    new_cases = c.nuovi_positivi
    deaths = c.deceduti
    new_deaths = c.nuovi_deceduti
    critical = c.terapia_intensiva
    recovered = c.dimessi_guariti

    message = '🦠 <b>[DAILY REPORT | COVID-19]</b> 🦠\n\nCountry: <b>{}</b> 🇮🇹\n\n⛑ Confirmed: <b>{}</b>\n⛑ New Cases: <b>{}</b>\n⚠️ Critical: <b>{}</b>\n\n✅ Recovered: <b>{}</b>\n\n☠️ Deaths: <b>{}</b>\n☠️ New deaths: <b>{}</b>\n'.format(country, confirmed, new_cases, critical, recovered, deaths, new_deaths)
    
    return message


def alarm(context):
    keyboard = [[InlineKeyboardButton('Dati 📊', url = 'https://github.com/pcm-dpc/COVID-19')],[InlineKeyboardButton('Info 🦠', url = 'http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?area=nuovoCoronavirus&id=5351&lingua=italiano&menu=vuoto')]]
    for x in config.covid_19_report:
        context.bot.send_message(chat_id = x, text=message_builder(), reply_markup = InlineKeyboardMarkup(keyboard), parse_mode= 'HTML')

@decorator.ownerbot
def set_timer(update, context):
    #chat_id = update.message.chat_id
    h = int(context.args[0])
    m = int(context.args[1])

    if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
    t = datetime.time(h, m, 00)
    new_job = context.job_queue.run_daily(alarm, t, days=(0, 1, 2, 3, 4, 5, 6), context=None, name=None)
    context.chat_data['job'] = new_job
    update.message.reply_text('Covid-19 report setted [DAILY][{}:{}]'.format(h, m))

def unset(update, context):
    if 'job' not in context.chat_data:
        update.message.reply_text('Nothing to do here')
        return

    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']

    update.message.reply_text('Covid-19 report unsetted')