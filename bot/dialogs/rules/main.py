from . import urlfilter, bad_words, non_latin_filter, admin_tag


async def init(update, context):
    await urlfilter.init(update, context)
    await bad_words.init(update, context)
    await non_latin_filter.init(update, context)
    await admin_tag.init(update, context)
    
    