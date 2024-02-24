import msvcrt
from clock import *
from basic import *

class Keyboard:

    @staticmethod
    def checkFor():
        if msvcrt.kbhit():
            return True
        else:
            return False

    class Key(BasicKey):

        def __init__(self, char, name, number):
            super().__init__(name, self, char)
            self.char = char
            self.name = name
            self.number = number

        

"""
class Keyboard:

    def __init__(self):
        pass

    def get_key(self):
        key = msvcrt.getwch()
        if ord(key) == 224:
            second = msvcrt.getwch()
            if ord(second) == 72:
                return 'KEY_UP'
            elif ord(second) == 80:
                return 'KEY_DOWN'
            elif ord(second) == 75:
                return 'KEY_LEFT'
            elif ord(second) == 77:
                return 'KEY_RIGHT'
            else:
                return ord(second)
        else:
            return key
"""