import pygame, sys
from settings import Settings
from wall import Wall
from wall2 import Wall2
import game_function as g_f
from ball import Ball


def init_game():
    pygame.init()

    game_settings = Settings()

    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    wall = Wall(screen)
    wall2 = Wall2(screen)
    ball = Ball(screen)


    while True:
       g_f.check_events(game_settings, wall, wall2, ball , screen)
       g_f.update_screen(screen, game_settings,wall, wall2, ball)
       wall.update()
       wall2.update()
       ball.update()


init_game()
