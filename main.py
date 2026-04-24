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
    font = pygame.font.SysFont(None, 48)
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
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
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
               
               
                font = pygame.font.SysFont(None, 48)
                game_over_text = font.render("Game Over!", True, (255, 0, 0))
                score_text = font.render(f"Score: {score}", True, (255, 255, 255))
                prompt_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

                screen.fill((0, 0, 0))
                screen.blit(game_over_text, (100, 100))
                screen.blit(score_text, (100, 200))
                screen.blit(prompt_text, (100, 300))
                pygame.display.flip()

                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                waiting = False  # Restart game
                            elif event.key == pygame.K_q:
                                pygame.quit()
                                exit()

            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
                    score +=  1
        pygame.display.flip()  
if __name__ == "__main__":
    main()