# -*- coding: utf-8 -*-
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # initialize game and create screen object and settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_settings, screen)

    #make groups to store bullets in
    bullets = Group()

    # start the main loop for the game
    while True:
        # watch keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()