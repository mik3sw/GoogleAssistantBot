from dialogs import misc, rules
def init(update, context):
    misc.handler.init(update, context)
    rules.main.init(update, context)