#basic
"""
change formatting to something easier to read, maybe even a system that just
handles the boarders separately and something that handles the labels and keys
all by itself too. im gonna hold off on the keyboard for now and focus on cleaning this up so
i have an actual system to work off of that can handle events and shi...
"""
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

"""
'Frame' based formatter
{0}{1}{2}
{3}{4}{5}
{6}{7}{8}

frames will ideally just be a cool way to abstract the way i can set up windowing with the cli

class Frame:

    def __init__(self, screen, cells=[]):
        if cells != []:
            self.cells = cells
        else:
            self.cells = [None for i in range(9)]
        self.screen = screen

    def cell(self, index):
        if index > 9 and index <= 0:
            return self.cells[index]
        else:
            raise ValueError('Must be less than 9 or more than 0')

    def loadCell(self, cell, index):
        if compare(cell, Cell) and (index > 9 && index <=0):
            self.cells[index] = cell
        else:
            raise ValueError("SET UP YOUR CELL LOADS CORRECTLY DUNCE")

    def packCells(self):
        for c in self.cells:
            if c == None:
                raise ValueError("LOAD YOUR GOD DAMN CELLS BUNGHOLE")
            else:
                
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

class Boarder:

    pass

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
        #_bars = '+'+((self.screen.width)-2)*'-'+'+'
        _bars = "+"+f"{'-'*(self.screen.width-2)}"+"+"

        #formatting title
        _title = self.title.upper().center(self.screen.width, ' ')
        _title = list(_title)
        _title[0] = '|'; _title[len(_title)-1:] = '|'
        _title = ''.join(_title)

        #formatting keys
        _keys = '' #get the key
        for key in self.keys: #look through them
            k = f'[{key.calling.upper()}] {key.name.title()}' #make the key with style
            #k = k.center(self.screen.width, ' ') #center the key
            #k = list(k) #convert to list of chars
            #k[0] = '|'; k[len(k)-1:] = '|' #some centering magic i figured out, this could be better but idc
            #k = ''.join(k) #pull it all back together again
            """

                this could be done using f-string padding,
                this might speed up the formatting process but at what speed?
                trivial given the whole formatter is an absolute fucking mess
                idk what im doing but it works so...

            k = f"|{k^(self.screen.width-2)}|"

                this might work... or it might not... i have no clue i dont want to test it yet

                that did not work...
                this did however tho.

            k = f'|{k:^{self.screen.width-2}}|'
                     ^
                     |--- this right here

            this worked because i finally realized how to format a string correctly


            """
            #k = f'|{value:{align}{width}}|'
            k = f'|{k:^{self.screen.width-2}}|'
            _keys = _keys+k


        #pull this shit apart and make it make sense
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
