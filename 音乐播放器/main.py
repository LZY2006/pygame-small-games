import sys
import time
from os import path, sep, walk

import pygame
import pygame.freetype
from pygame.locals import *

# 初始化pygame和pygame的混音器
pygame.init()
pygame.mixer.init()

#设置screen变量
size = width, height = 300, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("music play --- Lee demo")
clock = pygame.time.Clock()

# 定义颜色
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0

# 寻找所有的音乐文件
def find_musics():
    
    for path, dirs, files in walk("musics"):
        for name in files:
            file = path + sep + name
            yield file

# 载入图片
play = pygame.image.load("play.png").convert_alpha()
play_rect = play.get_rect()
play_rect.center = width // 2, height - play_rect.height // 2
pause = pygame.image.load("pause.png").convert_alpha()
pause_rect = pause.get_rect()
pause_rect.center = width // 2, height - pause_rect.height // 2

# 载入音乐
font = pygame.freetype.Font("msyh.ttc", size = 15)
music_list = find_musics()
music_list = list(music_list)

font_text_list = []
musics = []
for each in music_list:
    
    #获取歌名
    name = path.split(path.splitext(each)[0])[1]

    music_num = 0
    musics.append(name)
    if each == music_list[music_num]:
        sur, rect = font.render(name, RED)
        font_text_list.append(sur)
    else:
        sur, rect = font.render(name, BLACK)
        font_text_list.append(sur)

pygame.mixer.music.load(music_list[music_num])
pygame.mixer.music.play()
MUSICPLAYDONE = USEREVENT
pygame.mixer.music.set_endevent(MUSICPLAYDONE)
isplay = True
restart = False, None

running = True
while running:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == ord(" "):
                if isplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

                isplay = not isplay
            
            elif event.key == K_DOWN:
                restart = True, 'DOWN'

            elif event.key == K_UP:
                restart = True, 'UP'
        
        elif event.type == MUSICPLAYDONE:
            
            music_num += 1
            try:
                pygame.mixer.music.load(music_list[music_num])
            except IndexError:
                music_num -= 1
            else:
                pygame.mixer.music.play()
            
                font_text_list = []
                for each in music_list:
                    name = path.split(path.splitext(each)[0])[1]
                    if each == music_list[music_num]:
                        sur, rect = font.render(name, RED)
                        font_text_list.append(sur)
                    else:
                        sur, rect = font.render(name, BLACK)
                        font_text_list.append(sur)
        elif restart[0]:
            if restart[1] == 'DOWN':
                music_num += 1
                try:
                    pygame.mixer.music.load(music_list[music_num])
                except IndexError:
                    music_num -= 1
                else:
                    pygame.mixer.music.play()
                
                    font_text_list = []
                    for each in music_list:
                        name = path.split(path.splitext(each)[0])[1]
                        if each == music_list[music_num]:
                            sur, rect = font.render(name, RED)
                            font_text_list.append(sur)
                        else:
                            sur, rect = font.render(name, BLACK)
                            font_text_list.append(sur)
                restart = False, None

            elif restart[1] == 'UP':
                
                if music_num - 1 >= 0:
                    music_num -= 1
                    pygame.mixer.music.load(music_list[music_num])
                    
                    pygame.mixer.music.play()
                        
                    font_text_list = []
                    for each in music_list:
                        name = path.split(path.splitext(each)[0])[1]
                        if each == music_list[music_num]:
                            sur, rect = font.render(name, RED)
                            font_text_list.append(sur)
                        else:
                            sur, rect = font.render(name, BLACK)
                            font_text_list.append(sur)
                restart = False, None

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and play_rect.collidepoint(event.pos[0], event.pos[1]):
                if isplay:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                isplay = not isplay
                
    #将页面刷成白色
    screen.fill(WHITE)

    #显示暂停/继续图标
    if isplay:
        #screen.blit(pause, (width//2 - pause_rect.width, height//2 - pause_rect.height))
        screen.blit(pause, pause_rect)
    else:
        #screen.blit(play, (width//2 - play_rect.width, height//2 - play_rect.height))
        screen.blit(play, play_rect)

    #显示选项
    num = 0
    for each in font_text_list:
        
        screen.blit(each, (0, num*15))
        num += 1

    pygame.display.update()
    clock.tick(10)

pygame.mixer.music.stop()
time.sleep(5)
