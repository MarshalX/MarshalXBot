from keyboards.keyboards import Keyboard


class MainKeyboard(Keyboard):
    def _generate(self, is_member=False, *args, **kwargs):
        # if not is_member:
        #     self.add_button('Принять участие в розыгрыше', callback_data='submit')
        #     self.add_row()
        self.add_button('Мой канал', url='https://t.me/MarshalC')
        self.add_row()
        self.add_button('Мой сайт', url='https://marshal.by/')
        self.add_row()
        self.add_button('Яндекс.Музыка Бот', url='https://t.me/music_yandex_bot')
