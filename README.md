# Google Assistant Bot

**[it]** - 
Bot Gestionale e di benvenuto interamente in lingua italiana ed OPEN SOURCE
Il Bot è stato realizzato per inserirlo nei gruppi facenti parte del network di [@AOSPitaliaNET](t.me\aospitaliaNET)
Per personalizzarlo e renderlo operativo basterà modificare il file "config.py"

**[en]** - 
This bot can manage your group, but only italian language is supported (for now)!
This is only an imitation, it isn't the real Google Assistant and it has no AI.
If you want to use this bot, just edit the "config.py" file

## Dependencies
```
- python-telegram-bot
- wikipedia
- configparser
```

## Configuration
Edit file 'config.py' to run your personal bot

```
bot_token = "Bot token here"       # bot token
bot_username = "@username"         # telegram bot username
language = "it"                    # bot language, check 'strings.ini' file
LIST_OF_ADMINS = [0000, 1111]      # admins' telegram id (to perform admin commands)
```

## What can i do?
I am online! --> http://t.me/PythonAndroidBot

### BOT QUESTIONS

- ok google/hey google
- nexus 5x
- buongiorno
- buonanotte
- google cosa pensi
- google che fai
- google curiosità


### BOT FUNCTION

- Welcome message
- Google cerca/search <something> (will send the definition from Wikipedia.org)


### BOT COMMANDS

- /regole - rules 
- /say <text here>
- /source [display source code]
- /muta - mute
- /smuta - unmute
- /ban
- /unban (incoming)
- /pin
- /annuncio <text here> - the bot will send and pin the message

# ToDo

- [x] ordered code
- [x] improve commands performance/exception
- [ ] settings command
- [ ] integrate database and admin list
- [ ] more languages
- [ ] more commands

dev: [@mike_2000](t.me/mike_2000)

Credits: http://github.com/mirkobrombin/pybotgram
