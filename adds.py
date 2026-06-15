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
    ads = ['boogierat (1).gif', 'hoprat.gif', 'pushuprat (1).gif', 'rat-dancebackrooms (1).gif', 'wtf_rat.gif', 'ratating_rat_gif.gif', 'ratmunchy_gif (1).gif', 'wobbly-wiggly_rat.gif']
    bg_image = pygame.image.load("starting_background.jpg")
    bg_image = pygame.transform.scale(bg_image, (1280, 720))
    adnumber = random.randint(0,7)
    print(adnumber)
    ad = ads[adnumber]
    ad_file = random.choice(ads)
    ad = gif_pygame.load(f"rat_ads/{ad_file}")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    print("Game Started!")
                    return True

        if gamerun == False:
            screen.fill("white")
            # screen.blit(bg_image, (0, 0))
            ad.render(screen, (350, 100))

            title_font = pygame.font.SysFont('Arial', 40, bold = True) 
            title = title_font.render('your game will resume shortly after this ad...', True, (0,0,0))
            screen.blit(title, (250, 10))

            start_font = pygame.font.SysFont('Arial', 30, bold = True) 
            start_button = pygame.draw.rect(screen, (100, 100, 255), (1200, 10, 50, 50))
            start_button_text = start_font.render('X', True, (0, 0, 0))
            screen.blit(start_button_text, (1215, 18))

        if start_button.collidepoint(pygame.mouse.get_pos()):
            # print("Hovering!")
            # removal_button = pygame.draw.rect(screen, (173, 216, 230), (50, 200, 300, 100))
            # screen.blit(bg_image, (0, 0))
            screen.fill('white')
            start_button = pygame.draw.rect(screen, (150, 150, 255), (1202, 12, 45, 45))
            ad.render(screen, (350, 100))
            start_button_text = start_font.render('X', True, (0, 0, 0))
            screen.blit(title, (250, 10))
            screen.blit(start_button_text, (1215, 18))


            

        pygame.display.flip()
