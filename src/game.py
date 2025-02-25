from .grid import Grid # ENBART Grid-klassen
from . import pickups # importerar hela pickups.py som en modul, inte en specifik klass eller funktion.
#from .pickups import Item # Fungerar ej för import, Varför ??
from .player import Player # ENBART Player-klassen


player = Player(17, 5)
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
pickups.randomize(g)

# funktionen print_status flyttad till player.py


# funktionen move_player flyttad till player.py

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    player.print_status(g)

    command = input("Use WASD to move, Q/X to quit or I to show inventory. ")
    command = command.casefold()[:1]  # gör strängen till gemener och tar ut första tecknet

    if command == "d":
        player.move_player(1, 0, g, inventory)  # move right

    elif command == "a":
        player.move_player(-1, 0, g, inventory)  # move left

    elif command == "s":
        player.move_player(0 ,1, g, inventory)  # move up

    elif command == "w":
        player.move_player(0, -1, g, inventory)  # move down

    elif command == "i":
        print(
            f"You have picked these items:{[p.name for p in inventory]}")  # ac, skriver ut vad som finns i inventory

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
