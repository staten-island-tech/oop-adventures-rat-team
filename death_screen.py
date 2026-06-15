import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

def death_screen(ckilled):
    import gif_pygame
    dance_gif = gif_pygame.load("rat-dance_gif.gif") 
    running = True
    gamerun = False
    pygame.font.init()
    # bg_image = pygame.image.load("starting_background.jpg")
    # bg_image = pygame.transform.scale(bg_image, (1280, 720))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    print("Game Started!")
                    gamerun = True
                    sys.exit()
                    return True
                
        screen.fill("light blue")
        dance_gif.render(screen, (780, 265))

        title_font = pygame.font.SysFont('Arial', 60, bold = True) 
        title = title_font.render('You died lolz', True, (0,0,0))
        count_font = pygame.font.SysFont('Arial', 40, bold = True) 
        count = count_font.render(f"You killed {ckilled} cats", True, (0,0,0))

        start_font = pygame.font.SysFont('Arial', 30, bold = True) 
        start_button = pygame.draw.rect(screen, (100, 100, 255), (480, 480, 200, 60))
        start_button_text = start_font.render('Exit Game', True, (255, 255, 255))
        screen.blit(start_button_text, (510, 495))
        screen.blit(title, (500, 10))
        screen.blit(count, (100, 200))
            
        pygame.display.flip()
