import random, time, sys
import pygame
from pygame.locals import *
from breakout_utils import *

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('BREAKOUT')
    
    board = generateBoard()

    pygame.mouse.set_pos((WINDOWWIDTH/2), PADDLEYPOS)

    ballAngle = 30
    ballDistance = 100

    ### MAIN LOOP HERE
    while True:
        checkForQuit()
        DISPLAYSURF.fill(GRAY)

        drawBoard(board, DISPLAYSURF)
        paddleRect = drawPaddle(DISPLAYSURF)

        

        drawBall(ballAngle, ballDistance, DISPLAYSURF)

        ballDistance += 5

    





        pygame.display.update()
        FPSCLOCK.tick(FPS)


    ### END LOOP

def generateBoard():
    board = []
    for x in range (BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append('BLOCK')
        board.append(column)
    return board

def leftTopCoordsOfBox (boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BLOCKSPACING + BLOCKXLENGTH + BLOCKSPACING) + XMARGIN
    top = boxy * (BLOCKSPACING + BLOCKYHEIGHT + BLOCKSPACING) + YMARGIN
    return (left, top)


def drawBoard(board, asurface):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if board[boxx][boxy] == 'BLOCK':
                pygame.draw.rect(asurface, RED, (left, top, BLOCKXLENGTH, BLOCKYHEIGHT))

def drawPaddle(asurface):
    mousex, mousey = pygame.mouse.get_pos()
    PADDLEXPOS = (mousex - (PADDLEXLENGTH/2))
    # PADDLEYPOS = PADDLEYPOS # Value comes from import *
    if PADDLEXPOS > WINDOWWIDTH - PADDLEXLENGTH:
        PADDLEXPOS = WINDOWWIDTH - PADDLEXLENGTH

    paddleRect = pygame.Rect((PADDLEXPOS, PADDLEYPOS), (PADDLEXLENGTH, PADDLEYHEIGHT))

    
    pygame.draw.rect(asurface, GREEN, paddleRect)

    return paddleRect

def drawBall(deg, distance, asurface):

    x, y = getTrigoXY(deg, distance)

    pygame.draw.circle(asurface, YELLOW, (x, y), 10)

def doBallDirection(xdirection, ydirection, degrees):
    pass










    


def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BLOCKXLENGTH, BLOCKYHEIGHT)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)






if __name__ == "__main__":
    main()
    # print(generateBoard())
