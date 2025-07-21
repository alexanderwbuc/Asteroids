import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *


def main():
    pygame.init()
    pygame.display.set_caption("Asteroids Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Create player and add to groups
    
    
 
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)

    AsteroidField.containers = updateable

    asteroid_field = AsteroidField()
  
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updateable.update(dt)

        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    print("Shot hit an asteroid!")
                    shot.kill()
                    asteroid.kill()
                    break
            if player.collides_with(asteroid):
                print("Collision detected!")
                print(f"Player position: {player.position}, Asteroid position: {asteroid.position}")
                print("Game Over!")
                running = False

        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

    


if __name__ == "__main__":
    main()
