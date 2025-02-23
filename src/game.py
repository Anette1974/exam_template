from .grid import Grid # ENBART Grid-klassen
from .player import Player # ENBART Player-klassen
from . import pickups # importerar hela pickups.py som en modul, inte en specifik klass eller funktion.
#from .pickups import Item # Fungerar ej för import, Varför ??

player = Player(17, 5)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)

# TODO: flytta denna till en annan fil
def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)

# borde funktionen move_player flyttas till en annan fil??
def move_player (dx, dy):
    global score # funktionen ändrar värdet på score och då tolkar pyton det som en lokal variabel, detta ger fel då variabeln behöver vara global
    if player.can_move(dx, dy, g):  # move according to command
        maybe_item = g.get(player.pos_x + dx, player.pos_y + dy)
        player.move(dx, dy)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            inventory.append(maybe_item) # ac, lägger till senaste frukten i inventory
            print(f"Du har lagt till {maybe_item.name} i inventory.") #ac, skriver ut senaste plockade frukten
            print(f"Inventory innehåller nu:{[p.name for p in inventory]}") # ac, skriver ut vad som finns i inventory
            g.clear(player.pos_x, player.pos_y)


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1] # gör strängen till gemener och tar ut första tecknet

    if command == "d":
        move_player (1,0) # move right

    elif command == "a":
        move_player(-1, 0) # move left

    elif command == "s":
        move_player(0, 1) # move up

    elif command == "w":
        move_player(0, -1) # move down

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
