import pygame
from constants import *
from player import *

print("Starting Asteroids!")
print(SCREEN_WIDTH)
print(SCREEN_HEIGHT)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000  # Get delta time in seconds
        player.move(dt)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()