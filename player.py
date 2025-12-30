import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        # This method just moves forward/backward based on dt
        # Positive dt = forward, negative dt = backward
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = velocity  # Set velocity AFTER creating the shot
        return shot

    shot_cd = 0

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)   # Rotate right
        
        # Movement
        if keys[pygame.K_w]:
            self.move(dt)      # Move forward
        if keys[pygame.K_s]:
            self.move(-dt)     # Move backward (negate dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cd > 0:
                self.shot_cd -= dt
                return None
            else:
                self.shot_cd = PLAYER_SHOOT_COOLDOWN_SECONDS
                return self.shoot()
