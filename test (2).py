import testgame
import pygame
fps=1
fclock=pygame.time.Clock()
game=testgame.gamestate()
for i in range(100):
    if i%2==0:
        game.step([1,0])
    else:
        game.step([0,1])
    fclock.tick(fps)
    print(i)
    print(game.bgcolor)
print('finish')
