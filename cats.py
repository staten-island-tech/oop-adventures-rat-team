import random 
import pygame
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
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 1
gridw = 12
gridh = 6
sprint = 1

grid = [[0 for _ in range(gridw)] for _ in range(gridh)]

grid[4][3] = 1

print(grid)
cat_pos = pygame.Vector2(screen.get_width() / 30, screen.get_height() / 2)

cellw = (screen.get_width() / gridw)
cellh = (screen.get_height() / gridh)

img_rotation = 0
img_flip = False
animations = ["attack1", "attack2", "attack3", "attack4", "attack5", "attack6", "hurt1", "hurt2", "hurt3", "hurt4", "stand", "walk1", "walk2", "walk3", "walk4", "walk5", "walk6"]
walks = ["walk1", "walk2", "walk3", "walk4", "walk5", "walk6"]
# animation = 0
walk = 0
standing = True
walking = False
animate = 1
visible = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    stand_animation = pygame.image.load(f"stand.png")
    walk_animation = pygame.image.load(f"{walks[walk]}.png")
    if animate == 1:
        animate += 0.5
        if walk == 5:
            walk = 0
        else:
            walk += 1
    elif animate == 3:
        animate = 1
    
    stand_animation = pygame.transform.rotate(stand_animation, img_rotation)
    walk_animation = pygame.transform.rotate(walk_animation, img_rotation)
    if (img_flip == True): 
        stand_animation = pygame.transform.flip(stand_animation, True, False)
        walk_animation = pygame.transform.flip(walk_animation, True, False)

    for x in range (gridw):
        for y in range (gridh):
            xpos = cellw * x
            ypos = cellh * y
            item = grid [y][x]
            if item == 0:  #empty
                pygame.draw.rect(screen, 'light blue', (xpos, ypos, cellw-2, cellh-2))
            if item == 1:  #wall
                pygame.draw.rect(screen, 'red', (xpos, ypos, cellw-2, cellh-2))

    # pygame.draw.circle(screen, "red", cat_pos, 40)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_e]:
        visible = True

    if standing == True and visible == True:
        screen.blit(stand_animation, cat_pos)
    elif visible == True:
        screen.blit(walk_animation, cat_pos)
 
    orig_x = cat_pos.x
    orig_y = cat_pos.y

    if visible == True:
        if cat_pos.x < player_pos.x:
            cat_pos.x += 1
        elif cat_pos.x > player_pos.x:
            cat_pos.x -= 1

        if cat_pos.y < player_pos.y:
            cat_pos.y += 1
        elif cat_pos.y > player_pos.y:
            cat_pos.y -= 1

    
    pygame.display.flip()

    dt = clock.tick(60) / 1000 * sprint

pygame.quit()