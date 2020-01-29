# create pygame window

import sys

import pygame

"""
First, we import the sys and pygame modules. The pygame module con- tains the functionality needed to make a game. We’ll use the sys module to exit the game when the player quits.

"""

def run_game():
    # Initialize game and create a screen object
    pygame.init()

    # The line pygame.init() initializes background settings that Pygame needs to work properly


    screen = pygame.display.set_mode((1200,800)) # a tuple

    # we call pygame.display.set_mode() to create a display window called screen, on which we’ll draw all of the game’s graphical elements


    pygame.display.set_caption("Alien Invasion")

    # Set the background color

    bg_color = (230, 230, 230)
    # colors in pygame are in rgb

    # Set main loop

    while True:

        # Watch for keyboard and mouse events

        screen.fill(bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Make the most recently drawn screen visible
        pygame.display.flip()

run_game()