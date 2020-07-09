import pygame, random, sys

pygame.init()
def wallsDraw():    #draws game borders
    pygame.draw.rect(gameDisplay, white, pygame.Rect(0,0,10,500))
    pygame.draw.rect(gameDisplay, white, pygame.Rect(490,0,10,500))
    pygame.draw.rect(gameDisplay, white, pygame.Rect(0,0,500,10))
    pygame.draw.rect(gameDisplay, white, pygame.Rect(0,490,500,10))
def fruitDraw():
    global fruitColor
    global randomX
    global randomY
    fruitColor = random.choice(colors)
    randomX = 10 * random.randint(2,48)
    randomY = 10 * random.randint(2,48)
    pygame.draw.rect(gameDisplay, fruitColor, pygame.Rect(randomX,randomY,10,10))


gameDisplay = pygame.display.set_mode((500,500))
cyan = (0, 217, 217)
yellow = (255, 217, 0)
white = (255,255,255)
black = (0,0,0)
green = (86, 168, 50)
red = (227, 18, 18)
blue = (0,0,255)
snakeColor = white
colors = [(255,255,255), (0,0,255), (227, 18, 18), (86, 168, 50), (255, 217, 0), (0, 217, 217), (255,255,255)]
x = 250
y = 250
moveY = 0
moveX = 0
posHistory = [0,0]
length = 10
Xhistory = []
Yhistory = []
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
crashed = False

fruitDraw()
wallsDraw()
while not crashed:
    moveD = False
    if not posHistory[-1] == y or not posHistory[-2] == x: #checks if the current position is in the history
        Xhistory.append(posHistory[-2])
        Yhistory.append(posHistory[-1])
        posHistory.append(x)                            #adds them if it isn't
        posHistory.append(y)
    if len(posHistory) > length + 6:                    #removes old locations
        del posHistory[0:3]
    if len(Xhistory) > length / 2:
        del Xhistory[0]
    if len(Yhistory) > length / 2:
        del Yhistory[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    pressed = pygame.key.get_pressed()          #movement mechanics
    if pressed[pygame.K_UP]:
        if not moveY == 10 and not moveD == True: moveY, moveX, moveD = -10, 0, True
    if pressed[pygame.K_DOWN]:
        if not moveY == -10 and not moveD == True: moveY, moveX, moveD = 10, 0, True
    if pressed[pygame.K_LEFT]:
        if not moveX == 10 and not moveD == True: moveX, moveY, moveD = -10, 0, True
    if pressed[pygame.K_RIGHT]:
        if not moveX == -10 and not moveD == True: moveX, moveY, moveD = 10, 0, True
    if x in Xhistory:
        if Yhistory[Xhistory.index(x)] == y:
            crashed = True
            break
    x += moveX
    y += moveY
    if x == randomX and y == randomY: #increases snake length, changes snake color and draws another fruit when the snake hits a fruit
        if not posHistory[-1] == y or not posHistory[-2] == x: #checks if the current position is in the history
            Xhistory.append(posHistory[-2])
            Yhistory.append(posHistory[-1])
            posHistory.append(x)                            #adds them if it isn't
            posHistory.append(y)
        snakeColor = fruitColor
        length += 2
        b = 1
        while b < (length / 2 - 1):
            pygame.draw.rect(gameDisplay, fruitColor, pygame.Rect(Xhistory[-b],Yhistory[-b],10,10))
            pygame.display.update()
            b += 1
        fruitDraw()
    if x <= 10 or x >= 490 or y <= 10 or y >= 490: #checks if the snake touches a wall
        crashed = True
    try:
        pygame.draw.rect(gameDisplay, black, pygame.Rect(posHistory[-length],posHistory[-(length - 1)],10,10))#moves the tail
        wallsDraw()
    except:
        length = length
    pygame.draw.rect(gameDisplay, snakeColor, pygame.Rect(x,y,10,10))    #moves the head
    
    
    
    
    pygame.display.update()
    clock.tick(15)

pygame.draw.rect(gameDisplay, blue, pygame.Rect(0,0,500,500))
pygame.display.update()

print('You are dead')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

