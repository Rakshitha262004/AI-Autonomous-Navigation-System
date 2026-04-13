import pygame
import sys
import os

# Fix imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulation.environment import create_grid
from algorithms.astar import astar
from simulation.agent import Agent

# Grid settings
ROWS, COLS = 20, 20
CELL_SIZE = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)    # Agent
RED = (255, 0, 0)      # Goal
BLUE = (0, 0, 255)     # Path
YELLOW = (255, 255, 0) # Start
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((COLS * CELL_SIZE, ROWS * CELL_SIZE))
pygame.display.set_caption("AI Autonomous Navigation System")

# Create grid
grid = create_grid(ROWS, COLS, obstacle_prob=0.1)

# Start and goal
start = (0, 0)
goal = (19, 19)

grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0

# Agent
agent = Agent(start)

clock = pygame.time.Clock()
reached_goal = False

def draw(path):
    screen.fill(GRAY)

    for i in range(ROWS):
        for j in range(COLS):
            color = WHITE
            if grid[i][j] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw path
    if path:
        for step in path:
            pygame.draw.rect(screen, BLUE, (step[1]*CELL_SIZE, step[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw start, goal, agent
    pygame.draw.rect(screen, YELLOW, (start[1]*CELL_SIZE, start[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (goal[1]*CELL_SIZE, goal[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (agent.position[1]*CELL_SIZE, agent.position[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.update()

running = True

while running:
    clock.tick(10)  # control speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 🖱️ LEFT CLICK → ADD OBSTACLE
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        row, col = y // CELL_SIZE, x // CELL_SIZE

        if (row, col) != start and (row, col) != goal:
            grid[row][col] = 1
            reached_goal = False   # restart movement

    # 🖱️ RIGHT CLICK → REMOVE OBSTACLE
    if pygame.mouse.get_pressed()[2]:
        x, y = pygame.mouse.get_pos()
        row, col = y // CELL_SIZE, x // CELL_SIZE
        grid[row][col] = 0
        reached_goal = False

    # 🔥 Recalculate path dynamically
    path = astar(grid, agent.position, goal)

    # 🚗 Continuous movement
    if path and not reached_goal:
        agent.move(path[0])

        if agent.position == goal:
            print("Goal Reached!")
            reached_goal = True

    draw(path)

pygame.quit()