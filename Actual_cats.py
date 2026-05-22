
def loadcat(cat_walks, cat_walk, cat_rotation):
    cat_stand_animation = pygame.image.load(f"stand.png")
    cat_walk_animation = pygame.image.load(f"{cat_walks[cat_walk]}.png")
    cat_stand_animation = pygame.transform.rotate(cat_stand_animation, cat_rotation)
    cat_walk_animation = pygame.transform.rotate(cat_walk_animation, cat_rotation)