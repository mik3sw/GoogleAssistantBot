# Google Assistant Bot
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2b80a4badc0f472186f735c3a1d0b726)](https://www.codacy.com/manual/mik3sw/GoogleAssistantBot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mik3sw/GoogleAssistantBot&amp;utm_campaign=Badge_Grade)
[![Python3.7+](https://img.shields.io/badge/Python-3.7%2B-green.svg)](https://www.python.org/downloads)
![](QDyD.gif)
## Table of content
- [Presentation](https://github.com/mik3sw/GoogleAssistantBot#Welcome)
- [Dependencies](https://github.com/mik3sw/GoogleAssistantBot#Dependencies)
- [Configuration](https://github.com/mik3sw/GoogleAssistantBot#configuration-work-in-progress)
- [Plugins](https://github.com/mik3sw/GoogleAssistantBot#Plugins)
- [Run the bot](https://github.com/mik3sw/GoogleAssistantBot#Run-the-bot)
- [Features](https://github.com/mik3sw/GoogleAssistantBot#Features)
- [Credits](https://github.com/mik3sw/GoogleAssistantBot#Credits)

## Welcome!

**[it]** - 
Bot Gestionale e di benvenuto interamente in lingua italiana ed OPEN SOURCE
Il Bot è stato realizzato per essere inserito nei gruppi facenti parte del network di [AOSPitaliaNET](https://t.me/aospitaliaNET)
(questo significa che è personalizzato secondo le esigenze dei miei gruppi)
Per personalizzarlo e renderlo operativo basterà modificare il file "config.py", "strings.ini" i file presenti nella cartella "dialogs"

**[en]** - 
This bot can manage your group, but only italian language is fully supported (for now)!
This is only an imitation, it isn't the real Google Assistant and it has no AI.
If you want to use this bot, just edit "config.py", "strings.ini" and files in "dialogs" folder


## Dependencies
```
- python-telegram-bot
- wikipedia
```

## Configuration (work in progress)

This bot needs some permissions to work:
- **can_restrict_members**
- **can_delete_messages**
- **can_pin_messages**

(to check permission use /check command)

**Edit file 'config.py' to run your personal bot**
```python
bot_token = "Bot token here"       # bot token
bot_username = "@username"         # telegram bot username
bot_id = 000000000000              # telegram bot id
language = "it"                    # bot language, check 'strings.ini' file
LIST_OF_ADMINS = [0000, 1111]      # admins' telegram id (to perform admin commands)(check utils/decorator.py to understand)
```

**Edit 'strings.ini' to change or create a new personal translation of the bot and set it in config.language**
```ini
[start]         # Start command
it = ciao!      # italian
en = hello!     # english
es = Hola!      # spanish
ru = Привет!    # russian
```

**Edit 'settings.ini' to change some settings of the bot** *(work in progress)*

**⚠️ Not Racism! ⚠️**
In several non-global groups a lot of userbots join with chinese/arabic names (and no username) only for **spamming/scamming**

The filter is based on this logic: if user's first_name contains chinese characters **AND** hasn't username --> ban

[*] work in progress
```ini
# settings about new users joined in a group
[new_user]

# don't allow chinese characters (True)
chinese_characters = True
# don't allow arabic characters (True)
arabic_characters = True
```

## Run the bot

Follow this steps:

0) install [Python](https://www.python.org/)
1) clone this project
2) edit configurations files
3) run this commands
```shell
pip3 install -r requirements.txt

python google.py

```

## Plugins
New Features incoming!
Check 'plugins' folder to see what is already implemented. The bot will send a message in every group/chat/channel setted in 'config.py' file

~~**Covid-19 daily report** [BETA][DELETED]~~
- ~~/covid <h> <min> command to set a daily report [h:min]~~
- ~~/uncovid to unset the daily report~~
 

**Weather daily report** [OPEN WEATHER API] [BETA]
- /weather <h> <min> command to set a daily report [h:min] (only for italy at the moment)


## Features
I am online! --> http://t.me/PythonAndroidBot

This bot offer some basic but useful commands and functions to help you managing your telegram group/community.

**For admins:**
- Ban/Unban
- Nuke
- Mute/Unmute
- Kick
- Night mode
- Pin messages

**In-Chat Controls**
- Can detect non-latin messages and users (chinese and arabic)
- Can detect blacklisted words (working)
- Can detect Amazon ref links (and other links)
- Can detect telegram spam links (working)

**Other**
- Welcome message
- Custom message handler

Other commands available in /help message


# ToDo

- [x] better code
- [x] improve commands performance/exception
- [x] blacklisted words/urls 
- [ ] more in-chat controls
- [ ] blacklist
- [ ] temp ban/mute
- [x] night mode
- [ ] settings command (got headache)

## Credits

Main dev: [@mike_2000](https://t.me/mike_2000)

Main telegram group: [Google Pixel IT](https://t.me/googlepixelit)

Credits: http://github.com/mirkobrombin/pybotgram
