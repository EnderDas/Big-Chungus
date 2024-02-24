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


