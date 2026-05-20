
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
sprint = 1
img_rotation = 0
img_flip = False


player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("light blue")


    my_image = pygame.image.load("RatRightSprite.png")
    my_image = pygame.transform.rotate(my_image, img_rotation)
    if (img_flip == True): 
        my_image = pygame.transform.flip(my_image, True, False)

    # pygame.draw.circle(screen, "red", player_pos, 40)
    left_wall = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 60, 900))
    right_wall = pygame.draw.rect(screen, (255, 0, 0), (1220, 0, 60, 900))
    top_wall = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 1220, 60))
    bottom_wall = pygame.draw.rect(screen, (255, 0, 0), (0, 660, 1220, 60))
    screen.blit(my_image, (player_pos.x - my_image.get_width()/2, player_pos.y - my_image.get_height()/2))
    
    origx = player_pos.x
    origy = player_pos.y
    hitboxx = player_pos.x
    hitboxy = player_pos.y
    hb = 50

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 600 * dt
        img_rotation = 90
        img_flip = False
        hitboxy = player_pos.y - hb


    if keys[pygame.K_s]:
        player_pos.y += 600 * dt
        img_rotation = 270
        img_flip = False
        hitboxy = player_pos.y + hb
        

    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
        img_rotation = 0
        img_flip = True
        hitboxx = player_pos.x - hb
        

    if keys[pygame.K_d]:
        player_pos.x += 600 * dt
        img_rotation = 0
        img_flip = False
        hitboxx = player_pos.x + hb

    if keys[pygame.K_LSHIFT]:
         sprint = 2

    else:
        sprint = 1

    radius = 40
    my_image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)

    pygame.draw.circle(my_image, (0, 0, 255), (radius, radius), radius)

    player_rect = my_image.get_rect(center=(hitboxx, hitboxy))
    # pygame.draw.rect(screen, (0,0,255), player_rect)
    


    if player_rect.colliderect(left_wall):
        #player_rect.left = left_wall.right
        player_pos.x = origx
        # player_pos.y = origy

    if player_rect.colliderect(right_wall):
        #player_rect.right = right_wall.left
        player_pos.x = origx
        # player_pos.y = origy

    if player_rect.colliderect(top_wall):
        #player_rect.top = top_wall.bottom
        # player_pos.x = origx
        player_pos.y = origy

    if player_rect.colliderect(bottom_wall):
        #player_rect.bottom = bottom_wall.top
        # player_pos.x = origx
        player_pos.y = origy
        

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000 * sprint
pygame.quit()