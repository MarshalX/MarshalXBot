from keyboards.keyboards import Keyboard


class DoActionKeyboard(Keyboard):
    def _generate(self, subscribe=False, auth=False, *args, **kwargs):
        if subscribe:
            self.add_button('Подписаться', url='https://t.me/MarshalC')
        elif auth:
            self.add_button('Войти в аккаунт', url='https://t.me/music_yandex_bot')
        self.add_button('Повторить попытку', callback_data='submit')
        self.add_row()
        self.add_button('Главное меню', callback_data='main')
