import pygame
import gif_pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
screen.fill("light blue")

dance_gif = gif_pygame.load("animation.gif") 

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    dance_gif.render(screen, (0, 0)) 
    pygame.display.flip()

    pygame.display.flip()

    start_button = pygame.draw.rect(screen, (0, 0, 255), (50, 200, 300, 100))

pygame.quit()