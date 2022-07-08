import pygame

from Conductor import Conductor
pygame.init()

class Note(pygame.sprite.Sprite):

    def __init__(self, strumTime, noteData):
        self.data = ["purple", "blue", "green", "red"]
        self.strumTime = strumTime
        self.noteData = noteData
        self.daImage = pygame.image.load("images/" + self.data[noteData] + ".png")
        self.rect = self.daImage.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.safeFrames = [50]
        self.canBeHit = False
