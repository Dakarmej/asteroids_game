import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from logger import log_state


def main():
    print("Starting Asteroids with pygame version: VERSION =", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Important: player must be a local variable in main()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000.0
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        
        
        
        # Call with NO arguments - it inspects local variables automatically
        log_state()
    
    pygame.quit()

if __name__ == "__main__":
    main()