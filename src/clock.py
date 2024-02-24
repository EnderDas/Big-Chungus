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
        if not work:
            pass #do all the work
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

loop = EventLoop()

@loop.event
def work():
    pass

print(loop.work[0].name)
