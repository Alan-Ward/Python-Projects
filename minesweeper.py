import pygame
import random

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 660

# Set square dimensions
SQUARE_SIZE = 60

# Set grid dimensions
GRID_WIDTH = int(WINDOW_WIDTH / SQUARE_SIZE)
GRID_HEIGHT = int((WINDOW_HEIGHT - 60) / SQUARE_SIZE)

# Set bomb percentage
BOMB_PERCENTAGE = 0.1

# Set colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set font
FONT = pygame.font.SysFont(None, 30)

# Create square class
class Square:
    def __init__(self, x, y, has_bomb):
        self.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        self.has_bomb = has_bomb
        self.clicked = False
        self.proximity = 0

    def display(self):
        if not self.clicked:
            pygame.draw.rect(screen, GRAY, self.rect)
        elif self.has_bomb:
            pygame.draw.rect(screen, RED, self.rect)
        else:
            pygame.draw.rect(screen, WHITE, self.rect)
            if self.proximity > 0:
                text = FONT.render(str(self.proximity), True, BLACK)
                text_rect = text.get_rect(center=self.rect.center)
                screen.blit(text, text_rect)

# Create grid of square objects
grid = []
for y in range(GRID_HEIGHT):
    row = []
    for x in range(GRID_WIDTH):
        has_bomb = random.random() < BOMB_PERCENTAGE
        row.append(Square(x * SQUARE_SIZE, y * SQUARE_SIZE + 60, has_bomb))
    grid.append(row)

# Determine proximity values for each square
for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        square = grid[y][x]
        if square.has_bomb:
            continue
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if x + dx < 0 or x + dx >= GRID_WIDTH:
                    continue
                if y + dy < 0 or y + dy >= GRID_HEIGHT:
                    continue
                if grid[y + dy][x + dx].has_bomb:
                    square.proximity += 1

# Set up the game screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Minesweeper")

# Start the game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = (y - 60) // SQUARE_SIZE
            col = x // SQUARE_SIZE
            grid[row][col].clicked = True

    # Draw the squares
    for row in grid:
        for square in row:
            square.display()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
