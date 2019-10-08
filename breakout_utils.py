import pygame, sys, math
from pygame.locals import *

# STATIC VARIABLES


FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

BOARDWIDTH = 10
BOARDHEIGHT = 4

BLOCKSPACING = 5
BLOCKXLENGTH = WINDOWWIDTH / (BOARDWIDTH + (BLOCKSPACING/2))
BLOCKYHEIGHT = 20

paddleDistanceFromBottom = 30
PADDLEXLENGTH = 50
PADDLEYHEIGHT = 20

PADDLEYPOS = WINDOWHEIGHT - paddleDistanceFromBottom


XMARGIN = 20
YMARGIN = 100




#             R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)
NOCOLOUR    = (  0,   0,   0,   0)


# UTIL FUNCTIONS

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

def degToRadian(deg):
    return deg * math.pi / 180

def getXcoord(deg, hypo):
    # The sin of the degree is equal to ANS divided by HYPO
    # Get sin of degree.
    # Multiply this number by the HYPO
    # This will be the length co-ord
    radA = degToRadian(deg)
    sinA = math.sin(radA)
    xLength = sinA * hypo

    return xLength

def getYcoord(deg, hypo):
    # The same but wit COSINE I think.
    radA = degToRadian(deg)
    cosA = math.cos(radA)
    yLength = cosA * hypo
    return yLength

def getTrigoXY(deg, hypo):
    x = getXcoord(deg, hypo)
    y = getYcoord(deg, hypo)
    intx = int(x)
    inty = int(y)
    return (intx, inty)


def terminate():
    pygame.quit()
    sys.exit()

# print(degToRadian(12))