
import pygame
import random
from loading_screen import starting_screen

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
img_rotation = 0
img_flip = False
gamerun = False


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
break_speed = False

player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)
cat_pos = pygame.Vector2(screen.get_width() / 30, screen.get_height() / 2)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if gamerun == False:
        starting_screen()
        gamerun = True
    if gamerun == True:
    

        screen.fill("light blue")

        my_image = pygame.image.load("RatRightSprite.png")
        my_image = pygame.transform.rotate(my_image, img_rotation)
        cat_stand_animation = pygame.image.load(f"stand.png")
        cat_walk_animation = pygame.image.load(f"{cat_walks[cat_walk]}.png")
        cat_stand_animation = pygame.transform.rotate(cat_stand_animation, cat_rotation)
        cat_walk_animation = pygame.transform.rotate(cat_walk_animation, cat_rotation)
        if (cat_flip == True): 
            cat_stand_animation = pygame.transform.flip(cat_stand_animation, True, False)
            cat_walk_animation = pygame.transform.flip(cat_walk_animation, True, False)

        my_image = pygame.image.load("RatRightSprite.png")
        my_image = pygame.transform.rotate(my_image, img_rotation)
        if (img_flip == True): 
            my_image = pygame.transform.flip(my_image, True, False)

        left_wall = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 60, 900))
        right_wall = pygame.draw.rect(screen, (255, 0, 0), (1220, 0, 60, 900))
        top_wall = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 1220, 60))
        bottom_wall = pygame.draw.rect(screen, (255, 0, 0), (0, 660, 1220, 60))
        screen.blit(my_image, (player_pos.x - my_image.get_width()/2, player_pos.y - my_image.get_height()/2))

        

        cat_keys = pygame.key.get_pressed()

        if cat_keys[pygame.K_e]:
            cat_visible = True

        if cat_standing == True and cat_visible == True:
            screen.blit(cat_stand_animation, cat_pos)
        elif cat_visible == True:
            screen.blit(cat_walk_animation, cat_pos)

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


        walk_break_check = False
        if cat_visible == True:
            if break_speed == False:
                break_speed = True
                player_pos.y += 1
                player_pos.y -= 1
            if cat_pos.x < player_pos.x + 1 and cat_pos.x > player_pos.x - 1 and cat_pos.y < player_pos.y + 1 and cat_pos.y > player_pos.y - 1:
                cat_standing = True
            else:
                cat_standing = False
                if cat_pos.x < player_pos.x + 1 and cat_pos.x > player_pos.x - 1:
                    pass
                else:
                    if cat_pos.x < player_pos.x:
                        cat_flip = False
                        if walk_break == 0:
                            if cat_walk != 5:
                                cat_walk += 1
                            else:
                                cat_walk = 0
                        cat_pos.x += 2
                        if walk_break_check == False:
                            if walk_break == 11:
                                walk_break = 0
                                walk_break_check = True
                            else:
                                walk_break += 1
                                walk_break_check = True
                    elif cat_pos.x > player_pos.x:
                        cat_flip = True
                        if walk_break == 0:
                            if cat_walk != 5:
                                cat_walk += 1
                            else:
                                cat_walk = 0
                        cat_pos.x -= 2
                        if walk_break_check == False:
                            if walk_break == 11:
                                walk_break = 0
                                walk_break_check = True
                            else:
                                walk_break += 1
                                walk_break_check = True
                    else:
                        cat_stand_maybe = 1
                if cat_pos.y < player_pos.y + 1 and cat_pos.y > player_pos.y - 1:
                    pass
                else:
                    if cat_pos.y < player_pos.y:
                        if walk_break == 0:
                            if cat_walk != 5:
                                cat_walk += 1
                            else:
                                cat_walk = 0
                        cat_pos.y += 2
                        if walk_break == 11:
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
                        if walk_break_check == False:
                            if walk_break == 11:
                                walk_break = 0
                                walk_break_check = True
                            else:
                                walk_break += 1
                                walk_break_check = True

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000 * sprint
pygame.quit()