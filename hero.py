class rat:
    def __init__(self, health, hitpower, speed, chezcoins, ratpack):
        self.health = health
        self.hitpower = hitpower
        self.speed = speed
        self.chezcoins = chezcoins
        self.ratpack = ratpack

    def takehit(self):
        health -= 10

    