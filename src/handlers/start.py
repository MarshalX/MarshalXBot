import html

from keyboards.main_keyboard import MainKeyboard

from utils.helpers import reply_or_edit
from utils.text_builder import TextBuilder
from utils.decorators import provide_context


@provide_context
def start_handler(update, context):
    text = TextBuilder()
    text.add(f'Приветствую, {html.escape(context.user.first_name)}')
    text.add()

    # if context.user.member_2019:
    #     text.add('Ты являешься участником моего розыгрыша!')
    # else:
    #     text.add('В данный момент проводится розыгрыш <b>годовой</b> подписки Яндекс.Плюс!')
    #     text.add()
    #     text.add('Чтобы принять участие необходимо выполнить всего два условия:')
    #     text.add()
    #     text.add('1. Подписаться на <a href="https://t.me/MarshalC">мой канал</a>')
    #     text.add('2. Авторизоваться в свой яндекс аккаунт в боте '
    #              '<a href="https://t.me/music_yandex_bot">Яндекс.Музыка</a>')

    reply_or_edit(update, context, text.get(), reply_markup=MainKeyboard().get(context.user.member_2019),
                  parse_mode='html')
