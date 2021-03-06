import pygame , sys
from settings import Settings
from wall import Wall
from wall2 import Wall2

class Ball():
    def __init__(self, screen):
        self.screen=screen

        self.wall = Wall(screen)
        self.wall2 = Wall2(screen)

        self.image = pygame.image.load("images/ball.png")
        self.image=pygame.transform.scale(self.image, (50,50))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()


        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery

        self.moving_ball_right = True
        self.moving_ball_left= False




    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        if self.moving_ball_right and self.rect.right > self.screen_rect.left:
           self.rect.centerx += 5

        if self.rect.right == self.wall2.rect.left :
           self.moving_ball_right = False
           self.moving_ball_left = True
        elif self.rect.right == self.screen_rect.right:
            sys.exit()


        if self.moving_ball_left and self.rect.left > 0:
           self.rect.centerx -= 5

        if self.rect.left == self.wall.rect.right:
           self.moving_ball_left = False
           self.moving_ball_right = True

