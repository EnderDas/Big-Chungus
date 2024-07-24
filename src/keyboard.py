import msvcrt
from basic import *

class Keyboard:

    @staticmethod
    def checkFor():
        if msvcrt.kbhit():
            return True
        else:
            return False
        
    def __init__(self):
        self.keys = []
        self.sticky = False

    class Key(BasicKey):

        def __init__(self, name, number, char):
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