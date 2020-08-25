# Google Assistant Bot
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/27f2a8ca8bf54058ab0fd97b1f184959)](https://app.codacy.com/manual/mik3sw/GoogleAssistantBot?utm_source=github.com&utm_medium=referral&utm_content=mik3sw/GoogleAssistantBot&utm_campaign=Badge_Grade_Dashboard)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/83eccd6f31ca4cdebb5af4a2cea14337)](https://app.codacy.com/manual/mik3sw/GoogleAssistantBot?utm_source=github.com&utm_medium=referral&utm_content=mik3sw/GoogleAssistantBot&utm_campaign=Badge_Grade_Dashboard)
[![Python3.7+](https://img.shields.io/badge/Python-3.7%2B-green.svg)](https://www.python.org/downloads)

## Table of content
- [Presentation](https://github.com/mik3sw/GoogleAssistantBot#Welcome)
- [Dependencies](https://github.com/mik3sw/GoogleAssistantBot#Dependencies)
- [Configuration](https://github.com/mik3sw/GoogleAssistantBot#configuration-work-in-progress)
- [Run the bot](https://github.com/mik3sw/GoogleAssistantBot#Run-the-bot)
- [What can i do?](https://github.com/mik3sw/GoogleAssistantBot#What-can-i-do)
- [Credits](https://github.com/mik3sw/GoogleAssistantBot#Credits)

## Welcome!

**[it]** - 
Bot Gestionale e di benvenuto interamente in lingua italiana ed OPEN SOURCE
Il Bot è stato realizzato per inserirlo nei gruppi facenti parte del network di [AOSPitaliaNET](https://t.me/aospitaliaNET)
Per personalizzarlo e renderlo operativo basterà modificare il file "config.py"

**[en]** - 
This bot can manage your group, but only italian language is fully supported (for now)!
This is only an imitation, it isn't the real Google Assistant and it has no AI.
If you want to use this bot, just edit the "config.py" file


## Dependencies
```
- python-telegram-bot
- wikipedia
- configparser
```

## Configuration (work in progress)

Edit file 'config.py' to run your personal bot
```
bot_token = "Bot token here"       # bot token
bot_username = "@username"         # telegram bot username
bot_id = 000000000000              # telegram bot id
language = "it"                    # bot language, check 'strings.ini' file
LIST_OF_ADMINS = [0000, 1111]      # admins' telegram id (to perform admin commands)(check utils/decorator.py to understand)
```

Edit 'strings.ini' to change or create a new personal translation of the bot and set it in config.language
```
[start]         # Start command
it = ciao!      # italian
en = hello!     # english
es = Hola!      # spanish
ru = Привет!    # russian
```

Edit 'settings.ini' to change some settings of the bot *(work in progress)*

**⚠️ Not Racism! ⚠️**

In several non-global groups a lot of userbots join with chinese/arabic names (and no username) only for **spamming/scamming**
The filter is based on this logic:

if user's first_name contains chinese characters **AND** hasn't username --> ban

[*] work in progress
```
# settings about new users joined in a group
[new_user]

# don't allow chinese characters (True)
chinese_characters = True
# don't allow arabic characters (True)
arabic_characters = True

# settings and rules in-chat 
[chat]

# don't allow chinese characters (True)
chinese_characters = True
# don't allow arabic characters (True)
arabic_characters = True
```

This bot also need some permissions to work:
- **can_restrict_members**
- **can_delete_messages**
- **can_pin_messages**

(to check permission use /check command)

## Run the bot

Follow this steps:

0) install [Python](https://www.python.org/)
1) clone this project
2) edit configurations files
3) run this commands
```
pip3 install -r requirements.txt

python google.py

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
- Google cerca/search <something> (will send the definition from Wikipedia.org)(only italian for now)
- Can detect non-latin messages and users (chinese and arabic) 
- Can detect spam links (work in progress)



### BOT COMMANDS

**ADMIN**
- ban/unban
- mute/unmute
- pin
- annuncio <text here> - the bot will send and pin the message
- nuke (ban a user in a theatrical way)
- check
- say <text here> - the bot will say what you want

**USER**
- rules 
- source [display source code]
- me (receive personal telegram information, like id, username, name...)
- help (display the list of available commands)
- start (display start message)

# ToDo

- [x] better code
- [x] improve commands performance/exception
- [ ] settings command (got headache :()
- [ ] more commands

## Credits

Main dev: [@mike_2000](https://t.me/mike_2000)

Main telegram group: [Google Pixel IT](https://t.me/googlepixelit)

Credits: http://github.com/mirkobrombin/pybotgram
