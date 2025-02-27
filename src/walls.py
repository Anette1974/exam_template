from .grid import Grid # ENBART Grid-klassen

class Walls:
    def __init__(self, grid):
        self.horiz_inner_walls()
        self.g = grid



    def horiz_inner_walls(self):
        horizontal = [5, 6, 7, 15, 16, 17, 22, 22, 22]
        vertical = [3, 3, 3, 9, 9, 9, 4, 5, 6]
        # skapar extra innerväggar i spelplanen
        #self.g.set(10, 3, "■") # sätter ut en vägg på en fast position
        for x, y, in zip(horizontal, vertical):
                self.g.set(x, y, "■")



    g = Grid() # skapar en instans av klassen Grid
