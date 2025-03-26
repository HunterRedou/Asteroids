import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 4)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        
        self.position += self.velocity*dt
        
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            one = self.velocity.rotate(random_angle)
            two = self.velocity.rotate(-random_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            
            astro_one = Asteroid(self.position.x, self.position.y, new_rad)
            astro_two = Asteroid(self.position.x, self.position.y, new_rad)
            
            astro_one.velocity = one*1.5
            astro_two.velocity = two*1.5
            
            