import pygame
from constants import *
print("Starting Asteroids!")
print(SCREEN_WIDTH)
print(SCREEN_HEIGHT)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def game_loop():

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        pygame.display.flip()




if __name__ == "__main__":
    game_loop()