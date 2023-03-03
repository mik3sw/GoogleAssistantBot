import config
from functions.general import message


async def init(update, context):
    hashtag = ['#vendo', '#cerco', '#scambio', "#feedback"]
    if update.message.text is not None:
        #print(update.message.text)
        if (update.message.chat_id == config.mercatino) and not(update.message.from_user.id in config.LIST_OF_ADMINS):
            if ("@admin" not in update.message.text.lower()) and (not str(update.message.text).lower().startswith(tuple(hashtag))):
                txt = "<b>ATTENZIONE</b>\n<b>{}</b> il tuo messaggio non rispetta le linee guida del gruppo, controlla il messaggio fissato per saperne di più!".format(update.message.from_user.first_name)
                await context.bot.delete_message(update.message.chat_id, update.message.message_id)
                await message(update, context, txt)

        