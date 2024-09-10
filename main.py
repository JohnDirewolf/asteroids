# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pyClock = pygame.time.Clock()
    dt = 0
    #test = pygame.display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #test.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Initiate Player Sprite
    player_ship = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    player_ship.draw(screen)

    # game loop
    while True:
        #code copy for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill screen with black
        screen.fill("black") 

        #Check for keypress to move player ship
        player_ship.update(dt)

        # render player ship
        player_ship.draw(screen)

        pygame.display.flip()
        # test.flip

        #Tick
        dt = pyClock.tick(60) / 1000

    pass


if __name__ == "__main__":
    main()