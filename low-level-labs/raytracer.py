import numpy as np
from PIL import Image

WIDTH = 400
HEIGHT = 300

camera = np.array([0,0,-1])
light = np.array([5,5,-10])

sphere_center = np.array([0,0,3])
sphere_radius = 1

image = np.zeros((HEIGHT,WIDTH,3))

for y in range(HEIGHT):
    for x in range(WIDTH):

        px = (x/WIDTH)*2 -1
        py = (y/HEIGHT)*2 -1

        ray = np.array([px,py,1])
        ray = ray/np.linalg.norm(ray)

        oc = camera - sphere_center

        a = np.dot(ray,ray)
        b = 2*np.dot(oc,ray)
        c = np.dot(oc,oc)-sphere_radius**2

        discriminant = b*b-4*a*c

        if discriminant > 0:
            t = (-b - np.sqrt(discriminant))/(2*a)

            hit = camera + ray*t
            normal = (hit-sphere_center)
            normal = normal/np.linalg.norm(normal)

            light_dir = light-hit
            light_dir = light_dir/np.linalg.norm(light_dir)

            brightness = max(np.dot(normal,light_dir),0)

            image[y,x] = [brightness]*3

img = Image.fromarray((image*255).astype(np.uint8))
img.save("render.png")
