# import modules
from dialogs import misc, rules


# init function
async def init(update, context):
    await misc.handler.init(update, context)
    await rules.main.init(update, context)
