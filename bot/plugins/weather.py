import requests, json
import datetime
import config
from utils import decorator

def timeToEmoji(status):
    emoji = 'test'
    if status == 'Clouds':
        emoji ='☁️'
    elif status == 'Clear':
        emoji ='☀️'
    elif status == 'Rain':
        emoji ='🌧'
    elif status == 'Drizzle':
        emoji ='🌧'
    elif status == 'Mist':
        emoji ='🌫'
    else:
        emoji = ''
    return emoji
   
def message_builder(cities):
    message = ''
    api_key = config.weather_api
    for city_name in cities:
        base_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang={}'.format(city_name, api_key, 'it')
        response = requests.get(base_url)
        x = response.json()

        #print(x)
        temp = round(x['main']['temp']-273.15, 1)
        weather = x['weather']
        status = timeToEmoji(weather[0]['main'])
        description = weather[0]['description']
    
        singular_city = '📍{}: {} {}, {}°C\n'.format(city_name, description, status, temp)
        message = message + singular_city
    return message

def final_message():
    nord = ['Genova', 'Torino', 'Aosta', 'Milano', 'Trento', 'Venezia', 'Bologna', 'Trieste']
    centro = ['Roma', 'Ancona', 'Firenze', 'Perugia']
    sud = ['L\'Aquila', 'Potenza', 'Catanzaro', 'Napoli', 'Campobasso', 'Bari', 'Cagliari', 'Palermo']

    message_nord = message_builder(nord)
    message_centro = message_builder(centro)
    message_sud = message_builder(sud)

    final = 'Buongiorno gruppo! Ecco il meteo di oggi:\n\n<b>NORD</b>\n{}\n\n<b>CENTRO</b>\n{}\n\n<b>SUD</b>\n{}'.format(message_nord, message_centro, message_sud)
    return final

def send_weather(context):
    for x in config.weather_report:
        context.bot.send_message(chat_id = x, text=final_message(), parse_mode= 'HTML')

@decorator.ownerbot
def init(update, context):
    h = int(context.args[0])
    m = int(context.args[1])
    t = datetime.time(h, m, 00)
    new_job = context.job_queue.run_daily(send_weather, t, days=(0, 1, 2, 3, 4, 5, 6), context=None, name=None)
    context.chat_data['job'] = new_job
    update.message.reply_text('Weather report setted [DAILY][{}:{}]'.format(h, m))