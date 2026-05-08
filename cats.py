import random
import pygame
from Main import player_pos

class cat:
    def __init__(self, health, power, speed):
        self.health = health
        self.power = power
        self.speed = speed
    def attack(self, rat):
        rat.health -= self.power



wild_cat = cat(random.randint(25, 45), random.randint(10 , 20), 10)

# pygame setup
pygame.init()
cat_screen = pygame.display.set_mode((1280, 720))
cat_clock = pygame.time.Clock()
cat_running = True
cat_dt = 1
cat_gridw = 12
cat_gridh = 6
cat_sprint = 1

cat_pos = pygame.Vector2(cat_screen.get_width() / 30, cat_screen.get_height() / 2)

cat_rotation = 0
cat_flip = False
cat_animations = ["attack1", "attack2", "attack3", "attack4", "attack5", "attack6", "hurt1", "hurt2", "hurt3", "hurt4", "stand", "walk1", "walk2", "walk3", "walk4", "walk5", "walk6"]
cat_walks = ["walk1", "walk2", "walk3", "walk4", "walk5", "walk6"]
# animation = 0
cat_walk = 0
cat_standing = True
cat_walking = False
cat_animate = 1
cat_visible = False
while cat_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cat_running = False

    cat_screen.fill("black")
    cat_stand_animation = pygame.image.load(f"stand.png")
    cat_walk_animation = pygame.image.load(f"{cat_walks[cat_walk]}.png")
    if cat_animate == 1:
        cat_animate += 0.5
        if cat_walk == 5:
            cat_walk = 0
        else:
            cat_walk += 1
    elif cat_animate == 3:
        cat_animate = 1
    
    cat_stand_animation = pygame.transform.rotate(cat_stand_animation, cat_rotation)
    cat_walk_animation = pygame.transform.rotate(cat_walk_animation, cat_rotation)
    if (cat_flip == True): 
        cat_stand_animation = pygame.transform.flip(cat_stand_animation, True, False)
        cat_walk_animation = pygame.transform.flip(cat_walk_animation, True, False)

    # pygame.draw.circle(cat_screen, "red", cat_pos, 40)
    
    cat_keys = pygame.key.get_pressed()

    if cat_keys[pygame.K_e]:
        cat_visible = True

    if cat_standing == True and cat_visible == True:
        cat_screen.blit(cat_stand_animation, cat_pos)
    elif cat_visible == True:
        cat_screen.blit(cat_walk_animation, cat_pos)
 
    cat_orig_x = cat_pos.x
    cat_orig_y = cat_pos.y

    if cat_visible == True:
        if cat_pos.x < player_pos.x:
            cat_pos.x += 1
        elif cat_pos.x > player_pos.x:
            cat_pos.x -= 1

        if cat_pos.y < player_pos.y:
            cat_pos.y += 1
        elif cat_pos.y > player_pos.y:
            cat_pos.y -= 1

    
    pygame.display.flip()

    cat_dt = cat_clock.tick(60) / 1000 * cat_sprint

pygame.quit()
