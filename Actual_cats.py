
def loadcat(screen, cat_visible, cat_pos, cat_walks, cat_walk, cat_rotation, cat_standing, cat_flip):
    import pygame
    cat_stand_animation = pygame.image.load(f"cat_images\stand.png")
    cat_walk_animation = pygame.image.load(f"cat_images\{cat_walks[cat_walk]}.png")
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

