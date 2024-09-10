from circleshape import *
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius) 
        pass

    def update(self, dt):
       self.position = self.position + (self.velocity * dt)
    pass