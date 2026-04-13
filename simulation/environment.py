import random

def create_grid(rows, cols, obstacle_prob=0.1):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if random.random() < obstacle_prob:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid