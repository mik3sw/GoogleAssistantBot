# Quick start

**Home page**: [Home page](./home.md)

**Previous**: [Introduction](./introduction.md)

## Download

Follow this steps:

- Install [Python](https://www.python.org/)
- Clone this project with:

```shell
git clone https://github.com/mik3sw/GoogleAssistantBot.git
```


## Dependencies
To install dependencies run:

```shell
cd this/directory/location

pip install -r requirements.txt
```


## Configuration

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

## First start

Open a terminal and start the bot with:
```shell
python3 bot/bot.py
```

This bot needs some permissions in your group to work properly:
- **can_restrict_members**
- **can_delete_messages**
- **can_pin_messages**

(to check permission use /check command)

## Hosting

Our bot is currently hosted on a **Raspberry Pi Zero W**.
You will need something similar or a VM with Linux on it.

Use the ```screen``` command to create a session.

```shell
screen -S <your_session_name>

python3 path/to/bot.py
```

To exit the session without killing it use ```CTRL+A+D```.

To reattach to a session use -ls to list all you session:

```shell
screen -ls
There are screens on:
	2309.shop	(05/11/22 11:47:33)	(Detached)
	2220.g	(05/11/22 11:43:32)	(Detached)
2 Sockets in /run/screen/S-pi.

```

For example you want to reattach to ```2220.g```, use:
```shell
screen -r 2220.g
```

For furter informations use: ```man screen```


**Next**: [How to use](./howtouse.md)