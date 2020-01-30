# create pygame window

import sys

import pygame

from settings import Settings

"""
First, we import the sys and pygame modules. The pygame module con- tains the functionality needed to make a game. We’ll use the sys module to exit the game when the player quits.

"""

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()

    # The line pygame.init() initializes background settings that Pygame needs to work properly

    ai_settings = Settings()


    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # a tuple

    # we call pygame.display.set_mode() to create a display window called screen, on which we’ll draw all of the game’s graphical elements


    pygame.display.set_caption("Alien Invasion")

    # Set the background color

#     bg_color = (230, 230, 230)
    # colors in pygame are in rgb

    # Set main loop

    while True:

        # Watch for keyboard and mouse events

        screen.fill(ai_settings.bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Make the most recently drawn screen visible
        pygame.display.flip()

run_game()