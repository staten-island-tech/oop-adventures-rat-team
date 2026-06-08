
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()


def shop ():
    import gif_pygame
    running = True
    gamerun = False
    import random
    pygame.font.init()
    bg_image = pygame.image.load("shopbg.png")
    bg_image = pygame.transform.scale(bg_image, (1280, 720))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    print("Game Started!")
                    loadtime = pygame.time.get_ticks() // 1000
                    return True
        screen.blit(bg_image, (0, 0))

        exit_font = pygame.font.SysFont('Arial', 30, bold = True) 
        exit_button = pygame.draw.rect(screen, (100, 100, 255), (1200, 10, 50, 50))
        exit_button_text = exit_font.render('X', True, (0, 0, 0))
        screen.blit(exit_button_text, (1215, 18))