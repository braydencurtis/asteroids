# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

#import the classes we need
from asteroid import *
from constants import *
from player import *
from asteroidfield import *

def main():
    # Initialize pygame
    pygame.init()
    
    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Set the frame rate and get dt
    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    # Create the asteroid field
    asteroid_field = AsteroidField()
    

    # Create the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update all ubdatable game objects
        updatable.update(dt)
        
        # Check for collisions between the player and asteroids
        for asteroid in asteroids:
            if asteroid.collision_detect(player):
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision_detect(bullet):
                    bullet.kill()
                    asteroid.kill()
                    break
        
        # Draw all drawable game objects
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)  # Assuming each entity has a draw method that takes the screen
        pygame.display.flip()

        # Limit the frame rate
        # and get dt
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()