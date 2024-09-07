# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    #test = pygame.display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #test.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # game loop
    while True:
        #code copy for quite
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255,255,255)) 
        pygame.display.flip
        # test.flip

    pass


if __name__ == "__main__":
    main()