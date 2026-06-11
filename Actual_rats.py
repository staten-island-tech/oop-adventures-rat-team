
def loadrat(rscreen, rat_visible, player_pos, rat_walks, rat_standing, rbreak_speed, rat_walk, rwalk_break, img_rotation, img_flip, rat_verticals, rat_vertical, rat_is_vertical):
    import pygame


    rat_stand_animation = pygame.image.load(f"rat_images\pstand.png")
    rat_walk_animation = pygame.image.load(f"rat_images\{rat_walks[rat_walk[0]]}.png")
    rat_stand_animation = pygame.transform.rotate(rat_stand_animation, img_rotation)
    rat_walk_animation = pygame.transform.rotate(rat_walk_animation, img_rotation)
    vrat_stand_animation = pygame.image.load(f"rat_images\pstandv.png")
    vrat_walk_animation = pygame.image.load(f"rat_images\{rat_verticals[rat_vertical[0]]}.png")
    
    rat_visible = True

   

    if img_flip == True:
        rat_stand_animation = pygame.transform.flip(rat_stand_animation, True, False)
        rat_walk_animation = pygame.transform.flip(rat_walk_animation, True, False)
        vrat_stand_animation = pygame.transform.flip(vrat_stand_animation, False, True)
        vrat_walk_animation = pygame.transform.flip(vrat_walk_animation, False, True)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_s]:
        rat_is_vertical[0] = True
    elif keys[pygame.K_a] or keys[pygame.K_d]:
        rat_is_vertical[0] = False

    if rat_standing[0] == True and rat_visible == True and rat_is_vertical[0] == False:
        rscreen.blit(rat_stand_animation, player_pos)
    if rat_visible == True and rat_is_vertical[0] == False and rat_standing[0] == False:
        rscreen.blit(rat_walk_animation, player_pos)
    if rat_standing[0] == True and rat_visible == True and rat_is_vertical[0] == True:
         print("vertical stand")
         rscreen.blit(vrat_stand_animation, player_pos)
    if rat_visible == True and rat_is_vertical[0] == True and rat_standing[0] == False:
         print("vertical walk")
         rscreen.blit(vrat_walk_animation, player_pos)

    rwalk_break_check = False
    if rat_visible == True:
        if rbreak_speed == False:
            rbreak_speed = True
            player_pos.y += 1
            player_pos.y -= 1
        if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
            rat_standing[0] = True
        else:
            rat_standing[0] = False
            if keys[pygame.K_d]:
                    img_flip = False
                    if rwalk_break[0] == 0:
                        if rat_walk[0] != 4:
                            rat_walk[0] += 1
                        else:
                            rat_walk[0] = 0
                        rat_vertical[0] = rat_walk[0]
                    if rwalk_break_check == False:
                        if rwalk_break[0] == 11:
                            rwalk_break[0] = 0
                            rwalk_break_check = True
                        else:
                            rwalk_break[0] += 1
                            rwalk_break_check = True
                            
            elif keys[pygame.K_a]:
                    img_flip = True
                    if rwalk_break[0] == 0:
                        if rat_walk[0] != 4:
                            rat_walk[0] += 1
                        else:
                            rat_walk[0] = 0
                        rat_vertical[0] = rat_walk[0]
                    if rwalk_break_check == False:
                        if rwalk_break[0] == 11:
                            rwalk_break[0] = 0
                            rwalk_break_check = True
                        else:
                            rwalk_break[0] += 1
                            rwalk_break_check = True
 #           else:
#                    rat_stand_maybe = 1
            elif keys[pygame.K_s]:
                    img_flip = True
                    print (rat_walk[0])
                    if rwalk_break[0] == 0:
                        if rat_vertical[0] != 4:
                            rat_vertical[0] += 1
                        else:
                            rat_vertical[0] = 0
                        rat_walk[0] = rat_vertical[0]
                    if rwalk_break[0] == 11:
                        rwalk_break[0] = 0
                    else:
                        if rwalk_break_check == False:
                            rwalk_break[0] += 1
                            rwalk_break_check = True

            elif keys[pygame.K_w]:
                    img_flip = False
                    print (rat_walk[0])
                    if rwalk_break[0] == 0:
                        if rat_vertical[0] != 4:
                            rat_vertical[0] += 1
                        else:
                            rat_vertical[0] = 0
                        rat_walk[0] = rat_vertical[0]
                    if rwalk_break_check == False:
                        if rwalk_break[0] == 11:
                            rwalk_break[0] = 0
                            rwalk_break_check = True
                        else:
                            rwalk_break[0] += 1
                            rwalk_break_check = True

        # cat_rect = my_image.get_rect(center=(hitboxx, hitboxy))

        # if cat_rect.colliderect(left_wall):
        #     player_pos.x = origx

        # if cat_rect.colliderect(right_wall):
        #     player_pos.x = origx

        # if cat_rect.colliderect(top_wall):
        #     player_pos.y = origy

        # if cat_rect.colliderect(bottom_wall):
        #     player_pos.y = origy

