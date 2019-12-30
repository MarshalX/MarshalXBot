from datetime import datetime


from data.users import User
from context import Context


def provide_context(func):
    def wrapper(update, bot_context, *args, **kwargs):
        if update.callback_query:
            update.message = update.callback_query.message
            update.message.from_user = update.callback_query.from_user

        telegram_user = update.message.from_user
        user = User.get(telegram_user.id)

        if user:
            user.first_name = telegram_user.first_name
            user.last_name = telegram_user.last_name
            user.username = telegram_user.username
            user.language_code = telegram_user.language_code

            user.block = False
            user.time_updated = datetime.utcnow()

            user.save()
        else:
            user = User(
                telegram_user.id,
                telegram_user.first_name,
                telegram_user.last_name,
                telegram_user.username,
                telegram_user.language_code
            )
            user.save()

        context = Context(bot_context, user)

        func(update, context, *args, **kwargs)

    return wrapper
