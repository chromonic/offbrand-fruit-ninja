import pygame

#appears upon clicking on a fruit 
class FruitSlice:
    def __init__(self, x:int, y: int, size: int, xvel:int, yvel: int, rot:int):
        self.x, self.y, self.size, self.xvel, self.yvel = x, y, size, xvel, yvel
        self.surface = pygame.Surface((self.size//2, self.size), pygame.SRCALPHA)
        self.surface.fill((100,100,100))
        self.surface = pygame.transform.rotate(self.surface, self.xvel+rot)
    def update(self):
        self.x += self.xvel * (5*(abs(self.xvel) <= 5))
        self.y -= self.yvel - (15*self.yvel <= 5) * 0.5
        self.yvel -= 2

    def render(self, surf):
        self.rect = pygame.Rect(self.x, self.y, self.size//2, self.size)
        surf.blit(self.surface, (self.x, self.y))
        

