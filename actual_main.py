import pygame
import random

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
gridw = 18
gridh = 9
sprint = 1

cat_clock = pygame.time.Clock()
cat_running = True
cat_dt = 1
cat_gridw = 12
cat_gridh = 6
cat_sprint = 1

grid = [[0 for _ in range(gridw)] for _ in range(gridh)]


grid[4][3] = 1

print(grid)
player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)
cat_pos = pygame.Vector2(screen.get_width() / 30, screen.get_height() / 2)

cellw = (screen.get_width() / gridw)
cellh = (screen.get_height() / gridh)

img_rotation = 0
img_flip = False

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
cat_stand_maybe = 1
walk_break = 0
walk_break_check = False

while running:
#    print(player_pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    my_image = pygame.image.load("RatRightSprite.png")
    my_image = pygame.transform.rotate(my_image, img_rotation)
    cat_stand_animation = pygame.image.load(f"stand.png")
    cat_walk_animation = pygame.image.load(f"{cat_walks[cat_walk]}.png")
    cat_stand_animation = pygame.transform.rotate(cat_stand_animation, cat_rotation)
    cat_walk_animation = pygame.transform.rotate(cat_walk_animation, cat_rotation)
    if (cat_flip == True): 
        cat_stand_animation = pygame.transform.flip(cat_stand_animation, True, False)
        cat_walk_animation = pygame.transform.flip(cat_walk_animation, True, False)
    
    if (img_flip == True): 
        my_image = pygame.transform.flip(my_image, True, False)
    

    for x in range (gridw):
        for y in range (gridh):
            xpos = cellw * x
            ypos = cellh * y
            item = grid [y][x]
            if item == 0:  #empty
                pygame.draw.rect(screen, 'light blue', (xpos, ypos, cellw-2, cellh-2))
            if item == 1:  #wall
                pygame.draw.rect(screen, 'red', (xpos, ypos, cellw-2, cellh-2))
    cat_keys = pygame.key.get_pressed()

    if cat_keys[pygame.K_e]:
        cat_visible = True

    if cat_standing == True and cat_visible == True:
        screen.blit(cat_stand_animation, cat_pos)
    elif cat_visible == True:
        screen.blit(cat_walk_animation, cat_pos)

    # pygame.draw.circle(screen, "red", player_pos, 40)
    screen.blit(my_image, (player_pos.x - my_image.get_width()/2, player_pos.y - my_image.get_height()/2))
#    my_image = pygame.transform.scale(my_image, (60, 80))
    hw = my_image.get_width()/2
    hh = my_image.get_height()/2

    keys = pygame.key.get_pressed()

    orig_x = player_pos.x
    orig_y = player_pos.y
    cat_orig_x = cat_pos.x
    cat_orig_y = cat_pos.y

    p1_x = 0
    p1_y = 0
    p2_x = 0
    p2_y = 0

    pressed = True
    if keys[pygame.K_w]:
        # print(keys)
        player_pos.y -= 600 * dt
        p1_x = player_pos.x - hw
        p1_y = player_pos.y - hh
        p2_x = p1_x + hw
        p2_y = p1_y - hh
        img_rotation = 90
        img_flip = False

    elif keys[pygame.K_s]:
        player_pos.y += 600 * dt
        p1_x = player_pos.x - hw
        p1_y = player_pos.y + hh
        p2_x = p1_x + hw
        p2_y = p1_y + hh
        img_rotation = 270
        img_flip = False

    elif keys[pygame.K_a]:
        player_pos.x -= 600 * dt 
        p1_x = player_pos.x - hw
        p1_y = player_pos.y - hh 
        p2_x = p1_x - hw
        p2_y = p1_y + hh
        img_rotation = 0
        img_flip = True

    elif keys[pygame.K_d]:
        player_pos.x += 600 * dt 
        p1_x = player_pos.x + hw
        p1_y = player_pos.y - hh
        p2_x = p1_x + hw     
        p2_y = p1_y + hh
        img_rotation = 0
        img_flip = False

    elif keys[pygame.K_LSHIFT]:
         sprint = 2

    else:
        pressed = False
        sprint = 1

    if (pressed == True):
        gridx1 = int(p1_x / cellw)
        gridy1 = int(p1_y / cellh)

        gridx2 = int(p2_x / cellw)
        gridy2 = int(p2_y / cellh)

        gridx3 = int(p2_x / cellw)
        gridy3 = int(p2_y / cellh)



        print(gridx1, gridy1)

        if (gridy1 < 0 or gridy1 >= gridh 
         #   or gridx1-1 < 0 or gridx1 >= gridw
          #  or gridy2-1 < 0 or gridy2 >= gridh -2
           # or gridx2-1 < 0 or gridx2 >= gridw -2
            or gridx1 < 0 or gridx1 >= gridw
            or gridy2 < 0 or gridy2 >= gridh 
            or gridx2 < 0 or gridx2 >= gridw 
            ):
            item = 1
            print("outside")
            
            player_pos.x = orig_x
            player_pos.y = orig_y
        else:
            item1 = grid[gridy1][gridx1]
            item2 = grid[gridy2][gridx2]
            item3 = grid[gridy3][gridx3]
            if (item1 == 1 or item2 == 1 or item2 == 1): #wall
                print("wall")
                player_pos.x = orig_x
                player_pos.y = orig_y
    walk_break_check = False
    if cat_visible == True:
        if cat_pos.x < player_pos.x:
            if walk_break == 0:
                if cat_walk != 5:
                    cat_walk += 1
                else:
                    cat_walk = 0
            cat_pos.x += 2
            cat_standing = False
            cat_stand_maybe = 0
            if walk_break_check == False:
                if walk_break == 3:
                    walk_break = 0
                    walk_break_check = True
                else:
                    walk_break += 1
                    walk_break_check = True
        elif cat_pos.x > player_pos.x:
            if walk_break == 0:
                if cat_walk != 5:
                    cat_walk += 1
                else:
                    cat_walk = 0
            cat_pos.x -= 2
            cat_standing = False
            cat_stand_maybe = 0
            if walk_break_check == False:
                if walk_break == 3:
                    walk_break = 0
                    walk_break_check = True
                else:
                    walk_break += 1
                    walk_break_check = True
        else:
            cat_stand_maybe = 1

        if cat_pos.y < player_pos.y:
            if walk_break == 0:
                if cat_walk != 5:
                    cat_walk += 1
                else:
                    cat_walk = 0
            cat_pos.y += 2
            cat_standing = False
            cat_stand_maybe = 0
            if walk_break == 3:
                walk_break = 0
            else:
                if walk_break_check == False:
                    walk_break += 1
                    walk_break_check = True

        elif cat_pos.y > player_pos.y:
            if walk_break == 0:
                if cat_walk != 5:
                    cat_walk += 1
                else:
                    cat_walk = 0
            cat_pos.y -= 2
            cat_standing = False
            cat_stand_maybe = 0
            if walk_break_check == False:
                if walk_break == 3:
                    walk_break = 0
                    walk_break_check = True
                else:
                    walk_break += 1
                    walk_break_check = True
        else:
            if cat_stand_maybe == 1:
                cat_standing = True
    pygame.display.flip()

    dt = clock.tick(60) / 1000 * sprint
    cat_dt = cat_clock.tick(60) / 1000 * cat_sprint

pygame.quit()
# fix rotations and the rat moving faster when going diagonal because of the walk break adding up multiple times