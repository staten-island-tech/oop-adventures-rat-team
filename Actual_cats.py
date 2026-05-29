
def loadcat(screen, cat_visible, cat_pos, cat_walks, cat_walk, cat_rotation, cat_standing, cat_flip, player_pos, break_speed, walk_break):
    import pygame
    cat_stand_animation = pygame.image.load(f"cat_images\stand.png")
    cat_walk_animation = pygame.image.load(f"cat_images\{cat_walks[cat_walk[0]]}.png")
    cat_stand_animation = pygame.transform.rotate(cat_stand_animation, cat_rotation)
    cat_walk_animation = pygame.transform.rotate(cat_walk_animation, cat_rotation)
    
    cat_keys = pygame.key.get_pressed()

    if cat_keys[pygame.K_e]:
        cat_visible = True

    if cat_standing == True and cat_visible == True:
        screen.blit(cat_stand_animation, cat_pos)
    elif cat_visible == True:
        screen.blit(cat_walk_animation, cat_pos)

    if (cat_flip == True): 
        cat_stand_animation = pygame.transform.flip(cat_stand_animation, True, False)
        cat_walk_animation = pygame.transform.flip(cat_walk_animation, True, False)

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
                        if cat_walk[0] != 5:
                            cat_walk[0] += 1
                        else:
                            cat_walk[0] = 0
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
                        if cat_walk[0] != 5:
                            cat_walk[0] += 1
                        else:
                            cat_walk[0] = 0
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
                        if cat_walk[0] != 5:
                            cat_walk[0] += 1
                        else:
                            cat_walk[0] = 0
                    cat_pos.y += 2
                    if walk_break == 11:
                        walk_break = 0
                    else:
                        if walk_break_check == False:
                            walk_break += 1
                            walk_break_check = True

                elif cat_pos.y > player_pos.y:
                    if walk_break == 0:
                        if cat_walk[0] != 5:
                            cat_walk[0] += 1
                        else:
                            cat_walk[0] = 0
                    cat_pos.y -= 2
                    if walk_break_check == False:
                        if walk_break == 11:
                            walk_break = 0
                            walk_break_check = True
                        else:
                            walk_break += 1
                            walk_break_check = True

