import pygame

class Jaime(pygame.sprite.Sprite):

    def __init__(self, speed, bg_size, pos, turn=False):
        pygame.sprite.Sprite.__init__(self)

        self.image_list = [
            pygame.image.load("images\\jaime walking-a.png").convert_alpha(),
            pygame.image.load("images\\jaime walking-b.png").convert_alpha(),
            pygame.image.load("images\\jaime walking-c.png").convert_alpha(),
            pygame.image.load("images\\jaime walking-d.png").convert_alpha(),
            pygame.image.load("images\\jaime walking-e.png").convert_alpha()
        ]
        self.speed = speed

        if turn:
            for i in range(len(self.image_list)):
                self.image_list[i] = pygame.transform.flip(self.image_list[i], True, False)

        self.rect = self.image_list[0].get_rect()
        self.rect.left, self.rect.top = pos

        self.width, self.height = bg_size
        self.turn = turn

    def move(self):

        if self.rect.left < 0 or self.rect.right > self.width:
            self.speed[0] = -self.speed[0]

            for i in range(len(self.image_list)):
                self.image_list[i] = pygame.transform.flip(self.image_list[i], True, False)
            self.turn = not self.turn

        self.rect = self.rect.move(self.speed[0], self.speed[1])