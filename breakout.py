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

    ballX = WINDOWWIDTH / 2
    ballY = WINDOWHEIGHT - 45
    ballXVel = 5
    ballYVel = 5

    ### MAIN LOOP HERE
    while True:
        checkForQuit()
        DISPLAYSURF.fill(GRAY)

        drawBoard(board, DISPLAYSURF)
        paddleRect = drawPaddle(DISPLAYSURF)

        

        ballRect = drawBallXY(ballX, ballY, DISPLAYSURF)

        ballX = ballX + ballXVel
        ballY = ballY + ballYVel

        ballXVel, ballYVel = doBallWallCollision(ballX, ballY, ballXVel, ballYVel)
        ballXVel, ballYVel = doPaddleCollision(paddleRect, ballRect, ballXVel, ballYVel)
        checkForQuit()





        

    





        pygame.display.update()
        FPSCLOCK.tick(FPS)


    ### END LOOP

def generateBoard():
    board = []
    for x in range (BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(1)
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
            if board[boxx][boxy] == 1:
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

def drawBallXY(x, y, asurface):
    circleSurf = pygame.Surface((20, 20), pygame.SRCALPHA)
    circleRect = circleSurf.get_rect()
    circleRect.center = (x, y)
    pygame.draw.circle(circleSurf, YELLOW, (10, 10), 10)
    asurface.blit(circleSurf, circleRect)
    
    return circleRect

def drawBall(deg, distance, asurface):

    x, y = getTrigoXY(deg, distance)

    pygame.draw.circle(asurface, YELLOW, (x, y), 10)
    
def doBallWallCollision(ballx, bally, ballXVel, ballYVel):
    checkForQuit()

    if ballx < 10:
        ballXVel = 5
    
    if bally < 10:
        ballYVel = 5
    
    if ballx > WINDOWWIDTH-10:
        ballXVel = -5
    
    if bally > WINDOWHEIGHT-10:
        ballYVel = -5

    return ballXVel, ballYVel        

def doPaddleCollision(paddleRect, ballRect, ballXVel, ballYVel):
    checkForQuit()
    if paddleRect.colliderect(ballRect):
        ballYVel = -5
    return ballXVel, ballYVel












    


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
