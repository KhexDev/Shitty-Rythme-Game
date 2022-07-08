import pygame
pygame.init()

class Receptor(pygame.sprite.Sprite):
    def __init__(self, imagePath):
        self.daImage = pygame.image.load(imagePath)
        self.rect = self.daImage.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.imagePath = imagePath