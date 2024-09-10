from circleshape import *
from constants import *
import pygame

#Player Class
class Player (CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        pass

    # Code Paste, define the triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #print(f"self.triangle {self.triangle()}")
        pygame.draw.polygon(screen, "white", self.triangle(), 2) 
        pass

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
        pass

    def update(self, dt):
        keys = pygame.key.get_pressed()

        print("Key Press!")

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        pass 

    pass