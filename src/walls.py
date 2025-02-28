from .grid import Grid # ENBART Grid-klassen

class Walls:
    def __init__(self, grid):
        self.horiz_inner_walls()
        self.g = grid

    # skapar extra innerväggar i spelplanen
    def horiz_inner_walls(self):
        horizontal = [5, 6, 7, 15, 16, 17, 22, 22, 22]
        vertical = [3, 3, 3, 9, 9, 9, 4, 5, 6]
        for x, y, in zip(horizontal, vertical):
                self.g.set(x, y, "■")

        #self.g.set(10, 3, "■") # första försöket, sätter ut en vägg på en fast position

    g = Grid()  # skapar en instans av klassen Grid
