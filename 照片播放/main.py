import pygame, sys, os, traceback
from PIL import Image
from pygame.locals import *

pygame.init()
pygame.mixer.init()

def get_files(top):
    targets = []
    for path, dirs, files in os.walk(top):
        for name in files:
            file = os.path.join(path, name)
            targets.append(file)
    return targets

size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("照片播放 --- Demo")

def main():

    # 获取所有照片的路径
    img_list = get_files("C:\\2017\\")
    index = 0

    # 载入音乐
    pygame.mixer.music.load("music.ogg")
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()

    num = 1000
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        image = Image.open(img_list[index])

        w, h = image.size
        if w > 2500:
            w, h = w//4, h//4
        elif w > 2000:
            w, h = w//3, h//3
        elif w > 1000 or h > 1000:
            w, h = w//2, h//2

        image = image.resize((w, h))
        try:
            image.save(img_list[index])
        except IndexError:
            pyame.mixer.music.fadeout(1000)
            pygame.quit()
            sys.exit()

        size = h, w

        screen = pygame.display.set_mode(size)
        img = pygame.image.load(img_list[index]).convert()
        img = pygame.transform.rotate(img, -90)
        screen.blit(img, (0, 0))

        if not(num % 40):
            index += 1
        if num <= 0:
            num = 1000
        num -= 1

        pygame.display.update()
        clock.tick(20)

try:
    main()
except SystemExit:
    pass
except:
    pygame.quit()
    traceback.print_exc()
    input()
