import pygame
import random

WIDTH = 100
HEIGHT = 80
CELL = 10

grid = [[random.randint(0,1) for x in range(WIDTH)] for y in range(HEIGHT)]

pygame.init()
screen = pygame.display.set_mode((WIDTH*CELL,HEIGHT*CELL))

def step():

    global grid

    new = [[0]*WIDTH for _ in range(HEIGHT)]

    for y in range(HEIGHT):
        for x in range(WIDTH):

            neighbors = 0

            for dy in [-1,0,1]:
                for dx in [-1,0,1]:

                    if dx==0 and dy==0:
                        continue

                    nx = x+dx
                    ny = y+dy

                    if 0<=nx<WIDTH and 0<=ny<HEIGHT:
                        neighbors += grid[ny][nx]

            if grid[y][x]==1 and neighbors in [2,3]:
                new[y][x]=1
            elif grid[y][x]==0 and neighbors==3:
                new[y][x]=1

    grid=new

while True:

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            exit()

    screen.fill((0,0,0))

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x]:
                pygame.draw.rect(screen,(255,255,255),
                                 (x*CELL,y*CELL,CELL,CELL))

    pygame.display.flip()
    step()
