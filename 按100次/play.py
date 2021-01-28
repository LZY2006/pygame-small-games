import sys,pygame
import pygame.freetype

pygame.init()
size = 600,400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Python游戏")

Green = pygame.Color("green")
White = pygame.Color("white")
Red = pygame.Color("red")

font = pygame.freetype.Font(r"c:\windows\fonts\msyh.ttf",size=50)


def wait():
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return


num=100
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == 13:
                if num<1:
                    
                    screen.fill(White)
                    surface, rect = font.render("恭喜你过关!!!", Red)
                    screen.blit(surface,(100,170))
                    pygame.display.update()
                    wait()
                    pygame.quit()
                    sys.exit()
                else:
                    num-=1

    screen.fill(White)
    surface, rect = font.render("请按回车键{}次".format(num), Green)
    screen.blit(surface,(100,170))
    pygame.display.update()
