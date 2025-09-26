# Example file showing a circle moving on screen

import pygame # import the module
import random

WIDTH = 1200
HEIGHT = 720

# pygame setup
pygame.init() # initialise the module
screen = pygame.display.set_mode((1280, 720)) # numbers show width and height, everything is shown on the pygame official documentation
clock = pygame.time.Clock()
running = True
dt = 0      

class Boid:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x,y)

    def draw (self, screen):
        top = pygame.Vector2(self.position.x,self.position.y)
        right = pygame.Vector2(self.position.x+2,self.position.y+2)
        left = pygame.Vector2(self.position.x+2,self.position.y+2)
        pygame.draw.polygon(screen, "green", [top, left, right], 2)


def create_boids(total_num_boids):

    boids_list = []
    for newBoid in range(total_num_boids):
        newBoid = [Boid(random.uniform(0,WIDTH), random.uniform(0, HEIGHT))]
        boids_list.append(newBoid)

    boids_list = [Boid(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)) for _ in range(total_num_boids)]
    return boids_list

def main():

    boids = create_boids(100)
    running = True

    while running:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                running = False

        screen.full ("fuschia")

        for boid in boids:
            boid.draw(screen)

        pygame.display.flip()

        dt = clock.tick (60)/1000

#pygame.quit()