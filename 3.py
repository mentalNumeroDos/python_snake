import pygame

pygame.init()
def wallsDraw():
    pygame.draw.rect(gameDisplay, white, pygame.Rect(0,0,10,500))
    pygame.draw.rect(gameDisplay, white, pygame.Rect(490,0,10,500))
    pygame.draw.rect(gameDisplay, white, pygame.Rect(0,0,500,10))
    pygame.draw.rect(gameDisplay, white, pygame.Rect(0,490,500,10))

gameDisplay = pygame.display.set_mode((500,500))
white = (255,255,255)
black = (0,0,0)
x = 250
y = 250
moveY = 0
moveX = 0
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

crashed = False

wallsDraw()
while not crashed:
    x += moveX
    y += moveY
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: moveY, moveX = -10, 0
    if pressed[pygame.K_DOWN]: moveY, moveX = 10, 0
    if pressed[pygame.K_LEFT]: moveX, moveY = -10, 0
    if pressed[pygame.K_RIGHT]: moveX, moveY = 10, 0
    
    pygame.draw.rect(gameDisplay, white, pygame.Rect(x,y,10,10))
    not for a in range(5)
        
    
    
    
    pygame.display.update()
    clock.tick(3)

pygame.quit()
quit()
