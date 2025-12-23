import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return

pygame.init()
number = 1
while number > 0:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")
    pygame.display.flip()

def main():
    print("Starting Asteroids with pygame version: VERSION =", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")   

if __name__ == "__main__":
    main()
