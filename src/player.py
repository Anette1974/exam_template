
class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        new_x = self.pos_x + dx # ac, adderar nytt x värde till befintligt position
        new_y = self.pos_y + dy # ac, adderar nytt y värde till befintlig position
        next_step = grid.get(new_x, new_y) # ac, hämtar vad som finns på nästa positions
        if next_step == "■": # ac, kontrollerar om nästa position är en vägg
            print("Du gick in i en vägg!")
            return False
        else:
            return True

class Inventory:
    def __init__(self):
        self.items = []
"""
    def add_item(self, item):
        self.items.append(item)
        print (f"Lagt till {item} i inventory.")"""