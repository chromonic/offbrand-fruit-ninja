import pygame
import random

class Fruit:
    def __init__(self, x:int, y:int, yvel:int, xvel:int, size:int = 30):
        self.x, self.y, self.yvel, self.xvel = x, y, yvel, xvel
        self.size = size
        self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.image = pygame.image.load(random.choice(["assets/watermelon.png",
                                                      "assets/tomato.png"]))
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.surface.blit(self.image, (0,0))
        self.surface = pygame.transform.rotate(self.surface,
                                               self.xvel) 

    def update(self):
        self.x += self.xvel
        self.y -= self.yvel * 0.5
        self.yvel -= 1

    def render(self, surf):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        surf.blit(self.surface, (self.x, self.y))
