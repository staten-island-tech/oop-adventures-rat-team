
def loadcat(screen, cat_visible, cat_pos, cat_walks, cat_walk, cat_rotation, cat_standing, cat_flip, player_pos, break_speed, walk_break, chealth, rattack_rect, current_time, attack_cooldown, last_attack_time, ckilled, cat_facing, player_rect, rhealth, cat_attack_cooldown, cat_last_attack_time):
    import pygame
    cat_stand_animation = pygame.image.load(f"cat_images\stand.png")
    cat_walk_animation = pygame.image.load(f"cat_images\{cat_walks[cat_walk[0]]}.png")
    cat_stand_animation = pygame.transform.rotate(cat_stand_animation, cat_rotation[0])
    cat_walk_animation = pygame.transform.rotate(cat_walk_animation, cat_rotation[0])
    dx = player_pos.x - cat_pos.x
    dy = player_pos.y - cat_pos.y

    cat_keys = pygame.key.get_pressed()

    chitboxx = cat_pos.x
    chitboxy = cat_pos.y

    if cat_keys[pygame.K_e]:
        cat_visible[0] = True

    if cat_flip[0] == True:
        cat_stand_animation = pygame.transform.flip(cat_stand_animation, True, False)
        cat_walk_animation = pygame.transform.flip(cat_walk_animation, True, False)

    if cat_standing[0] == True and cat_visible == True:
        screen.blit(cat_stand_animation, cat_pos)
    elif cat_visible[0] == True:
        screen.blit(cat_walk_animation, cat_pos)

    walk_break_check = False
    if cat_visible[0] == True:
        if break_speed == False:
            break_speed = True
            player_pos.y += 1
            player_pos.y -= 1
        if cat_pos.x < player_pos.x + 1 and cat_pos.x > player_pos.x - 1 and cat_pos.y < player_pos.y + 1 and cat_pos.y > player_pos.y - 1:
            cat_standing[0] = True
        else:
            cat_standing[0] = False
            if cat_pos.x < player_pos.x + 1 and cat_pos.x > player_pos.x - 1:
                pass
            else:
                if cat_pos.x < player_pos.x:
                    cat_flip[0] = False
                    if walk_break[0] == 0:
                        if cat_walk[0] != 5:
                            cat_walk[0] += 1
                        else:
                            cat_walk[0] = 0
                    cat_pos.x += 2
                    if walk_break_check == False:
                        if walk_break[0] == 11:
                            walk_break[0] = 0
                            walk_break_check = True
                        else:
                            walk_break[0] += 1
                            walk_break_check = True
                elif cat_pos.x > player_pos.x:
                    cat_flip[0] = True
                    if walk_break[0] == 0:
                        if cat_walk[0] != 5:
                            cat_walk[0] += 1
                        else:
                            cat_walk[0] = 0
                    cat_pos.x -= 2
                    if walk_break_check == False:
                        if walk_break[0] == 11:
                            walk_break[0] = 0
                            walk_break_check = True
                        else:
                            walk_break[0] += 1
                            walk_break_check = True
                else:
                    cat_stand_maybe = 1
            if cat_pos.y < player_pos.y + 1 and cat_pos.y > player_pos.y - 1:
                pass
            else:
                if cat_pos.y < player_pos.y:
                    if walk_break[0] == 0:
                        if cat_walk[0] != 5:
                            cat_walk[0] += 1
                        else:
                            cat_walk[0] = 0
                    cat_pos.y += 2
                    if walk_break[0] == 11:
                        walk_break[0] = 0
                    else:
                        if walk_break_check == False:
                            walk_break[0] += 1
                            walk_break_check = True

                elif cat_pos.y > player_pos.y:
                    if walk_break[0] == 0:
                        if cat_walk[0] != 5:
                            cat_walk[0] += 1
                        else:
                            cat_walk[0] = 0
                    cat_pos.y -= 2
                    if walk_break_check == False:
                        if walk_break[0] == 11:
                            walk_break[0] = 0
                            walk_break_check = True
                        else:
                            walk_break[0] += 1
                            walk_break_check = True


        radius = 45
        cat_walk_surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)

        pygame.draw.circle(cat_walk_surf, (0, 0, 255), (radius, radius), radius)

        cat_rect = cat_walk_surf.get_rect(center=(chitboxx+110, chitboxy+120))

        cat_attack_rect = cat_walk_surf.get_rect()

        if cat_keys[pygame.K_k]:
            # print(rattack_rect)
            # print(cat_rect)
            if rattack_rect.colliderect(cat_rect):
                # print (current_time - last_attack_time[0])
                if current_time - last_attack_time[0] >= attack_cooldown:
                    chealth[0] -= 10
                    last_attack_time[0] = current_time
                    print ('hit')
                    print (chealth)

        if chealth[0] == 50:
            chealth_bar = pygame.draw.rect(screen, (0, 0, 255), (60, 680, 150, 10))

        if chealth[0] == 40:
            chealth_bar = pygame.draw.rect(screen, (0, 0, 255), (60, 680, 120, 10))

        if chealth[0] == 30:
            chealth_bar = pygame.draw.rect(screen, (0, 0, 255), (60, 680, 90, 10))
        
        if chealth[0] == 20:
            chealth_bar = pygame.draw.rect(screen, (0, 0, 255), (60, 680, 60, 10))

        if chealth[0] == 10:
            chealth_bar = pygame.draw.rect(screen, (0, 0, 255), (60, 680, 30, 10))

        if chealth[0] == 0:
            print ('died')
            cat_visible[0] = False
            ckilled[0] += 1
            print (ckilled)


        if abs(dx) > abs(dy):
            if dx > 0:
                cat_facing[0] = "right"
            else:
                cat_facing[0] = "left"
        else:
            if dy > 0:
                cat_facing[0] = "down"
            else:
                cat_facing[0] = "up"

        if cat_facing[0] == "right":
            cat_attack_rect.midleft = (cat_rect.right + 10, cat_rect.centery)

        elif cat_facing[0] == "left":
            cat_attack_rect.midright = (cat_rect.left - 10, cat_rect.centery)

        elif cat_facing[0] == "up":
            cat_attack_rect.midbottom = (cat_rect.centerx, cat_rect.top - 10)

        elif cat_facing[0] == "down":
            cat_attack_rect.midtop = (cat_rect.centerx, cat_rect.bottom + 10)

        if cat_attack_rect.colliderect(player_rect):
            if current_time - cat_last_attack_time[0] >= cat_attack_cooldown:
                rhealth[0] -= 10
                cat_last_attack_time[0] = current_time

        if cat_keys[pygame.K_p]:
            pygame.draw.rect(screen, (0, 255, 0), rattack_rect)
            pygame.draw.rect(screen, (255,0,0), cat_rect)
            pygame.draw.rect(screen, 'yellow', cat_attack_rect)
            pygame.draw.rect(screen, (0,0,255), player_rect)

        # cat_rect = my_image.get_rect(center=(hitboxx, hitboxy))

        # if cat_rect.colliderect(left_wall):
        #     player_pos.x = origx

        # if cat_rect.colliderect(right_wall):
        #     player_pos.x = origx

        # if cat_rect.colliderect(top_wall):
        #     player_pos.y = origy

        # if cat_rect.colliderect(bottom_wall):
        #     player_pos.y = origy

