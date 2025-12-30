import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids with pygame version: VERSION =", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)

    Asteroid.containers = (asteroids, updatable, drawable)
    
    Player.containers = (updatable, drawable)

    Shot.containers = (shots, updatable, drawable)

    # Important: player must be a local variable in main()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        dt = clock.tick(60) / 1000.0
        
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print ("Game Over!")
                sys.exit()
                running = False
        
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        
        
        
        # Call with NO arguments - it inspects local variables automatically
        log_state()
    
    pygame.quit()

if __name__ == "__main__":
    main()