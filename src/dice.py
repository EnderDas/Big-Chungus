import random

class Dice:

    def __init__(self):
        self.cash = []
        self.coins = []
        self.dry = False
        self.wet = False
        self.flex()
        self.flex()

    def flex(self):
        self.coins = self.cash
        self.cash = [random.randint(1, 6) for i in range(6)]

    def blow(self):
        if self.dry:
            self.wet = True
            self.dry = False
        else:
            self.dry = True

    def roll(self):
        shoe = random.choice(self.coins)
        lot = random.choice(self.cash)

        if shoe > lot & shoe is not lot: #if shoe is more than lot flipem
            lot, shoe = shoe, lot

        if lot < 6: #is it less than six?
            if not shoe+lot > 6: #are they more together?
                comp = shoe+lot #comp them together
            else: #give lot since they were compared already
                comp = lot
        else: #if lot is six give them the shoe
            comp = shoe
        
        self.flex()

        if not self.wet: #did they double blow?
            if self.dry: #did they blow?
                self.dry = False
                return comp #if they blew and didnt trick give the best
            else:
                return lot #if they didnt trick give them the runner up
        else:
            self.wet = False
            if self.dry: #did they try tricking to dry
                self.dry = False
                return 1
            else:
                return shoe #they were just unlucky