from circleshape import *
import pygame
from constants import *
from asteroid import Asteroid

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (int(self.position.x), int(self.position.y)), SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
