import pygame, sys
import pygame.freetype
from pygame.locals import *
import time
import os
import base64 as ba

def load_image(path):
    
    with open(path, "rb") as f1:
        x = f1.read()
    x = ba.decodestring(x)

    with open("$"+path, "wb") as f2:
        f2.write(x)

    surface = pygame.image.load("$"+path).convert()
    os.remove("$"+path)
    return surface

pygame.init()
pygame.mixer.init()

RED = 255, 0, 0
WHITE = 255, 255, 255

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("模拟病毒")

font = pygame.freetype.Font("C:\Windows\Fonts\msyh.ttc", size=50)
sur, rect = font.render("大坑待填...", RED)
rect.center = width//2, height//2

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            running = False
    
    if running:
        screen.fill(WHITE)
        screen.blit(sur, rect)

        pygame.display.update()
        clock.tick(10)

time.sleep(10)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(size)

img = load_image("image.bas")

with open("sound.bas", "rb") as f1:
    x = f1.read()
x = ba.decodestring(x)

with open("$sound.wav", "wb") as f2:
    f2.write(x)

sound = pygame.mixer.Sound("$sound.wav")
os.remove("$sound.wav")

sound.play()
num = 0
while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    screen.blit(img, (0, 0))

    if num > 80:
        pygame.quit()
        sys.exit()
    else:
        num += 1

    pygame.display.update()
    clock.tick(10)