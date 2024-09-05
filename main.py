import pygame
import sys
import math 
import random

import config
import entitys

# innitilise pygame
pygame.init()

# create a window
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
outerHT = 400
MARGIN = 30
clock = pygame.time.Clock()
fps = 300

# set the window title
pygame.display.set_caption("8 Ball Pool Game")


gameWall = entitys.RunningState(screen)


# create all the balls and starting positions
ball0 = entitys.Ball(config.BALLSTARTPOS, config.HEIGHT/2, config.RED, 'RED_BALL_1', screen)
ball1 = entitys.Ball(config.BALLSTARTPOS - (2 * config.BALLRADIUS), (config.HEIGHT/2) + config.BALLRADIUS, config.YELLOW, 'YELLOW_BALL_1', screen)
ball2 = entitys.Ball(config.BALLSTARTPOS - (2 * config.BALLRADIUS), (config.HEIGHT/2) - config.BALLRADIUS, config.RED, 'RED_BALL_2', screen)
ball3 = entitys.Ball(config.BALLSTARTPOS - (4 * config.BALLRADIUS), config.HEIGHT/2, config.BLACK, 'CUE_BALL', screen)
ball4 = entitys.Ball(config.BALLSTARTPOS - (4 * config.BALLRADIUS), (config.HEIGHT/2) - config.BALLRADIUS * 2 , config.YELLOW, 'YELLOW_BALL_2', screen)
ball5 = entitys.Ball(config.BALLSTARTPOS - (4 * config.BALLRADIUS), (config.HEIGHT/2) + config.BALLRADIUS * 2 , config.RED, 'RED_BALL_3', screen)
ball6 = entitys.Ball(config.BALLSTARTPOS - (6 * config.BALLRADIUS), (config.HEIGHT/2) - config.BALLRADIUS * 3, config.YELLOW, 'YELLOW_BALL_3',screen)
ball7 = entitys.Ball(config.BALLSTARTPOS - (6 * config.BALLRADIUS), (config.HEIGHT/2) - config.BALLRADIUS * 1, config.RED, 'RED_BALL_4', screen)
ball8 = entitys.Ball(config.BALLSTARTPOS - (6 * config.BALLRADIUS), (config.HEIGHT/2) + config.BALLRADIUS, config.YELLOW, 'YELLOW_BALL_4', screen)
ball9 = entitys.Ball(config.BALLSTARTPOS - (6 * config.BALLRADIUS), (config.HEIGHT/2) + config.BALLRADIUS * 3, config.RED, 'RED_BALL_5', screen)
ball10 = entitys.Ball(config.BALLSTARTPOS - (8 * config.BALLRADIUS), (config.HEIGHT/2) - config.BALLRADIUS * 4, config.YELLOW, 'YELLOW_BALL_5', screen)
ball11 = entitys.Ball(config.BALLSTARTPOS - (8 * config.BALLRADIUS), (config.HEIGHT/2) - config.BALLRADIUS * 2, config.RED, 'RED_BALL_6', screen)
ball12 = entitys.Ball(config.BALLSTARTPOS - (8 * config.BALLRADIUS), (config.HEIGHT/2) , config.YELLOW, 'YELLOW_BALL_6', screen)
ball13 = entitys.Ball(config.BALLSTARTPOS - (8 * config.BALLRADIUS), (config.HEIGHT/2) + config.BALLRADIUS * 2, config.RED, 'RED_BALL_7', screen)
ball14 = entitys.Ball(config.BALLSTARTPOS - (8 * config.BALLRADIUS), (config.HEIGHT/2) + config.BALLRADIUS * 4,config.YELLOW, 'YELLOW_BALL_7', screen)

cueBall0 = entitys.CueBall(config.CUEBALLSTARTPOS[0], config.CUEBALLSTARTPOS[1], screen)

ballArr = [ball0, ball1, ball2, ball3, ball4,ball5, ball6, ball7, ball8, ball9, ball10, ball11, ball12, ball13, ball14,cueBall0]


def gameLoop(ballArr):
    for i in range(len(ballArr)):
        ballArr[i].checkWallCollition()
        for j in range(i + 1, len(ballArr)):
            if ballArr[i].checkCollitionBall(ballArr[j]):
                print(ballArr[i].velocityCanculation(ballArr[j]))
    

def ballsUpdate(ballArr):
    for i in range(len(ballArr)): ballArr[i].movingState()
    cueBall0.movingState()


cueBall0.ballUpdate(-1,0)
active = True

while active:
    clock.tick(fps)
    screen.fill(config.FELTBACK)
    gameWall.drawRunningState()
    
    gameLoop(ballArr)
    
    
    
    ballsUpdate(ballArr)
    
    
    
    #ball2.checkWallCollition()
    
    pygame.display.update()    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        else: pass



# had a problem with over updating creating flashes in game 
# this was resolved by removing the updates after changing the frame rate