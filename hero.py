
#Character ____ Hero
#         |____ Enemy


# TODO
# Player heal
# Use items
# Connect the two files



class Hero ():
    def __init__(self):

        self.max_health = 100.0

        self.health_potion_strength = 5

        self.stats = {
            "name" : "hero",
            "strength" : 10,
            "health" : 70,
        }

        self.inventory = ["sword", "health potion", "rope"]

    def print_stats(self):
        print("Your stats are: ")
        for key, value in self.stats.items():
            print(f"{key} : {value}")

    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats

    def move(self):
        pass

    def attack(self):
        pass

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print(f"Your health is now {self.stats['health']}")
        pass

    def heal(self, item_name):
        
        #TODO > Move this to this use item function
        if(self.inventory.count("health potion") <=0):
            print(f"You don't have any {item_name}")

        print (f"You used a {item_name} you've restored {self.health_potion_strength} health")
        self.stats["health"] = self.stats["health"] + self.health_potion_strength

        if (self.stats["health"]>= self.max_health):
            print ("You've reached max health")
            self.stats["health"] = self.max_health

        print (f"Your health is now {self.stats['health']}")
        self.inventory.remove("health potion")
        print(f"Your inventory is now{self.inventory}")

    def use_item(self):
        item_name = input (f"What item do you want to use? {self.inventory}\n").lower()
        print (f"The item you want to use is {item_name}")
        match item_name:
            case "sword":
                pass
            case "health potion":
                self.heal(item_name)

            case "rope":
                pass
            case _:
                print(f"{item_name} is not in your inventory")

#---------------------------

player = Hero()

# print(f"Here are your Hero Stats {self.stats}")

hero = Hero()
hero.print_stats()
print("\n-------------------------------")
hero.stats["health"] = 70
hero.heal("health potion")
print("\n-------------------------------")

player.print_stats()