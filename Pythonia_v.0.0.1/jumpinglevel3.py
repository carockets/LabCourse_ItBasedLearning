"""
    My final test (not really) for 2D platformer movement.
    Here we have collision detection, smooth accelerated movement,
    seperate world and window coordinates, and camera movement.
    
    Some code and variable names here was totally ripped off from
    Al Sweigart in his book "Making Games With Python & Pygame". You
    should totally read it if you're new to Pygame.

    -Deiphiz
"""

import pygame, sys, time
from pygame.locals import *
pygame.init()


#-------------------------------------------------------------
# Set constant variables
#-------------------------------------------------------------

# Display stuff-----------
FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
FLAGS = HWSURFACE|DOUBLEBUF
PLAYERSIZE = 50
CAMERASLACK = 0 # How much the player can move before the camera moves with him

# Bindings----------------
LEFT = K_LEFT
RIGHT = K_RIGHT
JUMP = K_SPACE
TEXT = K_x
ORANGE = K_t

# X movement--------------
PLAYERACCEL = 3
PLAYERDEACCEL = 5
MAXSPEED = 20

# Y movement--------------
AIRACCEL = 2
FALLACCEL = 5
JUMPMOD = 3.5 # How much we subtract from the fall acceleration while jumping (helps to control the jump height)
JUMPACCEL = 31
MAXFALLSPEED = 50

#-------  R    G    B  ----------------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
PLAYERCOLOR = (0 , 255, 0)

# Setting up the level-----------------
BLANK = '.'
BLOCK = '0'
BLOCK2 = '2'
EVENT = '1'
NOHITBOX = '3'

level = ['00000000000000000000',
         '0..................0',
         '0000............0000',
         '0..................0',
         '0..................0',
         '0....0000000.......0',
         '0..00000000000.....0',
         '0..................0',
         '0................000',
         '0000...........3...0',
         '0..............33..0',
         '0......0000000000..0',
         '0..................0',
         '00000.....33...00000',
         '0.........33.......0',
         '00000000000000000000']
LEVELWIDTH = len(level[0])
LEVELHEIGHT = len(level)
BLOCKWIDTH = 100
BLOCKHEIGHT = 100

graphiclevel = ['00000000000000000000',
                '2..................2',
                '2000............0002',
                '2..................2',
                '2..................2',
                '2....0000000.......2',
                '2..00222222200.....2',
                '2..................2',
                '2................002',
                '2000...........3...2',
                '2..............33..2',
                '2......0000000000..2',
                '2..................2',
                '20000.....33...00002',
                '2.........33.......2',
                '20000000000000000002']

#-------------------------------------------------------------
# Define functions
#-------------------------------------------------------------

# Einbinden von Bildern
def loadImage(filename, colorkey=None):
    # Pygame das Bild laden lassen.
    image = pygame.image.load(filename)

    # Das Pixelformat der Surface an den Bildschirm (genauer: die screen-Surface) anpassen.
    # Dabei die passende Funktion verwenden, je nach dem, ob wir ein Bild mit Alpha-Kanal haben oder nicht.
    if image.get_alpha() is None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    # Die Farbe Magenta (r,g,b) = (255, 0, 255) wird ausgelassen waehrend des Rendering => "runde" Figuren moeglich
    colorkey = (255, 0, 255)
    image.set_colorkey(colorkey, pygame.RLEACCEL)

    return image


# This function is ripped off from Al Sweigart
def drawText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def convertPixelToLevel(x, y):
    for levelX in range(LEVELWIDTH):
        for levelY in range(LEVELHEIGHT):
            tempRect = pygame.Rect(levelX * BLOCKWIDTH, levelY * BLOCKHEIGHT, BLOCKWIDTH, BLOCKHEIGHT)
            if tempRect.collidepoint(x, y):
                return (levelX, levelY)

# This function is the key to the collision detection algorithm.
# Basically, it calculates the distance between the "front" side of the player
# and the nearest obstacle on either the X axis or the Y axis.
#    
# If that distance is shorter than the current speed of the player, then move by
# that distance instead.
def calculateDistance(coord, lines, dir):
    distances = []
    for line in lines:

        # Which blocks are scanned are dependent on which direction the player is moving in.
        if dir == 'left':
            playerX = convertPixelToLevel(coord, 0)[0]
            for levelX in range(playerX, -1, -1):
                if level[line][levelX] == BLOCK:
                    distances.append(levelX * BLOCKWIDTH + BLOCKWIDTH - coord)
        elif dir == 'right':
            playerX = convertPixelToLevel(coord, 0)[0]
            for levelX in range(playerX, LEVELWIDTH, 1):
                if level[line][levelX] == BLOCK:
                    distances.append(levelX * BLOCKWIDTH - coord)

        if dir == 'up':
            playerY = convertPixelToLevel(0, coord)[1]
            for levelY in range(playerY, -1, -1):
                if level[levelY][line] == BLOCK:
                    distances.append(levelY * BLOCKHEIGHT + BLOCKHEIGHT - coord)
        elif dir == 'down':
            playerY = convertPixelToLevel(0, coord)[1]
            for levelY in range(playerY, LEVELHEIGHT, 1):
                if level[levelY][line] == BLOCK:
                    distances.append(levelY * BLOCKHEIGHT - coord)

    # The function should return the shortest or longest distance 
    # out of the lines which were checked depending on which 
    # direction the player was moving in.
    if dir == 'left' or dir == 'up':
        desiredValue = -100000
    if dir == 'right' or dir == 'down':
        desiredValue = 100000
    for value in distances:
        if dir == 'left' or dir == 'up':
            if value > desiredValue:
                desiredValue = value
        elif dir == 'right' or dir == 'down':
            if value < desiredValue:
                desiredValue = value
    return desiredValue


#-------------------------------------------------------------
# Set in-game variables
#-------------------------------------------------------------
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), FLAGS)
pygame.display.set_caption('Pythonia - Learning Python')
clock = pygame.time.Clock()
#font = pygame.font.SysFont("monospace", 30)
player = pygame.Rect(10*BLOCKWIDTH, 12*BLOCKHEIGHT - 300, PLAYERSIZE, PLAYERSIZE*2)
imagerect = pygame.Rect(10*BLOCKWIDTH, 12*BLOCKHEIGHT - 300, PLAYERSIZE, PLAYERSIZE*2)

myimage_left = loadImage("left.png")
myimage_right = loadImage("right.png")
myimage_jump = loadImage("jump.png")
myimage_stand= loadImage("stand.png")
myimage_orange = loadImage("orange.png")
myimage_wall = loadImage("wall.png")
myimage_wall2 = loadImage("wall2.png")
myimage_nothitbox = loadImage("coin.png")


accelX = 0
playerSpeedX = 0
playerSpeedY = 0
jumping = False

camerax = player.centerx-(WINDOWWIDTH/2)
cameray = player.centery-(WINDOWHEIGHT/2)

showText = True # To toggle whether OSD is shown or not

background_image = loadImage("back.png")
#-------------------------------------------------------------
# THE GAME LOOP
#-------------------------------------------------------------
while True:

#///////////////////////Event Point Test //////////////////////#
#FAILED
    listXAxis = range (1090,1195)
    listYAxis = range(700,600)

    listCamXAxis = range (180,210)
    listCamYAxis = range (465,200)
    if camerax in listCamXAxis and cameray in listCamYAxis:
        jumping = True

#///////////////////////Event handling///////////////////////#
    for event in pygame.event.get():
        if event.type == QUIT or\
        (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == JUMP and not jumping:
                jumping = True
        if event.type == KEYUP:
            if event.key == JUMP:
                jumping = False
            if event.key == TEXT:
                showText = not showText



    Xkeys = pygame.key.get_pressed()

    if not jumping:
        accelX = (Xkeys[RIGHT] - Xkeys[LEFT]) * PLAYERACCEL
    elif jumping:
        accelX = (Xkeys[RIGHT] - Xkeys[LEFT]) * AIRACCEL



#///////////////////////X-axis movement///////////////////////#

    # Accelerate the player towards the maximum speed
    if accelX != 0:
        if playerSpeedX <= MAXSPEED and playerSpeedX >= -MAXSPEED:
            playerSpeedX += accelX
            if playerSpeedX > MAXSPEED:
                playerSpeedX = MAXSPEED
            if playerSpeedX < -MAXSPEED:
                playerSpeedX = -MAXSPEED

    # Deaccelerate the player when no keys are pressed
    if accelX == 0:
        if playerSpeedX > 0:
            playerSpeedX -= PLAYERDEACCEL
            if playerSpeedX < 0:
                playerSpeedX = 0
        if playerSpeedX < 0:
            playerSpeedX += PLAYERDEACCEL
            if playerSpeedX > 0:
                playerSpeedX = 0

    # The player will intersect multiple rows while moving.
    # Here we check which rows those are to pass to the calculateDistance() function.
    rowsToCheck = []
    for y in range(LEVELHEIGHT):
        if player.colliderect(pygame.Rect(0, y*BLOCKHEIGHT, LEVELWIDTH*BLOCKWIDTH, BLOCKHEIGHT)):
            rowsToCheck.append(y)

    # The calculateDistance() function needs to know which way the player is moving
    if playerSpeedX < 0:
        minXDistance = calculateDistance(player.left, rowsToCheck, 'left')
    elif playerSpeedX > 0:
        minXDistance = calculateDistance(player.right, rowsToCheck, 'right')
    else:
        minXDistance = 0

    # If minumum X distance is shorter than the player's deltaX,
    # move the player by that distance instead.
    if playerSpeedX < 0:
        if minXDistance > playerSpeedX:
            player.left += minXDistance
            playerSpeedX = 0
        else:
            player.left += playerSpeedX
    elif playerSpeedX > 0:
        if minXDistance < playerSpeedX:
            player.left += minXDistance
            playerSpeedX = 0
        else:
            player.left += playerSpeedX


#///////////////////////Y-axis movement///////////////////////#

    # Unfortunately, this causes the player to jump indefintely
    # if JUMPACCEL is divisible by FALLACCEL
    if jumping and playerSpeedY == 0:
        playerSpeedY -= JUMPACCEL

    # Gravity is decreased while jumping so the player can control
    # the height of his jump.
    # Another problem is the player may have a slight window of time 
    # to double jump if the JUMPACCEL is divisible by FALLACCEL - JUMPMOD
    if jumping:
        playerSpeedY += FALLACCEL - JUMPMOD
    else:
        playerSpeedY += FALLACCEL

    # Simulate terminal velocity
    if playerSpeedY > MAXFALLSPEED:
        playerSpeedY = MAXFALLSPEED

    # The collision detection code here works exactly like the X axis
    columnsToCheck = []
    for x in range(LEVELWIDTH):
        if player.colliderect(pygame.Rect(x*BLOCKWIDTH, 0, BLOCKWIDTH, LEVELHEIGHT*BLOCKHEIGHT)):
            columnsToCheck.append(x)

    if playerSpeedY < 0:
        minYDistance = calculateDistance(player.top, columnsToCheck, 'up')
    elif playerSpeedY > 0:
        minYDistance = calculateDistance(player.bottom, columnsToCheck, 'down')
    else:
        minYDistance = 0

    if playerSpeedY < 0:
        if minYDistance > playerSpeedY:
            player.bottom += minYDistance
            #jumping = False
            playerSpeedY = -1 # This is my attempt at combatting the indefinite jump problem
        else:
            player.bottom += playerSpeedY
    elif playerSpeedY > 0:
        if minYDistance < playerSpeedY:
            player.bottom += minYDistance
            playerSpeedY = 0
        else:
            player.bottom += playerSpeedY



#///////////////////////Camera Movement///////////////////////#

    # This code was ripped off from Al Sweigart. 
    # Basically, this sets up a small area the player can move
    # around the screen before the camera starts moving along with him
    if (camerax + WINDOWWIDTH/2) - player.centerx > CAMERASLACK:
        camerax = player.centerx + CAMERASLACK - WINDOWWIDTH/2
    elif player.centerx - (camerax + WINDOWWIDTH/2) > CAMERASLACK:
        camerax = player.centerx - CAMERASLACK - WINDOWWIDTH/2
    if (cameray + WINDOWHEIGHT/2) - player.centery > CAMERASLACK:
        cameray = player.centery + CAMERASLACK - WINDOWHEIGHT/2
    elif player.centery - (cameray + WINDOWHEIGHT/2) > CAMERASLACK:
        cameray = player.centery - CAMERASLACK - WINDOWHEIGHT/2
    # Uncomment below to have the camera always locked to the player
    # camerax, cameray = player.centerx-(WINDOWWIDTH/2), player.centery-(WINDOWHEIGHT/2)

    # This keeps the camera within the boundaries of the level
    cameraRect = pygame.Rect(camerax, cameray, WINDOWWIDTH, WINDOWHEIGHT)
    if cameraRect.right > LEVELWIDTH*BLOCKWIDTH:
        camerax = (LEVELWIDTH*BLOCKWIDTH)-WINDOWWIDTH
    elif cameraRect.left < 0:
        camerax = 0
    if cameraRect.top < 0:
        cameray = 0
    elif cameraRect.bottom > LEVELHEIGHT*BLOCKHEIGHT:
        cameray = (LEVELHEIGHT*BLOCKHEIGHT)-WINDOWHEIGHT


#///////////////////////Rendering///////////////////////#

    # Rendering involves a little conversion of level coordinates to window coordinates
    #screen.fill(BLACK)
    # Set a background image instead of the black background
    screen.blit(background_image, [0, 0])

    # draw a rectangle shape
    # rect(Surface, color, Rect, width=0) -> Rect
    # width = 0 => rectangle is filled.
    pygame.draw.rect(screen, PLAYERCOLOR, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2), 2)

    # The active area makes sure only blocks that are shown on screen are rendered
    activeArea = pygame.Rect(camerax-BLOCKWIDTH, cameray-BLOCKHEIGHT, WINDOWWIDTH+(BLOCKWIDTH*2), WINDOWHEIGHT+(BLOCKHEIGHT*2))
    for y in range(LEVELHEIGHT):
        for x in range(LEVELWIDTH):
            if activeArea.collidepoint((x*BLOCKWIDTH), (y*BLOCKHEIGHT)):
                if level[y][x] == BLANK:
                    continue
                if level [y][x] == NOHITBOX:
                    screen.blit(myimage_nothitbox, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level[y][x] == BLOCK:
                    if graphiclevel[y][x] == BLOCK2:
                        screen.blit (myimage_wall2, ((x*BLOCKWIDTH) - camerax, (y*BLOCKHEIGHT) - cameray, BLOCKWIDTH, BLOCKHEIGHT))
                    else:
                        screen.blit (myimage_wall, ((x*BLOCKWIDTH) - camerax, (y*BLOCKHEIGHT) - cameray, BLOCKWIDTH, BLOCKHEIGHT))



    #if showText:
        # Customise the OSD here. This was the information I found the most useful.
        #drawText('BoxL: %r BoxR: %r BoxU: %r BoxD: %r' %(player.left, player.right, player.top, player.bottom), font, WHITE, screen, 10, 0)
        #drawText('Jumping: %r CameraX: %r CameraY: %r' %(jumping, camerax, cameray), font, WHITE, screen, 10, 30)
        #drawText('deltaX: %r deltaY: %r' %(playerSpeedX, playerSpeedY), font, WHITE, screen, 10, 60)
        #drawText('minX: %r minY: %r' %(minXDistance, minYDistance), font, WHITE, screen, 10, 90)

    # Character movement -  images being drawn
    if Xkeys[RIGHT] < Xkeys[LEFT]:
        screen.blit(myimage_left, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    elif Xkeys[LEFT] < Xkeys[RIGHT]:
        screen.blit(myimage_right, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    elif jumping == True:
        screen.blit(myimage_jump, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    else:
        screen.blit(myimage_stand, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)


################### ADDITIONAL CODE #######################






