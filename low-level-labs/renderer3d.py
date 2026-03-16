import pygame
import math

WIDTH, HEIGHT = 800, 600

vertices = [
(-1,-1,1),
(1,-1,1),
(1,1,1),
(-1,1,1),
(-1,-1,-1),
(1,-1,-1),
(1,1,-1),
(-1,1,-1)
]

edges = [
(0,1),(1,2),(2,3),(3,0),
(4,5),(5,6),(6,7),(7,4),
(0,4),(1,5),(2,6),(3,7)
]

def rotate(vertex, angle):
    x,y,z = vertex
    cos = math.cos(angle)
    sin = math.sin(angle)
    return (x*cos - z*sin, y, x*sin + z*cos)

def project(vertex):
    x,y,z = vertex
    f = 200/(z+3)
    return (int(x*f+WIDTH/2), int(y*f+HEIGHT/2))

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

angle = 0

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0,0,0))

    rotated = [rotate(v,angle) for v in vertices]
    projected = [project(v) for v in rotated]

    for edge in edges:
        pygame.draw.line(screen,(255,255,255),
                         projected[edge[0]],
                         projected[edge[1]])

    pygame.display.flip()
    angle += 0.01
