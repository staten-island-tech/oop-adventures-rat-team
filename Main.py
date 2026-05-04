import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 1

player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("light blue")
    my_image = pygame.image.load("RatRightSprite.png")

    # pygame.draw.circle(screen, "red", player_pos, 40)
    screen.blit(my_image, player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 600 * dt
    if keys[pygame.K_s]:
        player_pos.y += 600 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt 
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt 

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()