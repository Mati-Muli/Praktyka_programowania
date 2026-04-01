import random
import os
import time

HEIGH, WIDTH = 40, 40
def randomize():
    return[[random.choice([0,1]) for _ in range(WIDTH)] for _ in range(HEIGH)]

def neighbors_moore(grid,x,y):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if j==0 and i ==0:
                continue
            nx,ny = x+i,y+j
            if 0<=nx<HEIGH and 0 <=ny<WIDTH:
                count += grid[nx][ny]
    return count

def update(grid):
    new_grid=[[0 for _ in range(WIDTH)] for _ in range(HEIGH)]
    for x in range(HEIGH):
        for y in range(WIDTH):
            neighbors = neighbors_moore(grid,x,y)
            if grid[x][y] == 1:
                new_grid[x][y] = 1 if neighbors in [2,3] else 0
            else:
                new_grid[x][y] = 1 if neighbors==3 else 0
    return new_grid

def print_grid(grid):
    os.system('cls')
    out = []
    for row in grid:
        out.append(" ".join(['0' if cell == 1 else '.' for cell in row]))
    print("\n".join(out))

if __name__ == '__main__':
    grid = randomize()
    try:
        while True:
            print_grid(grid)
            grid = update(grid)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStop!")



