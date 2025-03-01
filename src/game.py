from .grid import Grid # ENBART Grid-klassen
from . import pickups # importerar hela pickups.py som en modul, inte en specifik klass eller funktion.
from .player import Player # ENBART Player-klassen

player = Player(17, 5) # Initierar en spelare med en position mitt på spelet med namnet player
inventory = [] # skapar en tom lista där spelarens plockade "frukter" lagras

g = Grid() # skapar en instans av klassen Grid
g.set_player(player)
g.make_walls()
g.inner_walls()
pickups.randomize(g)

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    player.print_status(g)


    command = input("Use WASD to move, Q/X to quit or I to show inventory: ")
    command = command.casefold()[:1]  # gör strängen till gemener och tar ut första tecknet

    if command == "d":
        player.move_player(1, 0, g, inventory)  # flytta höger

    elif command == "a":
        player.move_player(-1, 0, g, inventory)  # flytta vänster

    elif command == "s":
        player.move_player(0 ,1, g, inventory)  # flytta upp

    elif command == "w":
        player.move_player(0, -1, g, inventory)  # flytta ner

    elif command == "i":
        print(
            f"You have picked these items: {', '.join(p.name for p in inventory)}")  # skriver ut vad som finns i inventory

# Hit kommer vi när while-loopen slutar
print(f"\nThank you for playing! \nYou got {player.score} points and you collected these items: {', '.join(p.name for p in inventory)}")

