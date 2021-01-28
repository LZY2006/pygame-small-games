import pygame,sys

pygame.init()
size=w,h=600,400

screen=pygame.display.set_mode(size)
pygame.display.set_caption("KeyDown")

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:

            print("button:",event.button,"pos:",event.pos)
            
    pygame.display.update()