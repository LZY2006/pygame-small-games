import pygame, sys
from pygame.locals import *
import traceback
import jaime

pygame.init()
pygame.mixer.init()

BLACK = pygame.Color("black")

speed = [2, 0]
size = width, height = 600, 400
screen = pygame.display.set_mode(size, RESIZABLE)
pygame.display.set_caption("Jaime walking --- Lee Demo")
clock = pygame.time.Clock()

jme = jaime.Jaime(speed, size, [0, 0])

index = 0
num = 360
pos = [0, 0]
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, RESIZABLE)
            size = width, height = event.size
            jme = jaime.Jaime(speed, size, pos, jme.turn)
    
    screen.fill(BLACK)

    jme.move()
    pos = jme.rect.left, jme.rect.top
    screen.blit(jme.image_list[index], jme.rect)
    pygame.display.update()
    clock.tick(30)
    if not (num % 5):
        if index >= 4:
            index = 0
        else:
            index += 1
    if num <= 0:
        num = 360
    else:
        num -= 1