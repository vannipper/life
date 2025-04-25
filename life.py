import pygame
from Particle import Particle
from screeninfo import get_monitors
import time
import random
import os

# MONITORS INITIALIZATION
monitors = get_monitors()

# DISPLAY INITIALIZATION
resx = monitors[0].width - 100
resy = monitors[0].height - 100

# PYGAME INITIALIZATION
pygame.init()
screen = pygame.display.set_mode((resx, resy))
pygame.display.set_caption('PyPhysics')
FPS = 60

# Initialize simulation variables
num_types = 4
num_particles = 100
colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 0, 255), (255, 165, 0), (255, 255, 0)]
colors = colors[:num_types]
forces = [[random.choice([1, -1]) for _ in range(num_types)] for _ in range(num_types)]
size = 12
particles = [Particle(random.randint(0, resx), random.randint(0, resy), size, random.choice(colors), forces) for _ in range(num_particles)]

# GAME LOOP
running = True
while running: # runtime will be measured in units per tick/frame

    start_time = time.time() # measure how long it takes to run all calculations

    # EVENT DETECTION (input)
    for event in pygame.event.get():

        if event.type == pygame.QUIT: # quit detection
            running = False
            
        if event.type == pygame.KEYDOWN: # check for specific key presses

            if event.key == pygame.K_SPACE:  # reset anchor
                anchorx = 0
                anchory = 0

            if event.key == pygame.K_ESCAPE:  # Check if 'ESC' key is pressed
                running = False  # Exit the loop and quit the game

    # SCREEN / DISPLAY LOGIC
    screen.fill((0, 0, 0))  # Clear screen

    # Physics update
    for particle in particles:
        particle.move(particles, resx, resy)

    # Update screen objects
    for particle in particles:
        particle.draw(screen, resx, resy)

    # GAME TICK UPDATE
    pygame.display.flip() # Update display
    time.sleep(max(1/FPS - time.time() + start_time, 0))
    stop_time = time.time() - start_time
    pygame.display.set_caption('PyPhysics | FPS: ' + str(1/stop_time)[:5])

os.system('clear')
pygame.quit()