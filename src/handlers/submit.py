import os

from mongoengine import get_db

from keyboards.do_action_keyboard import DoActionKeyboard
from keyboards.main_keyboard import MainKeyboard

from utils.decorators import provide_context
from utils.helpers import reply_or_edit, is_channel_member
from utils.text_builder import TextBuilder


@provide_context
def submit_handler(update, context):
    text = TextBuilder()

    if not is_channel_member(context, os.environ.get('CHANNEL'), context.user):
        text.add(f'Ты не подписался на канал :)')
        reply_or_edit(update, context, text.get(), reply_markup=DoActionKeyboard().get(subscribe=True))
        return

    db = get_db('yandex-music-bot')
    mongo_client = db.client
    collection = mongo_client[db.name]['user']

    user = collection.find_one({
        'telegram_id': context.user.telegram_id,
        'yandex_music_token': {'$exists': 'true'}
    })

    if not user:
        text.add(f'Ты не авторизовался в свой аккаунт в боте для Яндекс.Музыки')
        reply_or_edit(update, context, text.get(), reply_markup=DoActionKeyboard().get(auth=True))
        return

    context.user.member_2019 = True
    context.user.save()

    text.add('Поздравляю, ты успешно записан в участники конкурса. '
             'Следи за моим каналом, чтобы быть в курсе новостей! ' 
             'Победитель будет выбран случайным образом 31 декабря. '
             'Я обязательно проверю наличие подписки на мой канал :)')

    update.callback_query.answer()
    reply_or_edit(update, context, text.get(), reply_markup=MainKeyboard().get(is_member=True))
