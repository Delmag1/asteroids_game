import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField 

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawables, updatables,)
    Asteroid.containers = (asteroids, drawables, updatables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, drawables, updatables)
    asteroid_field = AsteroidField()
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000  # Get delta time in seconds
        player.move(dt)
        player.update(dt)
        player.draw(screen)
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)

        # Check for collisions
        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                print(f"Score: {score}")
                sys.exit()
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
                    score +=  1
        pygame.display.flip()  
if __name__ == "__main__":
    main()