import random
import pygame

class character_stats:
    def __init__(self, health, power, speed):
        self.health = health
        self.power = power
        self.speed = speed
    def catattack(self, rat): #only use this function in the actual cats file
        # in actual cats have: every 10 seconds it will do attack animation, when the attack happens, sense if the attack hitbox touches the rat hitbox, then do this function to lower the rat health variable which will determine the rat health bar (if rat health variable goes down then make it so that the health bar for the rat also goes down)
        rat.health -= self.power
        #include health bar changes here ex: rathealthbar -= self.power aka cat power (or 2nd option:) ex: rathealthbar = rat.health
    def ratattack(self, cat): #only use this function in the actual rats file
        # in actual rats have: when k is pressed it will do attack animation, when the attack happens, sense if the attack hitbox touches the cat hitbox, then do this function to lower the cat health variable which will determine the cat health bar (if cat health variable goes down then make it so that the health bar for the cat also goes down)
        cat.health -= self.power
        #include health bar changes here ex: cathealthbar -= self.power aka rat power (or 2nd option:) ex: cathealthbar = cat.health

# class rat:
#     def __init__(self, health, hitpower, speed, chezcoins, ratpack):
#         self.health = health
#         self.hitpower = hitpower
#         self.speed = speed
#         self.chezcoins = chezcoins
#         self.ratpack = ratpack

#     def takehit(self):
#         health -= 10