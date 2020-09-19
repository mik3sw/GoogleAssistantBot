from . import urlfilter, bad_words
def init(update, context):
    urlfilter.init(update, context)
    bad_words.init(update, context)