import os
import html
import random

from telegram.error import BadRequest, TelegramError

from data.users import User

from utils.decorators import provide_context
from utils.helpers import is_channel_member, reply_or_edit


@provide_context
def play_out_handler(update, context):
    if os.environ.get('ADMIN') != context.user.username:
        return

    start_text = 'Начат розыгрыш, идёт выбор победителя...'

    actual_members = []
    for user in User.objects.filter(member_2019=True):
        try:
            context.bot.send_message(user.telegram_id, start_text)

            if is_channel_member(context, os.environ.get('CHANNEL'), user):
                actual_members.append(user)
            else:
                context.bot.send_message(user.telegram_id, 'Ты не принимаешь участие в конкурсе из-за отписки.')
        except (BadRequest, TelegramError):
            user.block = True
            user.save()

    winner = random.choice(actual_members)
    winners_link = f'<a href="tg://user?id={winner.telegram_id}">{html.escape(winner.first_name)}</a>'

    end_text = f'Годовая подписка на Яндекс.Музыку достаётся {winners_link}, поздравляем с победой!'

    for member in actual_members:
        context.bot.send_message(member.telegram_id, end_text, parse_mode='html')

    context.bot.send_message(os.environ.get('CHANNEL'), start_text, parse_mode='html')
    context.bot.send_message(os.environ.get('CHANNEL'), end_text, parse_mode='html')

    reply_or_edit(update, context, 'Красавчик')
