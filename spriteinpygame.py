import pygame
WIDTH = 750
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("rocket blasting to space")
stars = pygame.image.load(r"rocketinspcace\image\a.png")
rocketimg = pygame.image.load(r"rocketinspcace\image\b.png")
class Rocket(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        super().__init__()
        self.image = rocketimg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
   
rocket=Rocket(350,50)   
rocketgroup = pygame.sprite.Group()
rocketgroup.add(rocket)
rocketgroup.add(rocket)
run = True
while run == True:
    screen.blit(stars,(0,0))
    rocketgroup.draw(screen) 
    key_press = pygame.key.get_pressed()
    
    
    if key_press[pygame.K_UP]:
        rocket.rect.y = rocket.rect.y - 10

    if key_press[pygame.K_DOWN]:
        rocket.rect.y = rocket.rect.y +10
    
    if key_press[pygame.K_LEFT]:
        rocket.rect.x = rocket.rect.x - 10

    if key_press[pygame.K_RIGHT]:
        rocket.rect.x = rocket.rect.x + 10

    if rocket.rect.right >= WIDTH:
        rocket.rect.right = WIDTH

    if rocket.rect.top <= 0:
        rocket.rect.top = 1

    if rocket.rect.bottom >= HEIGHT:
        rocket.rect.bottom = HEIGHT

    if rocket.rect.left <= 0:
        rocket.rect.left = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
            
        
            
    
    pygame.display.update()