# create pygame window

import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship


import game_functions as gf # game_functions imports sys

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

    #Make a ship
    ship = Ship(ai_settings, screen)    
    # Set the background color

#     bg_color = (230, 230, 230)
    # colors in pygame are in rgb

    # Set main loop

    #Make group to store bullets in
    bullets = Group()

    while True:

        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

        bullets.update()

        for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                        bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)


        

        

run_game()