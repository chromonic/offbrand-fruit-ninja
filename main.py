import random
import pygame

from fruit import Fruit 
from fruit_slice import FruitSlice
#from bomb import Bomb

pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Consolas', 30)


class App:
    def __init__(self):
        self.width, self.height = 700,500
        self.window = pygame.display.set_mode((self.width, self.height))
        self.bg_img_tile = pygame.image.load("assets/bg_tile.png")
        self.bg_img_tile = pygame.transform.scale(self.bg_img_tile, (64,64))
        self.clock = pygame.time.Clock()

        self.fruits = []
        self.slices = []
        #self.bombs = []
        self.score = 0
        self.max_fruits = 3

    def fill_wallpaper(self):
        for y in range(0,self.height, 64):
            for x in range(0,self.width, 64):
                self.window.blit(self.bg_img_tile, (x, y))

    def create_slices(self, frt:Fruit):
        angle = random.randint(0,45)
        self.slices.append(FruitSlice(frt.x, frt.y, frt.size, frt.xvel, frt.yvel,
                                      angle))
        self.slices.append(FruitSlice(frt.rect.midtop[0], frt.y, frt.size, -frt.xvel, frt.yvel, -angle))
    
#    def create_bombs(self):
#        if len(self.bombs) < 1: #and random.random() < 90:
#            self.bombs.append(Bomb(
#                random.randint(100, self.width-100),
#                self.height-15,
#                random.randint(100,self.width-100),
#                25,
#            ))
#    
#    def manage_bombs(self):
#        for bomb in self.bombs:
#            bomb.update()
#            bomb.render(self.window)
#            if bomb.rect.top >= self.height:
#                self.bombs = list(filter(lambda x: x!=bomb, self.bombs))

    def manage_slices(self):
        for slice in self.slices:
            slice.update()
            slice.render(self.window)
            if (slice.rect.top >= self.height):
                self.slices = list(filter(lambda x: x!=slice, self.slices))
    
    def manage_fruits(self):
        if len(self.fruits) < self.max_fruits:
            self.fruits.append(Fruit(
                random.randint(100,self.width-100),
                self.height-15,
                30,
                random.choice([random.randint(-8, -1), random.randint(1,8)]),
                random.randint(30,40)
            ))
        
        for fruit in self.fruits:
            fruit.update()
            fruit.render(self.window)
            
            # removal
            if (fruit.rect.top >= self.height):
                self.fruits = list(filter(lambda x: x != fruit,self.fruits))
            elif (pygame.mouse.get_pressed()[0] and 
                  fruit.rect.collidepoint( pygame.mouse.get_pos() )):
                self.score += 1
                self.create_slices(fruit)
                self.fruits = list(filter(lambda x: x != fruit,self.fruits))


    def show_score(self):
        textsurface = myfont.render(f'Score: {self.score}', False, (0, 255, 0))
        self.window.blit(textsurface,(0,0))

    def mainloop(self):
        self.running = True
        while self.running:
            self.clock.tick(30)
            self.fill_wallpaper()

            self.manage_fruits()
            self.manage_slices()
            #self.create_bombs()
            #self.manage_bombs()
            self.show_score()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        pygame.quit()

app = App()
app.mainloop()
