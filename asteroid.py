import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH
from logger import log_event, log_state
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
    
    # Don't split if already at minimum size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
    
    # Log the split event
        log_event("asteroid_split")
    
    # Calculate random angle for splitting
        angle = random.uniform(20, 50)
    
    # Calculate new radius for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
    # Create two child asteroids with independent velocity vectors
        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child1.velocity = self.velocity.copy().rotate(angle)  # Use .copy()!
    
        child2 = Asteroid(self.position.x, self.position.y, new_radius)
        child2.velocity = self.velocity.copy().rotate(-angle)  # Use .copy()!