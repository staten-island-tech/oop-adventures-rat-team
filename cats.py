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
player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)

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
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    stand_animation = pygame.image.load(f"stand.png")
    walk_animation = pygame.image.load(f"{walks[walk]}.png")
    
    if walk == 5:
        walk = 0
    else:
        walk += 1
    stand_animation = pygame.transform.rotate(stand_animation, img_rotation)
    if (img_flip == True): 
        stand_animation = pygame.transform.flip(stand_animation, True, False)

    for x in range (gridw):
        for y in range (gridh):
            xpos = cellw * x
            ypos = cellh * y
            item = grid [y][x]
            if item == 0:  #empty
                pygame.draw.rect(screen, 'light blue', (xpos, ypos, cellw-2, cellh-2))
            if item == 1:  #wall
                pygame.draw.rect(screen, 'red', (xpos, ypos, cellw-2, cellh-2))

    # pygame.draw.circle(screen, "red", player_pos, 40)
    if standing == True:
        screen.blit(stand_animation, player_pos)
    else:
        screen.blit(walk_animation, player_pos)

    keys = pygame.key.get_pressed()
 
    orig_x = player_pos.x
    orig_y = player_pos.y

    p1_x = 0
    p1_y = 0
    p2_x = 0
    p2_y = 0

    pressed = True
    if keys[pygame.K_w]:
        print(keys)
        player_pos.y -= 600 * dt
        p1_x = player_pos.x
        p1_y = player_pos.y
        p2_x = p1_x + stand_animation.get_width()
        p2_y = p1_y
        img_rotation = 90
        img_flip = False
        standing = False


    elif keys[pygame.K_s]:
        player_pos.y += 600 * dt
        p1_x = player_pos.x
        p1_y = player_pos.y + stand_animation.get_height()
        p2_x = p1_x + stand_animation.get_width()
        p2_y = p1_y 
        img_rotation = 270
        img_flip = False
        standing = False

    elif keys[pygame.K_a]:
        player_pos.x -= 600 * dt 
        p1_x = player_pos.x
        p1_y = player_pos.y
        p2_x = p1_x 
        p2_y = p1_y + stand_animation.get_height()
        img_rotation = 0
        img_flip = True
        standing = False

    elif keys[pygame.K_d]:
        player_pos.x += 600 * dt 
        p1_x = player_pos.x + stand_animation.get_width()
        p1_y = player_pos.y
        p2_x = p1_x     
        p2_y = p1_y + stand_animation.get_height()
        img_rotation = 0
        img_flip = False
        standing = False

    elif keys[pygame.K_r]:
         sprint = 2

    else:
        pressed = False
        sprint = 1
        
    if pressed == False:
        walking = False
        standing = True

    if (pressed == True):
        standing = False
        gridx1 = int(p1_x / cellw)
        gridy1 = int(p1_y / cellh)

        gridx2 = int(p2_x / cellw)
        gridy2 = int(p2_y / cellh)

        print(gridx1, gridy1)

        if (gridy1 < 0 or gridy1 >= gridh 
            or gridx1 < 0 or gridx1 >= gridw
            or gridy2 < 0 or gridy2 >= gridh 
            or gridx2 < 0 or gridx2 >= gridw
            ):
            print("outside")
            player_pos.x = orig_x
            player_pos.y = orig_y
        else:
            item1 = grid[gridy1][gridx1]
            item2 = grid[gridy2][gridx2]
            if (item1 == 1 or item2 == 1): #wall
                print("wall")
                player_pos.x = orig_x
                player_pos.y = orig_y

    pygame.display.flip()

    dt = clock.tick(60) / 1000 * sprint

pygame.quit()