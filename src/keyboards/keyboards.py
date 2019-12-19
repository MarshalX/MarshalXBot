from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class NotGeneratedKeyboard(Exception):
    pass


class Keyboard:
    def __init__(self):
        self.buttons = [[]]
        self._row = 0

    def add_row(self):
        self.buttons.append([])
        self._row += 1

    def add_button(self, text, callback_data=None, *args, **kwargs):
        self.buttons[self._row].append(InlineKeyboardButton(text, callback_data=callback_data, *args, **kwargs))

    def _generate(self, *args, **kwargs):
        raise NotImplementedError()

    def get(self, *args, **kwargs):
        self._generate(*args, **kwargs)

        return InlineKeyboardMarkup(self.buttons)
