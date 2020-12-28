import pygame
import random
import sys
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 20
HEIGHT = 20
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCALE = SCREEN_WIDTH / WIDTH

class Cell:

    def __init__(self):
        self.state = random.randint(0, 1)
    
    def __repr__(self):
        return f'{self.state}'

    def update_state(self, neighbors):
        sum = 0
        for cell in neighbors:
            sum += cell.state
        if self.state == 1:
            if sum <= 1 or sum >= 4:
                self.state = 0
        else:
            if sum == 3:
                self.state = 1
        
class Grid:
    
    def __init__(self, width=WIDTH, height=HEIGHT, scale=SCALE):
        self.width = width
        self.height = height
        self.scale = scale
        # self.grid = [[Cell() for cell in range(10)] for row in range(10)]
        self.grid = {(x, y): Cell() for x in range(self.width) for y in range(self.height)}
    
    def draw(self):
        for coordinate, cell in self.grid.items():
            if cell.state == 1:
                x, y = coordinate[0], coordinate[1]
                rect = pygame.Rect(x*self.scale, y*self.scale, self.scale, self.scale)
                pygame.draw.rect(screen, BLACK, rect)

    
    def update(self):
        for coordinate, cell in self.grid.items():
            x, y = coordinate[0], coordinate[1]
            neighbors = self.get_neighbors(x, y)
            cell.update_state(neighbors)
                                
    def get_neighbors(self, x, y):
        for x, y in [(x+i, y+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
            if (x, y) in self.grid:
                yield self.grid[(x, y)]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
grid = Grid()
grid.draw()
pygame.display.update()

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    screen.fill(WHITE)
    grid.update()
    grid.draw()
    pygame.display.update()

    pygame.time.wait(500)