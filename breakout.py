import random, time, sys
import pygame
from pygame.locals import *
from breakout_utils import *

origXVel = 3
origYVel = 5

def game(DISPLAYSURF):

    gameState = True

    origXVel = 3
    origYVel = 5

    ballXVel = 3
    ballYVel = 5
    
    

    board = generateBoard()

    pygame.mouse.set_pos((WINDOWWIDTH/2), PADDLEYPOS)

    ballX = WINDOWWIDTH / 2
    ballY = WINDOWHEIGHT - 45

    

    ### MAIN LOOP HERE
    while gameState == True:
        checkForQuit()
        DISPLAYSURF.fill(GRAY)

        drawBoard(board, DISPLAYSURF)
        paddleRect = drawPaddle(DISPLAYSURF)

        

        ballRect = drawBallXY(ballX, ballY, DISPLAYSURF)

        ballX = ballX + ballXVel
        ballY = ballY + ballYVel

        ballXVel, ballYVel, gameState = doBallWallCollision(ballX, ballY, ballXVel, ballYVel, gameState)
        ballXVel, ballYVel = doPaddleCollision(paddleRect, ballRect, ballXVel, ballYVel)
        board, ballYVel = doBlockCollision(board, ballRect, ballYVel)

        checkForQuit()





        

    





        pygame.display.update()
        FPSCLOCK.tick(FPS)


    ### END LOOP

def welcome(DISPLAYSURF):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 70)
    introSurf = BASICFONT.render('BREAKOUT!', 1, GREEN) 
    introRect = introSurf.get_rect()
    introRect.center = (WINDOWWIDTH /2, WINDOWHEIGHT/2)
    DISPLAYSURF.blit(introSurf, introRect)


    while True:
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                return


def youLose(DISPLAYSURF):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 70)
    introSurf = BASICFONT.render('GAME OVER', 1, GREEN) 
    introRect = introSurf.get_rect()
    introRect.center = (WINDOWWIDTH /2, WINDOWHEIGHT/2)
    DISPLAYSURF.blit(introSurf, introRect)
     


    while True:
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        checkForQuit()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                return




def generateBoard():
    board = []
    for x in range(BOARDWIDTH):
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
            elif board[boxx][boxy] >= 2:
                pygame.draw.rect(asurface, BLUE, (left, top, BLOCKXLENGTH, BLOCKYHEIGHT))
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
    
def doBallWallCollision(ballx, bally, ballXVel, ballYVel, gameState):
    checkForQuit()

    if ballx < 10:
        ballXVel = origXVel
    
    if bally < 10:
        ballYVel = origYVel
    
    if ballx > WINDOWWIDTH-10:
        ballXVel = -origXVel
    
    if bally > WINDOWHEIGHT-10:
        gameState = False

    return ballXVel, ballYVel, gameState        

def doPaddleCollision(paddleRect, ballRect, ballXVel, ballYVel):
    checkForQuit()
    if paddleRect.colliderect(ballRect):
        ballYVel = -origYVel
    return ballXVel, ballYVel


def doBlockCollision(board, ballRect, ballYVel):
    checkForQuit()
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            if board[boxx][boxy] > 0:

                left, top = leftTopCoordsOfBox(boxx, boxy)
                boxRect = pygame.Rect(left, top, BLOCKXLENGTH, BLOCKYHEIGHT)
                if boxRect.colliderect(ballRect):
                    board[boxx][boxy] -= 1
                    ballYVel = -ballYVel

    return board, ballYVel










    


def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BLOCKXLENGTH, BLOCKYHEIGHT)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def main():
    global FPSCLOCK, origXVel, origYVel


    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('BREAKOUT')

    welcome(DISPLAYSURF)
    game(DISPLAYSURF)
    youLose(DISPLAYSURF)



if __name__ == "__main__":
    main()
    # print(generateBoard())
