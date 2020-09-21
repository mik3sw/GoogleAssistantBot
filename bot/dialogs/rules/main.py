from . import urlfilter, bad_words, non_latin_filter
def init(update, context):
    urlfilter.init(update, context)
    bad_words.init(update, context)
    non_latin_filter.init(update, context)
    