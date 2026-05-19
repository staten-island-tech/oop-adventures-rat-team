import pygame
import gif_pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pygame.font.init()
gamerune = False

dance_gif = gif_pygame.load("rat-dance_gif.gif") 

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                print("Button clicked!")
                gamerune = True
            
    screen.fill("light blue")
    dance_gif.render(screen, (800, 200))

    title_font = pygame.font.SysFont('Arial', 60, bold = True) 
    title = title_font.render('RAT RUNNER', True, (0,0,0))
    screen.blit(title, (500, 10))

    start_font = pygame.font.SysFont('Arial', 30, bold = True) 
    start_button = pygame.draw.rect(screen, (100, 100, 255), (50, 200, 300, 100))
    start_button_text = start_font.render('START', True, (255, 255, 255))
    screen.blit(start_button_text, (150, 230))

        

    pygame.display.flip()

    

pygame.quit()