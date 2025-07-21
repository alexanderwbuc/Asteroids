import pygame
from constants import *
from circleshape import CircleShape
import random


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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            one_direction = self.velocity.rotate(new_angle)
            second_direction = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = one_direction
            asteroid2.velocity = second_direction
            return [asteroid1, asteroid2]

        