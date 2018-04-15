import pygame
from settings import Settings

class Wall():
    def __init__(self, screen):
        self.screen=screen

        self.image = pygame.image.load("images/wall2.png")
        self.image=pygame.transform.scale(self.image, (100,300))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.left=self.screen_rect.left
        self.rect.centery=self.screen_rect.centery

        #ggo = self.rect.left

        # self.moving_right = False
        # self.moving_left =  False
        self.moving_d = False
        self.moving_u = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
       # if self.moving_right and self.rect.right<self.screen_rect.right:
       #      self.rect.centerx += 5
       # if self.moving_left and self.rect.left > 0:
       #     self.rect.centerx -= 5
        if self.moving_d and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 5
        if self.moving_u and self.rect.top > 0:
            self.rect.bottom -= 5

