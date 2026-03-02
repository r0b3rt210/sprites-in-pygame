import pygame
WIDTH = 750
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("rocket blasting to space")
stars = pygame.image.load(r"rocketinspcace\image\a.png")
rocketimg = pygame.image.load(r"rocketinspcace\image\b.png")
class Rocket(pygame.sprite.Sprite):
    def __init__(self,x ,y,):
        super().__init__()
        self.image = rocketimg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
   
rocket=Rocket(WIDTH//2 , HEIGHT//2)   
rocketgroup = pygame.sprite.Group()
rocketgroup.add(rocket)
run = True
while run == True:
    screen.blit(stars,(0,0))
    rocketgroup.draw(screen) 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.display.update()