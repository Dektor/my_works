import pygame,sys

def check_events(game_settings,wall , wall2 , ball ,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key==pygame.K_UP:
                wall2.moving_up= True
            if event.key==pygame.K_DOWN:
                wall2.moving_down= True

        if event.type == pygame.KEYUP:

            if event.key==pygame.K_UP:
                wall2.moving_up = False
            if event.key==pygame.K_DOWN:
                wall2.moving_down = False

        if event.type == pygame.KEYDOWN:

            if event.key==pygame.K_w:
                wall.moving_u= True
            if event.key==pygame.K_s:
                wall.moving_d= True

        if event.type == pygame.KEYUP:

                if event.key == pygame.K_w:
                    wall.moving_u = False
                if event.key == pygame.K_s:
                    wall.moving_d = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                ball.moving_ball_right = True
            if event.key == pygame.K_o:
                ball.moving_ball_left = True


        if event.type == pygame.KEYUP:

            if event.key == pygame.K_p:
                ball.moving_ball_right = False
            if event.key == pygame.K_o:
                ball.moving_ball_left = False


def update_screen(screen, game_settings, wall, wall2, ball):
    pygame.display.flip()
    screen.fill(game_settings.bg_color)
    wall.blitme()
    wall2.blitme()
    ball.blitme()
