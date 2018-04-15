import pygame

class Wall2():
    def __init__(self, screen):
        self.screen=screen

        self.image = pygame.image.load("images/wall2.png")
        self.image=pygame.transform.scale(self.image, (100,300))
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        self.rect.right=self.screen_rect.right
        self.rect.centery=self.screen_rect.centery

        #self.moving_r = False
        #self.moving_l =  False
        self.moving_down = False
        self.moving_up = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
      #  if self.moving_r and self.rect.right<self.screen_rect.right:
       #     self.rect.centerx += 5
        #if self.moving_l and self.rect.left > 0:
         #   self.rect.centerx -= 5
        if self.moving_down and self.rect.bottom< self.screen_rect.bottom:
            self.rect.bottom += 5
        if self.moving_up and self.rect.top > 0:
            self.rect.bottom -= 5

