#basic

"""
basic formatter
+------------------------------------------+
|                   <NAME>                 |
|                                          |
|               [LABEL] <VALUE>            |
|                [KEY] <ITEM>              |
|               [LABEL] <VALUE>            |
|                [KEY] <ITEM>              |
|                                          |
+------------------------------------------+
"""

_FORMAT_STR = """
{highbar}
{spacings_one}
{title}
{labels}
{keys}
{spacings_two}
{lowbar}
"""

class BasicKey:

    """
    Renamed to remove confusion with Keyboard.Key

    Move self.function & self.calling into Keyboard.Key handle them there
    to save space and make it make sense.

    Keyboard.Key should inherent this class to use it as a base class and remove
    unnecessary names from Keyboard.Key
    """


    def __init__(self, name, function, calling):
        self.name = name
        self.function = function #this should be changed to match up with key
        self.calling = calling #this can probably be handled in key also

class BasicLabel:

    """
    Renamed to follow suite to BasicKey's rename
    """
    
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Basic:

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', 'TITLE')
        self.keys = kwargs.get('keys', [])
        self.labels = kwargs.get('labels', [])
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

        _labels = ''
        for label in self.labels:
            l = f'[{label.desc.upper()}] {label.name.title()}'
            l = l.center(self.screen.width, ' ')
            l = list(l)
            l[0] = '|'; l[len(l)-1:] = '|'
            l = ''.join(l)
            _labels = _labels+l

        #formatting spacings
        _spacings_one = ''
        _spacings_two = ''

        range_ = (
            self.screen.height - (
                5 + len( self.keys+self.labels )
                    )
                ) // 2
        
        #print(self.screen.height-(5+len(self.keys)))
        #print(range_)
        for i in range(
            self.screen.height - (5 + len(self.keys + self.labels))):

            space = ' ' * self.screen.width
            space = list(space)
            space[0] = '|'; space[len(space) - 1:] = '|'
            space = ''.join(space)
            if i < range_:
                _spacings_one = _spacings_one + space
            else:
                _spacings_two = _spacings_two + space

        format = _FORMAT_STR.format(
            highbar = _bars, 
            spacings_one = _spacings_one, 
            title = _title, 
            keys = _keys, 
            labels = _labels, 
            spacings_two = _spacings_two, 
            lowbar = _bars
            )
        return format
