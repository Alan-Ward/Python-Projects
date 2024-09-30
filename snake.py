import pygame, sys, random
pygame.init()


clock = pygame.time.Clock()

#################################
background_colour = (50, 50, 50)
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Snake Game')
screen.fill(background_colour)
pygame.display.flip()
#################################

######## COORDINATES ############
snakeX = [400]
snakeY = [220]

AppleX = 580
AppleY = 340

grow = 0
#################################


########### DIRECTIONS ##########
# up = 1, down = 2, left = 3, right = 4
direction = 0

####################################




while True:
     
    ############# INPUT ############
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        events = pygame.event.get()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if not direction == 4 or len(snakeX) == 1:
                    direction = 3
                
            elif event.key == pygame.K_RIGHT:
                if not direction == 3 or len(snakeX) == 1:
                    direction = 4
                
            elif event.key == pygame.K_UP:
                if not direction == 2 or len(snakeX) == 1:
                    direction = 1
                
            elif event.key == pygame.K_DOWN:
                if not direction == 1 or len(snakeX) == 1:
                    direction = 2
                
    ##################################
    
    ######## APPLE COLLISTION ########
    if snakeX[0] == AppleX and snakeY[0] == AppleY:
        grow += 4
        tempX = random.randint(0,59)*20
        tempY = random.randint(0,29)*20
        colistion = True
        while colistion:
            colistion = False
            tempX = random.randint(0,59)*20
            tempY = random.randint(0,29)*20
            for i in range(len(snakeX)):
                if snakeX[0] == tempX and snakeY[0] == tempY:
                    colistion = True
        AppleX = tempX
        AppleY = tempY
    ##################################

    ############# DIRECTION ##########    
    if direction == 1:
        tempX = snakeX[0]
        tempY = snakeY[0]
        snakeX.insert(0, tempX)
        snakeY.insert(0, tempY-20)
        if grow <= 0:
            snakeX.pop()
            snakeY.pop()
            
        else:
            grow -= 1
    if direction == 2:
        tempX = snakeX[0]
        tempY = snakeY[0]
        snakeX.insert(0, tempX)
        snakeY.insert(0, tempY+20)
        if grow <= 0:
            snakeX.pop()
            snakeY.pop()
        else:
            grow -= 1
    if direction == 3:
        tempX = snakeX[0]
        tempY = snakeY[0]
        snakeX.insert(0, tempX-20)
        snakeY.insert(0, tempY)
        if grow <= 0:
            snakeX.pop()
            snakeY.pop()
        else:
            grow -= 1
    if direction == 4:
        tempX = snakeX[0]
        tempY = snakeY[0]
        snakeX.insert(0,tempX+20)
        snakeY.insert(0, tempY)
        if grow <= 0:
            snakeX.pop()
            snakeY.pop()
        else:
            grow -= 1
    ##################################
        
    for i in range(1, len(snakeX)):
        if snakeX[0] == snakeX[i] and snakeY[0] == snakeY[i]:
            pygame.quit()
            sys.exit()
    if snakeX[0] > 1180 or snakeX[0] < 0:
        pygame.quit()
        sys.exit()
    if snakeY[0] > 580 or snakeY[0] < 0:
        pygame.quit()
        sys.exit()
    
    screen.fill((55,55,55))
    for i in range(len(snakeX)):
        print(len(snakeX))
        pygame.draw.rect(screen, (0,200,0), pygame.Rect((snakeX[i], snakeY[i]), (19, 19)))
    
    pygame.draw.rect(screen, (200,0,0), pygame.Rect((AppleX, AppleY), (19, 19)))
    
    pygame.display.update()
    clock.tick(10)
