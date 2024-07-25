from console import *

class Clock:

    def __init__(self):
        self.tick = 0

    @classmethod
    def click(self):
        self.tick += 1
        return self

    def reset(self):
        self.tick = 0

class Loop:

    def __init__(self):
        self.work = []
        self.iteration = 0
        self.stopwork = False
    
    def doWork(self, work=None):
        if work != None:
            for i in self.work:
                if i == work:
                    i.func()
        else:
            for i in self.work:
                i.func()
        self.iteration += 1

    def addWork(self, work):
        self.work.append(work)

    def prioityPrint(self, work):
        self.doWork(work)

    def stopWork(self):
        self.stopwork = True

    def start(self):
        while True:
            if self.stopwork:
                break
            else:
                pass

class Event:

    def __init__(self, func, name, loop):
        self.func = func
        self.name = name
        self.loop = loop

class EventLoop(Loop):


    def __init__(self):
        super().__init__()

    def event(self, func, priority=False):

        event = Event(func, func.__name__, self)

        def addEvent(event, priority):
            self.addWork(event)
            if priority:
                self.priorityPrint(event)
        return addEvent(event, priority)
    
class EventKeyboard(keyboard.Keyboard):

    def __init__(self, loop=None):
        super().__init__()
        if loop == None:
            Exception("ADD A DAMN LOOP TO THE KEYBOARD DOLT")
        else:
            self.loop = loop
        

loop = EventLoop()

@loop.event
def work():
    print("butthole")

loop.doWork(work)

#lmao no idea what im actually gonna do with any of this
#might be wishful thinking to act like any of this complexity is necessary
#for a game so simple