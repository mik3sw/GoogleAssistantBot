# How to use

**Home page**: [Home page](./home.md)

**Previous**: [Quick start](./quickstart.md)

## Setup

You will need to edit the [config.py](../bot/config.py) file
```python
# Bot configuration file
# ======================
bot_token = 'TOKEN'
bot_username = 'username'
bot_id = '0000000'
log_channel = -123456789
language = 'it' #check 'strings.ini' file
OWNER_LIST= [123456,3456789]
LIST_OF_ADMINS = [12345, 111111, 22222]
COLLABORATORS = [12345667]
TITLES = ['creator', 'administrator'] #do not change
# =======================


# Chat controls
# =======================
bad_words = ['word1', 'word2'] # messages with this words will be deleted
# =======================


# URL Filter
# =======================
url_denylist = ["t.me"]
url_whitelist = ["t.me/googlepixelit", "t.me/aospitalia", "t.me/aospitaliashop", "t.me/pixelwatchitalia", "t.me/googlepixelitchannel"]

# Market id
mercatino = -12345678


admin_group = -1234567

```

Then edit your [string.ini](../bot/strings.ini) and [settings.ini](../bot/settings.ini)

## Commands
This is the complete list of available commands and functions.

### Banning and kicking users (and unban)

<i>For both ban and kick command you can also pass the "ban reason" as argument</i>

- Reply to a message with [/ban]() to ban the user who sent the message. It **doesn't work** with usernames or user_id ("/ban @username")

- If you want to ban with style, you can [/nuke]() a user! (Reply to a message with this command). Authorization will be requested via a button and after a countdown a nuke will be dropped.

- To unban a user just reply to a message with [/unban]().

- To kick a user reply to a message (from that user) with [/kick]()

- To kick or ban an user with a delay of 60 seconds to let him/her know the ban/kick reason you can reply to a message using: 
    - [/autokick]() [reason]
    - [/autoban]() [reason]


### Mute users (and unmute)
<i>For every command you can also pass telegram_id as argument without replying to a message.</i>

- Reply to a message with [/mute]() to mute the user who sent the message.
- To unmute a user just reply to a message with [/unmute]().

### Pin a message

- Reply to a message with [/pin]()
- Use "[/saypin]() _[text]_" to let the bot write and pin the "_[text]_" message

### Delete a message

- Reply to a message with [/del]() to delete it.

### Night mode

- Use [/night]() or [/silence]() command to update users settings (can't send messages and media). It will also appear a button to disable the night/silence mode.

### Slow mode (custom, not like Telegram)

Slow mode is a custom rule that let users send only a certain number of consecutive messages, after that the user who sent too many messages will be muted for a certain amounth of time.

To activate it use 
```[/slow]() [messages] [time]```

<i>[/slow]() 3 30: after 4 consecutive messages the user will be muted for 30 seconds</i>


- [/slow]() 1 5 60   
    - activate slow mode
    - msg_num=5
    - seconds=60

- [/slow]() 1 5
    - equivalent to [/slow]() 1 5 30

- [/slow]() 0
    - equivalent to [/slow]() 0 3 30 (here 3 and 30 are meaningless, whatever value is ok for both)

- [/slow]() 
    - equivalent to [/slow]() 1 3 30

- [/slow]() -ls
    - shows settings applied in a group

### Get

Reply to a message with [/get]() to obtain detailed information about the message, like telegram_id and message_id.

### Check permission
To check if the bot has the correct permissions on your group use [/check]() command.
The correct output is:

```
Check permissions

can_restrict_members: ✅
can_delete_messages: ✅
can_pin_messages: ✅
```

### Start
[/start]() command will display a default start message.

### Help
[/help]() command will show this documentation about the bot.

### Rules
[/rules]() command will display the group rules.

### Me
[/me]() command will show detailed info about the user who typed the command.

### Source
[/source]() command will show the GitHub link of the bot repository.


## Functions

### Welcome
The bot will display a welcome message to new users who join the group. (currently not working with Telegram topics)

#### New user filters
The bot will automatically check if the new user ```first_name``` contains Chinese, Japanese, Russian or Arabs characters and if the user has no ```username``` it will be automatically blocked.

**⚠️ Not Racism! ⚠️**<br>
In several non-global groups a lot of userbots join with chinese/arabic names (and no username) only for **spamming/scamming**

#### Different welcome
You can set different welcomes based on ```telegram_chat_id```, see ```dialogs/welcome.py```

### Custom chat filters
Our bot can also block banned words, banned links and banned characters or languages (also on images). See ```settings.ini``` file.

### Admin tag
You can use @admin tag to send a report to the admin group (you can set it in the config file)

### Misc

#### Custom answers
You can set custom question and answers, check ```dialogs/misc``` folder. (text is currently in italian)

#### Wikipedia search
In italian "Google cerca [something]" that stands for "Google search [something]" will provide Wikipedia information about [something]





**Next**: [Code](./code.md)