import pygame, random, sys, tkinter

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

def displaytext(text, color, pos, size):
    textSurf = text1(size).render(text,True,color)
    gameDisplay.blit(textSurf,pos)

def gameLoop(fps):
    x = 250
    y = 250
    length = 10
    moveX = 0
    moveY = 0
    snakeColor = white
    crashed = False
    pygame.draw.rect(gameDisplay,black, pygame.Rect(0,0,500,500))
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
        if len(Xhistory) > length / 2 + 1:
            del Xhistory[0]
        if len(Yhistory) > length / 2 + 1:
            del Yhistory[0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
        clock.tick(fps)
        
def fullLoop():
    gameLoop(15)
    pygame.draw.rect(gameDisplay, BSODcolor, pygame.Rect(0,0,500,500))
    displaytext('An exception has occured(error code: death).', white, (5,5), 25)
    displaytext('Would you like to continue? (Y/N)', white, (5,45), 25)
    pygame.display.update()

def mainMenu():
    goingBack = False
    pygame.draw.rect(gameDisplay, black, pygame.Rect(0,0,500,500))
    pygame.draw.rect(gameDisplay, white, pygame.Rect(30,30,440,220))
    displaytext('Start', white, (35,260), 30)
    displaytext('Options', white, (35,285), 30)
    displaytext('Quit', white, (35,310), 30)
    pygame.display.update()
    print(6)
    optionStart()
    print(5)
    if goingBack == True:
        print(7)
        mainMenu()

def blinkingArrow(x, y, size):
    displaytext('>', white, (x,y), size)
    pygame.display.update()
    pygame.time.wait(500)
    pygame.draw.rect(gameDisplay, black, pygame.Rect(10,250,25,100))
    pygame.display.update()
    pygame.time.wait(500)
def optionStart():
    global goingBack
    onQuit = False
    onOption = False
    onStart = True
    inMenu = True
    while onStart:
        blinkingArrow(20, 257, 30)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    onOption = True
                    break
                if event.key == pygame.K_RETURN:
                    inMenu = False
                    return None
        break
    if onOption:
        optionOptions()
        if goingBack:
            goingBack = True
            
            return None
    if inMenu:
        optionStart()
    

def optionOptions():
    onStart = False
    onQuit = False
    while True:
        blinkingArrow(20, 282, 30)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    onQuit = True
                    optionQuit()
                if event.key == pygame.K_UP:
                    onStart = True
                    return None
                if event.key == pygame.K_RETURN:
                    inOptions = True
                    optionsMenu()
                    if goingBack:
                        return None

def optionQuit():
    onStart = False
    onOption = False
    while True:
        blinkingArrow(20, 305, 30)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    onOption = True
                    return None
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()
def text1(size):
    return pygame.font.SysFont("lucidaconsole.ttf",size)

def optionsMenu():
    if goingBack == True:
        return None
    pygame.draw.rect(gameDisplay, black, pygame.Rect(0,0,500,500))
    displaytext('Difficulty', white, (40,20), 60)
    displaytext('Eating Animation', white, (40,160), 60)
    displaytext('Resolution', white, (40,300), 60)
    displaytext('Back', white, (40,440), 60)
    pygame.display.update()
    optionDifficulty()

def optionDifficulty():
    print(1)
    onDifficulty = True
    while True:
        blinkingArrow(35, 20, 40)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    underDifficulty()
                if event.key == pygame.K_DOWN:
                    optionEatingAnim()
            if goingBack == True:
                return None

def optionEatingAnim():
    print(2)
    onDifficulty = False
    onEatingAnim = True
    while True:
        blinkingArrow(35, 160, 40)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    underEatingAnim()
                if event.key == pygame.K_UP:
                    onEatingAnim = False
                    return None
                if event.key == pygame.K_DOWN:
                    optionResolution()
            if goingBack == True:
                return None
def optionResolution():
    print(3)
    onEatingAnim = False
    onResolution = True
    while True:
        blinkingArrow(35, 300, 40)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    underResolution()
                if event.key == pygame.K_UP:
                    onResolution = False
                    return None
                if event.key == pygame.K_DOWN:
                    optionBack()
            if goingBack == True:
                return None

def optionBack():
    print(4)
    global goingBack
    onResolution = False
    onBack = True
    while True:
        blinkingArrow(35, 440, 40)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    goingBack = True
                    return None
                if event.key == pygame.K_UP:
                    return None
global goingBack
goingBack = False
lucidaConsoleFont = pygame.font.SysFont("lucidaconsole.ttf",25)
gameDisplay = pygame.display.set_mode((500,500))
cyan = (0, 217, 217)
yellow = (255, 217, 0)
white = (255,255,255)
black = (0,0,0)
green = (86, 168, 50)
red = (227, 18, 18)
blue = (0,0,255)
BSODcolor = (0,0,170)
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
responded = 1
playing = True

mainMenu()
while True:
    fullLoop()
    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            pygame.quit()
            sys.exit()
        elif keys[pygame.K_y]:
            global crashed
            crashed = False
            fullLoop()
        pygame.event.pump()


print('You are dead')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

