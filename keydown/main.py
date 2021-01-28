import pygame,sys

pygame.init()
size=w,h=600,400

screen=pygame.display.set_mode(size)
pygame.display.set_caption("KeyDown")

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()
        
        elif event.type == pygame.KEYDOWN:

            print("unicode:",event.unicode,"key:",chr(event.key),"mod:",event.mod)
            
    pygame.display.update()