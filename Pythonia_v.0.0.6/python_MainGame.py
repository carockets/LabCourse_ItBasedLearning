import pygame, sys, time
import subprocess
from Tkinter import *
from pygame.locals import *

pygame.init()

######################
# Setting variables
######################

###########################
# Important Variables. Not necessary for the save/load -process.
# They stay the same at all times.
###########################

# Display
FPS = 30 # Set maximum of 30 Frames per Second. Game pauses in between game-loops so it doesnt run too fast on fast computers.
WINDOWWIDTH = 900
WINDOWHEIGHT = 650
FLAGS = HWSURFACE|DOUBLEBUF
PLAYERSIZE = 50  # Width of character. Height = 2* width.
CAMERASLACK = 0 # How much the player can move before the camera moves with him

# Set key bindings
LEFT = K_LEFT
RIGHT = K_RIGHT
JUMP = K_SPACE
TEXT = K_x
MUSIC = K_m

# X movement--------------
PLAYERACCEL = 3
PLAYERDEACCEL = 5
MAXSPEED = 20

enemySpeedX = 5
enemysize = 50

# Y movement--------------
AIRACCEL = 2
FALLACCEL = 5
JUMPMOD = 3.5  # Controls jumping height.
# Use this variable as an example for the first chapter in the Lessons.

JUMPACCEL = 31
MAXFALLSPEED = 50

BLOCKWIDTH = 100
BLOCKHEIGHT = 100

global coin_counter
coin_counter = 0
playerHP = 3
died_counter = 0

screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), FLAGS)
pygame.display.set_caption('Pythonia - Learning Python')
clock = pygame.time.Clock() # We need this for FPS reduction.
font = pygame.font.SysFont("Calibri", 30) # Font for ingame text
bigfont = pygame.font.SysFont("monospace", 60)


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

myimage_left = loadImage("graphics/left.png")
myimage_right = loadImage("graphics/right.png")
myimage_jump = loadImage("graphics/jump.png")
myimage_stand= loadImage("graphics/stand.png")
myimage_coin = loadImage("graphics/coin.png")
myimage_coinCounter = loadImage("graphics/coins.png")
myimage_flagdown = loadImage("graphics/flag_down.png")
myimage_flagup = loadImage("graphics/flag_up.png")
myimage_kill= loadImage("graphics/barbs.png")
myimage_enemy= loadImage("graphics/enemy.png")
myimage_hp = loadImage("graphics/hp.png")
myimage_heart = loadImage ("graphics/heart.png")

############ COLORSPECTRUM #############
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 150,   0)
LIGHTGREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
PLAYERCOLOR = (0 , 0,0)



############# LEVEL DESIGN #########
BLANK = '.' # No HitBox, Background visible.

BLOCK = '0' # HitBox, Graphic 0
COIN = '3'
FLAGDOWN = '4' # Flags will be down if not yet encountered.
FLAGUP = '5'
KILL = '1' # Barbed wire
HEART = '6' # HP to collect

currentflags = []

global background_image

######### The following variables have to be saved in case of a crash to reload a level! ################
global levelcounter
levelcounter = 1
global level
level = []


level1 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '06.............3...3...3..............0..................00..................................................0',
          '0000.........0000000000011.33..11..3...0.................0.........................3........................60',
          '0..................0..000000000000000..0.................00.......................000....................3.000',
          '0......3..3........0.................00033...............00........................00.0.................000000',
          '0....0000000.......0..3..........3.....033...............00....................3...00.0.3............3..000000',
          '0.....00000000.....000000......0000....0000000...........00...................000..00.0000......3..0000......0',
          '003..............110.3............3.1110000000003........00.......3...3.....000....00..........00............0',
          '000..............000000000..000000000000......0000.......0.......00..00...3........00......00000.............0',
          '00003..............0.3.............3...0........0000.............00..00..000.......00.....000................0',
          '000000.............0000000000000000000.0............4...........3..................0000011...................0',
          '00000000000000000......................0..........3.00..........000......00........0000000...................0',
          '0......3............0003.......3.....3.0..........00000000.....0000...........3....0......................00.0',
          '0..............000000000......0000000000...3...0000000000011111000000011....0000.............3.....3.........0',
          '0113.............3.00000003...............0000000000000000000000000000001111111111111111111100000000004....4.0',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000']


level2 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '0.............................00......000..................................................00................0',
          '0.............................00......0006.................................................00................0',
          '0.........................3...00......00000....3...........................................00................0',
          '0.................3.00000000..00..............0000....................................3....00................0',
          '0................000000.......00.....................3...........................3.110000..00................0',
          '0.........3....0000...........00...................0000.....................3..000000.3....00................0',
          '0.....300000....00............00.........................3...........3......00000..3..000000000000000........0',
          '0..000000000....00..3......0000..........................00...............0000.....00000000........00000.....0',
          '01..............0000011....00............................00..................00.3....3...3......3.....00000000',
          '000................000011...3........................3..........3..00000......0000000000000000000............0',
          '0000...00000..........0000000000....................000.........0000..........000000000000000000000.3........0',
          '0.....000000.3..3........3....00....3.....3.....3.00000.......00..........00000000000000000000000000000......0',
          '0....0000000000000...........300...000...000....000000......00......3.....0000000000000000000000000000000....0',
          '0.3......3......60....3.....3.001110001110001111000000....4.00111111....0000000000000000000000000000000000.4.0',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]


level3 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '0000000000000000000000000000000000000000000000...300000000000000000000000000000000000000000000000....3...00000',
          '000000000000000000000000000000000000000000....3...0000000000000000000000000000000000000000000.......000..00000',
          '000000000000000000000000000000000000003......000..00000000000000000000000000000000..........3.0000000000.3...0',
          '0000000000000000000000000000000003......00000000..000000000000000000000000000000.3..........000000000000000..0',
          '000000000000000000000000000........000000000000...00000000000000000000000000........00000000000000000000000..0',
          '000............000000000...3.0000000000000...3....00000000000000000000000........0000000000000000000000..3...0',
          '000.3...........0000.....000000000000000....00000.000000000000000000......3..0000000000000000000000000..000000',
          '000................3.0000000000000000.....00000011000000000000000.........0000000000000000000000000000..000000',
          '00011.........30000000000000000......3.0000000000000000000000000.........00000000000000000000000000000.......0',
          '000000000000000000000000000..3...000000000000000000000000000000......11.300000000000000000000000000000.3...4.0',
          '000000000000000000000000000..000000000000000000000000000000......3.0000000000000000000000000000000000000000000',
          '00000000000000000000000...3..0000000..........00000.3.000...00000000000000000000000000000000000000000000000000',
          '0000000000000000000......0000000000.....3......0.........3..00000000000000000000000000000000000000000000000000',
          '0000000000000000000..4.....3...........11...6.....00...0000000000000000000000000000000000000000000000000000000',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]


level4 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '0.............................00000...6........................000000000000..............00000000............0',
          '0.............................00000000000.........................0000000..................000000..........4.0',
          '0.......................3.00..00000003..00...3......................0000..............3........00.....3..00000',
          '0.......................0000...0000003...000.00......................00..............................000000000',
          '0...................3.000000........00....00.00.00.3.................00.........................3.000000000000',
          '0................3.000000000..3.....000.........00.00................00..........3.000000000..0000000000000000',
          '0.............3.0000000000000.......000000000......00.................0.........000000000000..0000000000000000',
          '0............000000000000000001.....000000000.........3...3..................0000000000000001100.............0',
          '0111111....00000000000........0003................0000000000.............3.0000000000....0000000.............0',
          '00000000000000000000...3....3....00..........00..........000...........0000000000000.....0000000.............0',
          '00000000000000000.....000..000......3......3..............0003....3.000000000000000..........................0',
          '0000000000000000......000110000000000...00000000....00....000011.0000000000000000000.........................0',
          '0.......0000000......000000000.....03...00000000....00....0000000000.........................................0',
          '0.......0000.3...........3.........6.111............00...........00000.......................................0',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]


level5 = ['00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
          '0............000..........................00......................................................000........0',
          '0............000..........................00.....................................................3000........0',
          '0............000.........................600.....................................................0000........0',
          '0.3..........000.....................3..0000......................................3.....3.....000000.........0',
          '0000.........000..................3.00..0000.................................3..000000000000..00.............0',
          '000000.......000.................00.00.....................................000000000..........00.............0',
          '0........3.................3...0000......................................00000000...........3.00.............0',
          '0.......0000.........3...0000............3.......3.........3......3..000000000......3..000000000.............0',
          '0111....0000........000.................000..00..00.......000...00000000000000.....000000....................0',
          '00000.3.........3.0000................00000..00..0000............000000000000......00............3...........0',
          '00000000........0000.............................000000....3.......00000000..................3..00...3.......0',
          '0000.......3......00............3.000......................00......00000000.........3.......00..00..00.......0',
          '00.......00000..............3...0000000..3...............000000................000000000.......3...........4.0',
          '00.3..0000000000.....3......0000000000000011111111110000000000000003........0000000000000001111000011110000000',
          '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',]




# sets all variables needed for the gamewindow
def prepare_level(level_counter):
    global levelcounter
    global LEVELHEIGHT
    global LEVELWIDTH
    global listenemy0
    global listenemy1
    global listenemy2
    global listenemies

    global map_coin_Preparation
    global listdyinglists
    global map_hearts_Preparation
    global map_flags_Preparation
    global listcoinlists
    global remaining_coins
    global listhearts
    global remaining_hearts
    global listflags
    global remaining_flags

    global player
    global myimage_wall
    global myimage_wall2
    global background_image

    levelcounter = level_counter



    if levelcounter == 1:
        LEVELWIDTH = len(level1[0])
        LEVELHEIGHT = len(level1)
# Blockwidth, Blockheight, dir(boolean - left for true), enemy_movement, enemy_movementMAX, speed, coord. in the array
        listenemy0 = [14,10,False,0,250,2,0]
        listenemy1 = [8,4,False,0,300,2,1]
        listenemy2 = [28,2,False,0,250,2,2]
        listenemies = [listenemy0, listenemy1, listenemy2]
        player = pygame.Rect(10*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_gras.png")
        myimage_wall2 = loadImage("graphics/brick_gras2.png")
        background_image = loadImage("graphics/background1.png")
    elif levelcounter == 2:
        LEVELWIDTH = len(level2[0])
        LEVELHEIGHT = len(level2)
        listenemies = []
        player = pygame.Rect(8*BLOCKWIDTH, 10*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_beach.png")
        myimage_wall2 = loadImage("graphics/brick_beach2.png")
        background_image = loadImage("graphics/background2.png")
    elif levelcounter == 3:
        LEVELWIDTH = len(level3[0])
        LEVELHEIGHT = len(level3)
        listenemies = []
        player = pygame.Rect(12*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_hill.png")
        myimage_wall2 = loadImage("graphics/brick_hill2.png")
        background_image3 = loadImage("graphics/background3.png")
    elif levelcounter == 4:
        LEVELWIDTH = len(level4[0])
        LEVELHEIGHT = len(level4)
        listenemies = []
        player = pygame.Rect(8*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_snow.png")
        myimage_wall2 = loadImage("graphics/brick_snow2.png")
        background_image = loadImage("graphics/background4.png")
    elif levelcounter == 5:
        LEVELWIDTH = len(level5[0])
        LEVELHEIGHT = len(level5)
        listenemies = []
        player = pygame.Rect(10*BLOCKWIDTH, 9*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_desert.png")
        myimage_wall2 = loadImage("graphics/brick_desert2.png")
        background_image = loadImage("graphics/background5.png")
    else:
        levelcounter = 5
        LEVELWIDTH = len(level5[0])
        LEVELHEIGHT = len(level5)
        listenemies = []
        player = pygame.Rect(6*BLOCKWIDTH, 13*BLOCKHEIGHT, PLAYERSIZE, PLAYERSIZE*2)
        myimage_wall = loadImage("graphics/brick_desert.png")
        myimage_wall2 = loadImage("graphics/brick_desert2.png")
        background_image = loadImage("graphics/background5.png")


# Prepare Coin for collecting....
# Prepare barbs for dying....
# Prepare hearts for collecting....
# Prepare flags for running into....
    if levelcounter == 1:
        map_coin_Preparation = setcoins(level1)
        listdyinglists = setbarbs(level1)
        map_hearts_Preparation = sethearts(level1)
        map_flags_Preparation = setflags(level1)
    elif levelcounter == 2:
        map_coin_Preparation = setcoins(level2)
        listdyinglists = setbarbs(level2)
        map_hearts_Preparation = sethearts(level2)
        map_flags_Preparation = setflags(level2)
    elif levelcounter == 3:
        map_coin_Preparation = setcoins(level3)
        listdyinglists = setbarbs(level3)
        map_hearts_Preparation = sethearts(level3)
        map_flags_Preparation = setflags(level3)
    elif levelcounter == 4:
        map_coin_Preparation = setcoins(level4)
        listdyinglists = setbarbs(level4)
        map_hearts_Preparation = sethearts(level4)
        map_flags_Preparation = setflags(level4)
    elif levelcounter == 5:
        map_coin_Preparation = setcoins(level5)
        listdyinglists = setbarbs(level5)
        map_hearts_Preparation = sethearts(level5)
        map_flags_Preparation = setflags(level5)
    else:
        map_coin_Preparation = setcoins(level5)
        listdyinglists = setbarbs(level5)
        map_hearts_Preparation = sethearts(level5)
        map_flags_Preparation = setflags(level5)


    print levelcounter
    listcoinlists = map_coin_Preparation[0]
    remaining_coins = map_coin_Preparation[1]

    listhearts = map_hearts_Preparation[0]
    remaining_hearts = map_hearts_Preparation[1]

    listflags = map_flags_Preparation[0]
    remaining_flags = map_flags_Preparation[1]



# Prepare coins
def setcoins(map_array):
    listofcoins = []
    remaining = []
    coin_coordinates = find_elem_in_2d_coordinates('3', map_array )
    for c in coin_coordinates:
        x = c[1]
        y = c[0]
        y = range (y*100, y*100+101)
        x = range (x*100-25, x*100+35)
        stringx = str(c[0])
        stringy = str (c[1])
        ges = stringx + "," + stringy
        remaining.append(ges)
        listofcoins.append( (x, y, (c[0],c[1]))  )
    return (listofcoins, remaining)

# Prepare hearts
def setbarbs(map_array):
    listhearts = []
    barb_coordinates = find_elem_in_2d_coordinates('1', map_array )
    for c in barb_coordinates:
        x = c[1]
        y = c[0]
        y = range (y*100+50 , y*100+101)
        x = range (x*100-40, x*100+100)
        listhearts.append( (x, y, (c[0],c[1])))
    return listhearts


def sethearts(map_array):
    listofhearts = []
    remaining_hearts = []
    heart_coordinates = find_elem_in_2d_coordinates('6', map_array )
    for c in heart_coordinates:
        x = c[1]
        y = c[0]
        y = range (y*100, y*100+101)
        x = range (x*100-25, x*100+35)
        stringx = str(c[0])
        stringy = str (c[1])
        ges = stringx + "," + stringy
        remaining_hearts.append(ges)
        listofhearts.append( (x, y, (c[0],c[1]))  )

    return (listofhearts, remaining_hearts)

def setflags(map_array):
    listofflags = []
    remaining_flags = []
    heart_coordinates = find_elem_in_2d_coordinates('4', map_array )
    heart_coordinates.sort(key=lambda tup: tup[1])


    i = 0
    for c in heart_coordinates:
        y = range (c[0]*100, c[0]*100+101)
        x = range (c[1]*100, c[1]*100+100)
        remaining_flags.append( (c[0], c[1]) )
        listofflags.append((x, y, (c[0],c[1]), i))
        i += 1
    # range, range, coordinate, whether opened or not
    return (listofflags, remaining_flags)




def find_elem_in_2d_coordinates(elem, list2D ):
    lss = list(enumerate(list2D))
    ls = []
    result = []
    for a in lss:
        if elem in a[1]:
            ls.append((a[0], list(enumerate(a[1]))))
    for c in ls:
        for d in c[1]:
            if d[1] == elem:
                result.append((c[0],d[0]))

    return result


def textobject (text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


######## Render a button with variable parameters ######
def button(msg, x, y ,w, h, ic, ac, action=None):
    global Music_paused
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x +  w > mouse[0]  > x and y + w > mouse[1] > y: # Mouse coordinates checking.
         pygame.draw.rect(screen , ac, (x,y,w,h) ) # mouse is over button (active color)
         if click[0] == 1 and action != None: # Left click
             if action == "music": # only one button implementet yet - music.
                                   # For  further buttons implement more actions.
                 if Music_paused == False:
                     pygame.mixer.music.pause()
                     Music_paused = True
                 elif Music_paused == True:
                     pygame.mixer.music.unpause()
                     Music_paused = False

    else: # Mouse is not over button, button should still be visible. (in-active color)
         pygame.draw.rect(screen , ic, (x,y,w,h) )

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = textobject(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

# Changes flag-image (down => up) (if part == "4")
# Deletes coin-images (else Part)
def change_graphic(x,y):
    global Music_paused
    global coin_counter
    global playerHP
    global remaining_hearts
    global remaining_coins
    global levelcounter
    global level1
    global level2
    global level3
    global level4
    global level5

    if levelcounter == 1:
        level = level1
    elif levelcounter == 2:
        level = level2
    elif levelcounter == 3:
        level = level3
    elif levelcounter == 4:
        level = level4
    elif levelcounter == 5:
        level = level5
    else:
        level = level5



    test = ("%r,%r" % (x,y))
    if test in remaining_coins:
        remaining_coins.remove(test)
        st1 =  level[x]
        st2 = st1[0:y]
        #if level[x][y] == '4':
        #    st3 = st2 + '5'
        #    level[x] = st3 + st1[y+1:len(level[0])]
        #    # Get Variable from other window whether or not Coding was successful, then give coins.
        #    coin_counter += 10
        if level[x][y] == '3':
            st3 = st2 + "."
            level[x] = st3 + st1[y+1:len(level[0])]
            coin_counter += 1
            if Music_paused == True:
                1+1
            else:
                sound_coin.play()

    intX = int(x)
    intY = int(y)
    flagtest = (intX,intY)
    if flagtest in remaining_flags:
        remaining_flags.remove(flagtest)
        st1 =  level[x]
        st2 = st1[0:y]
        if level[x][y] == '4':
            st3 = st2 + '5'
            level[x] = st3 + st1[y+1:len(level[0])]
            # Get Variable from other window whether or not Coding was successful, then give coins.
            coin_counter += 10

    if test in remaining_hearts:
        remaining_hearts.remove(test)
        st1 = level[x]
        st2 = st1[0:y]
        if level[x][y] == '6':
            st3 = st2 + '.'
            level[x] = st3 + st1[y+1:len(level[0])]
            if playerHP ==3:
                playerHP += 0
            else:
                playerHP += 1


# Collision detection with coins, flags, hearts and enemies.
def listcoins(playerleft, playerbottom):
    global listcoinlists
    global listflag1

    # Detection of coins
    for x in listcoinlists:
        if playerleft in x[0]:
            if playerbottom in x[1]:
                return x[2]

    # Detection of flags
    for x in listflags:
        if playerleft in x[0]:
            if playerbottom in x[1]:
                if x[2] in remaining_flags:
                        currentflags.append(x[3])
                        return x[2]

    # Detection of hearts
    for x in listhearts:
        if playerleft in x[0]:
            if playerbottom in x[1]:
                return x[2]

    # detection of enemies
    for y in listdyinglists:
        if playerleft in y[0]:
            if playerbottom in y[1]:
                dying()


    else:
        return (0,0)


# So we dont have to write 4 functions every time we want to display text.
def drawText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def convertPixelToLevel(x, y): # Pixel
    for levelX in range(LEVELWIDTH):
        for levelY in range(LEVELHEIGHT):
            tempRect = pygame.Rect(levelX * BLOCKWIDTH, levelY * BLOCKHEIGHT, BLOCKWIDTH, BLOCKHEIGHT)
            if tempRect.collidepoint(x, y):
                return (levelX, levelY)

# Collision detection
# Calculating the distance between player and the nearest wall on X / Y
# If player is faster than the distance, move by distance instead.
def calculateDistance(coord, lines, dir):
    distances = []
    global levelcounter
    global level1
    global level2
    global level3
    global level4
    global level5
    global level

    if levelcounter == 1:
        level = level1
    elif levelcounter == 2:
        level = level2
    elif levelcounter == 3:
        level = level3
    elif levelcounter == 4:
        level = level4
    elif levelcounter == 5:
        level = level5
    else:
        level = level5

    for line in lines:
        # Which blocks are scanned are dependent on which direction the player is moving in.
        if dir == 'left':
            playerX = convertPixelToLevel(coord, 0)[0]
            for levelX in range(playerX, -1, -1):
                if level[line][levelX] == BLOCK: # HitBox, Player can't move through there.
                    distances.append(levelX * BLOCKWIDTH + BLOCKWIDTH - coord)
        elif dir == 'right':
            playerX = convertPixelToLevel(coord, 0)[0]
            for levelX in range(playerX, LEVELWIDTH, 1):
                if level[line][levelX] == BLOCK: # HitBox, Player can't move through there.
                    distances.append(levelX * BLOCKWIDTH - coord)

        if dir == 'up':
            playerY = convertPixelToLevel(0, coord)[1]
            for levelY in range(playerY, -1, -1):
                if level[levelY][line] == BLOCK: # HitBox, Player can't move through there.
                    distances.append(levelY * BLOCKHEIGHT + BLOCKHEIGHT - coord)
        elif dir == 'down':
            playerY = convertPixelToLevel(0, coord)[1]
            for levelY in range(playerY, LEVELHEIGHT, 1):
                if level[levelY][line] == BLOCK:  # HitBox, Player can't move through there.
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


def gameprint(text,xx,yy,color,textsize=40, font=pygame.font.get_default_font()):
   font = pygame.font.SysFont(font,textsize)
   ren = font.render(text,1,color)
   screen.blit(ren, (xx,yy))

def dying():
    global player
    global playerHP
    global died_counter

    drawText('YOU DIED!', bigfont, RED, screen, 300, 300)
    pygame.display.flip()
    pygame.display.update()
    pygame.time.delay(1200)
    player = pygame.Rect(10*BLOCKWIDTH, 12*BLOCKHEIGHT - 300, PLAYERSIZE, PLAYERSIZE*2) # Startposition of the player

    #Reset Player HP
    playerHP = 3
    died_counter += 1



def enemymove(xblock, yblock, en_dir_L, enemy_mov, enemy_movementMAX, speed, coord):

    if enemy_mov == enemy_movementMAX:
        listenemies[coord][2]= False # save direction of enemy in its list
        en_dir_L = False # change direction for this method
    if enemy_mov == 0:
        listenemies[coord][2] = True
        en_dir_L = True

    if en_dir_L == True:
        listenemies[coord][3] += speed # save speed of enemy in its list
    if en_dir_L == False:
        listenemies[coord][3] -= speed # save speed of enemy in its list

    if en_dir_L == True:
        screen.blit(myimage_enemy, ((xblock*BLOCKWIDTH)-camerax-enemy_mov, (yblock*BLOCKHEIGHT)-cameray, BLOCKWIDTH, BLOCKHEIGHT))
    else:
        screen.blit(myimage_enemy, ((xblock*BLOCKWIDTH)-camerax-enemy_mov, (yblock*BLOCKHEIGHT)-cameray, BLOCKWIDTH, BLOCKHEIGHT))


# Communication with the second Window over a textfile. Ugly and not programmer style but... HEY IT WORKS! :D
def start_communication(number):
    comm_file = open("communication_file.txt","w") # create new file
    comm_file.write(str(number)+"\nrunning")
    comm_file.close()

def check_communication():
    comm_file = open("communication_file.txt","r")
    communication = [x.strip('\n') for x in comm_file.readlines()]
    comm_file.close()
    if communication != []:
        if communication[1] == "running":
        # Stop time for a second each round (30 FPS usually), does not stop Game completely (lead to a crash usually)
            time.sleep(1)
    if communication == "":
        pass


global player
player = pygame.Rect(10*BLOCKWIDTH, 12*BLOCKHEIGHT - 300, PLAYERSIZE, PLAYERSIZE*2) # Startposition of the player

# Acceleration, Speed along the X/Y axis and Jumping. Set to zero/false at the beginning => No movement.
accelX = 0
playerSpeedX = 0
playerSpeedY = 0
jumping = False
camerax = player.centerx-(WINDOWWIDTH/2)
cameray = player.centery-(WINDOWHEIGHT/2)
showText = True # Set True if additional text is to be shown (coordinates etc)
showText2 = True # Set True for Coin Counter and HP to be shown
# Music Mixer Variable. False if music in On.
Music_paused = False
# Sounds
sound_coin = pygame.mixer.Sound("sounds/coin.wav") # collecting coin
sound_coin.set_volume(0.2) # set low volume
sound_flag = pygame.mixer.Sound("sounds/flag.wav") # reaching flag
sound_flag.set_volume(0.2) # set low volume
# Fixes the bug that game starts with 1FPS if game crashes without resetting the file
comm_file = open("communication_file.txt","w") # create new file
comm_file.write("")
comm_file.close()


#-------------------------------------------------------------
# Initializing
#-------------------------------------------------------------

# Background music
pygame.mixer.music.load('sounds/bgSound1.ogg')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0) # play in an endless loop
# Load level x
prepare_level(1)


#-------------------------------------------------------------
# THE GAME LOOP
#-------------------------------------------------------------

while True:
    check_communication()
############## Key Input Handling / Events #############

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
                jumping = False # Player keeps jumping until spacebar is not pressed anymore.
            if event.key == TEXT:
                showText = not showText
            if event.key == MUSIC:
                if Music_paused == False:
                    pygame.mixer.music.pause()
                    Music_paused = True
                else:
                    pygame.mixer.music.unpause()
                    Music_paused = False





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

    # The player moves over several rows when he runs.
    # We want to find out which ones we have to check for HitBoxes. (== BLOCK)
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
            playerSpeedY = -1
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
    # The active area makes sure only blocks that are shown on screen are rendered

    activeArea = pygame.Rect(camerax-BLOCKWIDTH, cameray-BLOCKHEIGHT, WINDOWWIDTH+(200), WINDOWHEIGHT+(200))
    #activeArea = pygame.Rect(0,0, len(level[0])*BLOCKWIDTH, len(level)*BLOCKHEIGHT)


    screen.blit(background_image, [0, 0])

    for y in range(LEVELHEIGHT):
        for x in range(LEVELWIDTH):
            if activeArea.collidepoint((x*BLOCKWIDTH), (y*BLOCKHEIGHT)):
                if level[y][x] == BLANK:
                    continue
                if level[y][x] == HEART:
                    screen.blit(myimage_heart, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level[y][x] == KILL:
                    screen.blit(myimage_kill, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level [y][x] == COIN:
                    screen.blit(myimage_coin, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level [y][x] == FLAGDOWN:
                    screen.blit(myimage_flagdown, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level [y][x] == FLAGUP:
                    screen.blit(myimage_flagup, ((x*BLOCKWIDTH)-camerax, (y*BLOCKHEIGHT)- cameray, BLOCKWIDTH, BLOCKHEIGHT))
                if level[y][x] == BLOCK:
                    if level[y-1][x] == BLOCK:
                        screen.blit (myimage_wall2, ((x*BLOCKWIDTH) - camerax, (y*BLOCKHEIGHT) - cameray, BLOCKWIDTH, BLOCKHEIGHT))
                    else:
                        screen.blit (myimage_wall, ((x*BLOCKWIDTH) - camerax, (y*BLOCKHEIGHT) - cameray, BLOCKWIDTH, BLOCKHEIGHT))

    #Enemy Movmeent
    for x in listenemies:
        enemymove(x[0],x[1],x[2],x[3],x[4],x[5],x[6])

    # Character movement -  images being drawn
    if Xkeys[RIGHT] < Xkeys[LEFT]:
        screen.blit(myimage_left, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    elif Xkeys[LEFT] < Xkeys[RIGHT]:
        screen.blit(myimage_right, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    elif jumping == True:
        screen.blit(myimage_jump, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    else:
        screen.blit(myimage_stand, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))

# Button Rendering #
    if Music_paused == True:
        button("Music off", 810,0,90,30 ,GREEN, LIGHTGREEN , "music")
    else:
        button("Music on", 810,0,90,30 ,GREEN, LIGHTGREEN , "music")

    coinTuple =  listcoins (player.left, player.bottom)
    if isinstance(coinTuple, tuple):
        if coinTuple != (0,0):
            change_graphic(coinTuple[0],coinTuple[1])

    # Collision detection of all enemies in the list
    for x in listenemies:
    # Left side collision detection with an enemy:
        if (player.left - camerax) in range ((x[0]*BLOCKWIDTH)-camerax-x[3], (x[0]*BLOCKWIDTH)-camerax-x[3]+50):
            if (player.top - cameray) in range ((x[1]*BLOCKHEIGHT)-cameray-100,(x[1]*BLOCKHEIGHT)-cameray+100):
                playerHP -= 1
                if playerHP == 0:
                    dying()
                else:
                    player.left +=150

    # Right side collision detection with an enemy:
        if (player.right - camerax) in range ((x[0]*BLOCKWIDTH)-camerax-x[3], (x[0]*BLOCKWIDTH)-camerax-x[3]+50):
            if (player.top - cameray) in range ((x[1]*BLOCKHEIGHT)-cameray-100,(x[1]*BLOCKHEIGHT)-cameray+100 ):
                playerHP -= 1
                if playerHP == 0:
                    dying()
                else:
                    player.left -= 150

    if currentflags != []:
        if remaining_flags != []:
            process = subprocess.Popen(["python","python_tk_text.py"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=False, bufsize= 0)
            start_communication(currentflags[0])
            currentflags.remove(currentflags[0])
        else:
            currentflags.remove(currentflags[0])
            levelcounter+=1
            prepare_level(levelcounter)

    screen.blit(myimage_coinCounter, pygame.rect.Rect(0,0, 100,38 ))
    drawText('%r' %(coin_counter), font, WHITE, screen, 80, 5)

    if playerHP == 1:
        screen.blit(myimage_hp, pygame.rect.Rect(150,0, 37,33 ))
    if playerHP == 2:
        screen.blit(myimage_hp, pygame.rect.Rect(150,0, 37,33 ))
        screen.blit(myimage_hp, pygame.rect.Rect(200,0, 37,33 ))
    if playerHP == 3:
        screen.blit(myimage_hp, pygame.rect.Rect(150,0, 37,33 ))
        screen.blit(myimage_hp, pygame.rect.Rect(200,0, 37,33 ))
        screen.blit(myimage_hp, pygame.rect.Rect(250,0, 37,33 ))

    pygame.display.flip()
    clock.tick(FPS)











