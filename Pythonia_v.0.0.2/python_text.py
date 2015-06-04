
import pygame, sys, time
from pygame.locals import *
pygame.init()


# Display stuff-----------
WINDOWWIDTH = 800
WINDOWHEIGHT = 600


display = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Pythonia - Lets learn Python!')
clock = pygame.time.Clock()
font = pygame.font.SysFont("Calibri", 30)

background = pygame.image.load('textbsp.png')



#-------  R    G    B  ----------------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
LIGHTGREEN = (  0, 150,   0)
BLUE  = (  0,   0, 255)
PLAYERCOLOR = (0 , 0,0)



########## INITIALIZE ##############
#sound_flag = pygame.mixer.Sound("flag.wav")
#sound_flag.set_volume(0.2)

#sound_flag.play()


########## GAME LOOP ################

while True:

    pygame.draw.rect(display, WHITE, (0, 0, 250, 800))
    pygame.draw.rect(display, BLACK, (250, 0, 550, 800))

    for event in pygame.event.get():
        if event.type == QUIT or\
        (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

   # display.blit(background, [0, 0])

    pygame.display.update()