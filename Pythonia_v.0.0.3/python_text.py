
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



def loadImage(filename, colorkey=None):
    # Pygame das Bild laden lassen.
    image
    image = image.load(filename)

    # Das Pixelformat der Surface an den Bildschirm (genauer: die screen-Surface) anpassen.
    # Dabei die passende Funktion verwenden, je nach dem, ob wir ein Bild mit Alpha-Kanal haben oder nicht.
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    # Die Farbe Magenta (r,g,b) = (255, 0, 255) wird ausgelassen waehrend des Rendering => "runde" Figuren moeglich
    image.set_colorkey(colorkey, RLEACCEL)

    return image


myimage_enemy=  image.load("enemy.png")


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

    screen.blit(myimage_enemy, (800,1100))

    pygame.display.update()