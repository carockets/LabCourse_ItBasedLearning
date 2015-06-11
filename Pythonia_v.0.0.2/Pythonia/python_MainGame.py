import pygame, sys, time
import subprocess
from Tkinter import *
from pygame.locals import *
pygame.init()



###########################
# Important Variables. Not necessary for the save/load -process.
# They stay the same at all times.
###########################

# Display
FPS = 30 # Set maximum of 30 Frames per Second. Game pauses in between game-loops so it doesnt run too fast on fast computers.
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
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
BLOCK2 = '2'
# ""HitBox"" - Graphic 2 is drawn  (using 'graphiclevel') over Graphic 0 to use its Hitbox.
# (No Object-inheritance, too complicated to implement further stand-alone-hitboxes at the moment. Mayber later)
# Costs only a little more ressources this way.

COIN = '3'
FLAGDOWN = '4' # Flags will be down if not yet encountered.
FLAGUP = '5'
KILL = '1' # Barbed wire
HEART = '6' # HP to collect


# Variable for the first flag. Becomes true when player in flag area.
player_in_flag1 = False # Must not be saved, as 2 variables control the new window opening.


######### The following variables have to be saved!! ################


# Coins/flags only have to be marked in this array.
global level
level = ['00000000000000000000',
         '04.............6...0',
         '0000.........0000000',
         '0..................0',
         '0.....6............0',
         '0....0000000.......0',
         '0.....00000000.....0',
         '00.................0',
         '000..............000',
         '00000..........3...0',
         '000000.........33..0',
         '00000000000000000..0',
         '0..................0',
         '00000.....33...00000',
         '011.......33.......0',
         '00000000000000000000']




# Only the 2nd wall images have to be marked in this array.
graphiclevel = ['22222222222222222222',
                '2..................2',
                '2000.........0000002',
                '2..................2',
                '2..................2',
                '2....0000000.......2',
                '2.....22222200.....2',
                '20.................2',
                '220..............002',
                '22200..............2',
                '222220.............2',
                '22222200000000000..2',
                '2..................2',
                '20000..........00002',
                '2..................2',
                '20000000000000000002']


LEVELWIDTH = len(level[0])
LEVELHEIGHT = len(level)
BLOCKWIDTH = 100
BLOCKHEIGHT = 100



# listcoin = [Range of Y-Axis, Range of X-Axis ]
# Example: 10,15
# X = 15 => 1475 bis 1535
# Y = 10 => 1000 bis 1101
# listcoin = [range ( ), range ( ) ]


#15 => 1475, 1535
#10 = 1000,1100

# "Hitboxes" for the Coins / Flags. Maybe make them smaller. Less effort for the gameloop when checking.
listcoin0 = [range(1475,1535), range(900,1001), (9,15)]     # 9,15
listcoin1 = [range(1475,1535), range(1000,1101), (10,15)]    # 10,15
listcoin2 = [range(1575,1635), range(1000,1101) ,(10,16)]    # 10,16
listcoin3 = [range (975,1035) , range (1300,1401), (13,10)]  # 13.10
listcoin4 = [range (1075,1135) , range (1300,1401), (13,11)] # 13,11
listcoin5 = [range (975,1035) , range (1400,1501) , (14,10)]  # 14,10
listcoin6 = [range (1075,1135) , range (1400,1501), (14,11)] # 14,11
listcoinlists = [listcoin0, listcoin1, listcoin2, listcoin3, listcoin4, listcoin5, listcoin6]
remaining_coins = ['9,15','10,15','10,16','13,10','13,11','14,10','14,11', '1,1' ]

# Blockwidth, Blockheight, dir(boolean - left for true), enemy_movement, enemy_movementMAX, speed, coord. in the array
listenemy0 = [14,10,False,0,250,2,0]
listenemy1 = [8,4,False,0,300,2,1]
listenemies = [listenemy0, listenemy1]
remaining_hearts = ['4,6','1,15']

# Hitboxes of HP Hearts
listheart0 = [range (600,700), range(400,501), (4,6)] #4,6
listheart1 = [range(1500,1600), range(100,201), (1,15) ] #1,15
listhearts = [listheart0, listheart1]

# Hitboxes of flags
listflag1 = [range (100 , 150 ), range(100,201), (1,1) ]  #  1,1
listflags=[listflag1]

# Hitboxes of barbed wire
listdying1 = [ range(150,200), range(1400,1501), (14,1)]
listdying2 = [ range(200,275), range(1400,1501), (14,2)]
listdyinglists = [listdying1,listdying2]


global coin_counter
coin_counter = 0
playerHP = 3
died_counter = 0

#-------------------------------------------------------------
# Define functions
#-------------------------------------------------------------




# This function finds all occurrences of an element in a 2D list and
# prints out the coordinates of these occurrences.
def find_elem_in_2d_coordinates(elem, list2D ):
    lss = list(enumerate(list2D))
    ls = []
    for a in lss:
        if elem in a[1]:
            ls.append((a[0], list(enumerate(a[1]))))
    for c in ls:
        for d in c[1]:
            if d[1] == elem:
                print "X-Coordinate: %r" %(c[0])
                print "Y-Coordinate: %r" %(d[0])
                print "----"


find_elem_in_2d_coordinates('1', level)


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
    test = ("%r,%r" % (x,y))
    if test in remaining_coins:
        remaining_coins.remove(test)
        st1 =  level[x]
        st2 = st1[0:y]
        if level[x][y] == '4':
            st3 = st2 + '5'
            level[x] = st3 + st1[y+1:len(level[0])]
            # Get Variable from other window whether or not Coding was successful, then give coins.
            coin_counter += 10
        if level[x][y] == '3':
            st3 = st2 + "."
            level[x] = st3 + st1[y+1:len(level[0])]
            coin_counter += 1
            if Music_paused == True:
                1+1
            else:
                sound_coin.play()
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
    global player_in_flag1
    global listcoinlists
    global listflag1

    # Coin collecting
    for x in listcoinlists:
        if playerleft in x[0]:
            if playerbottom in x[1]:
                return x[2]

    # Sets player_in_flag1 to TRUE if player runs into flag.
    for x in listflags:
        if playerleft in listflag1[0]:
            if playerbottom in listflag1[1]:
                player_in_flag1 = True
                return x[2]

    for x in listhearts:
        if playerleft in x[0]:
            if playerbottom in x[1]:
                return x[2]

    # Enemy detection
    for y in listdyinglists:
        if playerleft in y[0]:
            if playerbottom in y[1]:
                dying()

    else:
        return (0,0)


#13 10 -  11
#14 10 -  11




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



#enemdir_R = True
#enemyDir_L = True
# Enemy1: [14,10,True,0,250]

def enemymove(xblock, yblock, en_dir_L, enemy_mov, enemy_movementMAX, speed, coord):

# Blockwidth, Blockheight, dir(boolean - true for left), enemy_movement, enemy_movementMAX, speed, coord. in the array

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




######################
# Setting variables
######################
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), FLAGS)
pygame.display.set_caption('Pythonia - Learning Python')
clock = pygame.time.Clock() # We need this for FPS reduction.
font = pygame.font.SysFont("Calibri", 30) # Font for ingame text
bigfont = pygame.font.SysFont("monospace", 60)
global player
player = pygame.Rect(10*BLOCKWIDTH, 12*BLOCKHEIGHT - 300, PLAYERSIZE, PLAYERSIZE*2) # Startposition of the player



myimage_left = loadImage("left.png")
myimage_right = loadImage("right.png")
myimage_jump = loadImage("jump.png")
myimage_stand= loadImage("stand.png")
myimage_wall = loadImage("wall.png")
myimage_wall2 = loadImage("wall2.png")
myimage_coin = loadImage("coin.png")
myimage_coinCounter = loadImage("coins.png")
myimage_flagdown = loadImage("flag_down.png")
myimage_flagup = loadImage("flag_up.png")
myimage_kill= loadImage("barbs.png")
myimage_enemy= loadImage("enemy.png")
myimage_hp = loadImage("hp.png")
myimage_heart = loadImage ("heart.png")

# Acceleration, Speed along the X/Y axis and Jumping. Set to zero/false at the beginning => No movement.
accelX = 0
playerSpeedX = 0
playerSpeedY = 0
jumping = False

camerax = player.centerx-(WINDOWWIDTH/2)
cameray = player.centery-(WINDOWHEIGHT/2)

showText = True # Set True if additional text is to be shown (coordinates etc)
showText2 = True # Set True for Coin Counter and HP to be shown
background_image = loadImage("background.png")



opened_Flag1 = False
# Flag 1 has not been opened before if " = False".
# Will be set to True if player runs into it. No further windows will be opened if this is True.


# Music Mixer Variable. False if music in On.
Music_paused = False

# Sounds
sound_coin = pygame.mixer.Sound("coin.wav") # collecting coin
sound_coin.set_volume(0.2) # set low volume
sound_flag = pygame.mixer.Sound("flag.wav") # reaching flag
sound_flag.set_volume(0.2) # set low volume




#-------------------------------------------------------------
# Initializing
#-------------------------------------------------------------

# Background music
pygame.mixer.music.load('rain.wav')
pygame.mixer.music.play(-1, 0.0) # play in an endless loop


# Find all first "3"s in the 2D array (to set coordinates for coin collecting)

#def find(l, elem):
#    for row, i in enumerate(l):
#        try:
#            column = i.index(elem)
#        except ValueError:
#            continue
#        print row, column




############## SECOND WINDOW Alternative #############

#input = <insert input>
#when you run the program and it requires something like a raw_input,
#  this will give it input. You could probably avoid needing to send the pygame program input,
#  because all you really want to do is receive an output from it.


# Comment this below out to open a second window
# process = subprocess.Popen(["python","python_text.py"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=False)


#output = process.communicate(input)[0]
#this will return any output the program prints,
# meaning you can communicate with the program and receive information from it
############################################


#-------------------------------------------------------------
# THE GAME LOOP
#-------------------------------------------------------------
count = 1
called = False


while True:




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
                print "TEXT"
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

    # Rendering involves a little conversion of level coordinates to window coordinates
    #screen.fill(BLACK)
    # Set a background image instead of the black background
    screen.blit(background_image, [0, 0])

    # do not (= comment) draw a rectangle shape
    # pygame.draw.rect(screen, PLAYERCOLOR, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2), 1)

    # The active area makes sure only blocks that are shown on screen are rendered
    #activeArea = pygame.Rect(camerax-BLOCKWIDTH, cameray-BLOCKHEIGHT, WINDOWWIDTH+(BLOCKWIDTH*2), WINDOWHEIGHT+(BLOCKHEIGHT*2))
    activeArea = pygame.Rect(0,0, len(level[0])*BLOCKWIDTH, len(level)*BLOCKHEIGHT)

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
                    if graphiclevel[y][x] == BLOCK2:
                        screen.blit (myimage_wall2, ((x*BLOCKWIDTH) - camerax, (y*BLOCKHEIGHT) - cameray, BLOCKWIDTH, BLOCKHEIGHT))
                    else:
                        screen.blit (myimage_wall, ((x*BLOCKWIDTH) - camerax, (y*BLOCKHEIGHT) - cameray, BLOCKWIDTH, BLOCKHEIGHT))

    #Enemy Movmeent
    for x in listenemies:
        enemymove(x[0],x[1],x[2],x[3],x[4],x[5],x[6])


    #print player.left - camerax
    #print (14*BLOCKWIDTH)-camerax-enemy_movement








        # Customise the OSD here. This was the information I found the most useful.
        #drawText('BoxL: %r BoxR: %r BoxU: %r BoxD: %r' %(player.left, player.right, player.top, player.bottom), font, WHITE, screen, 10, 30)
        #drawText('Jumping: %r CameraX: %r CameraY: %r' %(jumping, camerax, cameray), font, WHITE, screen, 10, 60)
        #drawText('deltaX: %r deltaY: %r' %(playerSpeedX, playerSpeedY), font, WHITE, screen, 10, 90)
        #drawText('minX: %r minY: %r' %(minXDistance, minYDistance), font, WHITE, screen, 10, 120)




        # Deprecated: blitted hearts instead.
        #drawText('HP: %r' %(playerHP), font, WHITE, screen, 170, 0)

    # Character movement -  images being drawn
    if Xkeys[RIGHT] < Xkeys[LEFT]:
        screen.blit(myimage_left, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    elif Xkeys[LEFT] < Xkeys[RIGHT]:
        screen.blit(myimage_right, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    elif jumping == True:
        screen.blit(myimage_jump, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))
    else:
        screen.blit(myimage_stand, (player.left - camerax, player.top - cameray, PLAYERSIZE, PLAYERSIZE*2))


    #screen.blit(myimage_enemy, (enemy.left,enemy.top, BLOCKWIDTH, BLOCKHEIGHT))


# Button Rendering #
    if Music_paused == True:
        button("Music on", 710,0,90,30 ,GREEN, LIGHTGREEN , "music")
    else:
        button("Music off", 710,0,90,30 ,GREEN, LIGHTGREEN , "music")





    coinTuple =  listcoins (player.left, player.bottom)
    if isinstance(coinTuple, tuple):
        if coinTuple != (0,0):
            change_graphic(coinTuple[0],coinTuple[1])



    if player_in_flag1 == True and opened_Flag1 == False :
        # print "OPEN SECOND WINDOW, TRUE, FALSE"
        opened_Flag1 = True
        process = subprocess.Popen(["python","python_tk_text.py"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell=False)


#[14,10,True,0,250,2]

    # Collision detection of all enemies in the list
    for x in listenemies:
    # Left side collision with an enemy
        if (player.left - camerax+20) in range ((x[0]*BLOCKWIDTH)-camerax-x[3], (x[0]*BLOCKWIDTH)-camerax-x[3]+100):
            if (player.top - cameray) in range ((x[1]*BLOCKHEIGHT)-cameray,(x[1]*BLOCKHEIGHT)-cameray+100 ):
                playerHP -= 1
                if playerHP == 0:
                    dying()
                else:
                    player.left +=150
    # Right side collision detection with an enemy:
        if (player.right - camerax-20) in range ((x[0]*BLOCKWIDTH)-camerax-x[3], (x[0]*BLOCKWIDTH)-camerax-x[3]+100):
            if (player.top - cameray) in range ((x[1]*BLOCKHEIGHT)-cameray,(x[1]*BLOCKHEIGHT)-cameray+100 ):
                playerHP -= 1
                if playerHP == 0:
                    dying()
                else:
                    player.left -= 150


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









