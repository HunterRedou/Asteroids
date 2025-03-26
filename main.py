import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot





def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_lock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_all = pygame.sprite.Group()
    shot_all = pygame.sprite.Group()
    Asteroid.containers = (asteroids_all, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (shot_all, updatable, drawable)
    player = Player(x, y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = fps_lock.tick(60)/1000
        updatable.update(dt)
        
        pygame.Surface.fill(screen, (0, 0, 0))#Black background
        for drawa in drawable:
            drawa.draw(screen)
            
        for astro in asteroids_all:
            if astro.collision(player):
                print("Game Over!")
                return
            
        for astro in asteroids_all:
            for shot in shot_all:
                if shot.collision(astro):
                    shot.kill()
                    astro.split()
        
        pygame.display.flip()
        
        #limits the FPS
        
        
    
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    


if __name__ == "__main__":
    main()