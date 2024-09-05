
import pygame
import math
import config
import numpy as np


class Ball:
    def __init__(self, xPos, yPos, color, id, serface) -> None:
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = 0
        self.yVel = 0
        self.moving = False
        self.active = False      
        self.__radius = config.BALLRADIUS
        self.__color = color
        self.__output = serface
        self._mass = config.BALLMASS
        self.__retention = config.BALLRETENTION
        self.__id = id     
        
    def drawBall(self) -> None:
        try:    
            pygame.draw.circle(self.__output, self.__color, (int(self.xPos), int(self.yPos)), self.__radius)
        except:
            pass
            
    def movingState(self) -> None:
        if self.xVel != 0 or self.yVel != 0:
            self.moving = True
            self.xPos += self.xVel
            self.yPos += self.yVel
            self.drawBall()
        else:
            self.moving = False
            self.drawBall()
        
    def checkCollitionBall(self, other) -> bool: # for collition between ball
        return math.sqrt((self.xPos - other.xPos)**2 + (self.yPos - other.yPos)**2) < (self.__radius + other.__radius)
    
    def velocityCanculation(self, other): # inter ball collitions]
        # validate a collition between balls has happened 
        if self.checkCollitionBall(other):
            otherVelocity = np.array([other.xVel, other.yVel]) # making out vel vectors into a np array
            selfVelocity = np.array([self.xVel, self.yVel])
            
            # using a NP array we work out the vetors after a collition
            selfVelocityf = selfVelocity - (2 * other._mass / (self._mass + other._mass)) * \
                np.dot(selfVelocity - otherVelocity, selfVelocity - otherVelocity) / \
                    np.linalg.norm(selfVelocity - otherVelocity)**2 * (selfVelocity - otherVelocity)
                    
                    
            otherVelocityf = otherVelocity - (2 * self._mass / (self._mass + other._mass)) * \
                np.dot(otherVelocity - selfVelocity, otherVelocity - selfVelocity) / \
                    np.linalg.norm(otherVelocity - selfVelocity)**2 * (otherVelocity - selfVelocity)
                    
            self.xVel, self.yVel = selfVelocityf[0], selfVelocityf[1]
            other.xVel, other.yVel = otherVelocityf[0], otherVelocityf[1]
            
            return selfVelocityf, otherVelocityf, True
        else: return (self.xVel * self.__retention, self.yVel * self.__retention), (other.xVel * self.__retention, self.yVel * self.__retention) 
        
    def checkWallCollition(self):
        if self.xPos - self.__radius < config.PADDING or self.xPos + self.__radius > config.WIDTH - config.PADDING:
            self.xVel *= -1 
        elif self.yPos - self.__radius < config.PADDING or self.yPos + self.__radius > config.HEIGHT - config.PADDING:
            self.yVel *= -1
        else:
            pass
        
    def isActive(self):
        if self.xVel != 0 or self.yVel != 0: self.active = True
        return self.active
    
    def ballUpdate(self, xVel, yVel):
        self.xVel = xVel
        self.yVel = yVel
    
    def getID(self):
        return self.__id
      
class CueBall(Ball):
    def __init__(self, xPos, yPos, serface):
        super().__init__(xPos, yPos, config.WHITE , 'CUE_BALL', serface) 

    def setPositionAndVelocity(self, xPos, yPos, xVel, yVel):
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        self.moving = True if xVel != 0 or yVel != 0 else False

    def reset(self):
        self.xPos = config.CUEBALLSTARTPOS[0]
        self.yPos = config.CUEBALLSTARTPOS[1]
        self.xVel = 0
        self.yVel = 0
        self.moving = False
        self.active = False
              
class RunningState:
    def __init__(self, serface):
        self.output = serface
        self.wallColor = config.wallColor
        self.pocketColor = config.pocketColor 
        self.__padding = config.PADDING 
        self.__pocketSize = config.POCKETSIZE
        
    def walls(self) -> list:
        leftWall = pygame.draw.rect(self.output, self.wallColor, (0,0,self.__padding, config.HEIGHT))
        topWall = pygame.draw.rect(self.output, self.wallColor, (0,0, config.WIDTH, self.__padding))
        bottomWall = pygame.draw.rect(self.output, self.wallColor, (0, config.HEIGHT - self.__padding, config.WIDTH, self.__padding))
        rightWall = pygame.draw.rect(self.output, self.wallColor, (config.WIDTH - self.__padding, 0, self.__padding, config.HEIGHT))
        wallList = [leftWall, topWall, bottomWall, rightWall]
        return wallList
    
    def pockets(self) -> list:
        topLeftPocket = pygame.draw.circle(self.output, self.pocketColor, (self.__padding, self.__padding), self.__pocketSize)
        topMidPocket = pygame.draw.circle(self.output, self.pocketColor, (((config.WIDTH)/2), self.__padding), self.__pocketSize)
        topRightPocket = pygame.draw.circle(self.output, self.pocketColor, ((config.WIDTH-self.__padding), self.__padding), self.__pocketSize)
        
        bottomLeftPocket = pygame.draw.circle(self.output, self.pocketColor, (self.__padding, (config.HEIGHT-self.__padding)), self.__pocketSize)
        bottomMidPocket = pygame.draw.circle(self.output, self.pocketColor, (config.WIDTH/2, config.HEIGHT-self.__padding), self.__pocketSize)
        bottomRightPocket = pygame.draw.circle(self.output, self.pocketColor, (config.WIDTH-self.__padding, config.HEIGHT-self.__padding), self.__pocketSize)
        
        pocketsArr = [topLeftPocket, topMidPocket, topRightPocket, bottomLeftPocket, bottomMidPocket, bottomRightPocket]
        
        return pocketsArr
        
    def drawRunningState(self) -> None:
        self.walls()
        self.pockets()
                    
class CueStick:
    def __init__(self):
        pass