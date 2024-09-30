import sys
import pygame
import math
import random


# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width = 800
height = 600
window_size = (width, height)

# Create the window
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Gravity Simulator")

clock = pygame.time.Clock()
target_fps = 120

class Planet:
    def __init__(self, radius, xvel, yvel, x, y, mass):
        self.radius = radius
        self.xvel = xvel
        self.yvel = yvel
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.radius)

    def move(self):
        self.x += self.xvel
        self.y += self.yvel
    
    def attract(self, other):
        g = 0.2
        gforce = g * self.mass * other.mass / ((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        angle = math.atan2(other.y - self.y, other.x - self.x)
        self.xvel += math.cos(angle) * gforce / self.mass
        self.yvel += math.sin(angle) * gforce / self.mass


planets = []
planets.append(Planet(20, 0, 0, width // 2, height // 2, 1000))
planets.append(Planet(5, 0, 1, width // 2 + 100, height // 2, 100))
planets.append(Planet(5, 0, -1, width // 2 - 100, height // 2 , 100))
planets.append(Planet(5, -1, 0, width // 2 , height // 2 + 100 , 100))
planets.append(Planet(5, 1, 0, width // 2 , height // 2 - 100 , 100))
planets.append(Planet(5, 1, 1, width // 2 + 200, height // 2 + 100, 10))

# Game loop
play_button = pygame.Rect(width // 2 - 50, height // 2 - 25, 100, 50)
play_button_color = (0, 255, 0)
play_button_text = pygame.font.SysFont(None, 30).render("Play", True, (0, 0, 0))

playing = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                playing = True

    if playing:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos 
            radius = random.randint(5, 20)
            mass = random.randint(50, 200)
            planets.append(Planet(radius, 0, 0, x, y, mass))
        # Update game logic
        for i in planets:
            i.move()
            i.draw(window)
        
        for i in planets:
            for j in planets:
                if i != j:
                    i.attract(j)
        pygame.display.flip()
        clock.tick(target_fps)
        window.fill((0, 0, 0))  # Fill the window with black color
    

    if not playing:
        pygame.draw.rect(window, play_button_color, play_button)
        window.blit(play_button_text, (width // 2 - 25, height // 2 - 15))
        pygame.display.flip()
        clock.tick(target_fps)
        window.fill((0, 0, 0))  # Fill the window with black color
