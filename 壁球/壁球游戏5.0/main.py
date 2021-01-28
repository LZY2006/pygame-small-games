# Unit PYG03: Pygame Wall Ball Game version 8  鼠标型
import pygame, sys
from pygame.locals import *
from random import *
import traceback
import time
import pygame.freetype
import base64 as ba

class Ball(pygame.sprite.Sprite):

    def __init__(self, speed, bg_size, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("PYG02-ball.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos
        self.speed = speed
        self.width, self.height = bg_size
        self.radius = self.rect.width / 2

    def move(self):
        self.rect = self.rect.move(self.speed[0], self.speed[1])
        if self.rect.right < 0:
            self.rect.left = self.width

        if self.rect.left > self.width:
            self.rect.right = 0

        if self.rect.bottom < 0:
            self.rect.top = self.height

        if self.rect.top > self.height:
            self.rect.bottom = 0


pygame.init()
pygame.mixer.init()

size = width, height = 1000, 664
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ball game --- Lee demo")
clock = pygame.time.Clock()
def main():

    # 生成5个小球
    balls = []
    ball_group = pygame.sprite.Group()
    for i in range(5):
        speed = [randint(-6, 6), randint(-6, 6)]
        ball = Ball(speed, size, (randint(0, 1000), randint(0, 664)))
        while pygame.sprite.spritecollide(ball, ball_group, False, pygame.sprite.collide_circle) and not(ball.rect.collidepoint(pygame.mouse.get_pos())):
            ball.rect.left, ball.rect.top = randint(0, 1000), randint(0, 664)
        balls.append(ball)
        ball_group.add(ball)

    # 加载图片
    background = pygame.image.load("background.jpg").convert()
    mouse_image = pygame.image.load("mouse_image.png").convert_alpha()
    mouse_image = pygame.transform.flip(mouse_image, True, False)

    # 加载背景音乐
    pygame.mixer.music.load("music.ogg")
    pygame.mixer.music.play(-1)
    # 设置字体
    font = pygame.freetype.Font(r"C:\Windows\Fonts\msyh.ttc", size = 50)

    pygame.mouse.set_visible(False)
    start_time = time.time()

    print_text = False
    num_sub = False
    mousebuttondown = False
    score = 0
    add1 = True
    add2 = True
    add3 = True

    with open("max_score.txt", "rb") as f:
        x = f.read()
        max_score = int(ba.decodestring(x).decode())

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                if score > max_score:
                    with open("max_score.txt", "wb") as f:
                        string = str(score).encode()
                        string = ba.encodestring(string)
                        f.write(string)
            elif event.type == MOUSEBUTTONDOWN and num_sub:
                mousebuttondown = True
                pygame.quit()
                sys.exit()
                
        screen.blit(background, (0, 0))

        # 增加3个球
        if score > 60 * 7000 and add1:
            for i in range(1):
                speed = [randint(-6, 6), randint(-6, 6)]
                ball = Ball(speed, size, (randint(0, 1000), randint(0, 664)))
                while pygame.sprite.spritecollide(ball, ball_group, False, pygame.sprite.collide_circle) and not(ball.rect.collidepoint(pygame.mouse.get_pos())):
                    ball.rect.left, ball.rect.top = randint(0, 1000), randint(0, 664)
                balls.append(ball)
                ball_group.add(ball)
                add1 = False
                
        elif score > 35 * 7000 and add2:
            for i in range(1):
                speed = [randint(-6, 6), randint(-6, 6)]
                ball = Ball(speed, size, (randint(0, 1000), randint(0, 664)))
                while pygame.sprite.spritecollide(ball, ball_group, False, pygame.sprite.collide_circle) and not(ball.rect.collidepoint(pygame.mouse.get_pos())):
                    ball.rect.left, ball.rect.top = randint(0, 1000), randint(0, 664)
                balls.append(ball)
                ball_group.add(ball)
                add2 = False
                
        elif score > 15 * 7000 and add3:
            for i in range(1):
                speed = [randint(-6, 6), randint(-6, 6)]
                ball = Ball(speed, size, (randint(0, 1000), randint(0, 664)))
                while pygame.sprite.spritecollide(ball, ball_group, False, pygame.sprite.collide_circle) and not(ball.rect.collidepoint(pygame.mouse.get_pos())):
                    ball.rect.left, ball.rect.top = randint(0, 1000), randint(0, 664)
                balls.append(ball)
                ball_group.add(ball)
                add3 = False
        
        for each in balls:
            screen.blit(each.image, each.rect)
            each.move()

        for each in ball_group:
            ball_group.remove(each)
            if pygame.sprite.spritecollide(each, ball_group, False, pygame.sprite.collide_circle):
                each.speed[0], each.speed[1] = - each.speed[0], - each.speed[1]
            ball_group.add(each)

        if time.time() - start_time >= 5:
            for each in balls:
                if each.rect.collidepoint(pygame.mouse.get_pos()):
                    text_sur, text_rect = \
                              font.render("Game Over!", (255, 0, 0))
                    text_sur2, text_rect2 = \
                               font.render("历史最高：%d"% max_score, (255, 0, 0))
                    text_rect.center = width//2, height//2
                    text_rect2.center = width//2, height//2 + 50
                    #running = False
                    print_text = True

        if not num_sub:
            if randint(0, 5) == 0:
                score += randint(70, 100) * 10
        score_sur, score_rect = font.render("Score: %d" % score, (0, 0, 255), \
                                            size=20)
        score_rect.top, score_rect.left = 0, 0
        screen.blit(score_sur, score_rect)
        
        screen.blit(mouse_image, pygame.mouse.get_pos())
        if print_text:
            screen.blit(text_sur, text_rect)
            screen.blit(text_sur2, text_rect2)
            pygame.mixer.music.fadeout(1000)
            for each in balls:
                each.speed = [0, 0]
            #num = 150
            num_sub = True
            print_text = False
        
        if num_sub:
            screen.blit(text_sur, text_rect)
            screen.blit(text_sur2, text_rect2)
            #num -= 1
            if mousebuttondown:
                
                if score > max_score:
                    with open("max_score.txt", "wb") as f:
                        string = str(score).encode()
                        string = ba.encodestring(string)
                        f.write(string)
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(50)

try:
    main()
except SystemExit:
    pass
except:
    pygame.quit()
    print(traceback.format_exc())
    input()
