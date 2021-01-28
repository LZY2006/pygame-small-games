import sys,pygame
import pygame.freetype as pf
import random
from os import sep

pygame.init()

size=600,400
screen=pygame.display.set_mode(size)
pygame.display.set_caption("pygame屏幕绘制")

BLACK=pygame.Color("white")
GOLD=pygame.Color("gold")
GREEN=pygame.Color("green")
RED=pygame.Color("red")

#msyh.ttc
Font=pf.Font("Fonts"+sep+"msyh.ttc", 50)
#surface ,rect= Font.render("你好,世界!", GOLD, size=50)
num=100
split = random.randint(30,70)
index=0
mouse = False
def wait():
    isbreak=False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    isbreak=True
        if isbreak:
            break

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            sys.exit()
        elif event.type == pygame.KEYDOWN:
            
            if event.key == 13 :
                
                if not mouse:
                    num-=1
                    index+=1
                else:
                    surface ,rect= Font.render("game over", RED, size=50)
                    nsurface ,nrect= Font.render("请按鼠标左键退出. . .", RED, size=20)
                    screen.fill(BLACK)
                    screen.blit(surface, (100,170))
                    screen.blit(nsurface, (100,220))
                    pygame.display.update()
                    wait()
                    pygame.quit()
                    sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and mouse:
                
                num-=1
                    
    if num<=1:
        
        surface ,rect= Font.render("恭喜过关!", GREEN, size=50)
        screen.fill(BLACK)
        screen.blit(surface, (100,170))
        pygame.display.update()
        wait()
        pygame.quit()
        sys.exit()

    if index == split:
        mouse=True

    screen.fill(BLACK)
    if mouse:
        surface ,rect= Font.render("请按鼠标左键{}下".format(num), GREEN, size=50)
    else:
        surface ,rect= Font.render("请按回车键{}下".format(num), GREEN, size=50)
    screen.blit(surface,(100,170))
    #screen.blit(surface,rect)
    pygame.display.update()
