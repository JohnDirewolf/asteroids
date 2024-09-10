from circleshape import *
from constants import *
import pygame

#Player Class
class Player (CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
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

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        pass

    def shoot(self):
        print(self.shot_timer)
        if self.shot_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        pass

    def update(self, dt):
        keys = pygame.key.get_pressed()

        #Update shot timer
        self.shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        pass 

    pass

class Shot(CircleShape):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2) 
        pass

    def update(self, dt):
        self.position += self.velocity * dt
    
    pass