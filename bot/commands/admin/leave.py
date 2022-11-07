from utils import decorator

@decorator.ownerbot
#@decorator.cancellacomandi
def init(update, context):

    try:
        groups = context.args
        print(groups)
        for g in groups:
            try:
                bot = context.bot
                #bot.send_message(update.message.chat_id, text="Leaving this group", parse_mode='HTML')
                bot.leaveChat(g)
                print(f"Leaving chat_id: {g} - success")
                update.message.reply_text(text=f"Leaving chat_id: {g} - success", parse_mode='HTML')
            except:
                print(f"Leaving chat_id: {g} - failed")
                update.message.reply_text(text=f"Leaving chat_id: {g} - failed", parse_mode='HTML')
        
    except:
        bot = context.bot
        update.message.reply_text(text="Leaving this group", parse_mode='HTML')
        bot.leaveChat(update.message.chat_id)
