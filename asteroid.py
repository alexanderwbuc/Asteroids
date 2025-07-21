import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.rotation += 0.1 * dt  # Rotate slowly for visual effect
        self.rotation %= 360