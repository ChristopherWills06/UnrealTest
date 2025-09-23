import random

hero_stats = {
    "name" : "hero", # key : value (name -> key) (hero -> value)
    "strength" : 10,
    "health" : 100.0,
}

enemy_stats = {
    "health" : 20,
 }



def quit ():
    print ("You chose to flee\n")
    print ("GAME OVER\n")
    return False

def player_stats ():
    print ("You are:")
    for key, value in hero_stats.items():
        print(f"{key} : {value}" )

def goblin_stats ():
    print ("\nGoblin Health Stats:")
    for key, value in enemy_stats.items():
        print(f"{key} : {value}" )

def player_move():
    pass

def player_attack():
    pass

isPlaying = True

hero_stats["name"] = input ("What is your name?\n")
player_stats()
goblin_stats()



# Nested loops to simulate a grid-based game world (e.g., a 2D map)
print("\nDisplaying game world (5x5 grid):")
game_world = [['.' for i in range(5)] for j in range(5)]
# Place the player in the center of the grid
player_position = (2, 2)
game_world[player_position[0]][player_position[1]] = 'P'
# Print the game world
for row in game_world:
    for cell in row:
        print(cell, end=' ')
    print()



while (isPlaying):

    action = input ("\nSelect Action: Attack, Move & Flee\n").lower()

    print (f"Player Action: {action}")

    if (action == "flee"):
        isPlaying = quit() # <-- isPlaying = False
    elif (action == "attack"):
        player_attack()
    elif (action == "move"):
        player_move()

    else:
        print (f"{action} is an invalid action")



    print ("END OF LOOP")