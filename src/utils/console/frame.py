"""
'Frame' based formatter
{0}{1}{2}
{3}{4}{5}
{6}{7}{8}

frames will ideally just be a cool way to abstract the way i can set up windowing with the cli
"""

class Cell:

    pass


class Frame:

    def __init__(self, screen, cells=[]):
        if cells != []:
            self.cells = cells
        else:
            self.cells = [None for i in range(8)]
        self.screen = screen

    def cell(self, index):
        #access cell with direct index
        if index > 9 and index <= 0:
            return self.cells[index]
        else:
            raise ValueError('Must be less than 9 or more than 0')
    
    def getCell(self, x, y):
        #could make a smart frame that accesses cells based on
        #just text, or even just the class scope itself as properties
        return self.cells

    def loadCell(self, cell, index):
        if cell.compare(Cell) & index > 9 & index <=0:
            self.cells[index] = cell
        else:
            raise ValueError("SET UP YOUR CELL LOADS CORRECTLY DUNCE")

    def packCells(self):
        for c in self.cells:
            if c == None:
                raise ValueError("LOAD YOUR GOD DAMN CELLS BUNGHOLE")
            else:
                pass
        #cells checked begin pack the cells into the form now
        #make some methods for rows and columns
        #make one that uses both to access a cell. 
        # |- this will be for easier access using for loops
        # |- and because i cant think of anything better lol

class FrameO:

    def __init__(self, screen, cells=[]):
        if cells != []:
            self.cells = cells
        else:
            self.cells = [
                [None for i in range(2)] for i in range(2)
            ]
            #wow an actual matrix
        self.screen = screen

    def getCell(self, x: int, y: int):
        return self.cells[y][x]
    
    def loadCell(self, cell: Cell, index: tuple):
        x, y = index
        self.cells[y][x] = cell

    def popFrame(self):
        #debating what to return here, either a str
        #or if i should pass the object with the packed string
        pass
