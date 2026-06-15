import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

def starting_screen():
    import gif_pygame
    dance_gif = gif_pygame.load("rat-dance_gif.gif") 
    running = True
    gamerun = False
    pygame.font.init()
    bg_image = pygame.image.load("starting_background.jpg")
    bg_image = pygame.transform.scale(bg_image, (1280, 720))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    print("Game Started!")
                    gamerun = True
                    return True

        if gamerun == False:
            screen.fill("light blue")
            screen.blit(bg_image, (0, 0))
            dance_gif.render(screen, (780, 265))

            title_font = pygame.font.SysFont('Arial', 60, bold = True) 
            title = title_font.render('Fast and Furriest', True, (255,255,255))
            screen.blit(title, (420, 10))

            start_font = pygame.font.SysFont('Arial', 30, bold = True) 
            start_button = pygame.draw.rect(screen, (100, 100, 255), (50, 200, 300, 100))
            start_button_text = start_font.render('START', True, (255, 255, 255))
            screen.blit(start_button_text, (150, 230))

        if start_button.collidepoint(pygame.mouse.get_pos()):
            # print("Hovering!")
            # removal_button = pygame.draw.rect(screen, (173, 216, 230), (50, 200, 300, 100))
            screen.blit(bg_image, (0, 0))
            start_button = pygame.draw.rect(screen, (140, 140, 255), (55, 205, 290, 90))
            dance_gif.render(screen, (780, 265))
            start_button_text = start_font.render('START', True, (0, 0, 0))
            screen.blit(start_button_text, (150, 230))
            screen.blit(title, (500, 10))
            screen.blit(start_button_text, (150, 230))


            

        pygame.display.flip()
