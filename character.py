class Character():


    def __init__(self):
        self.max_health = 100.0
        print ("This is the character class")
        
        self.stats = {
            "name" : "{self.name}",
            "strength" : "{self.strength}",
            "health" : "{self.health}",
        }

    def retreat(self):
        print ("The hero is retreating!")

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print(f"Your health is now {self.stats['health']}")