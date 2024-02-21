#basic

"""
basic formatter
+------------------------------------------+
|                   <NAME>                 |
|                                          |
|                [KEY] <ITEM>              |
|                [KEY] <ITEM>              |
|                [KEY] <ITEM>              |
|                [KEY] <ITEM>              |
|                                          |
+------------------------------------------+
"""

_FORMAT_STR = """
{lowbar}
{spaceings_one}
{title}
{keys}
{spaceings_two}
{lowbar}
"""

class Key:

    def __init__(self, name, function, calling):
        self.name = name
        self.function = function
        self.calling = calling

class Basic:

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', 'TITLE')
        self.keys = kwargs.get('keys', [])
        self.screen = kwargs.get('screen', None)

    def create(self):
        #formatting high/low bars
        _bars = '+'+((self.screen.width)-2)*'-'+'+'

        #formatting title
        _title = self.title.upper().center(self.screen.width, ' ')
        _title = list(_title)
        _title[0] = '|'; _title[len(_title)-1:] = '|'
        _title = ''.join(_title)

        #formatting keys
        _keys = ''
        for key in self.keys:
            k = f'[{key.calling.upper()}] {key.name.title()}'
            k = k.center(self.screen.width, ' ')
            k = list(k)
            k[0] = '|'; k[len(k)-1:] = '|'
            k = ''.join(k)
            _keys = _keys+k

        #formatting spacings
        _spaceings_one = ''
        _spaceings_two = ''
        range_ = (self.screen.height-(5+len(self.keys)))//2
        print(self.screen.height-(5+len(self.keys)))
        print(range_)
        for i in range(self.screen.height-(5+len(self.keys))):
            space = ' '*self.screen.width
            space = list(space)
            space[0] = '|'; space[len(space)-1:] = '|'
            space = ''.join(space)
            if i < range_:
                _spaceings_one = _spaceings_one+space
            else:
                _spaceings_two = _spaceings_two+space

        format = _FORMAT_STR.format(highbar=_bars, spaceings_one=_spaceings_one, title=_title, keys=_keys, spaceings_two=_spaceings_two, lowbar=_bars)
        return format
