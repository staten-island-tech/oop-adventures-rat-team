
import pygame
import random
from loading_screen import starting_screen
from Actual_cats import loadcat
from Actual_rats import *
from adds import pls_wait_30secs
from Shop import shop
import random
 

# print(Actual_cats.__file__)
# print(dir(Actual_cats))

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
dt = 0
sprint = 1
gamerun = False
actualbg_image = pygame.image.load("rat bg.png")

adtime = random.randint(60,100)
loadtime = 0
shop_open = False
img_flip = False
gamerun = False
adrun = False

cat_rotation = [0]
cat_flip = [False]
cat_flip[0] = False
cat_animations = ["attack1", "attack2", "attack3", "attack4", "attack5", "attack6", "hurt1", "hurt2", "hurt3", "hurt4", "stand", "walk1", "walk2", "walk3", "walk4", "walk5", "walk6"]
cat_walks = ["walk1", "walk2", "walk3", "walk4", "walk5", "walk6"]
# animation = 0
cat_walk = [0]
cat_walk[0] = 0
cat_standing = [True]
cat_walking = False
cat_animate = 1
cat_visible = False
cat_stand_maybe = 1
walk_break = [0]
walk_break[0] = 0
walk_break_check = False
break_speed = False
rscreen = pygame.display.set_mode((1280, 720))
rat_visible = True
rat_walks = ["rwalk1", "rwalk2", "rwalk3", "rwalk4", "rwalk5"]
rat_verticals = ['rwalkv1', 'rwalkv2', 'rwalkv3', 'rwalkv4', 'rwalkv5', 'rwalkv6']
rat_vertical = [0]
rat_vertical[0] = 0
rat_standing = [True]
rbreak_speed = False
rat_walk = [0]
rwalk_break = [0]
img_rotation = 0
img_flip = False
rat_is_vertical = [False]

rhealth =100

player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)
cat_pos = pygame.Vector2(screen.get_width() / 30, screen.get_height() / 2)


while running:

    time = pygame.time.get_ticks() // 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if gamerun == False:
        starting_screen()
        loadtime = time
        gamerun = True
    if shop_open == True :
        print("Shop Opened")
        shop()
    
    if gamerun == True: # and shop_open == False:
        screen.fill("light blue")
    

        screen.fill("light blue")
        screen.blit(actualbg_image, (0, 0))

        loadrat(rscreen, rat_visible, player_pos, rat_walks, rat_standing, rbreak_speed, rat_walk, rwalk_break, img_rotation, img_flip, rat_verticals, rat_vertical, rat_is_vertical)
        loadcat(screen, cat_visible, cat_pos, cat_walks, cat_walk, cat_rotation, cat_standing, cat_flip, player_pos, break_speed, walk_break)
        # print(cat_walk)
        cat_keys = pygame.key.get_pressed()

        if cat_keys[pygame.K_e]:
            cat_visible = True

        left_wall = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 60, 900))
        right_wall = pygame.draw.rect(screen, (0, 0, 0), (1220, 0, 60, 900))
        top_wall = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1220, 60))
        bottom_wall = pygame.draw.rect(screen, (0, 0, 0), (0, 660, 1220, 60))
        # screen.blit(my_image, (player_pos.x - my_image.get_width()/2, player_pos.y - my_image.get_height()/2))

        
        # =pygame.draw.circle(screen, "red", player_pos, 40)
        left_wall = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 60, 900))
        right_wall = pygame.draw.rect(screen, (0, 0, 0), (1220, 0, 60, 900))
        top_wall = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1220, 60))
        bottom_wall = pygame.draw.rect(screen, (0, 0, 0), (0, 660, 1220, 60))
        # screen.blit(my_image, (player_pos.x - my_image.get_width()/2, player_pos.y - my_image.get_height()/2))

        attack_font = pygame.font.SysFont('Arial', 30, bold = True) 
        attack_text = attack_font.render('Press "K" to Attack', True, (255, 255, 255))
        screen.blit(attack_text, (1000, 10))

        if rhealth == 100:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 300, 10))

        if rhealth == 90:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 270, 10))

        if rhealth == 80:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 240, 10))
        
        if rhealth == 70:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 210, 10))
        
        if rhealth == 60:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 180, 10))
        
        if rhealth == 50:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 150, 10))

        if rhealth == 40:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 120, 10))

        if rhealth == 30:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 90, 10))
        
        if rhealth == 20:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 60, 10))

        if rhealth == 10:
            health_bar = pygame.draw.rect(screen, (255, 0, 0), (60, 10, 30, 10))


        origx = player_pos.x
        origy = player_pos.y
        hitboxx = player_pos.x
        hitboxy = player_pos.y
        hb = 60

        # shop_font = pygame.font.SysFont('Arial', 30, bold = True) 
        # shop_button = pygame.draw.rect(screen, (100, 100, 255), (1150, 10, 100, 50))
        # shop_button_text = shop_font.render('Shop', True, (0, 0, 0))
        # screen.blit(shop_button_text, (1167, 18))

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if shop_button.collidepoint(event.pos):
        #         shop_open = True
                

        print (time-loadtime, adtime)
        if time - loadtime == adtime:
            pls_wait_30secs()
            loadtime = pygame.time.get_ticks() // 1000
            adtime = random.randint(60,100)
            print('check works')
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 600 * dt
            img_rotation = 90
            img_flip = False
            hitboxy = player_pos.y - hb +30


        if keys[pygame.K_s]:
            player_pos.y += 600 * dt
            img_rotation = 270
            img_flip = True
            hitboxy = player_pos.y + hb
            

        if keys[pygame.K_a]:
            player_pos.x -= 600 * dt
            img_rotation = 0
            img_flip = True
            hitboxx = player_pos.x - hb -20
            

        if keys[pygame.K_d]:
            player_pos.x += 600 * dt
            img_rotation = 0
            img_flip = False
            hitboxx = player_pos.x + hb -40

        if keys[pygame.K_LSHIFT]:
            sprint = 2

        if keys[pygame.K_k]:
            rhealth -=10

        else:
            sprint = 1

        radius = 40
        rat_walk_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)

        pygame.draw.circle(rat_walk_surf, (0, 0, 255), (radius, radius), radius)

        player_rect = rat_walk_surf.get_rect(center=(hitboxx+120, hitboxy+60))
        pygame.draw.rect(screen, (0,0,255), player_rect)

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