from decorators import provide_context

from utils.helpers import reply_or_edit


@provide_context
def start_handler(update, context):
    reply_or_edit(update, context, 'Ok')
