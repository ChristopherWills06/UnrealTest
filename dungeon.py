

hero_stats = {
    "name" : "hero", # key : value (name -> key) (hero -> value)
    "strength" : 10,
    "health" : 100.0,
}

enemy_stats = {
    "health" : 20,
 }

hero_max_health = 100

health_potion_strength = 5
hero_inventory = ["sword", "health potion", "rope"]


def quit ():
    print ("You chose to flee\n")
    print ("GAME OVER\n")
    return False

def player_stats ():
    print ("You are:")
    for key, value in hero_stats.items():
        print(f"{key} : {value}" )

def player_move():
    pass

def player_attack():
    pass

def player_heal(item_name):

    if (hero_inventory.count("health potion") <=0 ):
        print (f"You don't have any items {item_name}")
        return

    print (f"You used a {item_name} you've restored {health_potion_strength} health")
    hero_stats["health"] = hero_stats["health"] + health_potion_strength

    # health = 100
    # use health potion
    # print -> you alreayd have max health
    # DO NOT remove the health potion

    if (hero_stats["health"] >= hero_max_health):
        print ("You've reached max health")
        hero_stats["health"] = hero_max_health

    print (f"Your health is now {hero_stats['health']}")
    hero_inventory.remove("health potion")
    print(f"Your inventory is now {hero_inventory}")

def use_item():
    item_name = input (f"What item do you want to use? {hero_inventory}\n").lower()
    print (f"The item you want to use is {item_name} ")
    match item_name:
        case "sword":
            pass
        case "health potion":
            player_heal(item_name)

        case "rope":
            pass
        case _:
            print(f"{item_name} is not in your inventory")

#TEMP FUNCT
def damage_player():
    hero_stats["health"] = hero_stats["health"] - 10
    print (f"Your health is now {hero_stats['health']}")

isPlaying = True

hero_stats["name"] = input ("What is your name?\n")
player_stats()

while (isPlaying):

    action = input ("\nSelect Action: Attack, Move, Use or Flee\n").lower()
    print (f"Player Action: {action}")

    if (action == "flee"):
        isPlaying = quit() # <-- isPlaying = False
    elif (action == "attack"):
        #player_attack()
        damage_player()
    elif (action == "use"):
        use_item()
    elif (action == "move"):
        player_move()

    else:
        print (f"{action} is an invalid action")



    print ("END OF LOOP")