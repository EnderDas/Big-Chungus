#just throwing this in here for a bit, will remove later
#__init__
from ctypes import *
from basic import *
from keyboard import *
from dice import *
import os
import time

os.system('mode 120, 30')

STD_OUTPUT_HANDLE = -11

class _COORD(Structure):
    pass

_COORD._fields_ = [("X", c_short), ("Y", c_short)]

_FORMATTERS = {
    "basic": Basic
}

class Screen:

    def __init__(self, format="basic", **kwargs):
        self.format = format
        self.width, self.height = os.get_terminal_size()
        self.formatter = _FORMATTERS[self.format](screen=self, **kwargs)

    def refresh(self):
        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(h, _COORD(0, 0))






"""
_keys = [
    Key('kek', None, 'k'),
    Key('lmao', None, 'l')
]

s = Screen(keys=_keys)
print(s.formatter.create())
time.sleep(10)
"""
die = Dice()
MAP = [
    Keyboard.Key('roll', die.roll(), 'r'),
    Keyboard.Key('blow', die.blow(), 'b')
]
num = 0
while True: #wheres the keyboard input?
    lab = [BasicLabel("number", str(num))]
    s = Screen(keys=MAP, labels=lab)
    print(s.formatter.create())# needs keyboard input for a mock testing
