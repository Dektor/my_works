import pygame

class Player1():
    def __init__(self, screen):
        self.screen=screen

        self.image = pygame.image.load("images/player1.png")
        self.image=pygame.transform.scale(self.image, (50,150))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.right=self.screen_rect.right
        self.rect.bottom=self.screen_rect.bottom

        self.moving_right = False
        self.moving_left =  False
        self.moving_down = False
        self.moving_up = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
           self.rect.centerx += 2
        if self.moving_left and self.rect.left > 0:
           self.rect.centerx -= 2
        if self.moving_down and self.rect.bottom< self.screen_rect.bottom:
           self.rect.bottom += 2
        if self.moving_up and self.rect.top > 0:
           self.rect.bottom -= 2

