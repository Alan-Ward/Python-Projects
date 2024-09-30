import pygame, sys, random, math


#### GAME INITIALIZATION ####
pygame.init()
WindowWidth = 800
WindowHeight = 600
window = pygame.display.set_mode((WindowWidth, WindowHeight))
window.fill((150, 150, 255))
clockSpeed = 60
movementSpeed = 4
clock = pygame.time.Clock()
x1= 1100
x2 = 1500
x3 = 1900
y1 = 0
y2 = 50
y3 = -100


#### SHAPE CLASS ####
class objects: 
    def __init__(self, width, height, x, y, colour):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.colour = colour

#### BIRD CLASS ####
class bird:
    def __init__(self, rad, y, vel, colour ):
        self.rad = rad
        self.y = y
        self.vel = vel
        self.colour = colour
    def jump(self):
        if self.vel < 15:
            self.vel += 4
        if self.vel < 15:
            self.vel += 4
        if self.vel < 15:
            self.vel += 4
    def col(self, other ,x, y):   
        # Find the closest point on the rectangle to the center of the circle
        closest_x = max(other.x + x, min(300, other.x + x +  other.width))
        closest_y = max(other.y + y, min(self.y, other.y + y + other.height))
    
        # Calculate the distance between the closest point and the center of the circle
        distance = math.sqrt((closest_x - 300)**2 + (closest_y - self.y)**2)
    
        # Check if the distance is less than or equal to the radius of the circle
        if distance <= self.rad:
            return True
        else:
            return False
    
       

# bird
b = bird(25,350,0, (250, 255, 50))  

# ground
g = objects(800,50,0,550,(50, 255, 50))

# pipe 1 
p1a = objects(60,800,100,350,(100, 255, 100))
p1b = objects(80,50,90,350,(100, 255, 100))
p1c = objects(60,800,100,-650,(100, 255, 100))
p1d = objects(80,50,90,150,(100, 255, 100))

# pipe 2
p2a = objects(60,800,100,350,(100, 255, 100))
p2b = objects(80,50,90,350,(100, 255, 100))
p2c = objects(60,800,100,-650,(100, 255, 100))
p2d = objects(80,50,90,150,(100, 255, 100))

# pipe 3
p3a = objects(60,800,100,350,(100, 255, 100))
p3b = objects(80,50,90,350,(100, 255, 100))
p3c = objects(60,800,100,-650,(100, 255, 100))
p3d = objects(80,50,90,150,(100, 255, 100))


# run the Pygame event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            b.jump()
       
            
    window.fill((150, 150, 255))
    if x1 < -100:
        x1 = 1100
        y1 = random.randint(-100, 100)
    x1 -= movementSpeed

    if x2 < -100:
        x2 = 1100
        y2 = random.randint(-100, 100)
    x2 -= movementSpeed

    if x3 < -100:
        x3 = 1100
        y3 = random.randint(-100, 100)
    x3 -= movementSpeed

    b.y -= b.vel
     
    if  b.vel > -6:
        b.vel -= 0.5 
    pygame.draw.rect(window, p1a.colour, (p1a.x + x1, p1a.y +y1, p1a.width, p1a.height))
    pygame.draw.rect(window, p1b.colour, (p1b.x + x1, p1b.y +y1, p1b.width, p1b.height))
    pygame.draw.rect(window, p1c.colour, (p1c.x + x1, p1c.y +y1, p1c.width, p1c.height))
    pygame.draw.rect(window, p1d.colour, (p1d.x + x1, p1d.y +y1, p1d.width, p1d.height))

    pygame.draw.rect(window, p2a.colour, (p2a.x + x2, p2a.y +y2, p2a.width, p2a.height))
    pygame.draw.rect(window, p2b.colour, (p2b.x + x2, p2b.y +y2, p2b.width, p2b.height))
    pygame.draw.rect(window, p2c.colour, (p2c.x + x2, p2c.y +y2, p2c.width, p2c.height))
    pygame.draw.rect(window, p2d.colour, (p2d.x + x2, p2d.y +y2, p2d.width, p2d.height))

    pygame.draw.rect(window, p3a.colour, (p3a.x + x3, p3a.y +y3, p3a.width, p3a.height))
    pygame.draw.rect(window, p3b.colour, (p3b.x + x3, p3b.y +y3, p3b.width, p3b.height))
    pygame.draw.rect(window, p3c.colour, (p3c.x + x3, p3c.y +y3, p3c.width, p3c.height))
    pygame.draw.rect(window, p3d.colour, (p3d.x + x3, p3d.y +y3, p3d.width, p3d.height))

    pygame.draw.circle(window, b.colour, (300, b.y), b.rad)
    pygame.draw.rect(window,(0,0,0), (300 , b.y , 25, 5))

    if b.col(p1a,x1,y1) or  b.col(p1b,x1,y1) or  b.col(p1c,x1,y1) or  b.col(p1d,x1,y1) or b.col(p2a,x2,y2) or b.col(p2b,x2,y2) or  b.col(p2c,x2,y2) or b.col(p2d,x2,y2) or b.col(p3a,x3,y3) or b.col(p3b,x3,y3) or b.col(p3c,x3,y3) or b.col(p3d,x3,y3):
        b.colour = (255, 0 ,0)
    else:
        b.colour = (250, 255, 50)
    
    
   
   
    
    
   
    
    pygame.draw.rect(window, g.colour, (g.x, g.y, g.width, g.height))
    pygame.display.update()
    clock.tick(clockSpeed)