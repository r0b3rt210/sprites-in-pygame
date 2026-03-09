import pygame
HEIGHT = 600
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space invaders")
ship1 = pygame.image.load(r"space invaders\images\ship1.png")
ship2 = pygame.image.load(r"space invaders\images\ship2.png")
backg = pygame.image.load(r"space invaders\images\bg.png")
run = True
while run == True:
    screen.blit(backg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()s