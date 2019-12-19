class TextBuilder:
    def __init__(self):
        self.lines = []
        self._empty = True

    def add(self, line=''):
        self.lines.append(line)
        self._empty = False

    def pre_add(self, line=''):
        self.lines.insert(0, line)
        self._empty = False

    def add_media(self, url):
        protocol = ''
        if 'https://' not in url and 'http://' not in url:
            protocol = 'https://'

        self.lines.append(f'<a href="{protocol}{url}">&#8203;</a>')

    def get(self):
        return '\n'.join(self.lines)

    @property
    def empty(self):
        return self._empty
