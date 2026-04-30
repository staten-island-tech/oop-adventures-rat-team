import random 
class cat:
    def __init__(self, health, power, speed):
        self.health = health
        self.power = power
        self.speed = speed
    def attack(self):



wild_cat = cat(random.randint(25, 45), random.randint(10 , 20), 10)