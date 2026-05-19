import pygame
import gif_pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.font.init()

dance_gif = gif_pygame.load("rat-dance_gif.gif") 

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("light blue")
    dance_gif.render(screen, (800, 200)) 
    converted_gif = dance_gif.convert_alpha()
    resized_gif = pygame.transform.smoothscale(converted_gif, (800, 200))
    screen.blit(resized_gif, (800, 2000))
    start_button = pygame.draw.rect(screen, (100, 100, 255), (50, 200, 300, 100))
    my_font = pygame.font.SysFont('Arial', 30, bold = True) 
    start_button = my_font.render('START', True, (255, 255, 255))
    screen.blit(start_button, (150, 230))

    pygame.display.flip()

    

pygame.quit()