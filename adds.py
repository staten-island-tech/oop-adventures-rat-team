import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

def pls_wait_30secs():
    import gif_pygame
    dance_gif = gif_pygame.load("rat-dance_gif.gif") 
    running = True
    gamerun = False
    import random
    pygame.font.init()
    ads = ['boogierat.gif', 'hoprat.gif', 'pushuprat.gif', 'rat-dancebackrooms.gif', 'wtf_rat.gif', 'ratating_rat_gif.gif', 'ratmunchy_gif.gif']
    bg_image = pygame.image.load("starting_background.jpg")
    bg_image = pygame.transform.scale(bg_image, (1280, 720))
    ad = ads[random.randint(0,6)]
    ad_file = random.choice(ads)
    ad = gif_pygame.load(ad_file)

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
            screen.fill("white")
            # screen.blit(bg_image, (0, 0))
            ad.render(screen, (300, 265))

            title_font = pygame.font.SysFont('Arial', 40, bold = True) 
            title = title_font.render('your game will resume shortly after this add...', True, (0,0,0))
            screen.blit(title, (250, 10))

            start_font = pygame.font.SysFont('Arial', 30, bold = True) 
            start_button = pygame.draw.rect(screen, (100, 100, 255), (1200, 10, 50, 50))
            start_button_text = start_font.render('X', True, (0, 0, 0))
            screen.blit(start_button_text, (1210, 10))

        if start_button.collidepoint(pygame.mouse.get_pos()):
            # print("Hovering!")
            # removal_button = pygame.draw.rect(screen, (173, 216, 230), (50, 200, 300, 100))
            # screen.blit(bg_image, (0, 0))
            screen.fill('white')
            start_button = pygame.draw.rect(screen, (100, 100, 255), (800, 0, 100, 100))
            ad.render(screen, (300, 265))
            start_button_text = start_font.render('X', True, (0, 0, 0))
            screen.blit(start_button_text, (150, 230))
            screen.blit(title, (250, 10))
            screen.blit(start_button_text, (810, 110))


            

        pygame.display.flip()
