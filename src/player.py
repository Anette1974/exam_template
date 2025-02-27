from . import pickups # importerar hela pickups.py som en modul, inte en specifik klass eller funktion.

class Player:
    marker = "@" #ac, spelarens symbol på spelplanen

    def __init__(self, x, y): # skapar ett objekt av klassen Player
        self.pos_x = x
        self.pos_y = y
        self.score = 0 #Spelaren börjar med 0 poäng

    def print_status(self, game_grid):
        """Visa spelvärlden och antal poäng."""
        print("--------------------------------------")
        print(f"You have {self.score} points.")
        print(game_grid)

    # Flyttar spelaren, "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        new_x = self.pos_x + dx # ac, adderar nytt x värde till befintligt position
        new_y = self.pos_y + dy # ac, adderar nytt y värde till befintlig position
        next_step = grid.get(new_x, new_y) # ac, hämtar vad som finns på nästa position
        if next_step == "■": # ac, kontrollerar om nästa position är en vägg
            print("\nYou hit a wall! Try again :-)")
            return False
        else:
            return True

    def move_player(self, dx, dy, grid,inventory):
        #global score  # funktionen ändrar värdet på score och då tolkar pyton det som en lokal variabel, detta ger fel då variabeln behöver vara global
        if self.can_move(dx, dy, grid):  # move according to command
            maybe_item = grid.get(self.pos_x + dx, self.pos_y + dy)
            self.move(dx, dy)
            self.score += -1

            if isinstance(maybe_item, pickups.Item):
                # we found something
                self.score += maybe_item.value
                print(f"\nYou found a {maybe_item.name}, +{maybe_item.value} points.")
                inventory.append(maybe_item)  # ac, lägger till senaste frukten i inventory
                grid.clear(self.pos_x, self.pos_y)

class Inventory:
    def __init__(self):
        self.items = []