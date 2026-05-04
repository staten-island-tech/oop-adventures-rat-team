import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 1
gridw = 12
gridh = 6

grid = [[0 for _ in range(gridw)] for _ in range(gridh)]

grid[4][3] = 1

print(grid)
player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)

cellw = (screen.get_width() / gridw)
cellh = (screen.get_height() / gridh)

img_rotation = 0
img_flip = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    my_image = pygame.image.load("RatRightSprite.png")
    my_image = pygame.transform.rotate(my_image, img_rotation)
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

    # pygame.draw.circle(screen, "red", player_pos, 40)
    screen.blit(my_image, player_pos)

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
        p2_x = p1_x + my_image.width
        p2_y = p1_y
        img_rotation = 90
        img_flip = False

    elif keys[pygame.K_s]:
        player_pos.y += 600 * dt
        p1_x = player_pos.x
        p1_y = player_pos.y + my_image.height
        p2_x = p1_x + my_image.width
        p2_y = p1_y 
        img_rotation = 270
        img_flip = False

    elif keys[pygame.K_a]:
        player_pos.x -= 600 * dt 
        p1_x = player_pos.x
        p1_y = player_pos.y
        p2_x = p1_x 
        p2_y = p1_y + my_image.height
        img_rotation = 0
        img_flip = True

    elif keys[pygame.K_d]:
        player_pos.x += 600 * dt 
        p1_x = player_pos.x + my_image.width
        p1_y = player_pos.y
        p2_x = p1_x     
        p2_y = p1_y + my_image.height
        img_rotation = 0
        img_flip = False


    else:
        pressed = False

    if (pressed == True):
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

    dt = clock.tick(60) / 1000

pygame.quit()