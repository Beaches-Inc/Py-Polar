import pygame
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# initialize pygame
pygame.init()
screen_size = (700, 500)
 
# create a window
screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
pygame.display.set_caption("POS")
bgimg = pygame.image.load("images/vectorArt.png").convert_alpha()
bg = pygame.transform.scale(bgimg,screen.get_size())


# clock is used to set a max fps
clock = pygame.time.Clock()
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    #clear the screen
    bg = pygame.transform.scale(bgimg,screen.get_size())
    screen.blit(bg, (0, 0))
    # window.get_size()
 
    # flip() updates the screen to make our changes visible
    pygame.display.flip()
     
    # how many updates per second
    clock.tick(60)
 
pygame.quit()